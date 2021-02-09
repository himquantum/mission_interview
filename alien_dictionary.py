#Luckily, humans have developed a technology to sort the english words lexicographicaly
#Let us convert the alien word to human word
class Solution:

    def alien_to_human(self, alien_word, alien_order):
        human_word = ""
        human_order = "abcdefghijklmnopqrstuvwxyz"
        for letter in alien_word:
            alien_index = alien_order.find(letter)
            human_word += human_order[alien_index]
        return human_word

    def isAlienSorted(self, alien_words, alien_order: str) -> bool:
        human_words = []
        for word in alien_words:
            human_word = self.alien_to_human(word, alien_order)
            human_words.append(human_word)

        return True if sorted(human_words) == human_words else False


obj1 = Solution()
print(obj1.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(obj1.isAlienSorted(["word","worzd","xrow"], "worldabcefghijkmnpqstuvxyz"))
print(obj1.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
