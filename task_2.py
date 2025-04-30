from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(
            isinstance(s, str) for s in strings
        ):
            raise ValueError("Input data must be a list of strings.")
        if not strings:
            return ""

        # Побудова дерева з усіх слів
        for word in strings:
            self.put(word)

        # Знаходження найдовшого спільного префікса
        prefix = ""
        node = self.root

        while True:
            if len(node.children) != 1:  
                break
            char, next_node = next(iter(node.children.items()))
            prefix += char
            node = next_node
        return prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"
    # print(trie.find_longest_common_word(strings))  

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"
    # print(trie.find_longest_common_word(strings))  

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    # print(trie.find_longest_common_word(strings))  

   