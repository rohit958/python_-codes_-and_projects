
def flipAndInvertImage( image) :
    for l in image:
        i = 0
        j = len(l) - 1

        while i <= j:

            #inversion
            if l[i] == 0:
                l[i] = 1
            else:
                l[i] = 0
            if i==j:
                break
            if l[j] == 0:
                l[j] = 1
            else:
                l[j] = 0

            i += 1
            j -= 1

    return image


image = [[1,1,0],[1,0,1],[0,0,0]]

print(flipAndInvertImage(image))

#Output: [[1,0,0],[0,1,0],[1,1,1]]