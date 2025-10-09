from application.configuration import (
    database, APPWRITE_DATABASE_ID, APPWRITE_PRODUCT_COLLECTION_ID, APPWRITE_CATEGORY_COLLECTION_ID, APPWRITE_MEASURE_UNIT_COLLECTION_ID, APPWRITE_AUDIT_TRAIL_COLLECTION_ID
)
from application.model import ProductItem, CategoryItem, MeasureUnitItem, UpdateCategoryItem, DeactivateCategoryItem, UpdateMeasureUnitItem, DeactivateMeasureUnitItem
from appwrite.query import Query
import traceback
import secrets

class ProductService:
    def __init__(self):
        self.database = database
        self.database_id = APPWRITE_DATABASE_ID
        self.product_collection_id = APPWRITE_PRODUCT_COLLECTION_ID
        self.category_collection_id = APPWRITE_CATEGORY_COLLECTION_ID
        self.measure_unit_collection_id = APPWRITE_MEASURE_UNIT_COLLECTION_ID
        self.audit_trail_collection_id = APPWRITE_AUDIT_TRAIL_COLLECTION_ID

    def create_product(self, data: ProductItem, current_user):
        try:
            user_id = current_user["id"]
            product = self.database.create_document(database_id=self.database_id, collection_id=self.product_collection_id, document_id=secrets.token_hex(16),
                data={
                    "product_name": data.product_name,
                    "product_description": data.product_description,
                    "product_code": data.product_code,
                    "product_type": data.product_type,
                    "product_origin": data.product_origin,
                    "category_id": data.category_id,
                    "measure_unit_id": data.measure_unit_id,
                    "supplier_id": data.supplier_id,
                    "vat_percentage": data.vat_percentage,
                    "quantity": data.quantity,
                    "reoder_level": data.reoder_level,
                    "date_added": data.date_added,
                    "created_by": user_id
                }
            )
            # Log the creation in the audit trail
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(16),
                data={
                    "module_name": "CREATE PRODUCT RECORDS",
                    "action_type": "CREATE",
                    "action_date": data.date_added,
                    "created_by": user_id
                }
            )
            return product
        except Exception as e:
            print(f"Error creating product: {e}")
            traceback.print_exc()
            return None

    def get_all_products(self):
        return self.database.list_documents(database_id=self.database_id, collection_id=self.product_collection_id)

    def get_product(self, product_id):
        return self.database.get_document(database_id=self.database_id, collection_id=self.product_collection_id, document_id=product_id)

    def update_product(self, product_id, data: ProductItem, current_user):
        try:
            user_id = current_user["id"]
            updated_product = self.database.update_document(database_id=self.database_id, collection_id=self.product_collection_id, document_id=product_id,
                data={
                    "product_name": data.product_name,
                    "product_description": data.product_description,
                    "product_code": data.product_code,
                    "product_type": data.product_type,
                    "product_origin": data.product_origin,
                    "category_id": data.category_id,
                    "measure_unit_id": data.measure_unit_id,
                    "supplier_id": data.supplier_id,
                    "vat_percentage": data.vat_percentage,
                    "quantity": data.quantity,
                    "reoder_level": data.reoder_level,
                    "created_by": user_id
                }
            )
            # Log the update in the audit trail
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(16),
                data={
                    "module_name": "UPDATE PRODUCT RECORDS",
                    "action_type": "UPDATE",
                    "action_date": data.date_added,
                    "created_by": user_id
                }
            )
            return updated_product
        except Exception as e:
            print(f"Error updating product: {e}")
            traceback.print_exc()
            return None

    def create_category(self, data: CategoryItem, current_user):
        try:
            user_id = current_user["id"]
            category = self.database.create_document(database_id=self.database_id, collection_id=self.category_collection_id, document_id=secrets.token_hex(16),
                data={
                    "category_name": data.category_name,
                    "category_status": data.category_status,
                    "date_added": data.date_added,
                    "created_by": user_id
                }
            )
            #register in audit trail
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(16),
                data={
                    "module_name": "CREATE PRODUCT CATEGORY",
                    "action_type": "CREATE",
                    "action_date": data.date_added,
                    "created_by": user_id
                }
            )
            return category
        except Exception as e:
            print(f"Error creating category: {e}")
            traceback.print_exc()
            return None

    def get_all_categories(self):
        return self.database.list_documents(database_id=self.database_id, collection_id=self.category_collection_id)

    def get_category(self, category_id):
        return self.database.get_document(database_id=self.database_id, collection_id=self.category_collection_id, document_id=category_id)

    def update_category(self, category_id, data: UpdateCategoryItem, current_user):
        try:
            user_id = current_user["id"]
            updated_category = self.database.update_document(database_id=self.database_id, collection_id=self.category_collection_id, document_id=category_id,
                data={
                    "category_name": data.category_name
                }
            )
            # Log the update in the audit trail
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(16),
                data={
                    "module_name": "UPDATE PRODUCT CATEGORY",
                    "action_type": "UPDATE",
                    "action_date": data.date_added,
                    "created_by": user_id
                }
            )
            return updated_category
        except Exception as e:
            print(f"Error updating category: {e}")
            traceback.print_exc()
            return None

    def deactivate_category(self, category_id, data: DeactivateCategoryItem, current_user):
        try:
            user_id = current_user["id"]
            updated_category = self.database.update_document(database_id=self.database_id, collection_id=self.category_collection_id, document_id=category_id,
                data={
                    "category_status": data.category_status
                }
            )
            # Log the update in the audit trail
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(16),
                data={
                    "module_name": "DEACTIVATE PRODUCT CATEGORY",
                    "action_type": "UPDATE",
                    "action_date": data.date_added,
                    "created_by": user_id
                }
            )
            return updated_category
        except Exception as e:
            print(f"Error deactivating category: {e}")
            traceback.print_exc()
            return None

    def create_measure_unit(self, data: MeasureUnitItem, current_user):
        try:
            user_id = current_user["id"]
            measure_unit = self.database.create_document(database_id=self.database_id, collection_id=self.measure_unit_collection_id, document_id=secrets.token_hex(16),
                data={
                    "unit_name": data.unit_name,
                    "unit_status": data.unit_status,
                    "date_added": data.date_added,
                    "created_by": user_id
                }
            )
            #register in audit trail
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(16),
                data={
                    "module_name": "CREATE MEASURE UNIT",
                    "action_type": "CREATE",
                    "action_date": data.date_added,
                    "created_by": user_id
                }
            )
            return measure_unit
        except Exception as e:
            print(f"Error creating measure unit: {e}")
            traceback.print_exc()
            return None

    def get_active_categories(self):
        return self.database.list_documents(database_id=self.database_id, collection_id=self.category_collection_id, queries=[Query.equal("category_status", "active")])

    def get_all_measure_units(self):
        return self.database.list_documents(database_id=self.database_id, collection_id=self.measure_unit_collection_id)

    def get_measure_unit(self, unit_id):
        return self.database.get_document(database_id=self.database_id, collection_id=self.measure_unit_collection_id, document_id=unit_id)

    def update_measure_unit(self, unit_id, data: UpdateMeasureUnitItem, current_user):
        try:
            user_id = current_user["id"]
            updated_unit = self.database.update_document(database_id=self.database_id, collection_id=self.measure_unit_collection_id, document_id=unit_id,
                data={
                    "unit_name": data.unit_name
                }
            )
            # Log the update in the audit trail
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(16),
                data={
                    "module_name": "UPDATE MEASURE UNIT",
                    "action_type": "UPDATE",
                    "action_date": data.date_added,
                    "created_by": user_id
                }
            )
            return updated_unit
        except Exception as e:
            print(f"Error updating measure unit: {e}")
            traceback.print_exc()
            return None

    def deactivate_measure_unit(self, unit_id, data: DeactivateMeasureUnitItem, current_user):
        try:
            user_id = current_user["id"]
            updated_unit = self.database.update_document(database_id=self.database_id, collection_id=self.measure_unit_collection_id, document_id=unit_id,
                data={
                    "unit_status": data.unit_status
                }
            )
            # Log the update in the audit trail
            self.database.create_document(database_id=self.database_id, collection_id=self.audit_trail_collection_id, document_id=secrets.token_hex(16),
                data={
                    "module_name": "DEACTIVATE MEASURE UNIT",
                    "action_type": "UPDATE",
                    "action_date": data.date_added,
                    "created_by": user_id
                }
            )
            return updated_unit
        except Exception as e:
            print(f"Error deactivating measure unit: {e}")
            traceback.print_exc()
            return None

    def get_active_measure_units(self):
        return self.database.list_documents(database_id=self.database_id, collection_id=self.measure_unit_collection_id, queries=[Query.equal("unit_status", "active")])