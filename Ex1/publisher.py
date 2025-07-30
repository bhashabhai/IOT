import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
topic = "test/topic"

client = mqtt.Client()
client.connect(broker, 1883, 60)
client.publish(topic, "Hello from MQTT Publisher!")
client.disconnect()