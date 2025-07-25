# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    # TODO: วนลูปแสดงชื่อหนังพร้อมราคาตั๋ว
    print("\n--- รายชื่อหนังทั้งหมด ---")
    for i, movie in enumerate(movie_list):
        print(f"{i + 1}. {movie['movie_name']} - ราคาตั๋ว: {movie['ticket_price']} บาท")
    print("-------------------------")

# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age, age_restriction):
    # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
    # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age
    if age_restriction == 'G':
        return True
    try:
        min_age = int(age_restriction)
        if user_age >= min_age:
            return True
        else:
            return False
    except ValueError:
        # Handle cases where age_restriction might be invalid (e.g., not 'G' and not a number)
        print("ข้อผิดพลาด: ข้อจำกัดอายุไม่ถูกต้อง")
        return False

# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    # TODO: ถ้า genre เป็น 'Romantic' บวกเพิ่ม 50 บาท
    # ถ้าไม่ใช่ คืนราคาเดิม
    if genre == 'Romantic':
        return base_price + 50
    else:
        return base_price

# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    print("\n--- ซื้อตั๋วหนัง ---")
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
    show_movies(movie_list)

    while True:
        try:
            # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
            movie_selection = int(input("กรุณาเลือกหนัง (ป้อนหมายเลข): "))
            if 1 <= movie_selection <= len(movie_list):
                selected_movie = movie_list[movie_selection - 1]
                break
            else:
                print("ตัวเลือกไม่ถูกต้อง กรุณาป้อนหมายเลขที่อยู่ในรายการ")
        except ValueError:
            print("ป้อนข้อมูลไม่ถูกต้อง กรุณาป้อนเป็นตัวเลข")

    # 3. รับอายุผู้ใช้
    while True:
        try:
            user_age = int(input("กรุณาป้อนอายุของคุณ: "))
            if user_age > 0:
                break
            else:
                print("อายุต้องเป็นตัวเลขบวก")
        except ValueError:
            print("ป้อนข้อมูลไม่ถูกต้อง กรุณาป้อนเป็นตัวเลข")

    # 4. ตรวจสอบอายุผ่าน check_age
    # - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
    if not check_age(user_age, selected_movie['age_restriction']):
        print(f"ขออภัย คุณอายุน้อยเกินไปสำหรับหนังเรื่อง '{selected_movie['movie_name']}'")
        print(f"ข้อจำกัดอายุ: {selected_movie['age_restriction']} ปีขึ้นไป (หรือ G สำหรับทุกวัย)")
        return

    # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
    print("\n--- เลือกเสียงพากย์ ---")
    print("1. พากย์ไทย")
    print("2. Soundtrack")
    while True:
        try:
            voice_choice = int(input("เลือกเสียงพากย์ (1 หรือ 2): "))
            if voice_choice == 1:
                selected_voice = "พากย์ไทย"
                break
            elif voice_choice == 2:
                selected_voice = "Soundtrack"
                break
            else:
                print("ตัวเลือกไม่ถูกต้อง กรุณาป้อน 1 หรือ 2")
        except ValueError:
            print("ป้อนข้อมูลไม่ถูกต้อง กรุณาป้อนเป็นตัวเลข")

    # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
    final_price = calculate_price(selected_movie['ticket_price'], selected_movie['genre'])

    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว
    print("\n--- รายละเอียดการซื้อบัตร ---")
    print(f"ชื่อหนัง: {selected_movie['movie_name']}")
    print(f"เสียงพากย์: {selected_voice}")
    print(f"ราคาตั๋ว: {final_price} บาท")
    print("ขอให้มีความสุขกับการรับชม!")
    print("-----------------------------")


def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    while True:
        # TODO: แสดงเมนูให้ผู้ใช้เลือก
        # 1. แสดงหนังทั้งหมด
        # 2. ซื้อตั๋วหนัง
        print("\n--- เมนูหลัก ---")
        print("1. แสดงหนังทั้งหมด")
        print("2. ซื้อตั๋วหนัง")
        print("3. ออกจากโปรแกรม")
        print("----------------")

        # รับค่าตัวเลือกเมนูจากผู้ใช้
        try:
            menu_choice = int(input("เลือกเมนู: "))
            # TODO: ตรวจสอบเมนูที่เลือก
            # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
            # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
            # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง
            if menu_choice == 1:
                show_movies(movies)
            elif menu_choice == 2:
                buy_ticket(movies)
            elif menu_choice == 3:
                print("ออกจากโปรแกรม...")
                break # Exit the loop and end the program
            else:
                print("เมนูไม่ถูกต้อง กรุณาเลือก 1, 2 หรือ 3")
        except ValueError:
            print("ป้อนข้อมูลไม่ถูกต้อง กรุณาป้อนเป็นตัวเลข")

# เรียก main เพื่อเริ่มโปรแกรม
main()