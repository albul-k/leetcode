"""
Given a string s, find the length of the longest substring without repeating characters.

Constraints:

* 0 <= s.length <= 5 * 104
* s consists of English letters, digits, symbols and spaces.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        elif len(set(s)) == 1:
            return 1

        substr: str = ''
        substr_length: int = 0
        counter: int = 0
        end: bool = False
        chars: set = set()
        for start in range(0, len(s)):
            for c in s[start::]:
                if c not in chars:
                    chars.add(c)
                    substr += c
                    counter += 1
                else:
                    if s[start::].replace(substr, '') == '':
                        end = True
                        break

                    chars.clear()
                    chars.add(c)
                    counter = 1

                if counter > substr_length:
                    substr_length = counter

            if end:
                break

            chars.clear()
            substr = ''
            counter = 0

        return substr_length


if __name__ == "__main__":
    solution = Solution()

    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("") == 0
    assert solution.lengthOfLongestSubstring("dvdf") == 3
    assert solution.lengthOfLongestSubstring("asjrgapa") == 6
    assert solution.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ") == 95
