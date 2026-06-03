import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

STREAM = "sentineliq_stream"


def publish(event: dict):
    r.xadd(STREAM, {"data": json.dumps(event)})


def consume(last_id="0-0"):
    while True:
        events = r.xread({STREAM: last_id}, block=0)
        for stream, messages in events:
            for msg_id, data in messages:
                yield msg_id, json.loads(data["data"])
                last_id = msg_id