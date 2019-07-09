import urllib
import logging
import json

def abcbtc_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.abcbtc')
    url = urllib.urlopen('https://api.binance.com/api/v1/ticker/price?symbol=BCHABCBTC')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    data_parse = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[Binance/BCash ABC to BTC - FUCK ROGER VER]\x03 > Last Price: \x0308' + str(round(float(data_parse['price']),8)) + ' BTC '
