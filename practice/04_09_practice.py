# # # # """
# # # # input前面加 int，讓他不要辨識成str
# # # # types拿來看變數型態，遇到type error時可用
# # # # """

# # # # hight = int(input("請輸入你的身高:"))
# # # # weight = int(input("請輸入你的體重:"))
# # # # print(hight)
# # # # print(weight)
# # # # print(type(hight))

# # # # if hight >= 190 and weight >= 100:
# # # #     print("高胖")
# # # # elif hight >= 180 and weight < 100:
# # # #     print("高瘦")
# # # # if hight >= 170 or weight >= 190:
# # # #     print("你很屌")
# # # # else:
# # # #     print("你超矮")

# # # # """
# # # # 邏輯 and or not
# # # # and 類似乘法 or 類似加法（有一個有就是true)

# # # # if 和elif差別 if會所有都跑一遍，所以如果藥像上面高胖和你很屌分開判斷，必須用if。如果要一起判斷，用elif就行
# # # # """


# # # for i in range(10) :
# # #     print(i)   
# # # schools=["一中", "二中", "興附"]
# # # for school in schools:
# # #     print(school)
# # """
# # # school為指到的東西（變數） 會print 一中 、二中 etc
# # """


# # for i in range(10):
# #     if i==5:
# #         break
# #     print(i)

# # print("="*20)


# # for i in range(10):   
# #     if i==5:
# #         continue
# #     print(i)

# schools=["台大", "清大", "交通"]
# print(schools[2])
# schools.append("成大")
# print(schools[3])

# schools[2]= "交大"
# print(schools[2])


