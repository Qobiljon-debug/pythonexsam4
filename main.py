###задача1
# numbers = [10, 20, 30]

# for i in range(len(numbers)):
#     print(numbers[i])

###задача2
# x = int(input("Enter: "))

# try:
#     print(100 / x)
# except:
#     print("Error")
# finally:
#     print("float harf namegirad: ")

### Задача 3
# name="Admin"
# if name == "Admin":
#     print("Welcome")

### Задача 4
# import random

# print(random.randint(1,100))

### Задача 5
# file = open("data.txt","w")
# file = open("data.txt", "r")
# file.close()

# string=(input("Enter your text: "))
# res=len(string)
# world=len(string.split())
# cnt=0
# hello=""
# for i in string:
#     if i.lower() in hello:
#         cnt=cnt+1
# reserv=string[::-1]
# print(res)
# print(world)
# print(cnt)
# print(hello)
## Часть 2

### Задача 1
# text=input("Enter your world: ")
# print(F"{len(text)}")

# res=text.split()
# print(f"darozi{len(res)}")
# hello="hello"
# cnt = 0
# for i in text:
#     if i in hello:
#         cnt+=1
# print(cnt)

# res2=""
# for n in text:
#     res2=i+res2
# print(f"sadonok{res2}")

# print(text[::1])

# res2=""
# for i in text:
#     if i in text:
#         print(f"{res2}")



### Задача 2
# res=[]
# for i in range(30):
#     res.append(res.randit(1,30))

# print(res)
# print(max(res))
# print(min(res))
# print(sum(res) / 30)
# even = 0
# for i in res:
#     if i%2!=0:
#         even=even+1
# print(even)
# res.sort()
# print(res)


### Задача 4
# file=open()
# file =open("stuedends.txt","w")
# while True:
#     name=input("Enter: ")
#     if name=="stop":
#         break
#     file.write(name)
# file.close()
# st=[]
# file=open("Students.txt","r")
# for s in st:
#     st.append(s.strip())
#     file.close()
#     st.sort()
#     for i in st:
#         print(st)

# class student:
#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score
#     def show_info(self):
#         print(f"{self.name}---{self.age}----{self.score}")

# st1=student("Ali",10,80)
# st2=student("Vali",20,90)
# st3=student("Saidvali",30,100)
# group=[st1,st2,st3]

# for i in group:
#     i.show_info()

# best=group[0]
# for i in group:
#     if i.score > best.score:
#         best=i
# print(best.name,best.score)
# for i in group:

#     sredniy_group = sredniy_group + i.score
# print(sredniy_group / len(group))