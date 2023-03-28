from kafka import KafkaConsumer

consumer = KafkaConsumer('test', bootstrap_servers=['192.168.1.8:9092'])

for message in consumer:
    print(message.value.decode('utf-8'))
