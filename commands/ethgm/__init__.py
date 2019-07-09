import urllib
import logging
import json

def ethgm_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.ethgm')
    url = urllib.urlopen('https://api.gemini.com/v1/pubticker/ethusd')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    data_parse = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[Gemini/ETH]\x03 > Last Price: ' + str(data_parse['last']) + ' | Volume ETH: ' + str(data_parse['volume']['ETH']) + ' | Volume USD: ' + str(data_parse['volume']['USD'])
