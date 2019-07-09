import urllib
import logging
import json

def work_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.work')
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :elgrecoFL: "Perhaps Ive failed to adequately express how shitty my working situation is"'
