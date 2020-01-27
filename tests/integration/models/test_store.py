from models.store import StoreModel
from models.item import ItemModel
from tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')
        self.assertListEqual(store.items.all(), [],
                             "The store's item list was not empty even though no items were added")

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')
            self.assertIsNone(StoreModel.find_by_name('test'),
                              "Store with name 'test' was found even though it was not writen to the database")
            store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name('test'),
                                 "Store with name 'test' was not found even though it was written from the database")
            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name('test'),
                              "Store with name 'test' was found even though it was deleted from the database")

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test item', 19.99, 1)
            store.save_to_db()
            item.save_to_db()
            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test item')

    def test_store_json(self):
        store = StoreModel('test')
        expected ={
            'id': None,
            'name': 'test',
            'items': []
        }
        self.assertDictEqual(store.json(), expected)

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test item', 19.99, 1)
            store.save_to_db()
            item.save_to_db()
            expected = {
                'id': 1,
                'name': 'test',
                'items': [{'name': 'test item', 'price': 19.99}]
            }
            self.assertDictEqual(store.json(), expected)