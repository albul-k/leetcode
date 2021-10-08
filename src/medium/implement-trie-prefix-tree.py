"""
Url: https://leetcode.com/problems/implement-trie-prefix-tree/
Author: Konstantin Albul

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store
and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true
if the string word is in the trie (i.e., was inserted before),
and false otherwise.

boolean startsWith(String prefix) Returns true
if there is a previously inserted string word that has the prefix prefix,
and false otherwise.

Constraints:
* 1 <= word.length, prefix.length <= 2000
* word and prefix consist only of lowercase English letters.
* At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""

from collections import defaultdict


# pylint: disable=too-few-public-methods
class Trie:
    """solution
    """

    # pylint: disable=no-self-use
    def __init__(self):
        """init
        """

        self.tree_data = defaultdict(Trie)
        self.is_exist = False

    def insert(self, word: str) -> None:
        """insert

        Parameters
        ----------
        word : str
            word
        """

        node = self
        for char in word:
            node = node.tree_data[char]
        node.is_exist = True

    def search(self, word: str) -> bool:
        """search

        Parameters
        ----------
        word : str
            word

        Returns
        -------
        bool
            is word in the trie
        """

        node = self
        for char in word:
            if char not in node.tree_data:
                return False
            node = node.tree_data[char]
        return node.is_exist

    def startswith(self, prefix: str) -> bool:
        """startswith

        Parameters
        ----------
        prefix : str
            prefix

        Returns
        -------
        bool
            is word starts with prefix
        """

        node = self
        for char in prefix:
            if char not in node.tree_data:
                return False
            node = node.tree_data[char]
        return True


if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startswith("app") is True

    trie.insert("app")
    assert trie.search("app") is True
