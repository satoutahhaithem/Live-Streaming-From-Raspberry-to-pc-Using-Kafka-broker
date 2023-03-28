import cv2
from kafka import KafkaProducer

topic = 'test'

producer = KafkaProducer(bootstrap_servers=['192.168.1.8:9092'])

vc = cv2.VideoCapture(0)

while True:
    ret, frame = vc.read()
    if not ret:
        print("Video stream not available!")
        break

    # Convert the frame to bytes
    is_success, buffer = cv2.imencode('.jpg', frame)
    if not is_success:
        print("Error converting frame to bytes!")
        break

    # Send the frame as a message to Kafka
    producer.send(topic, buffer.tobytes())