number=[1,1,2,3,4,4,5,5,6,6,7,7,7,8,8,9,9,0,0,0]
unique=[]
for item in number:
    if item not in unique:
         unique.append(item)
        
print(unique) 