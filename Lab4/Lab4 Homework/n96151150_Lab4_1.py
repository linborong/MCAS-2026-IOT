import time
import board
import adafruit_dht

sensor = adafruit_dht.DHT11(board.D4)

print("學號：n96151150", flush=True)

try:
    while True:
        try:
            temperature = sensor.temperature
            humidity = sensor.humidity
            print(f"溫度：{temperature} °C　濕度：{humidity} %", flush=True)
        except RuntimeError as error:
            print(error.args[0])
        time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    sensor.exit()
