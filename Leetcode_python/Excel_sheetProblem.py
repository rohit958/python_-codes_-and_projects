alphanum=('0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')


def excelcolumn(colnum):
    res=""
    rem=(colnum%26)
    colnum=(colnum//26)
    if colnum>=1:
        res+=alphanum[colnum]+ alphanum[rem]
    else:
        res+=alphanum[rem]
    return res

colnum=[1,34,701]
for x in colnum:
    print(excelcolumn(x))