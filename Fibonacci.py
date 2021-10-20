class Fibonacci:
    	
    def fibonacci(self, n : int) -> int:
        fibonacci_final=1		#Initialize 1st element of series to 1, this variable will eventually hold the final value
        fibonacci_intermediate=0	#Use a temporary variable to hold previous Fibonacci Number
        i=2				#As 1st Fibonacci Number is fixed to 1, begin iteration with 2
        if(n==0):
            fibonacci_final=0		#For index as 0, Fibonacci Number must be 0
        elif(n>0):
            while(i<=n):
                fibonacci_final=fibonacci_intermediate+fibonacci_final		#Update new fibonacci number by adding it with the previous number
                fibonacci_intermediate=fibonacci_final-fibonacci_intermediate	#Bring back the temporary variable back to its previous value to add it for next number
                i=i+1								#Update iterator variable, keep iterating till i reaches the index number
                
        else:
           return "Invalid Input"	#Negative index cannot hold Fibonacci numbers
        
        return fibonacci_final

#f=Fibonacci()
#print(f.fibonacci(46))

#for i in range(47):
#	print(i, "th fibonacci number is", f.fibonacci(i))

