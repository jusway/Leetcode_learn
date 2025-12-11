class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        my_set=set()
        max_len=0
        while right<len(s):
            if s[right] in my_set: # set记录过
                my_set.remove(s[left])
                left+=1
            else: # 当前元素没记录过
                my_set.add(s[right])
                max_len=max(max_len,len(my_set))
                right+=1

        return max_len