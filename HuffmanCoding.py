from heapq import heappush, heappop, heapify
from typing import Any

class HuffmanCoding:

	def build(self, text : str) -> Any:
	    
	    char_freq={}
	    for i in range(len(text)):
	    	char_freq[text[i]]=0

	    for i in text:
	    	char_freq[i]+=1

	    print(char_freq)

	    heap = [[value, [key, ""]] for key, value in char_freq.items()]

	    heapify(heap)
	    while len(heap) > 1:
	    	low = heappop(heap)
	    	high = heappop(heap)
	    	for pair in low[1:]:
	    		pair[1] = '0' + pair[1]
	    	for pair in high[1:]:
	    		pair[1] = '1' + pair[1]
	    	heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

	    sorted_dict=sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
	    
	    for i in range(len(sorted_dict)):
	    	char_freq[sorted_dict[i][0]]=sorted_dict[i][1]

	    char_freq=dict(sorted(char_freq.items(), key=lambda item: item[1]))
	    encoded=self.encode(char_freq,text)
	    decoded=self.decode(char_freq,encoded)
	    return char_freq
	
	def encode(self, Dic : Any, text : str) -> str:

		encoded=""
		for i in text:
			encoded=encoded+Dic[i]

		return(encoded)


	def decode(self, Dic : Any, text : str) -> str:
		new_dict = dict([(value, key) for key, value in Dic.items()])
		decoded=""
		temp_decode=""

		encoded_chars=[]

		for key,value in new_dict.items():
			encoded_chars.append(key)

		for i in text:
			temp_decode+=i
			if temp_decode in encoded_chars:
				decoded+=new_dict[temp_decode]
				temp_decode=""
			else:
				continue
		
		return(decoded)


h=HuffmanCoding()

text = "this is an example for huffman encoding"

print(h.build(text))
