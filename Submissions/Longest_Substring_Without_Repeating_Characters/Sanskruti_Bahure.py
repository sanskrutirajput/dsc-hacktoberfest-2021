# Longest Substring of non-repeating characters in python 
# Sanskruti Bahure (sanskrutirajput)

# Approach:
# Index will be 0 at the beginning. 
# And declaring a variable max_len which will keep the track of the longest substring length.
# Scan the string from left to right one character at a time and store the characters in set named as char_set.

# Time complexity: O(n)
# Space complexity: O(n)

# Code 
class Solution(object):
    def LengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        start = 0
        end = 0
        max_len = 0
        char_set = set()
        while end < len(s):
            if s[end] not in char_set:
                char_set.add(s[end])
                end += 1
                max_len = max(max_len, len(char_set))
            else:
                char_set.remove(s[start])
                start += 1
        return max_len
    
 # Driver code
def main():
    x = Solution()

    print(x.LengthOfLongestSubstring("abcabcbb"))   
    print(x.LengthOfLongestSubstring("bbbbb"))   
    print(x.LengthOfLongestSubstring("pwwkew"))   

if __name__ == "__main__":
    main()
        