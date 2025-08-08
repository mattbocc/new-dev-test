# Problem 1

Note: This README file may be more clear to view in Github or by using a markdown preview plugin

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
list1 = None, list2 = [0]
```

Output: 
```Python
[0]
```

### Visual Example

![test1_image](../imgs/merge.jpeg)

## Writing/Running Code

You are to write your solution in the problem.py file within the solution function. To test your code afterwards you can run ```python test_1/test.py``` which will run a series of test to see if your solution is providing the correct answer returning something like the response below.

```
% python test_1/test.py

CORRECT implementation for first example

Answer key list: [1, 1, 2, 3, 4, 4]
Your list: [1, 1, 2, 3, 4, 4]

------------------------------------------------

INCORRECT implementation for second example

Answer key list: [-100, 10, 12, 16, 50, 100]
Your list: [1, 1, 2, 3, 4, 4]

------------------------------------------------

INCORRECT implementation for third example

Answer key list: [0]
Your list: [1, 1, 2, 3, 4, 4]

------------------------------------------------
```