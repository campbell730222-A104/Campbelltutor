# # # # high_school=["一中", "二中", "文華"]
# # # # print(high_school)
# # # # print(high_school[1])
# # # # high_school.append("興附")
# # # # print(high_school[3])

# # # # for x in high_school:
# # # #     print(x)


# # # # dictionnary practice
# # # from rich import print
# # # user_info={
# # #     "姓名":"廖柏誠",
# # #     "性別":"男性",
# # #     "年齡":22
# # #            }
# # # print(user_info)
# # # user_info["國籍"]= "台灣"
# # # user_info["居住地"]= "巴黎"
# # # print(user_info)
# # # print(user_info["年齡"])
# # # user_info["年齡"]= 25
# # # print(user_info["年齡"])

# # # def user_name(name):
# # #     print(f"你好, 我叫 {name}")

# # # def user_inf0(name, age):
# # #     print(f"我叫{name}, 我今年{age}")

# # # user_inf0("廖柏誠", 23)
# # # user_name("Liao BO Cheng")
# # # user_name("Liao BO Cheng")
# # # user_name("廖柏誠")

# # def user_info(name, age):
# #     output_string=f"我叫{name}, 我今年{age}"
# #     return output_string
# # x=user_info("廖柏誠", 23)
# # print(user_info("廖柏誠", 23))  
# # # print 將name跟age帶入fontion 可以用x=fonction(name,age)
# # # print(x)


# # default用法
# def user_info(name="廖柏誠",age=23):
#     output_string= f"我叫{name}，我今年{age}歲\n"
#     output_string_english= f"I'm {name}, I'm {age} years old\n"
#     output_string_french= f"j'mappelle{name}, j'ai {age}\n"
    
#     return output_string, output_string_english, output_string_french

# output_string= user_info("campbell", 23)

# print(output_string)

# # x=user_info("廖柏誠", 24)
# # print(x)

# # y=user_info()
# # print(y)

# # z=user_info("白宗民")
# # print(z)

# numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
# unique_numbers = {1, 5, 4, 3, 1, 1, 5, 4}

# print(f"原列表: {numbers_list}")
# print(f"去重後的集合: {unique_numbers}")



numbers_str = "1,2,3,2,4,3,5,1"
numbers_list = list(numbers_str)