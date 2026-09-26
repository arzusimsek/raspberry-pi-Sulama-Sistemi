[github_readme_ablonu.md](https://github.com/user-attachments/files/32688967/github_readme_ablonu.md)
# 🌱 Akıllı Saksı Sulama Sistemi (Smart Plant Watering System)

---

## 📌 Proje Hakkında

Bu proje, bitkilerin toprak nem seviyesini anlık olarak izleyerek sulama ihtiyacını otomatik tespit eden ve gerektiğinde sulama motorunu devreye sokan Raspberry Pi tabanlı bir sistemdir.

### ⚙️ Çalışma Mantığı

* **Nem Yeterli:** Yeşil LED yanar, kırmızı LED ve buzzer kapalıdır; sulama motoru pasiftir.
* **Nem Yetersiz:** Toprak kuruduğunda sistem otomatik olarak sulama motorunu (röle üzerinden) çalıştırır. Aynı anda kırmızı LED yanar ve sesli uyarı için buzzer öter.

---

## 🛠️ Kullanılan Donanım Bileşenleri

* **Raspberry Pi** (GPIO desteği olan model)
* **Toprak Nem Sensörü** (Dijital çıkışlı prob & modül)
* **Röle Modülü** (5V / Tekli/Çiftli)
* **Mini Dalgıç Su Pompası / Motoru**
* **Harici Güç Kaynağı** (Pil yuvası - Motor beslemesi için)
* **Buzzer** (Aktif/Pasif ses modülü)
* **LED'ler:** 1x Yeşil LED, 1x Kırmızı LED
* **Breadboard & Jumper Kablolar**

---

## 🔌 Bağlantı Şeması (Pinout)

| Bileşen | Bileşen Pini | Raspberry Pi / Diğer Bağlantı |
| :--- | :--- | :--- |
| **Toprak Nem Sensörü** | VCC | 5V |
| | GND | Ground (GND) |
| | DO (Digital Out) | **GPIO 21** |
| **Röle Modülü** | VCC | 5V |
| | GND | Ground (GND) |
| | IN2 | **GPIO 19** |
| | COM | Harici Pil (+) Ucu |
| | NO (Normally Open) | Su Motoru (+) Ucu |
| **Su Motoru** | (-) Uç | Harici Pil (-) Ucu |
| **Yeşil LED** | Anot (+) | **GPIO 17** |
| | Katot (-) | Ground (GND) |
| **Kırmızı LED** | Anot (+) | **GPIO 27** |
| | Katot (-) | Ground (GND) |
| **Buzzer** | Pozitif (+) | **GPIO 4** |
| | Negatif (-) | Ground (GND) |

> ⚠️ *Not: LED'ler kullanılırken akım koruma dirençleri (örn. 220Ω - 330Ω) kullanılması önerilir.*

---

## 💻 Kurulum ve Çalıştırma

### 1. Depoyu Klonlayın

```bash
git clone https://github.com/KULLANICI_ADINIZ/akilli-saksi-sulama-sistemi.git
cd akilli-saksi-sulama-sistemi
```

### 2. Gerekli Kütüphaneleri Yükleyin

Raspberry Pi üzerinde GPIO pinlerini kontrol etmek için:

```bash
sudo apt-get update
sudo apt-get install python3-rpi.gpio
```

### 3. Programı Başlatın

```bash
python3 main.py
```

*(Programı durdurmak için klavyeden `Ctrl + C` kombinasyonunu kullanabilirsiniz.)*

---

## 📝 Kaynak Kod (`main.py`)

```python
import RPi.GPIO as GPIO
import time

# Pin Tanımlamaları (BCM Formatında)
TOPRAK_NEM_PIN = 21
ROLE_PIN = 19
KIRMIZI_LED_PIN = 27
YESIL_LED_PIN = 17
BUZZER_PIN = 4  

GPIO.setmode(GPIO.BCM)
GPIO.setup(TOPRAK_NEM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ROLE_PIN, GPIO.OUT)
GPIO.setup(KIRMIZI_LED_PIN, GPIO.OUT)
GPIO.setup(YESIL_LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

try:
    print("Sistem baslatildi. Nem degeri okunuyor...")
    while True:
        nem_durumu = GPIO.input(TOPRAK_NEM_PIN)
        
        if nem_durumu == GPIO.LOW:
            # Nem yeterli durumu
            GPIO.output(ROLE_PIN, GPIO.HIGH)
            GPIO.output(KIRMIZI_LED_PIN, GPIO.LOW)
            GPIO.output(YESIL_LED_PIN, GPIO.HIGH)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            print("Nem yeterli, sulama durdu.")
        else:
            # Nem yetersiz durumu
            GPIO.output(ROLE_PIN, GPIO.LOW)
            GPIO.output(KIRMIZI_LED_PIN, GPIO.HIGH)
            GPIO.output(YESIL_LED_PIN, GPIO.LOW)
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            print("Nem yetersiz, sulama basladi.")
            
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram kullanıcı tarafından sonlandırıldı.")
finally:
    GPIO.cleanup()
```
