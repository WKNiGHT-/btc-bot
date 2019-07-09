import urllib
import logging
import json

def btcbs_run_cmd(line2, config):
    logger = logging.getLogger('bot.cmd.btc_bs')

    url = urllib.urlopen('https://www.bitstamp.net/api/ticker/')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    data_parse_bs = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[Bitstamp/BTC]\x03 > Last Price: \x0308$' + str(data_parse_bs['last']) + ' USD\x03 | High:\x0303 $' + str(data_parse_bs['high']) + '\x03 | Low:\x0304 $' + str(data_parse_bs['low'])  + '\x03 | Volume: ' + str(round(float(data_parse_bs['volume']),0))
