"""
Url: https://leetcode.com/problems/longest-palindromic-substring/
Author: Konstantin Albul

Given a string s, return the longest palindromic substring in s.

Constraints:
* 1 <= s.length <= 1000
* s consist of only digits and English letters.
"""


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def longest_palindrome(self, s_str: str) -> str:
        """longest-palindromic-substring

        Parameters
        ----------
        s_str : str
            string

        Returns
        -------
        str
            longest palindromic substring
        """

        palindromic_substr = ''
        matrix = [[0] * len(s_str) for _ in range(len(s_str))]
        for idx, _ in enumerate(s_str):
            matrix[idx][idx] = True
            palindromic_substr = s_str[idx]

        for i in range(len(s_str) - 1, -1, -1):
            for j in range(i + 1,len(s_str)):
                if s_str[i] == s_str[j]:
                    if j-i == 1 or matrix[i + 1][j - 1] is True:
                        matrix[i][j] = True
                        if len(palindromic_substr) < len(s_str[i:j + 1]):
                            palindromic_substr = s_str[i:j + 1]

        return palindromic_substr


if __name__ == "__main__":
    solution = Solution()

    assert solution.longest_palindrome("babad") in ("bab","aba")
    assert solution.longest_palindrome("cbbd") == "bb"
    assert solution.longest_palindrome("a") == "a"
    assert solution.longest_palindrome("ac") in ("a", "c")
    assert solution.longest_palindrome("aaa") == "aaa"
    assert solution.longest_palindrome("ccd") == "cc"

    TEST_STR = "kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsi"
    TEST_STR += "povhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeau"
    TEST_STR += "rqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfoje"
    TEST_STR += "uzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolost"
    TEST_STR += "mtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrun"
    TEST_STR += "yunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllz"
    TEST_STR += "upxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkog"
    TEST_STR += "bltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxso"
    TEST_STR += "fhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxh"
    TEST_STR += "fvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwois"
    TEST_STR += "niv"
    assert solution.longest_palindrome(TEST_STR) == "qahaq"
