def groupAnagrams(strs):
    result = {}

    for word in sorted(strs):
        key = tuple(sorted(word))
        print(key)
        result[key] = result.get(key, []) + [word] # result[key]가 가지고 있는 value + word
        print(result)

    return result.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(strs)