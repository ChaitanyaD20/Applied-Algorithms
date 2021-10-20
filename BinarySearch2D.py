class BinarySearch2D:
	
	def search(self, M: [[int]], q: int) -> [int, int]:
		low_outer=0				#Initialize low_outer to track 1st row of the matrix as	0																	
		high_outer=len(M)-1		#Initialize high_outer to track last row of matrix as len(M)-1						
		if(len(M)>0):

			while(low_outer<=high_outer):							
				mid_outer=(low_outer+high_outer)//2
				if(q==M[mid_outer][len(M[mid_outer])-1]):			 
					return [mid_outer,len(M[mid_outer])-1]

				elif(q<M[mid_outer][0] and q>M[mid_outer-1][len(M[mid_outer-1])-1]):
					return [-1,-1]

				elif((q<M[mid_outer][len(M[mid_outer])-1])):
					if(q>=M[mid_outer][0]):							
						if(self.search_1D(M[mid_outer],q)==-1):		
							return [-1,-1]
						else:				
							return [mid_outer,self.search_1D(M[mid_outer],q)]
					else:
						high_outer=mid_outer-1
						
				elif((q>M[mid_outer][len(M[mid_outer])-1])):
						low_outer=mid_outer+1

		return [-1,-1]

	"""I have reused and extended the idea of 1D binary search to implement 2D Binary Search. Initialize mid_outer to (low_outer+high_outer)//2.
	Considered 6 cases here:
	1. If q is present on the last index of the mid_outer sub-array, we return that index.
	2. If q is lesser than the 1st element of mid_outer sub-array and if it is greater than the last element of previous sub-array, return [-1,-1] as it does not exist in the matrix.
	3. If q is lesser than the value of last index element of mid_outer sub-array and if q is greater than or equal to 1st element of mid_order sub-array, then perform 1D Binary Search on the mid_outer sub array, if element is present, return index, else return [-1,-1]
	4. If q is lesser than the value of last index element of mid_outer sub-array and if q is less than 1st element of mid_order sub-array, change value of high_outer to mid_outer-1 and iterate further(Extending Idea from 1D Binary Search).
	5. If q is greater than the value of last index element of mid_outer sub-array, then change value of low_outer to mid_outer+1 to iterate again(Extending Idea from 1D Binary Search).
	6. If q is less than smallest or greater than largest element of the matrix, return [-1,-1]
	"""	


	def search_1D(self,A,key):
		low=0										#Initialize low as 0, i.e. index of 1st element
		high=len(A)-1								#Initialize high as len(A)-1, as element count begins from 0
		if(len(A)>0):								#It should only enter Binary Search if length of array is greater than 0
			while(low<=high):						#To reiterate within the sub-arrays
				mid=(low+high)//2					#mid is assigned with the temporary value as average of low and high
				if key==A[mid]:						#If key is found as mid at a particular iteration, the index value is mid
					return mid
				elif(key<A[mid]):					#If key is lesser than mid at a particular iteration, we update high value to mid-1, and reiterate with the new sub-array
					high=mid-1
				elif(key>A[mid]):					#If key is higher than mid at a particular iteration, we update low value to mid+1, and reiterate with the new sub-array
					low=mid+1

		return -1									#If element is not existing in array, return -1



