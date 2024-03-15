def countGoodTriplets( arr, a: int, b: int, c: int):
    res = []
    for x in range(len(arr) - 2):
        # window creation
        window = [arr[x], arr[x + 1], arr[x + 2]]
        if abs(arr[0] - arr[1]) <= a and abs(arr[0] - arr[2]) <= b and abs(arr[0] - arr[2]) <= c:
            res.append(window)
        else:
            continue
    return len(res)

print(countGoodTriplets([7,3,7,3,12,1,12,2,3],5,8,1))
