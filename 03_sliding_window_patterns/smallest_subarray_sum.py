arr = [2,3,5,7,1,8,4,4,8]
N = len(arr)
target_sum = 8
subarr_size = 100

running_sum = 0
start_idx = 0

for i in range(N):
    running_sum += arr[i]
    while running_sum >= target_sum:
        window_size = i-start_idx+1
        subarr_size = min(subarr_size, window_size)
        running_sum -= arr[start_idx]
        start_idx+=1

print(subarr_size)