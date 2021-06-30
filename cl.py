import logging

class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        uuid = kwargs.pop('uuid', self.extra['uuid'])
        f1 = str(kwargs.pop('f1', self.extra['f1']))
        f2 = str(kwargs.pop('f2', self.extra['f2']))
        f3 = str(kwargs.pop('f3', self.extra['f3']))
        return 'uuid[%s] || f1[%s] f2[%s] f3[%s] || %s' % (uuid, f1, f2, f3, msg), kwargs

def get_logger(log_target, level=logging.INFO):
    logger = logging.getLogger(__name__)
    for hdlr in logger.handlers[:]:  # remove all old handlers
            logger.removeHandler(hdlr)
    logger.setLevel(level)
    _log_format = f"%(asctime)s || [%(levelname)s] || %(name)s || (%(filename)s).%(funcName)s(%(lineno)d) || {log_target} || %(message)s"
    # file handler
    file_handler = logging.FileHandler(f"logs/{log_target}.log")
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter(_log_format))
    logger.addHandler(file_handler)
    # stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    logger.addHandler(stream_handler)
    # custom handler
    logger = CustomAdapter(logger, {'uuid': None, 'f1': None, 'f2': None, 'f3': None})
    return logger

if __name__=='__main__':
    logger = get_logger('jarvis')
    logger.info('Order placed successfully', f1={'trade_id':'asfsadfasfsda'}, f2={'order_id':122})
