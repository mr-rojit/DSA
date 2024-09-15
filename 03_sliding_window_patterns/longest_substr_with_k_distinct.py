s = "AAAHHIBC"
N = len(s)
k = 2
longest_size = -10

map = {}
start_idx = 0

for i in range(N):
    if s[i] not in map:
        map[s[i]] = 1
    else:
        map[s[i]] +=1

    while len(map) > 2:
        longest_size = max(longest_size, i-start_idx)
        if map[s[start_idx]] == 1:
            del map[s[start_idx]]
        else:
            map[s[start_idx]] -=1
        start_idx +=1
        

print(longest_size)


