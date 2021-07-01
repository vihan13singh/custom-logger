import cl

def agent(uuid):
    logger = cl.get_logger(uuid)
    logger.info('yo yo')
    logger.warning('TONY SINGH!')
