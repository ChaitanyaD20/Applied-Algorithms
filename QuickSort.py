import random

class QuickSort:

    def sort(self,A,p,r):
        if p<r:
            q=self.random_partition(A,p,r)
            self.sort(A,p,q)
            self.sort(A,q+1,r)   

    def random_partition(self,A,p,r):
        random_pivot=random.randrange(p,r)
        A[p], A[random_pivot]=A[random_pivot], A[p]
        return self.partition(A,p,r)        

    def partition(self,A,p,r):
        pivot=A[p]
        i=p+1
        j=r-1
        #print(A[p:r+1])
        print(pivot)
        flag=False
        while not flag:
            while i<=j and A[i]<=pivot:
                i=i+1
            while i<=j and A[j]>=pivot:
                j=j-1
            if j<i:
                flag=True
            else:
                A[i],A[j]=A[j],A[i]
        
        A[p],A[j]=A[j],A[p]
        print(A[p],A[j])
        print(A)
        return j


q=QuickSort()
A=[17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
q.sort(A,0,len(A))
print(A)