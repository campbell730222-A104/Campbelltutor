# # # # # # # # PR1
# # # # # # # # age=23
# # # # # # # # if age >=18 :
# # # # # # # #     print("您已成年")

# # # # # # # # else :
# # # # # # # #     print("您是未成年人")

# # # # # # # # PR2
# # # # # # # score= 87
# # # # # # # if score >= 90:
# # # # # # #     print("A level")
# # # # # # # elif score >= 80:
# # # # # # #     print("B level")
# # # # # # # elif score >= 70:
# # # # # # #     print("C level")
# # # # # # # elif score >= 60:
# # # # # # #     print("D level")
# # # # # # # else :
# # # # # # #     print("Fail")

# # # # # #  Pr3
# # # # #  a = 10
# # # # #  b = 5
# # # # #  c = 10

# # # # # print(f"a==c :{a==c}")
# # # # # print(f"a!=c :{a!=c}")
# # # # # print(f"a>b :{a>b}")
# # # # # print(f"a<b, :{a<b}")
# # # # # print(f"a<=c :{a<c}")
# # # # # print(f"a>=c :{a>=c}")

# # # # # temperature=int(input("請輸入溫度"))
# # # # # print(temperature)
# # # # # if temperature >=30:
# # # # #     print("非常熱")
# # # # # elif temperature >=20:
# # # # #     print("溫暖")
# # # # # elif temperature >=10:
# # # # #     print("涼爽")
# # # # # else :
# # # # #     print("寒冷") 

# # # # correct_username= "Campbell"
# # # # correct_password= "75014"

# # # # username=input()
# # # # password=input()

# # # # if username==correct_username and password==correct_password:
# # # #     print("帳號密碼正確")
# # # # else:
# # # #     print("ˋ帳號密碼錯誤")

# # # # day=input()
# # # # if day=="Saturday" or "Sunday":
# # # #     print("今天是週末！")
# # # # else:
# # # #     print("今天是工作日")

# # # # is_raining= True
# # # # if not is_raining:
# # # #     print("可以出門")
# # # # else:
# # # #     print("不可以出門")

# # # # PR5
# # # # for i in range(5):
# # # #     print(i)

# # # # for i in range(21):
# # # #     if i % 2 ==0:
# # # #         continue
# # # #     print(i)

# # # fruits=["Grenade", "Figue", "Raisin", "Madarine", "Citron"]
# # # for i in fruits:
# # #     print(f"我喜歡吃 {i}")


# # # total=0
# # # for s in range(101):
# # #     total+=s
# # # print(f"一到一百的總和是: {total}")
# # # i=1
# # # while i < 6:
# # #     print(i)
# # #     i +=  1

# # factorial=1 
# # # factorial=階乘
# # n=1

# # while n <= 10:
# #     factorial *= n
# #     n += 1
# # print(f"十的階乘是{fa}")



# # 猜數字遊戲
# # import random
# # target =random.randint(1,10)
# # guess = 0
# # attempt = 0
# # print("歡迎來到猜數字遊戲")
# # print("我想了一個 1 到 10 之間的數字，請猜猜看！")
# # guess=int(input("請輸入你的猜測："))

# # while target != guess:
# #     guess=int(input("請輸入你的猜測："))
# #     attempt += 1
    
# #     if target == guess:
# #         print(f"恭喜你猜對對了, 正確答案是{target}")
# #         print(f"你總共猜了{attempt}次")
# #         break

# # PR7

# # for i in range(1,21):
# #     if i == 13:
# #         break
# #     print(f"最後印出的數字是{i-1}")

# # numbers= [2, 5, 8, 10, 15, 20, 25, 30]
# # target_number= 15
# # print(f"\n在列表中尋找 {target_number}")
# # for i, num in enumerate(numbers):
# #     if num == target_number:
# #         print(f"找到目標數字{num}, 在index{i}")
# #         break

# for i in range(1,21):
#     if i % 2 == 0:
#         continue
#     print(i)

mixed_list=[1, "hello", 3, "world", 5, "python", 7, 9]
print("\n只處理數字:")
for item in mixed_list:
    if isinstance(item, int):
        print(item)