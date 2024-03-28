import paho.mqtt.publish as publish
import random
import time
import datetime

class SensorDataGenerator:
    def __init__(self):
        self.temperature_range = (-50, 50)
        self.humidity_range = (0, 100)
        self.co2_range = (300, 2000)

    def generate_sensor_values(self):
        temperature = random.uniform(*self.temperature_range)
        humidity = random.uniform(*self.humidity_range)
        co2 = random.uniform(*self.co2_range)
        return temperature, humidity, co2

# MQTT Configuration
MQTT_CHANNEL_ID = ""
MQTT_HOST = "mqtt3.thingspeak.com"
MQTT_CLIENT_ID = ""
MQTT_USERNAME = ""
MQTT_PASSWORD = ""
TRANSPORT = "websockets"
PORT = 80
TOPIC = "channels/" + MQTT_CHANNEL_ID + "/publish"

sensor_data_generator = SensorDataGenerator()

while True:
    temperature, humidity, co2 = sensor_data_generator.generate_sensor_values()

    payload = "field1=" + str(temperature) + "&field2=" + str(humidity) + "&field3=" + str(co2)

    # Print logs
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + " Writing Payload=", payload, " to host=", MQTT_HOST, " clientID=", MQTT_CLIENT_ID)

    publish.single(TOPIC, payload, hostname=MQTT_HOST, transport=TRANSPORT, port=PORT, client_id=MQTT_CLIENT_ID, auth={'username': MQTT_USERNAME, 'password': MQTT_PASSWORD})

    time.sleep(5)
