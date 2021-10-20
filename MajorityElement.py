class MajorityElement:
    def majority(self, A):
        dictionary={}
        for i in range(len(A)):
            if A[i] in dictionary:
                dictionary[A[i]]+=1
            else:
                dictionary[A[i]]=1
        for element in dictionary:
            if dictionary[element]>len(A)//2:
                return element
            else:
                continue
        return -1

