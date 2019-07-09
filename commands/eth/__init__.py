import urllib
import logging
import json

def eth_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.eth')
    url = urllib.urlopen('https://api.gdax.com/products/ETH-USD/ticker')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    data_parse = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[GDAX/ETH]\x03 > Last Price: \x0308$' + str(round(float(data_parse['price']),2)) + ' USD\x03 | Volume: ' + str(round(float(data_parse['volume']),0))
