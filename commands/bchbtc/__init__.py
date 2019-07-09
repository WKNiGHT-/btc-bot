import urllib
import logging
import json

def bchbtc_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.bchbtc')
    url = urllib.urlopen('https://api.gdax.com/products/BCH-BTC/stats')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    data_parse = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[GDAX/BCash to BTC]\x03 > Last Price: \x0308' + str(round(float(data_parse['last']),8)) + ' BTC\x03 | High:\x0303 ' + str(round(float(data_parse['high']),8)) + '\x03 | Low:\x0304 ' + str(round(float(data_parse['low']),8))  + '\x03 | Volume: ' + str(round(float(data_parse['volume']),0))
