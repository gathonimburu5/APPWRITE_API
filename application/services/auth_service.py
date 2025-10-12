from application.configuration import database, APPWRITE_DATABASE_ID, APPWRITE_USER_COLLECTION_ID, APPWRITE_AUDIT_TRAIL_COLLECTION_ID
from application.model import RegisterUserItem, UpdateUserItem, ChangePassword
from application.utils.security import hash_password, verify_password
from application.utils.file import upload_profile
from appwrite.query import Query
from datetime import datetime
import secrets
import traceback


class AuthenticationService:
    def __init__(self):
        self.database = database
        self.database_id = APPWRITE_DATABASE_ID
        self.user_collection_id = APPWRITE_USER_COLLECTION_ID
        self.audit_trail_collection_id = APPWRITE_AUDIT_TRAIL_COLLECTION_ID

    def register_user(self, data: RegisterUserItem, current_user, file):
        try:
            if data.password != data.confirm_password:
                return {"message" : "password does not match please check!"}

            user_id = current_user["id"]
            profile_image = upload_profile(file)
            user = self.database.create_document(database_id=self.database_id, collection_id=self.user_collection_id, document_id=secrets.token_hex(8),
                data={
                    "full_name": data.full_name,
                    "email_address": data.email_address,
                    "username": data.username,
                    "password": hash_password(data.password),
                    "phone_number": data.phone_number,
                    "dob": data.dob.isoformat(),
                    "profile": profile_image,
                    "date_added": data.date_added,
                    "created_by": user_id
                }
            )

            #handle audit trails
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(8),
                data={
                    "module_name": "CREATE USER RECORDS",
                    "action_type": "CREATE",
                    "action_date": data.date_added,
                    "created_by": user_id
                }
            )
            return user
        except Exception as e:
            print(f"Error creating user records: {e}")
            traceback.print_exc()
            return None

    def get_all_registered_users(self):
        return self.database.list_documents(database_id=self.database_id, collection_id=self.user_collection_id)

    def update_registered_user(self, data: UpdateUserItem, user_id: str, file):
        try:
            profile_image = upload_profile(file)
            update_user = self.database.update_document(database_id=self.database_id, collection_id=self.user_collection_id, document_id=user_id, data={
                "full_name": data.full_name,
                "email_address": data.email_address,
                "phone_number": data.phone_number,
                "profile": profile_image
            })
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(8), data={
                "module_name": "UPDATE USER RECORDS",
                "action_type": "UPDATE",
                "action_date": datetime.utcnow().isoformat(),
                "created_by": user_id
            })
            return update_user
        except Exception as e:
            print(f"Error updating user records: {e}")
            traceback.print_exc()
            return None

    def change_user_password(self, data: ChangePassword, user_id: str):
        try:
            if data.new_password != data.confirm_password:
                return { "message": "new password does not match confirm password" }

            user = self.database.get_document(database_id=self.database_id, collection_id=self.user_collection_id, document_id=user_id)
            if not user:
                return { "message": "user not found, please check again" }
            if not verify_password(data.old_password, user.get("password")):
                return { "message" : "your old password not found, please check again." }
            hassed_password = hash_password(data.new_password)
            changePass = self.database.update_document(database_id=self.database_id, collection_id=self.user_collection_id, document_id=user_id, data={"password": hassed_password})
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(8), data={
                "module_name": "CHANGE USER PASSWORD",
                "action_type": "UPDATE",
                "action_date": datetime.utcnow().isoformat(),
                "created_by": user_id
            })
            return { "message":"password successfully changed", "user id":user_id }
        except Exception as e:
            print(f"Error changing user password: {e}")
            traceback.print_exc()
            return None

    def authenticate_user(self, username: str, password: str):
        try:
            userList = self.database.list_documents(database_id=self.database_id, collection_id=self.user_collection_id, queries=[Query.equal("username", [username])])["documents"]
            if not userList:
                print(f"no user found with this username: {username}")
                raise ValueError(f"user details not found with this username: {username}")

            user = userList[0]

            if not verify_password(password, user["password"]):
                print("incorrect password")
                raise ValueError("incorrect password")

            return user
        except Exception as e:
            print(f"failed to authenticate this use: {e}")
            traceback.print_exc()
            return None