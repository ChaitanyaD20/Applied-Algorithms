class HeapSort:

    def heapify(self,A,n,i):
        
        max = i
        
        left = 2*i+1
        right = 2*i+2

        if left<n and A[max]<A[left]:
            max=left

        if right<n and A[max]<A[right]:
            max=right

        if max!= i:
            A[i],A[max] = A[max],A[i]

            self.heapify(A,n,max)
     
    def heapSort(self,A):
        
        n = len(A)

        for i in range((n//2)-1,-1,-1):
            self.heapify(A,n,i)

        for i in range(n-1,0,-1):
            A[i],A[0] = A[0],A[i]
            self.heapify(A,i,0)
