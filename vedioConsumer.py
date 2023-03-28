from kafka import KafkaConsumer
import cv2
import numpy as np

topic = 'test'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=['192.168.1.8:9092'],
)

cv2.namedWindow("Video Feed")

for msg in consumer:
    nparr = np.frombuffer(msg.value, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow("Video Feed", frame)
    
    # Check for the 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()
