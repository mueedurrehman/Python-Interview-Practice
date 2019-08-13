def romanToInt(s):
    roman_mappings_uncon = {"IV": 4, "IX": 9, "XL": 50, "XC": 90, "CD": 400, "CM": 900}
    roman_reg = {"I": 1, "V": 5, "X": 10, "C": 50, "D": 500, "M": 1000}
    result = 0
    for roman, value in roman_mappings_uncon.items():
        while roman in s:
            s = s.replace(roman, "", 1)
            result += value
    for char in s:
        result += roman_reg[char]
    return result

print(romanToInt("IV"))