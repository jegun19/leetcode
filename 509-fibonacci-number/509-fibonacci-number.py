class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            arr = [0, 1]
            for i in range(2, n+1):
                num = arr[0] + arr[1]
                arr [0] = arr[1]
                arr[1] = num
                
            return num