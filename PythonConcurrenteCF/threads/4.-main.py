import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(thread)s %(threadName)s : %(message)s"
)

if __name__ == "__main__":
    logging.debug("Hola, me encuentro en el Thread princial!")