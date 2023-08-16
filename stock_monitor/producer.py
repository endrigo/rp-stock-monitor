import json
import traceback
from datetime import datetime

import websocket
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(
    bootstrap_servers="localhost:9092", 
    value_serializer=lambda m: json.dumps(m).encode("utf-8"),
)

topic = "finnhub-trades"


# Redpanda handlers
def on_success(metadata):
    print(f"Message produced to topic '{metadata.topic}' at offset {metadata.offset}")


def on_error(e):
    print(f"Error sending message: {e}")


# WS handlers
def on_ws_message(ws, message):
    data = json.loads(message)["data"]
    records = [
        {
            "symbol": d["s"],
            "price": d["p"],
            "volume": d["v"],
            "timestamp": datetime.utcfromtimestamp(d["t"] / 1000).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }
        for d in data
    ]

    for record in records:
        future = producer.send(topic, value=record)
        future.add_callback(on_success)
        future.add_errback(on_error)
        producer.flush()


def on_ws_error(ws, error):
    print(error)


def on_ws_close(ws, close_status_code, close_msg):
    producer.close()
    print("### closed ###")


def on_ws_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://ws.finnhub.io?token=cj5eb61r01qpipiaaps0cj5eb61r01qpipiaapsg", #Set your APIKEY here. Create it in https://finnhub.io/
        on_message=on_ws_message,
        on_error=on_ws_error,
        on_close=on_ws_close,
    )
    ws.on_open = on_ws_open
    ws.run_forever()
