import urllib
import logging
import json

def btcgm_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.btcgm')
    url = urllib.urlopen('https://api.gemini.com/v1/pubticker/btcusd')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    data_parse = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[Gemini/BTC]\x03 > Last Price: $' + str(data_parse['last']) + ' | Volume BTC: ' + str(data_parse['volume']['BTC']) + ' | Volume USD: $' + str(round(float(data_parse['volume']['USD']),0))

#def btc_run_cmd(line2, config):
#    logger = logging.getLogger('bot.cmd.btc_bs')
#
#    url = urllib.urlopen('https://www.bitstamp.net/api/ticker/')
#    if url.getcode() != 200:
#        logger.error('Request failed with http error: ' + str(url.getcode()))
#        return False
#    data_parse_bs = json.loads(url.read())
#    logger.info('Completed command')
#    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[Bitstamp/BTC]\x03 > Last Price: ' + str(data_parse_bs['last']) + ' | High: ' + str(data_parse_bs['high'])  + ' | Volume: ' + str(data_parse_bs['volume'])
