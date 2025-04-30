from trie import Trie


class Homework(Trie):

    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError(" 'pattern' must be a string")

        # всі ключі зі словника
        all_words = list(self.keys())

        # слова, що закінчуються на заданий суфікс
        return sum(1 for word in all_words if word.endswith(pattern))

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("'pattern' must be a string")

        # Метод keys_with_prefix(prefix) повертає список усіх ключів із заданим префіксом
        return len(self.keys_with_prefix(prefix)) > 0


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
    
    # print(trie.count_words_with_suffix("e"))     
    # print(trie.count_words_with_suffix("ion"))   
    # print(trie.count_words_with_suffix("a"))     
    # print(trie.count_words_with_suffix("at"))    

    # print(trie.has_prefix("app"))  
    # print(trie.has_prefix("bat"))  
    # print(trie.has_prefix("ban"))  
    # print(trie.has_prefix("ca"))   
