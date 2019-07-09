import urllib
import logging
import json

def ticker_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.ticker')
    url = urllib.urlopen('https://api.gdax.com/products/LTC-USD/ticker')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    data_parse = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + '[Coinbase/LTC ticker] > Last: ' + str(data_parse['price']) + ' | Volume: ' + str(data_parse['volume'])
