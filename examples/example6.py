from httpMethods import *

# Reads from Kafka JSON in the format {"temperature": degrees, "date": "thedate"} and sends JSON back to Kafka if the temperature is 30 degrees or higher.
post('/api/actors', {"data": {"type": "actors", "attributes": {"type":"kafka-consumer", "params": {"topic": "source", "kafka": {"zookeeper.connect": "localhost:2181", "group.id": "uniqueid"}}}}})
post('/api/actors', {"data": {"type": "actors", "attributes": {"type":"threshold", "params": {"key": "temperature", "threshold": 30}}}})
post('/api/actors', {"data": {"type": "actors", "attributes": {"type":"json", "params": {"template": {"message": {"temperature": "${temperature}", "date": "${date}"}}}}}})
post('/api/actors', {"data": {"type": "actors", "attributes": {"type":"kafka-producer", "params": {"topic": "destination", "kafka": {"metadata.broker.list": "localhost:9092"}}}}})

patch('/api/actors/2',  {"data": {"type": "actors", "id": "2", "attributes": {"input":{"trigger":{"in":{"type":"actor", "source":1}}}}}})
patch('/api/actors/3',  {"data": {"type": "actors", "id": "3", "attributes": {"input":{"trigger":{"in":{"type":"actor", "source":2}}}}}})
patch('/api/actors/4',  {"data": {"type": "actors", "id": "4", "attributes": {"input":{"trigger":{"in":{"type":"actor", "source":3}}}}}})