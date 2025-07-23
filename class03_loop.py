# for i in range(5):
#     i + 1 
#     print(i)

#---------------------------------------------------

# for i in range(1 , 10 ,2):
#     print(i)


#--------------------------------------------------

# for i in range(5):
#     print('halo')


#--------------------------------------------------

# sum = 0
# n = 3

# for  i in range(n):
#     sum += i+1
# print(sum)

#--------------------------------------------------

# for i in range( 1 , 10 ):
#     if (i % 2) == 0:
#         print(i, 'is even num')

#--------------------------------------------------

#WorkSHOP
#ตารางสูตรคูณ

# yournum = int(input('Input your num : '))

# for i in range(1,13):
#     ans = yournum * i
#     print (yournum , 'x' ,i , '=' , ans )


    # print(f"{yournum} * {i} = {ans}") การปริ้นโดยที่ไม่ให้ติดตัวแปรอีกแบบนึงโดนไม่ใช่ quote

#------------------loopWHILE------------------------



# i = 0
# while i < 5:
#     i = i + 1
#     print('hello' , i)
    
#--------------------------------------------------

monster = 100
weapon1 = 20 
weapon2 = 40 
weapon3 = 60 


start = True
while  start:
    print('Fight or Run Away?')
    print('choose way [1] : Fight ')
    print('choose way [2] : Run Away ')
    x = int(input('Choose way : '))
    
    if (x == 1):
        
        print('You will Fight with a MONSTER!!')
        print('MONSTER' ,':', monster ,'HP')
        round = int(input('จำนวนครั้งที่ต้องการโจมตี : '))
        for i in range(round):
            # print('MONSTER' ,':', monster,'HP')
            print('WEAPON[1] 20 damage')
            print('WEAPON[2] 40 damage')
            print('WEAPON[3] 60 damage')
            print('เหลือการโจทตีอีก', round - i , 'ครั้ง' )
            weapon = int(input('เลือกอาวุธที่ต้องการใช้ : '))
            if (weapon == 1):
                monster -= weapon1
            if (weapon == 3):
                monster -= weapon2
            if (weapon == 2):
                monster -= weapon3

            
        break


    else:
        print('You Run Away!')
        break
            
    


    


