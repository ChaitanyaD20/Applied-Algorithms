import copy
class Scheduling:
    def schedule(self, A : [[int]]) -> int:
        same_day = []
        next_day = []
        output = []
        for i in A:
            if i[0]>i[1]:
                next_day.append(i)
            else:
                same_day.append(i)
        A_copy = copy.deepcopy(same_day)
        A_copy.sort(key = lambda x:x[1])
        r = A_copy[0][1]
        count = 1
        for i in range(1,len(A_copy)):
            start = A_copy[i][0]
            end = A_copy[i][1]
            if start>=r:
                count+=1
                r=end
        output.append(count)
    
        for day in next_day:
            count = 1
            end = day[1]
            start = day[0]
            for j in A_copy:
                if (j[0]>=end) and (j[1]<=start):
                    count+=1
                    end = j[1]
            output.append(count)
        return max(output)
        