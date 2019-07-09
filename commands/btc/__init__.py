import urllib
import logging
import json

def btc_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.btc')
    url = urllib.urlopen('https://api.gdax.com/products/BTC-USD/stats')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    data_parse = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[GDAX/BTC]\x03 > Last Price: \x0308$' + str(round(float(data_parse['last']),2)) + ' USD\x03 | High:\x0303 $' + str(round(float(data_parse['high']),2)) + '\x03 | Low:\x0304 $' + str(round(float(data_parse['low']),2))  + '\x03 | Volume: ' + str(round(float(data_parse['volume']),0))
