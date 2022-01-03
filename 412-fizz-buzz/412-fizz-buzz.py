class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = list()
        for i in range (1, n+1):
            check_fizz = int(i % 3)
            check_buzz = int(i % 5) 
            if check_fizz == 0 and check_buzz == 0:
                answer.append("FizzBuzz")
            elif check_fizz == 0:
                answer.append("Fizz")
            elif check_buzz == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
                
        return answer