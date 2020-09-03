from typing import List, Dict, Tuple, Sequence, Set 
from collections import deque
import copy

# constants
INVENTORY = "inventory"
NAME = "name"

# If a single item in the order is incomplete, then drop the item and ship the remaining
ALLOW_PARTIAL = True


def trim_shipments(shipments: List[Dict], incomplete_items: Set) -> List:
    """
    Removes unfulfilled items from shipments.
    """
    
    if incomplete_items and not ALLOW_PARTIAL:
        return []
    
    trimmed_shipments = copy.deepcopy(shipments)
    drop_shipments = set()

    for index, shipment in enumerate(shipments):
        name = next(iter(shipment))
            
        for item in shipment[name].keys():
            if item in incomplete_items or not shipment[name][item]:
                del trimmed_shipments[index][name][item]
        
        # Shipment that no longer has a single item after deleting unfulfilled items
        if not trimmed_shipments[index][name]:
            drop_shipments.add(index)
    
    resulting_shipments = []

    # some shipment will now be empty and should be removed
    for index, shipment in enumerate(trimmed_shipments):
        if not index in drop_shipments:
            resulting_shipments.append(shipment)
    

    return resulting_shipments

def allocate(order: Dict, warehouses: List[Dict]) -> List:
    """
    Allocates fulfillable items from order according to warehouse inventory.
    """
    shipments = []

    # Invalid inputs
    if not order or not warehouses:
        return shipments

    unfulfilled_order = order.copy()

    for warehouse in warehouses:
        inventory = warehouse[INVENTORY]
        name = warehouse[NAME]
        shipment = {name: {}}
        single_shipment = True
        
        for item, count in order.items():
            if item in inventory:
                if unfulfilled_order[item] > 0:
                    amount = min(unfulfilled_order[item], inventory[item])
                    unfulfilled_order[item] -= amount
                    shipment[name][item] = amount
                    
            if not item in inventory or inventory[item] < count:
                single_shipment = False
        
        # If a single warehouse can satisfy the entire order
        if single_shipment:
            return [{name : order}]

        # If shipment is not none
        if shipment[name]: 
            shipments.append(shipment)
    
    # All unfulfilled items from order
    incomplete_items = set([item for item, count in unfulfilled_order.items() if count > 0])

    return trim_shipments(shipments, incomplete_items)    


def main():
    order = {"apple": 5, "orange": 6, "banana": 7}
    warehouses = [{"name": "Florida", "inventory": {"apple": 5}},
                  {"name": "California", "inventory": {"orange": 6}},
                  {"name": "Texas", "inventory": {"banana": 7}}]

    print(allocate(order, warehouses))

if __name__ == '__main__':
    main()