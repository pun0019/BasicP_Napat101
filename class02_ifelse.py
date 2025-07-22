# generation = int(input("ITปัจจุบันรุ่นอะไร"))

# if (generation == 31):
#     print("Correct")
# else :
#     print("Wrong")



# way = int(input("Distance = "))

# if (way < 5):
#     print("ไม่ส่ง")
# elif (way >= 5 and way <= 50):
#     print("10bath")
# elif (way >= 51 and way <= 100 ):
#     print("15bath")
# elif (way >= 101 and way <= 300):
#     print("25bath")
# elif (way >= 301 and way <= 500):
#     print("35bath")
# else:
#     print("45bath")



way = int(input("Distance = "))

if (way < 5):
    print("ไม่ส่ง")
elif (way <= 50):
    print("10bath")
elif (way <= 100 ):
    print("15bath")
elif (way <= 300):
    print("25bath")
elif (way <= 500):
    print("35bath")
else:
    print("45bath")
