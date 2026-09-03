class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output=[]
        for word in words:

            def find(word,pattern):

                map_wordtopattern={}
                map_patterntoword={}

                for i in range(len(word)):

                    word_char=word[i]
                    pattern_char=pattern[i]
                    
                    if word_char in map_wordtopattern:
                        if map_wordtopattern[word_char]!=pattern_char:
                            return False
                    else:
                        if pattern_char in map_patterntoword:
                            return False

                    map_wordtopattern[word_char]=pattern_char
                    map_patterntoword[pattern_char]=word_char
                return True

            if find(word,pattern):
                output.append(word)
        return output

        