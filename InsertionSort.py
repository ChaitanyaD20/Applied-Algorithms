class InsertionSort:

	def insertionsort(self, a):
		for j in range(1,len(a)):  		#Iterate from 2nd element to last element, as we need to begin comparison from 2nd element.       
			key=a[j]           		#Initialize temporary variable to 2nd element of list
			i=j                        	#Initialize another counter to 2
			while i>0 and a[i-1]>key:	#Compare with previous elements of array
				a[i]=a[i-1]		#If the previous element is greater than the current one, replace bigger element with the current one.				
				i=i-1
			a[i]=key		        #Assign the current element in the correct position, to ensure sorted sub array till j  
			#print(a) 	
		return(a)    
		

#The print(a) command which has been commented was used to see the intermediate results during the sort. To verify the correct implementation, kindly remove the comment symbols.
