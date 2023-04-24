from random import randint
import math 


class Solution:
    def mySqrt(self, x):#memory error - no need to maintain the whole array
        arr = list(range(x + 1))
        first_len = x//2
        #print(arr)
        while len(arr) > 1:            
            middle = len(arr)//2
            #print(middle)
            if arr[middle]**2 > x:
                arr = arr[:middle]
            else:
                arr = arr[middle:]
            #print(arr)
        return arr[0]

    def mySqrto(self, x):
        if x == 1:
            return 1
        arr = [0, x//2, x]
        #print(arr)
        while arr[2] - arr[0] > 1:            
            if arr[1]**2 > x:
                arr[2] = arr[1]
                arr[1] //= 2
            else:
                arr[0] = arr[1]
                arr[1] += (arr[2] - arr[1])//2
            #print(arr)
        return arr[0]


test_arr = [0, 1, 2000000000] + [randint(0, 10000) for _ in range(40)]
s = Solution()

for test_value in test_arr:
    result = s.mySqrto(test_value)
    check = math.floor(test_value**0.5)
    if result != check:
        print(f"number: {test_value}, my func res: {result}({result**2}), check: {check}({check**2})\n")
    else:
        print(f"ok, number: {test_value}")