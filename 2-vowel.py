file1=open("/home/root63/Desktop/vowel.txt","r")
str1=file1.read()
cnt=0
for i in str1:
	if(i=='A'or i=='a'or i=='E'or i=='e'or i=='I'or i=='i'or i=='O'or i=='o'or i=='U'or 	i=='u'):
		cnt+=1
print("no of vowels",cnt)
file1.close()
