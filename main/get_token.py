import logging
import webbrowser
import argparse


def get_access_token(client_id: int, scope: str) -> None:
    """
        Get token using Use Implicit Flow to call VK API methods directly from the user's device
        (for example, from Javascript). An access key obtained in this way cannot be used for requests from the server.

            1.Client_id (required) - Your application ID.
            2.Redirect_uri (required) — the address to which the user will be redirected after authorization (see redirect_uri).
            3.Scope is a bitmask of the application's access settings that must be checked during user
              authorization and requested for missing ones.
    :param client_id:
    :param scope:
    :return:
    """

    assert isinstance(client_id, int), 'clinet_id must be positive integer'
    assert isinstance(scope, str), 'scope must be string'
    assert client_id > 0, 'clinet_id must be positive integer'
    url = """\
    https://oauth.vk.com/authorize?client_id={client_id}&\
    redirect_uri=https://oauth.vk.com/blank.hmtl&\
    scope={scope}&\
    &response_type=token&\
    display=page\
    """.replace(' ', '').format(client_id=client_id, scope=scope)
    logging.info('Openning auth page in webbrowser..')
    webbrowser.open_new_tab(url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('client_id', help='Application Id', type=int)
    parser.add_argument('-s', dest="scope", help='Permissions', type=str, default='', required=False)
    args = parser.parse_args()
    get_access_token(args.client_id, args.scope)