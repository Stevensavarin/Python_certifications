import os
import time
import logging
import multiprocessing


logging.basicConfig(level=logging.DEBUG, format="%(process)s %(processName)s %(message)s")


def nuevo_proceso(mensaje):
    logging.info("Hola, soy un nuevo proceso")

    time.sleep(2)

    logging.info(mensaje)

    logging.info("fin del proceso")

if __name__ == "__main__":
    #args or kwargs
    process = multiprocessing.Process(target=nuevo_proceso, name="proceso-hijo",
                                        #daemon=True,
                                        kwargs={"mensaje": "Nuevo mensaje, desde un argumento!"})
    process.start()

    #process.join

    logging.info("Hola, desde el proceso padre")