#this is a comment 
#print hello world
print("hello world!!")

'''
this is 
 example of 
 multiple line comments
'''

"""
this is 
 example of 
 multiple line comments

 """

 #variables in python

a=10
b=10.5
c="Twinkle Shukla"

print(a)
print("value of b is:",b)
print("company nameis :",c) 

name="twinkle Shukla"
print("Name is:",name)

#assigning a new value to website

name="Twinkle.com"
print("Name is:",name)

#assigning multiple values to multiple variables

a,b,c=10,10.5,"Twinkle Shukla"

print(a)
print("value of b is:",b)
print("company name is:",c)


a=b=c=10

print("value of a is:",a)
print("value of b is:",b)
print("value of c is:",c)

#number data-type

n1=10
print(n1,"is type of",type(n1))

n2=10.5
print(n2,"is type of",type(n2))
print(n2,"is complex number?",isinstance(10.5,int))

n3=1+2j
print(n3,"is complex number?",isinstance(1+2j,complex))

#string data-type
name="twinkle shukla"
print("name is:",name)

print(name[0])
print(name[2:5])
print(name[2:])
print(name*5)
print(name+ "hello how r u")

#list data-type
l1=[10,10.5,'twinkle shukla is here']
print(l1)

l2=[10,20,30,"twinkle",40,50,"shukla",60]
print("l2[2]=",l2[2])

print("l2[0:3]=",l2[0:3])

print("l2[5:]=",l2[5:])

t1=(10,20,30,"twinkle",40,50,"shukla",60)
print(t1)

print("t1[2]=",t1[2])

print("t1[0:3]=",t1[0:3])

print("t1[5:]=",t1[5:])

#dictionary data-type 
d={1:'abc',2:'def','key':9}
print(type(d))

print("d[1]=",d[1])

print("d[2]=",d[2])

print("d['key']=",d['key'])

