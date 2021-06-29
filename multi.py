import multiprocessing as mp
import cl

def wallet(message):
    logger = cl.get_logger('admin')
    #while True:
    for i in range(3):
        logger.info(message)

def legion(message):
    logger = cl.get_logger(69)
    #while True:
    for i in range(3):
        logger.info(message)

def trading(message):
    logger = cl.get_logger(169)
    #while True:
    for i in range(3):
        logger.info(message)

if __name__=="__main__":
    mp.Process(target=wallet, args=('#1',)).start()
    mp.Process(target=legion, args=('#2',)).start()
    mp.Process(target=trading, args=('#3',)).start()
