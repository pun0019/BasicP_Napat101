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
        # print('MONSTER' ,':', monster ,'HP')
        round = int(input('จำนวนครั้งที่ต้องการโจมตี : '))
        for i in range(round):
            print('MONSTER' ,':', monster,'HP')
            print('WEAPON[1] 20 damage')
            print('WEAPON[2] 40 damage')
            print('WEAPON[3] 60 damage')
            print('เหลือการโจทตีอีก', round - i , 'ครั้ง' )
            weapon = int(input('เลือกอาวุธที่ต้องการใช้ : '))
            if (weapon == 1):
                monster -= weapon1
            if (weapon == 2):
                monster -= weapon2
            if (weapon == 3):
                monster -= weapon3
                

            if (monster < 0):
                monster = 20 
                print('ตีแรงเกินมอนคืนชีพ!!!')
           
        if monster == 0 :
            print('Win')
        elif monster > 0:
            print('จำนวนตีหมดแต่มอนไม่แตก คนแตกแทน')

            
        break

    else:
        print('You Run Away!')
        break
            
    