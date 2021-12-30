
def flippingMatrix(matrix):
    # Write your code here

    leng = int(len(matrix))

    n = int(leng/2)

    times = leng

    k = 0
    l = 2*n-1
    res = [0]*times

    final = 0

    while k<times/2:

        r = 0
        while r<times/2:

            res[k] = max(matrix[k][r], matrix[k][l-r], matrix[l-k][r], matrix[l-k][l-r])
            final  = final + res[k]
            r += 1
        k += 1

    return final


matrix = []

matrix.append(list(map(int, input("matrix:").rstrip().split())))

result = flippingMatrix(matrix)

print(result)

