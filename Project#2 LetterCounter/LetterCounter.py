txt=input("Enter the Text: ")
c=False
cnt=0

def check(word,cnt):
	if word in txt:
		for i in txt:
			if i == word :
				cnt=cnt+1
		print()
		print("***********", cnt, "Matches Found**************")
	else:
		print()
		print("***********No Matches Found*********************")
while c==False:
	word = input("Enter the word/string to search:")
	if len(word) == 1:
		check(word,cnt)
		c=True
	else:
		print()
		print("***************Please Enter Only One word/string**********************")