import urllib
import logging
import json

def xrp_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.xrp')
    url = urllib.urlopen('https://www.bitstamp.net/api/v2/ticker/xrpusd/')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    data_parse = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[Bitstamp/XRP]\x03 > Last Price: ' + str(data_parse['last']) + ' | \x0303High:\x03 ' + str(data_parse['high']) + ' | \x0308Low:\x03 ' + str(data_parse['low']) + ' | Volume: ' + str(data_parse['volume'])

#def xrp_run_cmd(line, config):
#    logger = logging.getLogger('bot.cmd.xrp')
#    url = urllib.urlopen('https://api.coinmarketcap.com/v1/ticker/RIPPLE/')
#    if url.getcode() != 200:
#        logger.error('Request failed with http error: ' + str(url.getcode()))
#        return False
#    data_parse = json.loads(url.read())
#    logger.info('Completed command')
#    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[Ripple (XRP)]\x03 > ' + str(data_parse[['price_usd']]) + ' | ' + str(data_parse[['price_btc']]) + 'BTC | (1h): ' + str(data_parse[['percent_change_1h']]) + '% | (24h): ' + str(data_parse[['percent_change_24h']]) + '% | (7d): ' + str(data_parse[['percent_change_7d']])+ '%'
