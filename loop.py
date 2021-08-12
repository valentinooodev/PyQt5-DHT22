import Adafruit_DHT
import RPi.GPIO as GPIO
import i2clcd
import websockets
import asyncio
import json
import requests
import serial
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
from time import sleep

API_KEY = 'a7079d4a0a4f425526276dd6356241d8'
api_url = 'http://api.openweathermap.org/data/2.5/weather?q=hanoi&appid=' + API_KEY
ser = serial.Serial('/dev/ttyACM0', 9600)
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "weatherstation-68afe",
  "private_key_id": "72837b1f72c3377c17ce7df062fa13aed2d9197d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDbMNu3Boiq6g8I\n/SbntAx6nO2p+N5cy2CLuBWDqw9PcgU/8YdW/RLl5Z8gAme2DOmeZf7b7Q4//2YZ\na6F8MB44G8Q0bd8Zi8ygkLsbu3BKoNtEfFj4atg+q0hcxVZg2vmws7+C4EbQVHCa\n/nbuZ56SqaU9Z+YKZddNfoBqwWjMx/RM28XB2XfcricopLgsFsObqH70pisyfxIX\nVAcaHtebNZPi+DGOOv/g4Moq5rsA9FtB2fDO4+j2SWrmykFMch8N3vevuc9g99qE\ne0taeJMPi+rotQSCEAQdk4YDHNOwV10AQsai8Seymy2CuxzIFRdzmCq+YviJSDG2\n61mBs7CzAgMBAAECggEACAgqzPKi2Gx6P5CTN+Nbn7SXauaRM2JKd+Q3eZsvlPAv\nLBAsLu5YHm+DHLep2Dxx5RmEtMdjgcnYkm7kvHnA6bpuvqMWDUgXp/yVtqbwLvPl\nBQXvdq7nnKhHHwsmJqdvhd+YUXHpdmHZvHw9nG/Umjg4M19WySPBN3g+uWq77eEG\neXQFH/qqDix/G/KhlRY6V+TfwF99bm/J41f5gtvhN5eiQFhSLakFD49kYn1HOesq\nNnrE2vCQdWqcWUptV2ZarRYpM/hn2alNy3I4JfhgpG05Vg39G0r/tVEnxdniYtV4\nLrjo+LZjMYscQTwP9/vq6sdQrVjJ4exh4F55jcdefQKBgQD7A0rbDsZOoBwIqj/A\nUjnevPsxxyuje1jKOu80kfV4/89ARqR1WNrDSfn044K+Igig5z+1KB8cJuOh0NOq\nGyelM/R0UkXGioZ6NuCiM9jc5t+1lZeyhvh033p44kfwx7HDMtaoJfxgo7ieevxe\nmADXy9epw3tfmeITAW1tje7K7QKBgQDfi7ZFk32LU25TG1ZcWgQu/0X9kwrw1LUk\nuNt71Jr/QZrlp6waqHub/OxGjdX5ObPNXdsQPjPjW60E88S9sZAvLykA0b4IuVMb\nQMHhJiQ0EwwRKFVSRUZADvEet3DRIvj11MSTk0AnYO9EABbhJc3nNapITg5tvVJr\nmBYMVOPWHwKBgE/qN23QoWAs51/22/8d7qC0aADsGT+eKKGR69A/2/ge8VvUYc2e\ncV+VcMf/mwNvkHGxzf2d/XGYDAbbllfk91VIWj6iZuaT+cZ1LEVX3mZN9tE4BCjp\ngbar47ES0badzUGJMQAtv9EArul93FU9bZ9Gna3Ft8SzGF/Wp4Emm+ztAoGBAKN9\nEE8OMREGcXdCVQSxqMGeXFe5hJThW6GBuLN1p+3q0xgGaq4MbmqErWBkNwtQkhkt\n/RqCA3zR/VXT2h1JkUOQ4BIDU1IaB5e04paBSJT1ISwjLVM/6sLKqrlmO5IYW6+e\nbi3n0VF7aUF4N0NuXIouC11aCN9lSLP7xJQ8OWzNAoGBAILte9szvTsvP923dzXv\nNjKYIIjbCCqQ5jSWv27Afj9+KzQH1is0lEeQx5uPG5z3O/VZza2Nw/4ilHttHEi8\nPgYZ/eHZsy5uH91bEnLWYsA8M3pO2UC4op5bdL+oMr3Sv66o7zc4OhMI6IKlC+vh\nFLzcrsFdH1kCFXSRYzCX6c8v\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-bd2ez@weatherstation-68afe.iam.gserviceaccount.com",
  "client_id": "100056067943175860168",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-bd2ez%40weatherstation-68afe.iam.gserviceaccount.com"
}
)

def tele_send(message):
    USER_ID = '1349411358'
    ACCESS_TOKKEN = '1896230537:AAHW2Xnybhrc23LfnuawSsnCS-XLJzKGch8'
    URL = 'https://api.telegram.org/bot' + ACCESS_TOKKEN + '/sendMessage?chat_id='+ USER_ID + '&text=' + message
    res = requests.get(URL)
    print('Send to Telegram: ', message)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN_1 = 4
DHT_PIN_2 = 17
        
initals = firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://weatherstation-68afe-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
root = db.reference('/')
lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr=0x27, lcd_width=20)
lcd.init()
config = db.reference("config/").get()
print(config)
message = ''
check_temp_1 = True
check_temp_2 = True
check_hum_1 = True
check_hum_2 = True

while True:
    push_data = {}
    time = datetime.now()
    ser.flushInput()
    uno_data = ser.readline().decode()
    print(len(uno_data))
    print(uno_data)
    if len(uno_data) == 10:
        light = int(uno_data[0:4])
        rain = int(uno_data[4:8])
        push_data["sensor_light"] = light
        push_data["sensor_rain"] = rain
    else:
        print("Arduino Error")
    response = requests.get(api_url)
    response = response.json()
    push_data["api_temp"] = response["main"]["temp"] - 273.15
    push_data["api_hum"] = response["main"]["humidity"]
    push_data["api_des"] = response["weather"][0]["description"]
    sensor_hum_1, sensor_temp_1 = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN_1)
    sensor_hum_2, sensor_temp_2 = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN_2)
    push_data["sensor_hum_1"] = float("{:.2f}".format(sensor_hum_1))
    push_data["sensor_temp_1"] = float("{:.2f}".format(sensor_temp_1))
    push_data["sensor_hum_2"] = float("{:.2f}".format(sensor_hum_2))
    push_data["sensor_temp_2"] = float("{:.2f}".format(sensor_temp_2))
    root.child(
        "history2/{}-{}-{}/{}/".format(
            time.year, time.month, time.day, time.strftime("%H")
        )
    ).set(push_data)
    print(push_data)
    try:
        if (light < config["light_sensor_sens"] and rain < config["rain_sensor_sens"]):
            des = "rainbow"
        elif (light < config["light_sensor_sens"] and rain >= config["rain_sensor_sens"]):
            des = "clear sky"
        elif (light >= config["light_sensor_sens"] and rain < config["rain_sensor_sens"]):
            des = "rain"
        else:
            des = "clouds"
        if des != message:
            message = des
            tele_send('Weather changed to {}'.format(message))
    except:
        pass

    if (push_data['sensor_hum_1'] >= config['max_hum']) and check_hum_1:
        tele_send('Inside Humidity is too high')
        check_hum_1 = False
    elif (push_data['sensor_hum_1'] <= config['min_hum']) and check_hum_1:
        tele_send('Inside Humidity is too low')
        check_hum_1 = False
    elif (push_data['sensor_hum_1'] >= config['min_hum']) and (push_data['sensor_hum_1'] <= config['max_hum']):
        check_hum_1 = True

    if (push_data['sensor_hum_2'] >= config['max_hum']) and check_hum_2:
        tele_send('Outside Humidity is too high')
        check_hum_2 = False
    elif (push_data['sensor_hum_2'] <= config['min_hum']) and check_hum_2:
        tele_send('Outside Humidity is too low')
        check_hum_2 = False
    elif (push_data['sensor_hum_2'] >= config['min_hum']) and (push_data['sensor_hum_2'] <= config['max_hum']):
        check_hum_2 = True

    if (push_data['sensor_temp_1'] >= config['max_temp']) and check_temp_1:
        tele_send('Inside Temperature is too high')
        check_temp_1 = False
    elif (push_data['sensor_temp_1'] <= config['min_temp']) and check_temp_1:
        tele_send('Inside Temperature is too low')
        check_temp_1 = False
    elif (push_data['sensor_temp_1'] >= config['min_temp']) and (push_data['sensor_temp_1'] <= config['max_temp']):
        check_temp_1 = True

    if (push_data['sensor_temp_2'] >= config['max_temp']) and check_temp_2:
        tele_send('Outside Temperature is too high')
        check_temp_2 = False
    elif (push_data['sensor_temp_2'] <= config['min_temp']) and check_temp_2:
        tele_send('Outside Temperature is too low')
        check_temp_2 = False
    elif (push_data['sensor_temp_2'] >= config['min_temp']) and (push_data['sensor_temp_2'] <= config['max_temp']):
        check_temp_2 = True

    

    

    try:
        lcd.print_line(
            "IS: {}*C, {}%".format(
                push_data["sensor_temp_1"], push_data["sensor_hum_1"]
            ),
            line=0,
        )
        lcd.print_line(
            "OS: {}*C, {}%".format(
                push_data["sensor_temp_2"], push_data["sensor_hum_2"]
            ),
            line=1,
        )
        lcd.print_line("DES: {}".format(des), line=2)
        lcd.print_line("API: {}".format(push_data["api_des"]), line=3)
    except:
        pass

    #ser.flushInput()
