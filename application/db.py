from application.configuration import client, database, APPWRITE_DATABASE_ID, APPWRITE_COLLECTION_ID, APPWRITE_EMPLOYEE_COLLECTION_ID
import secrets

# database = Databases(client)
# result = database.create(database_id=secrets.token_hex(8), name="api_db")
# print(result)

#create a collection
# result = database.create_collection(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=secrets.token_hex(8),
#     name="todo_collections",
# )

#create a attribute
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_COLLECTION_ID,
#     key="title",
#     size=255,
#     required=True,
# )

# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_COLLECTION_ID,
#     key="description",
#     size=255,
#     required=True,
# )

# result = database.create_datetime_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_COLLECTION_ID,
#     key="created_on",
#     required=True,
# )

#create employee collection
# result = database.create_collection(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=secrets.token_hex(8),
#     name="employee_collections",
# )

#CREATE EMPLOYEE ATTRIBUTES
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_EMPLOYEE_COLLECTION_ID,
#     key="employee_name",
#     size=255,
#     required=True,
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_EMPLOYEE_COLLECTION_ID,
#     key="employee_email",
#     size=255,
#     required=True,
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_EMPLOYEE_COLLECTION_ID,
#     key="phone_number",
#     size=255,
#     required=True,
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_EMPLOYEE_COLLECTION_ID,
#     key="postal_address",
#     size=255,
#     required=True,
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_EMPLOYEE_COLLECTION_ID,
#     key="physical_address",
#     size=255,
#     required=True,
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_EMPLOYEE_COLLECTION_ID,
#     key="department",
#     size=255,
#     required=True,
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_EMPLOYEE_COLLECTION_ID,
#     key="gender",
#     size=50,
#     required=True,
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_EMPLOYEE_COLLECTION_ID,
#     key="kra_pin",
#     size=50,
#     required=True,
# )
# result = database.create_datetime_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_EMPLOYEE_COLLECTION_ID,
#     key="date_birth",
#     required=True,
# )
# result = database.create_datetime_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_EMPLOYEE_COLLECTION_ID,
#     key="created_on",
#     required=True,
# )
# print(result)