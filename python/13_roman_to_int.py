class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # IV = 4, IX = 9
        # XL = 40, XC = 90
        # CD = 400, CM = 900
        # CMIV
        if len(s) == 1:
            return mappings.get(s)

        sum = 0
        for i in range(len(s) - 1):
            if (mappings.get(s[i]) < mappings.get(s[i + 1])):
                sum -= mappings.get(s[i])
                # below not valid as doing negative addition e.g. -900 overall (for CM, C = -100 M = +1000, overall +900)
                # below is doing -900 overall
                # sum += (mappings.get(s[i]) - mappings.get(s[i + 1]))
            else:
                sum += mappings.get(s[i])
        sum += mappings.get(s[-1])
        return sum


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
