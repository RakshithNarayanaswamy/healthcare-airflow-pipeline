from kafka import KafkaProducer
import json
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_event():
    event = {
        "pipeline": "healthcare_vitals_pipeline",
        "status": "SUCCESS",
        "timestamp": datetime.utcnow().isoformat()
    }

    producer.send("airflow_pipeline_events", event)
    producer.flush()
    print("Kafka event sent:", event)