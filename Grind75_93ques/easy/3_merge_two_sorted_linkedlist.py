"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

"""

def merge(lst1, lst2):
    new_lst = []
    n1, n2 = len(lst1), len(lst2)
    n = min(n1, n2)
    p1, p2 = 0, 0

    new_list = []

    while p1 < n:
        if lst1[p1] <= lst2[p2]:
            new_list.append(lst1[p1])
            p1+=1
        else:
            new_list.append(lst2[p2])
            p2 += 1
    
    new_list += lst2[p2:]
    print(new_list)



list1 = [1,2,4,5]
list2 = [1,3,4,7,8]

merge(list1, list2)