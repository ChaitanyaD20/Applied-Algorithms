class QuickSelect:
    
    def select(self, A: [int], k: int) -> int:
    	return self.select_helper(A,0,len(A)-1,k)

    def select_helper(self,A,lo,hi,k):
    	
        if(k>=0 and k<=len(A)-1):
            pivot=self.partition(A,lo,hi)
            if k==pivot:
                return A[k]
            elif(k<pivot):
                return self.select_helper(A,lo,pivot-1,k)
            else:
                return self.select_helper(A,pivot+1,hi,k)

    def partition(self, A: [int], lo: int, hi: int) -> int:
        p=lo
        r=hi
        print(p,r)                                               
        i=p+1
        j=r-1
        pivot=self.medianOfMedians(A[lo:hi+1])
        print(pivot)
        flag=False
        while not flag:
            while i<=j and A[i]<=A[pivot]:
                i=i+1
            while i<=j and A[j]>=A[pivot]:
                j=j-1
            if j<i:
                flag=True
            else:
                A[i],A[j]=A[j],A[i]
        
        A[p],A[j]=A[j],A[p]
        print(A)
        return j


    def medianOfMedians(self,A):
    	i=0
    	n=len(A)
    	medians=[]
    	while(i<n//5):
    		medians.append(self.calc_median(A[(i*5):(i+1)*5]))
    		i=i+1
    	while(i*5<n):
    		medians.append(self.calc_median(A[i*5:]))
    		i=i+1

    	return self.calc_median(medians)

    def calc_median(self,A):
    	A.sort()
    	return(A[len(A)//2])	

q=QuickSelect()
A=[17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
print(q.select(A,10))