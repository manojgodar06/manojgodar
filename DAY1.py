''''
a=0
for item in [10,20,30]:
    a +=item
print(f'Total is :{a}')
'''
'''for i in range(5):
    if i==0 or i==2:
        print('*'*5)
    else:
        print('*'*2)
 item= [5,2,5,2,2]
 for x_count in item:
     count=''
     for man in range(x_count):
         count +='x'
     print(count)
     '''
numbers=[1,4,2,6,7,8,9,34,67,23]
max=numbers[0]
for item in numbers:
    if item>max:
        max=item
    else:
        continue
print('Largest number is: ',max)
        
