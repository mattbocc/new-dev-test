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
user_ans_arr = []
for i in range (0, 6):
    if user_ans.val != test_ans.val:
        passed = False

    user_ans_arr.append(user_ans.val)

    user_ans = user_ans.next
    test_ans = test_ans.next

if passed:
    print(f"\nCorrect implementation\n\nAnswer key list: [1, 1, 2, 3, 4, 4] \n Your list: {user_ans_arr}\n")
else:
    print(f"\nIncorrect implementation\n\nAnswer key list: [1, 1, 2, 3, 4, 4] \n Your list: {user_ans_arr}\n")




    
