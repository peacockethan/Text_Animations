import time
import random
import os

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','<',' ','>', '9']
alen=len(alphabet)

def print_letter(prefix, a, postfix):
	correct_flag = False
	while correct_flag is False:
		time.sleep(0.005)
		xchar=alphabet[random.randint(0,alen-1)]
		print(prefix,end='')
		print(xchar,end='')
		print(postfix)
		if a == xchar:
			correct_flag = True
			break
			
prefix = ''
word = 'hello there'
postfix=''
for char in word:
	print_letter(prefix, char, postfix)
	prefix += char
	
prefix2 = ''
word2 = 'how are you today'
for i in range(len(word2)):
	postfix2= word[(i+1):]
	print_letter(prefix2,word2[i],postfix2)
	prefix2 += word2[i:i+1]
	


# TODO: make it possible to pass a message thread in:
# align receiver left and sender right like message thread
# use screen clear and running history to print out encrypted message
# animation in message thread format