import urllib
import logging
import json

def fuck_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.fuck')
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :abracadabra: Fuck Roger Ver, Fuck Craig Wright, Fuck Bitmain, Fuck Luke-Jr, Fuck Alt Coins (tm)'
