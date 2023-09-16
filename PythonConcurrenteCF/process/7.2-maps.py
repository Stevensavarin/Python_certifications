import time
import logging
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def is_even(number):
    time.sleep(1)
    return number % 2 == 0


def show_results(results):
    logging.info(f"El resultado es: {results}")


if __name__ == "__main__":
    with Pool(processes=2) as executor:
        numbers = [ number for number in range(1, 11) ]

        for element in executor.imap_unordered(is_even, numbers): #yield
            logging.info(element)