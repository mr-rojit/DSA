arr = [1,23,1,1,7,6,12]
k = 3

max_sum = 0
running_sum = 0

for i in range(len(arr)):
    running_sum += arr[i]
    if i >= k-1:
        max_sum = max(running_sum, max_sum)
        running_sum -= arr[i-k+1]

print(max_sum)