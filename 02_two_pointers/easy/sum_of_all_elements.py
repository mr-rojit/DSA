
def sum_using_two_pointers(arr):
    i, j = 0, len(arr)-1
    sum = 0
    while(i <= j):

        if i == j:
            sum += arr[i]
            break

        sum += arr[i] + arr[j]
        i+=1
        j-=1
    return sum


arr = [1, 2, 3, 4, 5, 6]
s = sum_using_two_pointers(arr)

print(s)