import argparse


def create_parser(args, defaults):
    """
        Parse config/stdin arguments and set program entry point (phase).
    :param args:
    :param defaults:
    :return:
    """

    parser = argparse.ArgumentParser()
    parser.prog = 'vkinfo'
    subparsers = parser.add_subparsers()

    # Global arguments
    parser_base = argparse.ArgumentParser(add_help=False)
    parser_base.add_argument('--format', dest='export_format',
                             choices=['csv', 'json', 'tsv'],
                             type=str, default=defaults.EXPORT_FORMAT,
                             help=('export forman (default: %s)'
                                   % defaults.EXPORT_FORMAT))
    parser_base.add_argument('--path', dest='export_path',
                             type=str, default=defaults.EXPORT_PATH,
                             help=('export path (default: %s)'
                                   % defaults.EXPORT_PATH))
    parser_base.add_argument('--log-path', dest='log_path',
                             type=str, default=defaults.LOG_PATH,
                             help=('log file path (default: %s)'
                                   % defaults.LOG_PATH))
    parser_base.set_defaults(scope=defaults.SCOPE)
    parser_base.set_defaults(app_id=defaults.CLIENT_ID)
    parser_base.set_defaults(fields=defaults.FIELDS)
    parser_base.set_defaults(api_version=defaults.API_V)
    parser_base.set_defaults(base_url=defaults.BASE_URL)

    # access_token generation
    parser_token = subparsers.add_parser('token',
                                         parents=[parser_base],
                                         help='get vk access_token.')
    parser_token.set_defaults(phase='token')

    # runtime arguments
    parser_run = subparsers.add_parser('run',
                                       parents=[parser_base],
                                       help='run script.')
    parser_run.set_defaults(phase='run')
    parser_run.add_argument('access_token',
                            help='access token to use for requests',
                            type=str)
    parser_run.add_argument('user_id',
                            help='ID of searched user',
                            type=str)

    parameters = parser.parse_args(args)

    return parameters