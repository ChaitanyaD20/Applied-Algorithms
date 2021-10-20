family_dict={}

class FamilyForest:


	def make_family(self, s: str) -> None:

		family_dict[s]=1		#We initialize each family member with 1.
		return

	def union(self, s: str, t: str) -> str:
		# We check the value of using family_dict dictionary using the type() function.

		# If both family_dict[s] and family_dict[t] have integer values, it means they are representatives of their families. 
		# So based on their individual family size, we assign the higher family size as representative. If they are equal, we make s as representative.
		
		if type(family_dict[s])==type(1) and type(family_dict[t])==type(1):
			if (family_dict[s]>=family_dict[t]):
				family_dict[s]+=1
				family_dict[t]=s

			else:
				family_dict[t]+=1
				family_dict[s]=t

		#If both family_dict[s] and family_dict[t] have string values, it means we have to return one of their representatives.
		#So we check the individual values of family_dict[family_dict[s]] and family_dict[family_dict[t]],
		#i.e. their representative's family size and return the family representative with the higher integer value.		
		
		elif type(family_dict[s])==type(s) and type(family_dict[t])==type(t):
			
			#We only check them if both the family representatives are different, othewise it means they are already of the same family.
			if family_dict[s]!=family_dict[t]:
				
				if(family_dict[family_dict[s]]>=family_dict[family_dict[t]]):

					family_dict[family_dict[s]]+=1
					family_dict[family_dict[t]]=family_dict[s]
					family_dict[t]=family_dict[s]

				else:

					family_dict[family_dict[s]]=family_dict[t]
					family_dict[s]=family_dict[t]
					family_dict[family_dict[t]]+=1
		
		#If the family_dict[s] is of type string, and family_dict[t] is of integer, it means, t is a head of an individual family.
		#So we compare the size of s's representative. If family_dict[family_dict[s]]>=family_dict[t], then we assign t and s with representative as family_dict[family_dict[s]].
		#Else we assign them all with representative as t.


		elif type(family_dict[s])==type(s) and type(family_dict[t])==type(1):

			if(family_dict[family_dict[s]]>=family_dict[t]):

				family_dict[t]=family_dict[s]
				family_dict[family_dict[s]]+=1

			else:

				family_dict[t]+=1
				family_dict[s]=t
				family_dict[family_dict[s]]=t

		#This case runs similar to the above elif case.		
				
		elif type(family_dict[s])==type(1) and type(family_dict[t])==type(t):

			if(family_dict[s]<=family_dict[family_dict[t]]):
				family_dict[s]=family_dict[t]
				family_dict[family_dict[t]]+=1

			else:
				family_dict[s]+=1
				family_dict[t]=s
				family_dict[family_dict[t]]=s

		print(family_dict)		
		return s

	#If representative value is an integer, it means it is already the representative of its family, so we return itself.	
	#If representative value is a string, it means we need to return the value of the s as key in dictionary.	
		
	def find(self, s: str) -> str:

		if type(family_dict[s])==type(1):
			
			return s

		elif type(family_dict[s])==type(s):
			
			return family_dict[s]

f=FamilyForest()

family=["Ricardo", "Sean", "Maya", "Ishaan", "Chia-Lin","Dhoni"]
for i in family:
	f.make_family(i)

f.union("Ricardo", "Sean")
f.union("Maya", "Ishaan")
f.union("Sean","Ishaan")
f.union("Sean","Maya")
f.union("Dhoni","Chia-Lin")
print(f.find("Chia-Lin"))