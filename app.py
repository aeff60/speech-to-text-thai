import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    # ฟังก์ชัน calibrate จะทำการเรียกเสียงจากไมค์เพื่อทำการปรับค่าเสียง
    # r.adjust_for_ambient_noise(source, duration=5)
    print("Say something!")
    audio = r.listen(source)


    # รอรับค่าจากไมค์และแปลงเป็นข้อความ จนกว่าจะเจอคำว่า "หยุด"
    while True:
        text = r.recognize_google(audio, language="th-TH")
        
        if text != "หยุด":
            print("You said: " + text)
            # รอรับค่าจากไมค์และแปลงเป็นข้อความ จนกว่าจะเจอคำว่า "หยุด"
            audio = r.listen(source)
        else:
            print("You said: " + text)
            break
