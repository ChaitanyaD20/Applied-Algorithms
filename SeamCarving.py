class SeamCarving:
    def carve_seam(self, disruption: [[int]]) -> [int]:
      # Calculate the minimum values and adding into 2D matrix
      minDisruptionArr = []
      for i in range (len(disruption)):
        temp = []
        for j in range (len(disruption[0])):
          if i == 0:	# For the 1st row						
            temp.append(disruption[i][j])
          else:
          
            if j == 0: # for 1st column 
              temp.append(disruption[i][j] + min(minDisruptionArr[i-1][j], minDisruptionArr[i-1][j+1]))
            elif j==len(disruption[0])-1:  # for last column 
              temp.append(disruption[i][j] + min(minDisruptionArr[i-1][j-1], minDisruptionArr[i-1][j]))
            else: # for 2nd to 2nd last column
              temp.append(disruption[i][j] + min(minDisruptionArr[i-1][j-1], minDisruptionArr[i-1][j], minDisruptionArr[i-1][j+1]))
        minDisruptionArr.append(temp)

      minimum = min(minDisruptionArr[i])
      j = minDisruptionArr[i].index(minimum)
      finalResult = [j]
      
      for i in range (len(disruption)-1, 0, -1):
        if j == 0:  # for first column 
          if (minDisruptionArr[i-1][j] < minDisruptionArr[i-1][j+1]):
            finalResult = [j] + finalResult
          else:
            finalResult = [j+1] + finalResult
            j = j+1
        elif j==len(disruption[0])-1:  # for last column
          if (minDisruptionArr[i-1][j-1] <= minDisruptionArr[i-1][j]):
            finalResult = [j-1] + finalResult
            j = j-1
          else:
            finalResult = [j] + finalResult
        else:  # for 2nd to 2nd last column
          if minDisruptionArr[i-1][j] <= minDisruptionArr[i-1][j-1] and minDisruptionArr[i-1][j] <= minDisruptionArr[i-1][j+1]:
            finalResult = [j] + finalResult
          elif minDisruptionArr[i-1][j-1] < minDisruptionArr[i-1][j] and minDisruptionArr[i-1][j-1] < minDisruptionArr[i-1][j+1]:
            finalResult = [j-1] + finalResult
            j = j-1
          else:
            finalResult = [j+1] + finalResult
            j = j+1
      return finalResult

"""
f=SeamCarving()
d=disruption = [
            [1, 2, 0, 3],
            [1, 2, 3, 0],
            [1, 2, 3, 0],
            [1, 2, 0, 3]
        ]
print(f.carve_seam(d))
"""