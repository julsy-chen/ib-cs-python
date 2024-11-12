class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #numOfOpenBracketInstances = {'(': 0, '{': 0, '[': 0}
        closedBrackets = (')', '}', ']')
        openBrackets = ('(', '{', '[')
        openBracketCases = []

        for i in range(len(s)): # iterates through the string
            currentLetter = s[i]

            if currentLetter in closedBrackets: # checking if the letter is a closing bracket, if there was no instance of an open bracket of this kind, then return false
                currentLettersOpenBracket = openBrackets[closedBrackets.index(currentLetter)] # the open bracket type of the current letter
                if not openBracketCases or openBracketCases.pop() != currentLettersOpenBracket: # checking if there was an instance of an open bracket of this kind AND if the latest open bracket is the same kind of this closing bracket
                    return False
            else:
                openBracketCases.append(currentLetter)

        if len(openBracketCases) == 0:
            return True
        else: False
            

solution = Solution()
print(solution.isValid("]"))
