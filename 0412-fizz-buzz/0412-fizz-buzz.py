class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = [str(i+1) for i in range(0,n)]
        
        for i in range(len(answer)):
            
            if (i+1)%3 == 0 and (i+1)%5 == 0:
                answer[i] = "FizzBuzz"
            elif (i+1)%3 == 0:
                answer[i] = "Fizz"
            elif (i+1)%5 == 0:
                answer[i] = "Buzz"
                
        return answer
        