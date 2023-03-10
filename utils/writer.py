import logging as log
import pandas as pd


pd.options.mode.chained_assignment = None


def parse_friends_df(df: pd.DataFrame) -> pd.DataFrame:
    """
        Transforming bdate -> in ISO Format
        Checking if bdate exists
        Sorting field by name

    :param df:
    :return:
    """

    log.info('Putting collected data in order..')

    df.rename(columns={'city.title': 'city',
                    'country.title': 'country'}, inplace=True)

    df = df[['id', 'first_name', 'last_name',
            'country', 'city', 'bdate', 'sex']]

    log.info('Formatting birth date to ISO..')
    df['format'] = 1  # If bdate == '%d.%m'
    df.loc[df.bdate.str.match(r'\d{1,2}\.\d{1,2}\.\d{4}', na=False), 'format'] = 2

    df.loc[df.format == 1, 'bdate'] = pd.to_datetime(df.loc[df.format == 1, 'bdate'] + '.2000', format = '%d.%m.%Y').dt.strftime('%m-%d')
    df.loc[df.format == 2, 'bdate'] = pd.to_datetime(df.loc[df.format == 2, 'bdate'], format = '%d.%m.%Y').dt.strftime('%Y-%m-%d')
    df.drop(columns=['format'], inplace=True)

    log.info('Removing deleted accounts..')
    log.debug(f'Deactivated objects count: {df[df["first_name"] == "DELETED"]["first_name"].count()}')
    df = df[df.first_name != 'DELETED']


    df.sort_values(by=['first_name'], inplace=True)
    
    return df