class InversionCount:
    
    def count(self, A: [int]) -> [int]:
        ans=[0]*len(A)
        index_a=[0]*len(A)
        for i in range(len(A)):
            index_a[i]=i
        self.sort(A,0,len(A)-1,ans,index_a)
        return ans


    def merge(self,A,p,q,r,ans,index_a):
        L = index_a[p:q+1]
        R = index_a[q+1:r+1] 
        i=0
        j=0
        k=p
        ans_count=0
        print(L,R)
        while(i<len(L) and j<len(R)):
            if(A[L[i]]<=A[R[j]]):
                ans[L[i]]=ans[L[i]]+ans_count
                print(ans)
                index_a[k]=L[i]
                k=k+1
                i=i+1
            else:
                ans_count=ans_count+1
                index_a[k]=R[j]
                k=k+1
                j=j+1
              
                
        while(i<len(L)):
            ans[L[i]]=ans[L[i]]+ans_count
            index_a[k]=L[i]
            i=i+1
            k=k+1

        while(j<len(R)):
            index_a[k]=R[j]
            j=j+1
            k=k+1
        

    def sort(self,A,p,r,ans,index_a):
        if(p<r):
            q=p+(r-p)//2
            self.sort(A,p,q,ans,index_a)
            self.sort(A,q+1,r,ans,index_a)
            self.merge(A,p,q,r,ans,index_a)

i=InversionCount()
A = [5,4,7,9,2]
print(i.count(A))