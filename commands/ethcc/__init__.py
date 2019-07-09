import urllib
import logging
import json

def ethcc_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.ethcc')
    url = urllib.urlopen('https://api.coinmarketcap.com/v1/ticker/ethereum/')
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    jsonData = json.loads(url.read())
    for i in jsonData:
        logger.info('Completed command')

        reset = '\x03'
        green = '\x0303'
        red = '\x034'
        yellow = '\x038'
        white = '\x0300'

        var7dcolor = green
        var24hcolor = green
        var1hcolor = green

        if float(i['percent_change_7d']) < 0: var7dcolor = red
        if float(i['percent_change_24h']) < 0: var24hcolor = red
        if float(i['percent_change_1h']) < 0: var1hcolor = red

        string = 'PRIVMSG ' + config['channel'] + ' :' + red + '[CoinMarketCap/Ethereum (ETH)]' + reset + ' > '  + '$' + i['price_usd'] + ' USD'  + ' | ' + i['price_btc'] + ' BTC  | (7d) ' + var7dcolor + i['percent_change_7d'] + '%' + reset + ' | (24h) ' + var24hcolor + i['percent_change_24h'] + '%' + reset + ' | (1h) ' + var1hcolor + i['percent_change_1h'] + '%'

        return string
