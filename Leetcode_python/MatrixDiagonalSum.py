
#Using a single loop - TIME COMPLEXTY=O(N)
def diagonalSum(mat) -> int:
    lim = len(mat)
    sum = 0
    for i in range(lim):
        sum += mat[i][i]
        if i != (lim - i - 1):
            sum += mat[i][lim - i - 1]
    return sum