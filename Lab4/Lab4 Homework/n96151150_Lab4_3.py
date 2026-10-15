import serial
import time

ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=2)

try:
    ser.reset_input_buffer()
    print("學號：n96151150", flush=True)

    while True:
        message = input("輸入要傳送的數字或文字：")
        ser.write((message + "\n").encode("utf-8"))
        ser.flush()

        received = ser.readline().decode("utf-8").strip()
        print(f"已傳送：{message}")
        print(f"已收到：{received}" if received else "未收到資料，請檢查接線")
        time.sleep(0.2)

except KeyboardInterrupt:
    print("\n程式停止")
finally:
    ser.close()
