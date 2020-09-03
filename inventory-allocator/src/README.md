## Approach

Find a single warehouse that fulfills the order, if no such order exists, linearly aggregate the items of warehouses in order of increasing cost until the order is fullfilled (if possible)

## Time & Space Complexity

If there are `I` items in the order, and `W` wareshouses, the function allocates shipments in `O(IW)` time and `O(I + W)` space.

## Limitations & Assumptions

This approach assumes that if a single warehouse cannot satisfy the order, then a linear aggregation of items in warehouses is acceptable. If an assumption were to be added that the cost of shipping from any two warehouses was less than shipping from the first three warehouses, and then generilze this for higher numbers, then this approach no longer gives the optimal solution.

## Testing

`python3 -m unittest src/InventoryAllocatorTest.Testing`
