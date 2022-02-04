def contiguous_array(arr):
    lookup = {}
    max_len, curr_sum = 0, 0
    for i in range(len(arr)):
        if arr[i] == 0:
            curr_sum -= 1
        else:
            curr_sum += 1
        if curr_sum == 0:
            max_len = i+1
        elif curr_sum in lookup:
            max_len = max(max_len, i-lookup[curr_sum])
        else:
            lookup[curr_sum] = i
    return max_len


arr = list(map(int, input().split()))
print(contiguous_array(arr))
