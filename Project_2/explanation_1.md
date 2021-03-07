We are using two hashmaps in order to achieve this
goal. One hashmap will count number of times
we are fetching this value. Another Hashmap 
will store the value linked to the the key.

When we set the item, we check if we reached 
the capacity. If we have reached capacity already,
we will iterate through all the items to find least
used item. Once we find least used item, we will
remove that from the count and value stored hasmaps.
Then we will have space to add new item.

Time Complexity of this solution will be O(1)
Space Complexity of this solution wil be O(2*capacity)