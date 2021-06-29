import logging

class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        print(self.extra)
        uuid = kwargs.pop('uuid', self.extra['uuid'])
        focus = kwargs.pop('focus', self.extra['focus'])
        return '[%s] [%s] %s' % (uuid, focus, msg), kwargs

def get_logger(uuid, level=logging.INFO):
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    _log_format = f"%(asctime)s | [%(levelname)s] | %(name)s | (%(filename)s).%(funcName)s(%(lineno)d) | {uuid} | %(message)s"
    # file handler
    file_handler = logging.FileHandler(f"logs/{uuid}.log")
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter(_log_format))
    logger.addHandler(file_handler)
    # stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    logger.addHandler(stream_handler)
    return logger

def get_custom_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )

    logger = logging.getLogger(__name__)
    logger = CustomAdapter(logger, {'uuid': None, 'focus': None})


if __name__=='__main__':

    logger.info('Both provided', uuid='123', focus='order')
    logger.info('UUID provided', uuid='123')
    logger.info('Neither provided')

