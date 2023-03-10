import logging

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s',
        filename="logs/" + "info.log")
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s'
)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)



