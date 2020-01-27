from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            # make a store because most sql databases (but not sqlite) need to satisfy a foreign key constraint.
            StoreModel('test').save_to_db()
            item = ItemModel('test', 19.99, 1)
            self.assertIsNone(ItemModel.find_by_name('test'),
                              f"Found an item with name {item.name} when it was not expected")
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 f"Did not find an item with name {item.name}")
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'),
                              f"Found an item with name {item.name} when it was not expected")

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test',  100, 1)

            store.save_to_db()
            item.save_to_db()
            # item.store is a store object because sqlalchemy does the thing
            self.assertEqual(item.store.name, 'test_store')