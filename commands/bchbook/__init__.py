import urllib
import logging
import json

def bchbook_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.bchbook')
    url = urllib.urlopen('https://api.binance.com/api/v3/ticker/price?symbol=BCCBTC')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    data_parse = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[Binance/BCASH to BTC Book]\x03 > Price: $'  + str(data_parse['price'])
