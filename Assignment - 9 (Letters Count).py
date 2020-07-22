#Assignment - 9 (Letters Count)


word= input("Enter a sentence 'hippo runs to us!' : ").lower().strip()
output={}
for i in word:
  output[i]=output.get(i,0)+1
print(output)