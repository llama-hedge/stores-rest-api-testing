from models.item import ItemModel
from tests.unit.unit_base_test import UnitBaseTest


class ItemTest(UnitBaseTest):
    def test_create_item(self):
        # the init method needs to be tested not because it might not work, but to make sure no one changes it in an
        # unexpected way
        item = ItemModel('test item', 100, 1)
        self.assertEqual(item.name, 'test item', "The name of the item does not equal the constructor argument")
        self.assertEqual(item.price, 100,
                         "The price of the item after creation does not equal the constructor argument")
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel('test item', 100, 1)
        self.assertDictEqual(item.json(), {'name': 'test item', 'price': 100}, "JSON export is incorrect")
