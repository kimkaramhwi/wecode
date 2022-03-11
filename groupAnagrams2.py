def groupAnagrams(strs):
    word = {}

    for i in strs:
        key = ''.join(sorted(i))

        if key not in word:
            word[key] = []
        word[key].append(i)

    result = []
    for key in word:
        result.append(word[key])

    return result

strs = ['apple','ppeal','star','arts','google','googel','tars','car']
print(groupAnagrams(strs))