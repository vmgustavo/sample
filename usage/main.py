import json
import logging
import logging.config as lconfig

from sample import function

with open('logger.json', 'rt') as cfg:
    lconfig.dictConfig(json.load(cfg))

logger = logging.getLogger(__name__)
logger.info(f'_____ START EXECUTION {__file__}')


def main():
    logger.info('Inside main')
    function(1, 2, True)


if __name__ == '__main__':
    main()
