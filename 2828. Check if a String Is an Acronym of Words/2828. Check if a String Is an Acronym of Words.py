class Solution:
    def isAcronym(self, words, s):

        acronym = ""

        for word in words:
            acronym += word[0]

        return acronym == s