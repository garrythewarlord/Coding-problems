
# Problem - https://leetcode.com/problems/pascals-triangle/


# Solution


class Solution:
    def generate(self, n):
        
        lst = [[1], [1,1]]

        if n == 0:
        	return []

        if n == 1:
            lst.pop(-1)

        if n > 2:
            x = 0
            for e in range(n-2):
                temp = []
                prev = 1+e
                for d in range(prev):
                    temp.append(lst[prev][d]+lst[prev][d+1])
                temp = [1] + temp + [1]
                x += 1
                lst.append(temp)

        return lst



test = Solution()

# Tests


n = 0
print(test.generate(n))

# Prints out [[1], [1, 1], [1, 2, 1]]

n = 3
print(test.generate(n))

# Prints out [[1], [1, 1], [1, 2, 1]]


n = 6
print(test.generate(n))

# Prints out [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]