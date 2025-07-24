list1 = ['Akon' , 'Ozzy Osbourne','ILLSLICK','PUN']
# print(len(list1))


#sample1 แสดงแค่ข้อมูลด้านในและได้ค่า I
# for i in range(len(list1)):
#     print(list1[i])

#sample2 แสดงแค่ข้อมูลด้านใน ไม่ได้ค่า I
# for speaker in list1:
#     print(speaker)

# list1[0] = 'Illslick' 
# print(list1)

# list1.append('Akon') #เพิ่มข้อมูล 
# print(list1)

# list1.pop() #ลบข้อมูลทิ้ง 
# print(list1)



# score = [10,20,30,40,50,60]
# sum =  0
# for i in range(len(score)):
#     sum += score[i]
# print('total :',sum)
    

# scorenum = [5,6,7,8,9,10]

# for i in scorenum :
#     if (i % 2 == 0):
#         print('even', i)
#     else:
#         print('odd', i)


# x = {'name':'pun','age':'18','weight':'72kg'}
# print(x['name'],x['age'])

# # x['height'] = 165
# # print(x)

# x['name'] = 'Manop'
# print(x)


z = [
    {'name':'manop' , 'id' :55612 , 'score':99},
    {'name':'yai' , 'id' : 56234 , 'score':91},
    {'name':'sunny' , 'id' : 55421 , 'score':65},
    {'name':'mango' , 'id' : 55421 , 'score':40}
]

for student in z:
    if (student['score'] >= 90 ):
        student['score'] = 'A'

    if (student['score'] >= 80 ):
        student['score'] = 'B'

    # if (student['score'] >= 70 ):
    #     student['score'] = 'C'

    else:
        student["score"] = "F"
    print(student)



# for studnets in student:
#     print(student)