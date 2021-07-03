import hashlib
user =input("enter a string name ")
user1= input("enter a password")
priya=hashlib.md5(user.encode())
priya1=hashlib.md5(user1.encode())
p2=priya.hexdigest()
p3=priya1.hexdigest()
print(p2)
print(p3)

