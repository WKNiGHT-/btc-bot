import urllib
import logging
import json

def ethbs_run_cmd(line2, config):
    logger = logging.getLogger('bot.cmd.eth_bs')

    url = urllib.urlopen('https://www.bitstamp.net/api/v2/ticker/ethusd/')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    data_parse_bs = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[Bitstamp/ETH]\x03 > Last Price: ' + str(data_parse_bs['last']) + ' | \x0303High:\x03 ' + str(data_parse_bs['high']) + ' | \x0308Low:\x03 ' + str(data_parse_bs['low'])  + ' | Volume: ' + str(data_parse_bs['volume'])
