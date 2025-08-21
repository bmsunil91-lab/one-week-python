list=["the","cat","in","the","bottom"]
dict={}
for i in list:
  if i in dict:
    dict[i]+1
  else:
    dict[i]=1
    print(dict)