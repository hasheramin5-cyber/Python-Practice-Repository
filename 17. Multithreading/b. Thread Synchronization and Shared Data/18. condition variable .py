# A Program to coordinate threads using a condition variable

import threading
import time


condition = threading.Condition()

data_ready = False


def consumer():
    global data_ready

    with condition:
        print("Consumer is waiting for data...")

        while not data_ready:
            condition.wait()

        print("Consumer received the data.")


def producer():
    global data_ready

    time.sleep(2)

    with condition:
        data_ready = True

        print("Producer created the data.")

        condition.notify()


consumer_thread = threading.Thread(target=consumer)
producer_thread = threading.Thread(target=producer)


consumer_thread.start()
producer_thread.start()


consumer_thread.join()
producer_thread.join()


print("Program finished.")


# Explanation:
# Condition provides a way for threads to wait for a specific state or condition to become true.
# The consumer acquires the condition and checks data_ready.
# While the data is not ready, condition.wait() temporarily releases the condition and puts the consumer into a waiting state.
# The producer later changes data_ready to True.
# condition.notify() wakes a waiting thread.
# The consumer then checks the condition again and continues.

# Real-Life Use:
# Conditions are useful for producer-consumer systems, task queues, buffers, and workflows where threads must wait for specific state changes.