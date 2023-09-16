import time
import logging
import threading

#sleep(segundos)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(thread)s %(threadName)s : %(message)s"
)

def task():
    logging.info("Nos encontramos ejecutando una nueva tarea")
    time.sleep(2)
    logging.info("Tarea finalizada")

if __name__ == "__main__":
    thread = threading.Thread(target=task)
    thread.start()