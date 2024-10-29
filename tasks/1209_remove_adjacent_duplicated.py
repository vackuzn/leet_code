class Solution(object):
    def removeDuplicates(self, s: str, k: int) -> str:
        #return self.stack_greedy(s, k) 
        return self.stack_counter(s, k) 

    def stack_greedy(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if len(stack) == 0:
                stack.append((c, 1))
            else:
                prev_c, prev_cnt = stack[-1]

                if prev_c == c:
                    if prev_cnt == k - 1:
                        for _ in range(k - 1):
                            stack.pop()
                    else:
                        stack.append((c, prev_cnt + 1))
                else:
                    stack.append((c, 1))

        return ''.join([c for c, _ in stack])
    
    def stack_counter(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if len(stack) == 0:
                stack.append([c, 1])
            else:
                prev_c, prev_cnt = stack[-1]

                if prev_c == c:
                    if prev_cnt == k - 1:
                        stack.pop()
                    else:
                        stack[-1][1] += 1
                else:
                    stack.append([c, 1])

        return ''.join([c * n for c, n in stack])


s = "abcd"; k = 2
s = "deeedbbcccbdaa"; k = 3
print(Solution().removeDuplicates(s, k))

# blunt approach - linear traverse 1..n till first bad version is found, then return it O(n)
# smart approach - binary search - 1..n is sorted so can be used
# divide interval by half, is bad version = True -> go left, else go right