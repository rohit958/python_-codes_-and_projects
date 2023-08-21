def defangIPaddr(address: str) -> str:
    result=""
    for pos in range(len(address)):
        if address[pos] == '.':
            result=result+"".join("[.]")
        else:
            result+="".join(address[pos])
    return result

print(defangIPaddr("1.1.1.1"))