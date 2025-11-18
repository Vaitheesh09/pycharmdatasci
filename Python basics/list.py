
#create
li=[]
for i in range(1,15):
    li.append(i)

print(li)

#append()
li.append(15)
print(li)

#insert
li.insert(8,0)
print(li)

#remove
li.remove(0)
print(li)

#pop
li.pop()
print(li)

#reverse
li.reverse()
print(li)

#count
print(li.count(4))

#list Slicing

a=li[:2]
b=li[-2:]
c=li[2:5]
d=li[1:10:2]
print(a)
print(b)
print(c)
print(d)

#index position printing
for i,v in enumerate(li):
    print(f"indx:{i}-value:{v}")