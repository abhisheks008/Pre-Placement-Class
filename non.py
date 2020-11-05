NO_OF_CHARS = 256
def getCharCountArray(string): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)]+= 1
	return count 

def firstNonRepeating(string): 
	count = getCharCountArray(string) 
	index = -1
	k = 0

	for i in string: 
		if count[ord(i)] == 1: 
			index = k 
			break
		k += 1

	return index 

test = int(input("Enter the number of testcases : "))
for i in range (0,test):
    string = input("Enter the string : ")
    index = firstNonRepeating(string) 
    if index == -1: 
	    print ("There is no non-repeating character", -1)
    else: 
	    print ("First non-repeating character is {} and the index position is {}".format(string[index],index)) 


