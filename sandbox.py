class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        prev_val = 0

        for char in s:
            curr_val = roman_to_int[char]

            if curr_val > prev_val:
                result += curr_val - 2 * prev_val

            else:
                result += curr_val

            prev_val = curr_val

        return result


result= Solution()
print(result.romanToInt("MCMXCIV"))
