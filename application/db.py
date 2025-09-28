from application.configuration import client, database, APPWRITE_DATABASE_ID, APPWRITE_COLLECTION_ID
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

# print(result)