# # # # # # # # # # # # # user1= "bob"
# # # # # # # # # # # # # user2= "max"
# # # # # # # # # # # # # print("user name is " + user1 + "user 2 nmae is " + user2)
# # # # # # # # # # # # # print(f"user name is {user1}, user2 name is {user2} ")
# # # # # # # # # # # # """
# # # # # # # # # # # # 0828 rich pratice
# # # # # # # # # # # # phoque
# # # # # # # # # # # # """
# # # # # # # # # # # # from rich import print
# # # # # # # # # # # # data = {
# # # # # # # # # # # #     "使用者資訊": {
# # # # # # # # # # # #         "姓名": "李小華",
# # # # # # # # # # # #         "年齡": 22,
# # # # # # # # # # # #         "技能": ["Python", "機器學習", "資料分析"],
# # # # # # # # # # # #         "專案": [
# # # # # # # # # # # #             {"名稱": "網站開發", "完成": True},
# # # # # # # # # # # #             {"名稱": "AI 聊天機器人", "完成": False}
# # # # # # # # # # # #         ]
# # # # # # # # # # # #     }
# # # # # # # # # # # # }
# # # # # # # # # # # # print(data)

# # # # # # # # # # # # x = 10
# # # # # # # # # # # # x **= 3
# # # # # # # # # # # # print(x)
# # # # # # # # # # # # print()
# # # # # # # # # # # # y = 10
# # # # # # # # # # # # y = y/6.9
# # # # # # # # # # # # print(y)
# # # # # # # # # # # # print()
# # # # # # # # # # # # z = 5 
# # # # # # # # # # # # z = 5+2-10
# # # # # # # # # # # # print(z)
# # # # # # # # # # # # print()
# # # # # # # # # # # # b = 7//3 
# # # # # # # # # # # # print(b)
# # # # # # # # # # # # c = 7/2
# # # # # # # # # # # # print(c)
# # # # # # # # # # # # print()
# # # # # # # # # # # # print(0/0)ls
# # # # # # # name= "廖柏誠"
# # # # # # #  age=23
# # # # # # #  school="索邦大學"
# # # # # # #  program="Erasmus TPTI"
# # # # # # #  print(f"我是{name} , 今年{age}歲 , 就讀於{school} {program}")
# # # # # # #  print(f"10年後我將{age+10}歲")
# # # # # # # # # # # pi = 3.14159265359
# # # # # # # # # # # price = 1250.5
# # # # # # # # # # # success_rate = 0.873
# # # # # # # # # # # print(f"圓周率約為 {pi:.2f}")
# # # # # # # # # # # print(f"這件商品的價格是 {price:.2f} 元")
# # # # # # # # # # # print(f"成功率為 {success_rate:.1%}")
# # # # # # # # # # fruits = ["蘋果", "香蕉", "橘子", "葡萄"]
# # # # # # # # # # print(" | ".join(fruits) )
# # # # # # # # # # print("載入中", end="fruits")
# # # # # # # # # # print(".", end ="")
# # # # # # # # # # print(".", end ="")
# # # # # # # # # # print(".", end ="")
# # # # # # # # # # # print(" 完成!")
# # # # # # # # # poem = """
# # # # # # # # # 同是天涯淪落人，相逢何必曾相識。
# # # # # # # # # 我從去年辭帝京，謫居臥病潯陽城。
# # # # # # # # # 潯陽地僻無音樂，終歲不聞絲竹聲。
# # # # # # # # # 住近湓江地低濕，黃蘆苦竹繞宅生。

# # # # # # # # # """
# # # # # # # # # print(poem)

# # # # # # # # # """

# # # # # # # # # 相逢何必曾相識 - 
# # # # # # # # # 出自唐代白居易的《琵琶行》。
# # # # # # # # # 這句詩的意思是：我們都是在外漂泊的人，
# # # # # # # # # 既然相遇了，何必在乎是否認識對方呢？這表達了一種淡泊名利、重視當下相聚的情感。

# # # # # # # # # """
# # # # # # # # students = [
# # # # # # # #     {"name": "張小明", "math": 95, "english": 88, "science": 92},
# # # # # # # #     {"name": "李小華", "math": 87, "english": 94, "science": 89},
# # # # # # # #     {"name": "王小美", "math": 92, "english": 85, "science": 96}
# # # # # # # # ]
# # # # # # # # print(f"{'姓名':<8}{'數學':<6}{'英文':<6}{'理化':<6}")
# # # # # # # # print("-" * 26)
# # # # # # # # for student in students:
# # # # # # # #     print(f"{student['name']:<8}{student['name']:>8}{student['name']:>8}{student['name']:>8}")
# # # # # # # total_tasks = 50
# # # # # # # completed_tasks = 30
# # # # # # # barlength = 30
# # # # # # # percentage =( completed_tasks / total_tasks) * 100
# # # # # # # print(percentage)
# # # # # # # filled_length = int(barlength * completed_tasks // total_tasks)
# # # # # # # bar =  "█" * filled_length + "░" * (barlength - filled_length)
# # # # # # # print(f"進度：|{bar}| {percentage: .1f}% {completed_tasks}/{total_tasks}")
# # # # # # # import json
# # # # # # # course_info = {
# # # # # # #     "課程名稱": "Python 程式設計",
# # # # # # #     "授課教師": "Tsung-Min Pai",
# # # # # # #     "學分數": 3,
# # # # # # #     "上課時間": {
# # # # # # #         "星期": "二",
# # # # # # #         "節次": ["2", "3", "4"]
# # # # # # #     },
# # # # # # #     "學生名單": [
# # # # # # #         {"姓名": "張同學", "學號": "B10901001", "出席率": 0.95},
# # # # # # #         {"姓名": "李同學", "學號": "B10901002", "出席率": 0.88},
# # # # # # #         {"姓名": "王同學", "學號": "B10901003", "出席率": 0.92}
# # # # # # #         ]
# # # # # # #     }
# # # # # # # print(course_info)
# # # # # # # print("=== 一般 print() 輸出 ===")
# # # # # # # print("=== JSON 格式化輸出 ===")
# # # # # # # print(json.dumps(course_info, ensure_ascii=False, indent=2))
# # # # # # # my_name = "Liao Bo-Cheng"
# # # # # # # print(my_name)
# # # # # # # age = 23
# # # # # # # print(age)
# # # # # # # name="廖柏誠"
# # # # # # # age=23
# # # # # # # school="索邦大學"
# # # # # # # program="Erasmus TPTI"
# # # # # # # print(f"我是{name} , 今年{age}歲 , 就讀於{school} {program}")
# # # # # # # print(f"10年後我將{age+10}歲")
# # # # # # student = [
# # # # # #     {"name": "張小明", "math": 95, "english": 88, "science": 92},
# # # # # #     {"name": "李小華", "math": 87, "english": 94, "science": 89},
# # # # # #     {"name": "王小美", "math": 92, "english": 85, "science": 96}
# # # # # # ]
# # # # # # print(f"{'姓名':<8}{'數學':<6}{'英文':<6}{'理化':<6}")
# # # # # # print("-" * 26)
# # # # # # for student in student:
# # # # # #     print(f"{student['name']:<8}{student['name']:>8}{student['name']:>8}{student['name']:>8}")
# # # # # #     print
# # # # # #     pass
# # # # # # print("\n=== 修正完成後的正確輸出 ===")
# # # # # # print("Hello World")
# # # # # # print( "我是" + "廖柏誠" + "，今年" + "23" + "歲")
# # # # # # print("身高:", "height")
# # # # # # print("他說：今天天氣很好")
# # # # # from rich.table import Table
# # # # # from rich.console import Console
# # # # # student_name = "Liao Bo Cheng"
# # # # # student_id = 104200123
# # # # # major = "TPTI"
# # # # # year = "M1"
# # # # # gpa = 3.98
# # # # # courses = [
# # # # #     {"name": "電子煙初級", "credit": 5, "grade": 85},
# # # # #     {"name": "紙菸中級", "credit": 3, "grade": 75},
# # # # #     {"name": "大麻菸初級", "credit": 1, "grade": 50}
# # # # # ]
# # # # # print("=" * 30)
# # # # # print(f"{'學生資訊系統':^30}")
# # # # # print("=" * 30)
# # # # # print(f"'姓名': {student_name}")
# # # # # print(f"'學號' : {student_id}")
# # # # # print(f"'科系': {major}")
# # # # # print(f"'年級':{year}")
# # # # # print("-" * 30)
# # # # # print(f"{'課程名稱':<12} {'學分':<6} {'成績':<6}")
# # # # # print("-" * 30)
# # # # # for course in courses:
# # # # #     print(f"{course['name']:<12} {course['credit']:<6} {course['grade']:<6}")


# # # # students = [
# # # #     {"name": "張小明", "math": 95, "english": 88, "science": 92},
# # # #     {"name": "李小華", "math": 87, "english": 94, "science": 89},
# # # #     {"name": "王小美", "math": 92, "english": 85, "science": 96}
# # # # ]

# # # # name= '姓名'
# # # # math= '數學'
# # # # english= '英文'
# # # # science='理化'
# # # # print(f"{name:<8}{math:<5}{english:<5}{science:<5}")
# # # # print("_" *30)
# # # # for student in students :
# # # #     # print(f"{student['name']:<8} {student['math']:<5} {student['english']:<5} {student['science']:<5}")
# poem="""
# sep 是 print 的參數，控制「項目之間」要放什麼。
# join 是 字串的方法，把 list 黏成一個字串
# """
# fruits = ["蘋果", "香蕉", "橘子", "葡萄"]
# print(*fruits, sep=" | ")
# # # print("載入中", end="")
# # # print(".", end="")
# # # print(".", end="")
# # # print(".", end="")
# # # print("完成!", end="")
# # name="shireen"
# # age=23
# # print(f"我是{name}, 今年{age}歲")

# pi = 3.14159265359
# price = 1250.5
# success_rate = 0.873
# print(f"圓周率約為{pi:.3f}")
# print(f"價格約為{price:.0f}")
# print(f"輸出百分成功比約為{success_rate:.3f}")


