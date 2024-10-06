class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        char_counter = {}
        max_subarray_len = min(k + 1, len(s))
        most_common_char_count = 0

        for i, c in enumerate(s):
            char_counter[c] = char_counter.get(c, 0) + 1
            
            # new character will always increase counter
            # if count is below maximum, we are in worse situation than before, skip to the next
            if most_common_char_count < char_counter[c]:
                most_common_char_count = char_counter[c]
            
            window_char_count = i - l + 1

            # normally while would be used to pull the tail
            # but as the most_common_char_count may increment for 1 max
            # one step in pulling l pointer is enough
            if window_char_count - most_common_char_count > k:
                char_counter[s[l]] -= 1
                l += 1
                window_char_count = i - l + 1
            
            max_subarray_len = max(max_subarray_len, window_char_count)
        
        return max_subarray_len


s = "ABAB"; k = 2
s = "AABABBA"; k = 1
#s = "ABCDCBA"; k = 1
#s = "AAAAA"; k = 5
#s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"; k = 4
#s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"; k = 4
print(Solution().characterReplacement(s,k))

# Can I replace 1 character k times or any character k times total?
# find longest subarray with the same char after replacement
# 1. as we can replace any character, array of len k+1 is minimum result, 
# as we can take one char and replace all others to it k times
#
# Solve with sliding window:
# left and right pointers, start at zero
# counter hashmap with chars and chat counts within window left:right
# keep the symbol with highest count, replace others using k changes
# if other chars count > k, increment left pointer
