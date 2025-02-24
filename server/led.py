# my_project/module1.py
import RPi.GPIO as GPIO
import time

# 设置GPIO的编号模式
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # 禁用警告

# 定义GPIO引脚
LED_PIN = 17  # 使用GPIO17引脚

# 设置GPIO引脚为输出模式
GPIO.setup(LED_PIN, GPIO.OUT)

def greet(name):
    return f"Hello, {name}!"

def openLed():
    # 打开LED灯
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED ON")
    time.sleep(2)  # 保持2秒

def closeLed():
    # 关闭LED灯
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED OFF")
    time.sleep(2)

def cleanup():
    # 清理GPIO引脚
    GPIO.cleanup()
    print("LED cleanup")

def autoLightLed():
    count = 0
    while count < 20:
        # 自动打开LED灯
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(2)  # 保持2秒
        # 自动关闭LED灯
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(2)
        count += 1
    cleanup()