def isPalindrome(word : str) -> bool:
    if not word: 
        return False
    elif len(word) == 1:
        return True
    elif len(word) == 3:
        return word[0] == word[-1]
    else:
        wordList = list(word)
        for i in range(0, len(word)):
            if wordList[i] != wordList[-i-1]:
                return False
        return True
    
