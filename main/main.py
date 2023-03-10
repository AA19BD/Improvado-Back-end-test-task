import sys

import logging as log

from parser import create_parser
from run import get_run
from ..assets.config import Default
from get_token import get_access_token


def main(args=None):
    """
        Main Function to Start code
    :param args:
    :return:
    """
    if args is None:
        args = sys.argv[1:]

    parameters = create_parser(args, Default)

    if parameters.phase == 'token':
        log.info('Starting.. Phase: Token')
        get_access_token(parameters.app_id, parameters.scope)

    elif parameters.phase == 'run':
        log.info('Starting.. Phase: Run')
        get_run(parameters)


if __name__ == '__main__':
    main()
