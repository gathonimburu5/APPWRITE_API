from application.configuration import (
    database, APPWRITE_DATABASE_ID, APPWRITE_SUPPLIER_COLLECTION_ID, APPWRITE_AUDIT_TRAIL_COLLECTION_ID
)
from application.model import SupplierItem
import secrets
import traceback

class SupplierService:
    def __init__(self):
        self.database = database
        self.database_id = APPWRITE_DATABASE_ID
        self.supplier_collection_id = APPWRITE_SUPPLIER_COLLECTION_ID
        self.audit_trail_collection_id = APPWRITE_AUDIT_TRAIL_COLLECTION_ID

    def create_supplier(self, data: SupplierItem):
        try:
            # Create the supplier record
            supplier = self.database.create_document(database_id=self.database_id, collection_id=self.supplier_collection_id, document_id=secrets.token_hex(16),
                data={
                    "supplier_name": data.supplier_name,
                    "supplier_code": data.supplier_code,
                    "supplier_email": data.supplier_email,
                    "supplier_phone": data.supplier_phone,
                    "postal_address": data.postal_address,
                    "physical_address": data.physical_address,
                    "dob": data.dob.isoformat(),
                    "supplier_status": data.supplier_status,
                    "date_added": data.date_added
                }
            )
            # Log in audit trail
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(16),
                data={
                    "module_name": "CREATE SUPPLIER RECORD",
                    "action_type": "CREATE",
                    "action_date": data.date_added
                }
            )
            return supplier
        except Exception as e:
            print(f"Error creating supplier: {e}")
            traceback.print_exc()
            return None

    def get_all_suppliers(self):
        return self.database.list_documents(database_id=self.database_id, collection_id=self.supplier_collection_id)

    def get_supplier(self, supplier_id: str):
        return self.database.get_document(database_id=self.database_id, collection_id=self.supplier_collection_id, document_id=supplier_id)

    def update_supplier(self, supplier_id: str, data: SupplierItem):
        try:
            # Update the supplier record
            supplier = self.database.update_document(database_id=self.database_id, collection_id=self.supplier_collection_id, document_id=supplier_id,
                data={
                    "supplier_name": data.supplier_name,
                    "supplier_code": data.supplier_code,
                    "supplier_email": data.supplier_email,
                    "supplier_phone": data.supplier_phone,
                    "postal_address": data.postal_address,
                    "physical_address": data.physical_address,
                    "dob": data.dob.isoformat(),
                    "date_added": data.date_added
                }
            )
            # Log in audit trail
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(16),
                data={
                    "module_name": "UPDATE SUPPLIER RECORD",
                    "action_type": "UPDATE",
                    "action_date": data.date_added
                }
            )
            return supplier
        except Exception as e:
            print(f"Error updating supplier: {e}")
            traceback.print_exc()
            return None