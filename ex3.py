class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        len_words = len(words[0])
        swindow = len(words) * len_words
        indexlist = []

        for i in range(0, len(s)-swindow+1):
            thismatch = s[i:i+len_words-1]
            windowlist = []
            for x in range(len(words)):
                windowlist.append(thismatch[x*len_words, (x+1)*len_words])
            flag = 1
            wordscopy = words
            for j in windowlist:
                if j in wordscopy:
                    wordscopy.remove(j)
                else:
                    flag = 0
                    break
            if flag:
                indexlist.append(i)
        return indexlist
                
