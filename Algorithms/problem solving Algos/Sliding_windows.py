# SLIDING WINDOW

# FIRST DEFINE WINDOW
# THEN SLIDE WINDOW

# EG.FINDING MAXIMUM SUB-ARRAY SUM

def sliding_window(arr,sub_size):
    l=len(arr)
    win_sum=0
    for i in range(sub_size): # to find window's sum
        win_sum+=arr[i]
    max_sum=win_sum
    for i in range(l-sub_size)  :# to slide window
        win_sum= win_sum -arr[i]+arr[sub_size+i]
        max_sum=max(win_sum,max_sum)
    return max_sum




print(" maximum sub_size sum:",sliding_window([1,6,7,8,3,5,2],3))