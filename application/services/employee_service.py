from application.configuration import database, APPWRITE_DATABASE_ID, APPWRITE_EMPLOYEE_COLLECTION_ID, APPWRITE_AUDIT_TRAIL_COLLECTION_ID
from application.model import EmployeeItem
import secrets

class EmployeeService:
    def __init__(self):
        self.database = database
        self.database_id = APPWRITE_DATABASE_ID
        self.collection_id = APPWRITE_EMPLOYEE_COLLECTION_ID

    def get_all_employees(self):
        employees = self.database.list_documents(
            database_id=self.database_id,
            collection_id=self.collection_id
        )
        return employees

    def create_employee(self, data: EmployeeItem):
        employee = self.database.create_document(
            database_id=self.database_id,
            collection_id=self.collection_id,
            document_id=secrets.token_hex(16),
            data =  {
                "employee_name": data.employee_name,
                "employee_email": data.employee_email,
                "phone_number": data.phone_number,
                "postal_address": data.postal_address,
                "physical_address": data.physical_address,
                "department": data.department,
                "gender": data.gender,
                "kra_pin": data.kra_pin,
                "date_birth": data.date_birth.isoformat(),
                "created_on": data.created_on
            }
        )
        # Log the creation in the audit trail
        self.database.create_document(database_id=self.database_id, collection_id=APPWRITE_AUDIT_TRAIL_COLLECTION_ID, document_id=secrets.token_hex(16),
            data={
                "module_name": "CREATE EMPLOYEE RECORDS",
                "action_type": "CREATE",
                "action_date": data.created_on
            }
        )
        return employee

    def get_employee(self, employee_id):
        employee = self.database.get_document(
            database_id=self.database_id,
            collection_id=self.collection_id,
            document_id=employee_id
        )
        return employee

    def update_employee(self, employee_id, data: EmployeeItem):
        updated_employee = self.database.update_document(
            database_id=self.database_id,
            collection_id=self.collection_id,
            document_id=employee_id,
            data= {
                "employee_name": data.employee_name,
                "employee_email": data.employee_email,
                "phone_number": data.phone_number,
                "postal_address": data.postal_address,
                "physical_address": data.physical_address,
                "department": data.department,
                "gender": data.gender,
                "kra_pin": data.kra_pin,
                "date_birth": data.date_birth.isoformat()
            }
        )
        # Log the update in the audit trail
        self.database.create_document(database_id=self.database_id, collection_id=APPWRITE_AUDIT_TRAIL_COLLECTION_ID, document_id=secrets.token_hex(16),
            data={
                "module_name": "UPDATE EMPLOYEE RECORDS",
                "action_type": "UPDATE",
                "action_date": data.created_on
            }
        )
        return updated_employee