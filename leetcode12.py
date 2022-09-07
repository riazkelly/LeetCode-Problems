''' Code for LeetCode problem #12 – Integer to Roman Conversion '''

def intToRoman(self, num: int) -> str:

    roman = ""
    s = str(num)
    index = len(s) - 1
    tens = ["I", "X", "C", "M"]
    fives = ["V", "L", "D"]
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arrayindex = 0

    while index >= 0:

        s = str(num)

        if s[index] == "0":
            arrayindex += 1
            index -= 1

        elif s[index] == "4":
            roman = tens[arrayindex] + fives[arrayindex] + roman
            num -= (d[fives[arrayindex]] - d[tens[arrayindex]])
            arrayindex += 1
            index -=1

        elif s[index] == "9":
            roman = tens[arrayindex] + tens[arrayindex + 1] + roman
            num -= (d[tens[arrayindex + 1]] - d[tens[arrayindex]])
            arrayindex += 1
            index -= 1

        elif s[index] == "5":
            roman = fives[arrayindex] + roman
            num -= d[fives[arrayindex]]
            arrayindex += 1
            index -= 1

        else:
            roman = tens[arrayindex] + roman
            num -= d[tens[arrayindex]]

    return roman

print(intToRoman(2, 2040))
print(intToRoman(2, 1890))
print(intToRoman(2, 1364))
print(intToRoman(2, 2761))
