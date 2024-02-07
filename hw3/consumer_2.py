import time

from kafka import KafkaConsumer
from functools import wraps

def backoff(tries, sleep):
    if tries < 0:
        raise ValueError("tries should be > 0")
    if sleep < 0:
        raise ValueError("sleep should be > 0")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(tries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}. Retrying in {sleep} seconds...")
                    time.sleep(sleep)
            raise Exception(f"Failed after {tries} retries.")

        return wrapper

    return decorator
@backoff(tries=10,sleep=60)
def message_handler(value)->None:
    print(value)


def create_consumer():
    print("Connecting to Kafka brokers")
    consumer = KafkaConsumer("itmo2023",
                             group_id='itmo_group1',
                             bootstrap_servers='localhost:29092',
                             auto_offset_reset='earliest',
                             enable_auto_commit=True)

    for message in consumer:
        # send to http get (rest api) to get response
        # save to db message (kafka) + external
        message_handler(message)
        print(message)




if __name__ == '__main__':
    create_consumer()
