# Problem 1

You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

### Ex. 1
Input: 
```Python
list1 = [1,2,4], list2 = [1,3,4]
```
Output: 
```Python
[1,1,2,3,4,4]
```

### Ex. 2
Input:
```Python
list1 = [-100,12,16], list2 = [10,50,100]
```

Output: 
```Python
[-100,10,12,16,50,100]
```


### Ex. 3
Input:
```Python
list1 = [], list2 = [0]
```

Output: 
```Python
[0]
```

## Visual Example

![test1_image](../imgs/merge.jpeg)