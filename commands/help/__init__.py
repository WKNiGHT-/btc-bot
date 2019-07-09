import urllib
import logging
import json

def help_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.help')
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :Commands supported: !btc, !bch, !eth, !ltc, !xlm, !xrp, !norris, Add (bs) for Bitstamp, (cc) for CoinMarketCap, and (gm) for Gemini i.e. !btcbs'
