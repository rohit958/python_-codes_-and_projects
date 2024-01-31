def checkIfPangram(sentence: str) -> bool:
    charset = set()
    leftpointer = 0
    rightpointer = len(sentence) - 1

    while leftpointer <= rightpointer:
        charset.add(sentence[leftpointer])
        charset.add(sentence[rightpointer])
        leftpointer += 1
        rightpointer -= 1
    if len(charset) == 26:
        return True
    else:
        return False


sentence ="thequickbrownfoxjumpsoverthelazydog"

print(checkIfPangram(sentence))
