class MergeSort:
	def merge(self,A,p,q,r):
		L = A[p:q+1]
		R = A[q+1:r+1]
		i=0
		j=0
		k=p

		while(i<len(L) and j<len(R)):
			if(L[i]<=R[j]):
				A[k]=L[i]
				i=i+1
			else:
				A[k]=R[j]
				j=j+1
			k=k+1	
				

		while(i<len(L)):
			A[k]=L[i]
			i=i+1
			k=k+1

		while(j<len(R)):
			A[k]=R[j]
			j=j+1
			k=k+1
		print(A)
		

	def sort(self,A,p,r):
		if(p<r):
			q=p+(r-p)//2
			self.sort(A,p,q)
			self.sort(A,q+1,r)
			self.merge(A,p,q,r)

m=MergeSort()
A=[10,6,6,5,4,3,2,1]
print(m.sort(A,0,len(A)-1))
