import logging as log

from api import ApiSession
from ..utils.save import SaveFormat


def get_run(parameters):
    """
        Main flow to check session, get_all_friends, save them
    :param parameters:
    :return:
    """

    sess = ApiSession(
        access_token=parameters.access_token,
        api_version=parameters.api_version,
        app_id=parameters.app_id,
        base_url=parameters.base_url
    )

    if not sess.token_validation():
        raise SystemExit('Your Token is not valid. It may be expired,\
                    try getting a new one.')

    fids = sess.method_execute(
        method='friends.get',
        values={
            'user_id': parameters.user_id,
            'count': 10000}
    )

    fids_count = fids['count']

    if not fids_count:
        log.debug('Friendlist is empty. Exiting')

        raise SystemExit('User has no friends')

    friends_df = sess.get_friends(
        fields=parameters.fields,
        search_user_id=parameters.user_id,
        fids_count=fids_count
    )

    log.info('Saving..')
    exporter = SaveFormat(friends_df)
    exporter.save(
        export_format=parameters.export_format,
        export_path=parameters.export_path
    )

