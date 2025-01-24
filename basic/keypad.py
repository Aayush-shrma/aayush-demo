x=["what is your name?:","what is your age?:","what is your gender?:","r u gay?:"]
Y=[("a.aayush","b.kezno","c.carlJohsnson","d.demon"),("a.19","b.20","c.21","c.22"),("a.male","b.female"),("a.yes","b.no")]
no=0
count=0
a=[]

ans=['a','a','a','b']

for i in x:
  print("--------")
  print(i)

  for options in Y[no]:
    print(options)


  k=str(input("whats your ans?:"))
  a.append(k)
  no+=1

for i in range(0,4):
  if(a[i]==ans[i]):
    print(f"Question no {i+1} is correct")
    count+=1
  else:
    print(f"question no {i+1} is incorrect!")
  