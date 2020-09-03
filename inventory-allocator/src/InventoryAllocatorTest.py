from InventoryAllocator import allocate
import unittest

class Testing(unittest.TestCase):

    # Test cases from FAQ
    def test_single_item_single_warehouse(self):
        order = {"apple": 1}
        warehouses = [{"name": "owd", "inventory": {"apple": 1}}]
        
        expected = [{"owd": {"apple": 1}}]
        self.assertEqual(allocate(order, warehouses), expected)

    def test_single_item_multiple_warehouses_multiple_needed(self):
        order = {"apple": 10}
        warehouses = [{"name": "owd", "inventory": {"apple": 5}}, 
                      {"name": "dm", "inventory": {"apple": 5}}]
        
        expected = [{"owd": {"apple": 5}}, {"dm": {"apple": 5}}]
        self.assertEqual(allocate(order, warehouses), expected)

    def test_single_item_zero_inventory(self):
        order = {"apple": 1}
        warehouses = [{"name": "owd", "inventory": {"apple": 0}}]
        expected = []
        self.assertEqual(allocate(order, warehouses), expected)
    
    def test_single_item_insufficient_inventory(self):
        order = {"apple": 2}
        warehouses = [{"name": "owd", "inventory": {"apple": 1}}]
        expected = []
        self.assertEqual(allocate(order, warehouses), expected)


    # Single Item
    def test_single_item_single_warehouse_excess_inventory(self):
        order = {"apple": 3}
        warehouses = [{"name": "Florida", "inventory": {"apple": 7}}]
        
        expected = [{"Florida": {"apple": 3}}]
        self.assertEqual(allocate(order, warehouses), expected)

    def test_single_item_multiple_warehouses(self):
        order = {"apple": 3}
        warehouses = [{"name": "Florida", "inventory": {"apple": 7}},
                      {"name": "California", "inventory": {"apple": 5}}]
        
        expected = [{"Florida": {"apple": 3}}]
        self.assertEqual(allocate(order, warehouses), expected)
    
    def test_single_item_multiple_warehouses_same_inventory(self):
        order = {"apple": 3}
        warehouses = [{"name": "Florida", "inventory": {"apple": 3}},
                      {"name": "California", "inventory": {"apple": 3}}]
        
        expected = [{"Florida": {"apple": 3}}]
        self.assertEqual(allocate(order, warehouses), expected)
    

    # Multiple Items
    def test_multiple_items_single_warehouse(self):
        order = {"apple": 5, "orange": 6, "banana": 7}
        warehouses = [{"name": "Florida", "inventory": {"apple": 5, "orange": 6, "banana": 7}}]
        
        expected = [{"Florida": {"apple": 5, "orange": 6, "banana": 7}}]
        self.assertEqual(allocate(order, warehouses), expected)

    def test_multiple_items_single_warehouse_excess_inventory(self):
        order = {"apple": 5, "orange": 6, "banana": 7}
        warehouses = [{"name": "Florida", "inventory": {"apple": 7, "orange": 8, "banana": 9}}]
        
        expected = [{"Florida": {"apple": 5, "orange": 6, "banana": 7}}]
        self.assertEqual(allocate(order, warehouses), expected)

    def test_multiple_items_multiple_warehouses_all_needed(self):
        order = {"apple": 5, "orange": 6, "banana": 7}
        warehouses = [{"name": "Florida", "inventory": {"apple": 5}},
                      {"name": "California", "inventory": {"orange": 6}},
                      {"name": "Texas", "inventory": {"banana": 7}}]
        
        expected = [{"Florida": {"apple": 5}},
                    {"California": {"orange": 6}},
                    {"Texas":{"banana": 7}}]
        self.assertEqual(allocate(order, warehouses), expected)

    def test_multiple_items_multiple_warehouses_single_needed(self):
        order = {"apple": 5, "orange": 6, "banana": 7}
        warehouses = [{"name": "Florida", "inventory": {"apple": 5, "orange": 6}},
                      {"name": "California", "inventory": {"orange": 6, "banana": 7}},
                      {"name": "Texas", "inventory": {"apple": 5, "orange": 6, "banana": 7}}]

        expected = [{"Texas": {"apple": 5, "orange": 6, "banana": 7}}]
        self.assertEqual(allocate(order, warehouses), expected)


    # Invalid inputs
    def test_empty_order(self):
        order = {}
        warehouses = [{"name": "Florida", "inventory": {"apple": 7}}]
        expected = []
        self.assertEqual(allocate(order, warehouses), expected)

    def test_empty_warehouse(self):
        order = {"apple": 3}
        warehouses = []
        expected = []
        self.assertEqual(allocate(order, warehouses), expected)

    def test_item_not_found(self):
        order = {"apple": 3}
        warehouses = [{"name": "Florida", "inventory": {"banana": 7}}]
        expected = []
        self.assertEqual(allocate(order, warehouses), expected)

    def test_partial_order(self):
        order = {"apple": 1, "banana": 3}
        warehouses = [{"name": "Florida", "inventory": {"apple": 1}}]

        expected = [{"Florida": {"apple": 1}}]
        self.assertEqual(allocate(order, warehouses), expected)


if __name__ == "__main__":
    unittest.main()