from application.configuration import database, APPWRITE_DATABASE_ID, APPWRITE_USER_COLLECTION_ID, APPWRITE_AUDIT_TRAIL_COLLECTION_ID
from application.model import RegisterUserItem
from application.utils.security import hash_password, verify_password
from appwrite.query import Query
import secrets
import traceback


class AuthenticationService:
    def __init__(self):
        self.database = database
        self.database_id = APPWRITE_DATABASE_ID
        self.user_collection_id = APPWRITE_USER_COLLECTION_ID
        self.audit_trail_collection_id = APPWRITE_AUDIT_TRAIL_COLLECTION_ID

    def register_user(self, data: RegisterUserItem, current_user):
        try:
            user_id = current_user["id"]
            user = self.database.create_document(database_id=self.database_id, collection_id=self.user_collection_id, document_id=secrets.token_hex(8),
                data={
                    "full_name": data.full_name,
                    "email_address": data.email_address,
                    "username": data.username,
                    "password": hash_password(data.password),
                    "phone_number": data.phone_number,
                    "dob": data.dob.isoformat(),
                    "profile": data.profile,
                    "date_added": data.date_added,
                    "created_by": user_id
                }
            )

            #handle audit trails
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(8),
                data={
                    "module_name": "CREATE USER RECORDS",
                    "action_type": "CREATE",
                    "action_date": data.date_added
                }
            )
            return user
        except Exception as e:
            print(f"Error creating user records: {e}")
            traceback.print_exc()
            return None

    def authenticate_user(self, username: str, password: str):
        try:
            userList = self.database.list_documents(database_id=self.database_id, collection_id=self.user_collection_id, queries=[Query.equal("username", [username])])["documents"]
            if not userList:
                print(f"no user found with this username: {username}")
                return { "message": f"user details not found with this username: {username}" }

            user = userList[0]

            if not verify_password(password, user["password"]):
                print("incorrect password")
                return { "message": "incorrect password" }

            return user
        except Exception as e:
            print(f"failed to authenticate this use: {e}")
            traceback.print_exc()
            return None