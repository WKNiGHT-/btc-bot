import urllib
import logging
import json

def global_run_cmd(line2, config):
    logger = logging.getLogger('bot.cmd.global')

    url = urllib.urlopen('https://api.coinmarketcap.com/v1/global/')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    data_parse_global = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + '\x0304[CoinMarketCap/Global Market]\x03 > Global Market Cap: $' + str(round(float(data_parse_global['total_market_cap_usd']),0)) + ' | BTC Dominance\x03: ' + str(data_parse_global['bitcoin_percentage_of_market_cap']) + '% | 24h Volume: $' + str(round(float(data_parse_global['total_24h_volume_usd']),0))
