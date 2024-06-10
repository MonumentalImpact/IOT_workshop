from umqtt.simple import MQTTClient

CLIENT_NAME = 'mp1'
BROKER_ADDR = 'pi5ub.local'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=60)

mqttc.publish(b'art/emotion', 'sad')
