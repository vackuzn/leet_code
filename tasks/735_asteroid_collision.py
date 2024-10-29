class Solution(object):
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        # If asteroid flies left (negative) with no previous asteroids right - it never hits any other and can be skipped
        # If asteroid moves right - add it to stack
        # If asteroid moves left and stack has elements:
        #   For each asteroid in stack:
        #       If left == right:
        #           stack.pop()
        #           advance
        #       If left < right:
        #           stack pop
        #           repeat check for next element in stack
        #       If left > right:
        #           advance
        #   If no asteroid in stack
        #                   

        stack = []

        for cur in asteroids:
            if len(stack) == 0:
                stack.append(cur)
                continue

            while len(stack) > 0:
                prev = stack[-1]

                # same sign - no collision
                if prev > 0 and cur > 0 or prev < 0 and cur < 0 or prev < 0 and cur > 0:
                    stack.append(cur)
                    break

                # Same size - destroy both
                if abs(prev) == abs(cur):
                    stack.pop()
                    break

                # Cur > Prev - destroy prev, keep cur
                if abs(prev) < abs(cur):
                    stack.pop()
                # Cur < Prev - destroy cur
                else:
                    break
            else:
                stack.append(cur)
        
        return stack


asteroids = [5, 10, -5]
#asteroids = [8, -8]
#asteroids = [10, 2, -5]
asteroids = [-2,-1,1,2]
asteroids = [1,-2,-2,-2]
print(Solution().asteroidCollision(asteroids))

# blunt approach - linear traverse 1..n till first bad version is found, then return it O(n)
# smart approach - binary search - 1..n is sorted so can be used
# divide interval by half, is bad version = True -> go left, else go right