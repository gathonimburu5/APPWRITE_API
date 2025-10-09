from application.configuration import (
    client,
    database,
    APPWRITE_DATABASE_ID,
    APPWRITE_COLLECTION_ID,
    APPWRITE_EMPLOYEE_COLLECTION_ID,
    APPWRITE_REQUEST_HEADER_COLLECTION_ID,
    APPWRITE_REQUEST_DETAILS_COLLECTION_ID,
    APPWRITE_PRODUCT_COLLECTION_ID,
    APPWRITE_CATEGORY_COLLECTION_ID,
    APPWRITE_MEASURE_UNIT_COLLECTION_ID,
    APPWRITE_AUDIT_TRAIL_COLLECTION_ID,
    APPWRITE_SUPPLIER_COLLECTION_ID,
    APPWRITE_USER_COLLECTION_ID
)

import secrets

#result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_SUPPLIER_COLLECTION_ID, key='supplier_status', size=50, required=True )
#create user collections
#result = database.create_collection(database_id=APPWRITE_DATABASE_ID, collection_id=secrets.token_hex(8), name="user_collections")

#create user attributes
# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_USER_COLLECTION_ID, key='full_name', size=255, required=True)
# result = database.create_email_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_USER_COLLECTION_ID, key='email_address', required=True)
# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_USER_COLLECTION_ID, key='username', size=255, required=True)
# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_USER_COLLECTION_ID, key='password', size=255, required=True)
# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_USER_COLLECTION_ID, key='phone_number', size=20, required=True)
# result = database.create_datetime_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_USER_COLLECTION_ID, key='dob', required=True)
# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_USER_COLLECTION_ID, key='profile', size=255, required=True)
# result = database.create_datetime_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_USER_COLLECTION_ID, key='date_added', required=True)

# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_EMPLOYEE_COLLECTION_ID, key='created_by', size=255, required=True)
# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_REQUEST_HEADER_COLLECTION_ID, key='created_by', size=255, required=True)
# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_PRODUCT_COLLECTION_ID, key='created_by', size=255, required=True)
# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_CATEGORY_COLLECTION_ID, key='created_by', size=255, required=True)
# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_MEASURE_UNIT_COLLECTION_ID, key='created_by', size=255, required=True)
# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_AUDIT_TRAIL_COLLECTION_ID, key='created_by', size=255, required=True)
# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_SUPPLIER_COLLECTION_ID, key='created_by', size=255, required=True)
# result = database.create_string_attribute(database_id=APPWRITE_DATABASE_ID, collection_id=APPWRITE_USER_COLLECTION_ID, key='created_by', size=255, required=True)
# print(result)