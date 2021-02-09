def one_edit_apart(word2, word1):
    # assume word2 is longer than word1, if not then Swap
    if abs(len(word1) - len(word2)) > 1:
        return False
    elif len(word1) == len(word2):
        diff = 0
        for i in range(0, len(word2)):
            if word1[i] != word2[i]:
                diff += 1
        return True if diff == 1 else False
    else:
        if len(word2) < len(word1):
            word1, word2 = word2, word1  # Swap

        diff = 0
        for j in range(0, len(word2)):
            if word2[0:j] + word2[j+1:] == word1:
                diff += 1
        return True if diff == 1 else False


print(one_edit_apart("cat", "dog"))
print(one_edit_apart("cat", "cuts"))
print(one_edit_apart("cat", "cut"))
print(one_edit_apart("cat", "cast"))
print(one_edit_apart("cat", "at"))
print(one_edit_apart("hello", "hello"))