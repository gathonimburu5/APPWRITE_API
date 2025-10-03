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
    APPWRITE_AUDIT_TRAIL_COLLECTION_ID
)

import secrets

# #setting category attributes
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_CATEGORY_COLLECTION_ID,
#     key='category_name',
#     size=255,
#     required=True
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_CATEGORY_COLLECTION_ID,
#     key='category_status',
#     size=255,
#     required=True
# )
# result = database.create_datetime_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_CATEGORY_COLLECTION_ID,
#     key='date_added',
#     required=True
# )

# #setting measure unit attributes
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_MEASURE_UNIT_COLLECTION_ID,
#     key='unit_name',
#     size=255,
#     required=True
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_MEASURE_UNIT_COLLECTION_ID,
#     key='unit_status',
#     size=255,
#     required=True
# )
# result = database.create_datetime_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_MEASURE_UNIT_COLLECTION_ID,
#     key='date_added',
#     required=True
# )
# #setting product attributes
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_PRODUCT_COLLECTION_ID,
#     key='product_name',
#     size=255,
#     required=True
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_PRODUCT_COLLECTION_ID,
#     key='product_description',
#     size=255,
#     required=True
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_PRODUCT_COLLECTION_ID,
#     key='product_code',
#     size=255,
#     required=True
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_PRODUCT_COLLECTION_ID,
#     key='product_type',
#     size=255,
#     required=True
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_PRODUCT_COLLECTION_ID,
#     key='product_origin',
#     size=255,
#     required=True
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_PRODUCT_COLLECTION_ID,
#     key='category_id',
#     size=255,
#     required=True
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_PRODUCT_COLLECTION_ID,
#     key='measure_unit_id',
#     size=255,
#     required=True
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_PRODUCT_COLLECTION_ID,
#     key='supplier_id',
#     size=255,
#     required=True
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_PRODUCT_COLLECTION_ID,
#     key='vat_id',
#     size=255,
#     required=True
# )
# result = database.create_integer_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_PRODUCT_COLLECTION_ID,
#     key='quantity',
#     required=True
# )
# result = database.create_integer_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_PRODUCT_COLLECTION_ID,
#     key='reorder_level',
#     required=True
# )
# result = database.create_datetime_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_PRODUCT_COLLECTION_ID,
#     key='date_added',
#     required=True
# )

# #setting audit trail attributes
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_AUDIT_TRAIL_COLLECTION_ID,
#     key='module_name',
#     size=255,
#     required=True
# )
# result = database.create_string_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_AUDIT_TRAIL_COLLECTION_ID,
#     key='action_type',
#     size=255,
#     required=True
# )
# result = database.create_datetime_attribute(
#     database_id=APPWRITE_DATABASE_ID,
#     collection_id=APPWRITE_AUDIT_TRAIL_COLLECTION_ID,
#     key='action_date',
#     required=True
# )
# print(result)