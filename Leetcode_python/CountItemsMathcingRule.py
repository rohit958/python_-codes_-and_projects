def countMatches( items, ruleKey, ruleValue) -> int:
    rulekeys = ["type", "color", "name"]
    chkInd = rulekeys.index(ruleKey)
    count=0
    for item in items:
        if item[chkInd]==ruleValue:
            count+=1
    return count

items=[["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
print(countMatches(items,ruleKey,ruleValue))