class BinarySearch:
	def search(self,A,key):
		low_index=0										#Initialize low_index as 0, i.e. 1st element
		high_index=len(A)-1								#Initialize high_index as len(A)-1, as element count begins from 0
		if(len(A)>0):									#It should only enter Binary Search if length of array is greater than 0
			while(low_index<=high_index):				#To reiterate within the sub-arrays
				mid_index=(low_index+high_index)//2		#mid_index is assigned with the temporary value as average of low_index and high_index
				if key==A[mid_index]:					#If key is found as mid_index at a particular iteration, the index value is mid_index
					return mid_index
				elif(key<A[mid_index]):					#If key is lesser than mid_index at a particular iteration, we update high_index value to mid_index-1, and reiterate with the new sub-array
					high_index=mid_index-1
				elif(key>A[mid_index]):					#If key is higher than mid_index at a particular iteration, we update low_index value to mid_index+1, and reiterate with the new sub-array
					low_index=mid_index+1

		return -1										#If element is not existing in array, return -1
            


