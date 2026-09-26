import RPi.GPIO as GPIO
import time

TOPRAK_NEM_PIN = 21
ROLE_PIN = 19
KIRMIZI_LED_PIN = 27
YESIL_LED_PIN = 17
BUZZER_PIN = 4  

GPIO.setmode(GPIO.BCM)
GPIO.setup(TOPRAK_NEM_PIN, 
GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ROLE_PIN, GPIO.OUT)
GPIO.setup(KIRMIZI_LED_PIN, GPIO.OUT)
GPIO.setup(YESIL_LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

try:
    while True:
        nem_durumu = GPIO.input(TOPRAK_NEM_PIN)

        if nem_durumu == GPIO.LOW:
            GPIO.output(ROLE_PIN, GPIO.HIGH)
            GPIO.output(KIRMIZI_LED_PIN, GPIO.LOW)
            GPIO.output(YESIL_LED_PIN, GPIO.HIGH)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            print("Nem yeterli, sulama durdu.")
        else:
            GPIO.output(ROLE_PIN, GPIO.LOW)
            GPIO.output(KIRMIZI_LED_PIN, GPIO.HIGH)
            GPIO.output(YESIL_LED_PIN, GPIO.LOW)
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            print("Nem yetersiz, sulama basladi.")

        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
