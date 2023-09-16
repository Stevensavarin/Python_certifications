import time 
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

# Colas
def get_elements(queue):
    while not queue.empty():
        element = queue.get(block=True)
        logging.info(f"El elemento es: {element}")


if __name__ == "__main__":
    manager = multiprocessing.Manager()
    queue = manager.Queue() #FIFO

    for x in range(1, 21):
        queue.put(x)

    logging.info("La cola ya posee elementos!")
    procces1 = multiprocessing.Process(target=get_elements, args=(queue, ))
    procces2 = multiprocessing.Process(target=get_elements, args=(queue, ))
    procces3 = multiprocessing.Process(target=get_elements, args=(queue, ))

    procces1.start()
    procces2.start()
    procces3.start()

    procces1.join()
    procces2.join()
    procces3.join()

    logging.info("Fin, de los procesos!")

