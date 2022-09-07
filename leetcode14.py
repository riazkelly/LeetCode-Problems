'''Code for LeetCode problem #14 – Longest Common Prefix'''

def longestCommonPrefix(self, strs: list[str]) -> str:
    prefix = ""
    prefixIndex = 0
    cont = True
    while cont == True:
        try:
            prefix = prefix + strs[0][prefixIndex]
        except IndexError:
            cont = False
            break
        for word in strs:
            try:
                if word[prefixIndex] != prefix[prefixIndex]:
                    cont = False
                    prefix = prefix[0:prefixIndex]
            except IndexError:
                cont = False
                prefix = prefix[0:prefixIndex]
                return prefix

        prefixIndex += 1
    return prefix

test1 = ["","flower", "flowing", "fl"]
test2 = ["f","flower", "flowing", "fl"]
test3 = ["flower", "flower"]
print(longestCommonPrefix(test1, test1)) # Should print a blank string
print(longestCommonPrefix(test2, test2)) # Should print "f"
print(longestCommonPrefix(test3, test3)) # Should print "flower"
