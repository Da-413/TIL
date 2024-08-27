n = int(input())
lst = list(map(int,input().split()))
 
left = [0] * (n + 1)
right = [0] * (n + 1)
 
for i in range(1,len(lst) + 1,2):
    if left[lst[i - 1]] == 0:
        left[lst[i - 1]] = lst[i]
    else:
        right[lst[i - 1]] = lst[i]
 
 
def preorder(node):
    if node == 0:
        return
 
    print(node, end = ' ')
    preorder(left[node])
    preorder(right[node])
 
preorder(lst[0])