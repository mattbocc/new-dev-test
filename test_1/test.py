# To execute test: "python test_1/test.py"
from problem import ListNode, solution


# Two SLL instantiations
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# User and test answer instantiation
user_ans = solution(list1, list2)
test_ans = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))

# Testing list 1
passed = True
for i in range (0, 6):
    if user_ans.val != test_ans.val:
        passed = False
    user_ans = user_ans.next
    test_ans = test_ans.next

# Feedback output
user_ans = solution(list1, list2)
user_ans_list = []
while user_ans:
    user_ans_list.append(user_ans.val)
    user_ans = user_ans.next

if passed:
    print(f"\nCORRECT implementation for first example\n\nAnswer key list: [1, 1, 2, 3, 4, 4]\nYour list: {user_ans_list}")
else:
    print(f"\nINCORRECT implementation for first example\n\nAnswer key list: [1, 1, 2, 3, 4, 4]\nYour list: {user_ans_list}")

print("\n------------------------------------------------")

# Two SLL instantiations
list1 = ListNode(-100, ListNode(12, ListNode(16)))
list2 = ListNode(10, ListNode(50, ListNode(100)))

# User and test answer instantiation
user_ans = solution(list1, list2)
test_ans = ListNode(-100, ListNode(10, ListNode(12, ListNode(16, ListNode(50, ListNode(100))))))

# Testing list 2
passed = True
for i in range (0, 6):
    if user_ans.val != test_ans.val:
        passed = False
    
    user_ans = user_ans.next
    test_ans = test_ans.next

# Feedback output
user_ans = solution(list1, list2)
user_ans_list = []
while user_ans:
    user_ans_list.append(user_ans.val)
    user_ans = user_ans.next


if passed:
    print(f"\nCORRECT implementation for second example\n\nAnswer key list: [-100, 10, 12, 16, 50, 100]\nYour list: {user_ans_list}")
else:
    print(f"\nINCORRECT implementation for second example\n\nAnswer key list: [-100, 10, 12, 16, 50, 100]\nYour list: {user_ans_list}")

print("\n------------------------------------------------")

# Two SLL instantiations
list1 = None
list2 = ListNode(0)

# User and test answer instantiation
user_ans = solution(list1, list2)
test_ans = ListNode(0)

# Testing list 3
passed = True
for i in range (0, 1):
    if user_ans.val != test_ans.val:
        passed = False

    user_ans = user_ans.next
    test_ans = test_ans.next

# Feedback output
user_ans = solution(list1, list2)
user_ans_list = []
while user_ans:
    user_ans_list.append(user_ans.val)
    user_ans = user_ans.next

if passed:
    print(f"\nCORRECT implementation for third example\n\nAnswer key list: [0]\nYour list: {user_ans_list}")
else:
    print(f"\nINCORRECT implementation for third example\n\nAnswer key list: [0]\nYour list: {user_ans_list}")

print("\n------------------------------------------------")


    
