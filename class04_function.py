# x = 5 

# def plus():
#     print('Result : ',x+num)

# num = int(input('you num : '))
# plus()

#======================================================

# def sam(a,b):
#     print(a , '+',b ,'=', a + b )

# a = int(input('เลขที่ 1 : '))
# b = int(input('เลขที่ 2 : '))
# sam(a,b)

#======================================================


def add(num1,num2):
   ans =  num1 + num2
   return ans

def minus(num1,num2):
   ans =  num1 - num2
   return ans

def koon(num1,num2):
   ans =  num1 * num2
   return ans

def haan(num1,num2):
   ans =  num1 / num2
   return ans

def is_even(num):
    result = num % 2 == 0
    return result

      

def main():
   num1 = int(input('เลขที่ 1 : '))
   num2 = int(input('เลขที่ 2 : '))   
   print('เลือกเครื่องหมายจ้า')
   print('[1] = + ')
   print('[2] = - ')
   print('[3] = * ')
   print('[4] = / ')
   opa = int(input('เลือกเลขตามเครื่องหมาย : '))

   if (opa == 1):
        result = add(num1,num2)
        print('ผลบวกคือ', result)
   if (opa == 2):
        result = minus(num1,num2)
        print('ผลลบคือ', result)
   if (opa == 3):
        result = koon(num1,num2)
        print('ผลคูณคือ', result)
   if (opa == 4):
        result = haan(num1,num2)
        print('ผลหารคือ', result)
    
   
   
   print('เป็นเลขคู่',is_even(result))

main()