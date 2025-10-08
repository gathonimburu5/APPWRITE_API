from application.configuration import (
    database, APPWRITE_DATABASE_ID, APPWRITE_REQUEST_HEADER_COLLECTION_ID, APPWRITE_REQUEST_DETAILS_COLLECTION_ID, APPWRITE_AUDIT_TRAIL_COLLECTION_ID
)
from application.model import RequestHeaderItem
from appwrite.query import Query
import secrets
import traceback

class RequestService:
    def __init__(self):
        self.database = database
        self.database_id = APPWRITE_DATABASE_ID
        self.request_header_collection_id = APPWRITE_REQUEST_HEADER_COLLECTION_ID
        self.request_details_collection_id = APPWRITE_REQUEST_DETAILS_COLLECTION_ID

    def create_request(self, data: RequestHeaderItem):
        try:
            # Create the request header
            request_header = self.database.create_document(
                database_id=self.database_id,
                collection_id=self.request_header_collection_id,
                document_id=secrets.token_hex(16),
                data={
                    "request_type": data.request_type,
                    "request_description": data.request_description,
                    "request_status": data.request_status,
                    "request_date": data.request_date.isoformat(),
                    "created_on": data.created_on
                }
            )
            # Create the request details
            for detail in data.details:
                self.database.create_document(
                    database_id=self.database_id,
                    collection_id=self.request_details_collection_id,
                    document_id=secrets.token_hex(16),
                    data={
                        "header_id": request_header['$id'],
                        "product_id": detail.product_id,
                        "extra_details": detail.extra_details,
                        "quantity": detail.quantity,
                        "unit_price": detail.unit_price,
                        "vat_percentage": detail.vat_percentage,
                        "vat_amount": detail.vat_amount,
                        "total_net": detail.total_net
                    }
                )
            #log in audit trail
            self.database.create_document(database_id=self.database_id, collection_id=APPWRITE_AUDIT_TRAIL_COLLECTION_ID, document_id=secrets.token_hex(16),
                data={
                    "module_name": "CREATE REQUEST RECORDS",
                    "action_type": "CREATE",
                    "action_date": data.created_on
                }
            )
            return request_header
        except Exception as e:
            print(f"Error creating request: {e}")
            traceback.print_exc()
            return None

    def get_all_requests(self):
        try:
            requests = self.database.list_documents(database_id=self.database_id, collection_id=self.request_header_collection_id)
            details = self.database.list_documents(database_id=self.database_id, collection_id=self.request_details_collection_id)

            # Map details to their respective headers
            requests_map = {request["$id"]: [] for request in requests['documents']}
            for detail in details["documents"]:
                if detail["header_id"] in requests_map:
                    requests_map[detail["header_id"]].append(detail)

            requests_result = []
            for request in requests["documents"]:
                request_data = {
                    "id": request["$id"],
                    "request_type": request["request_type"],
                    "request_description": request["request_description"],
                    "request_status": request["request_status"],
                    "request_date": request["request_date"],
                    "created_on": request["created_on"],
                    "details": requests_map.get(request["$id"], [])
                }
                requests_result.append(request_data)
            return requests_result
        except Exception as e:
            print(f"Error retrieving requests: {e}")
            traceback.print_exc()
            return None

    def get_request(self, request_id):
        try:
            request = self.database.get_document(database_id=self.database_id, collection_id=self.request_header_collection_id, document_id=request_id)
            headerId = request["$id"]
            detail_data = self.database.list_documents(database_id=self.database_id, collection_id=self.request_details_collection_id, queries=[Query.equal("header_id", headerId)])["documents"]
            details = []
            for data in detail_data:
                details.append({
                    "id": data["$id"],
                    "header_id": data["header_id"],
                    "product_id": data["product_id"],
                    "extra_details": data["extra_details"],
                    "quantity": data["quantity"],
                    "unit_price": data["unit_price"],
                    "vat_percentage": data["vat_percentage"],
                    "vat_amount": data["vat_amount"],
                    "total_net": data["total_net"]
                })

            request_data = {
                "id": request["$id"],
                "request_type": request["request_type"],
                "request_description": request["request_description"],
                "request_status": request["request_status"],
                "request_date": request["request_date"],
                "created_on": request["created_on"],
                "details": details
            }
            return request_data
        except Exception as e:
            print(f"error occurred retrieving request: {e}")
            traceback.print_exc()
            return None
