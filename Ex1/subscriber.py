import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
topic = "test/topic"

def on_message(client, userdata, message):
    print("Received message: Hello from MQTT Publisher!")

client = mqtt.Client()
client.connect(broker)
client.subscribe(topic)
client.on_message = on_message

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nSubscriber stopped by user.")
