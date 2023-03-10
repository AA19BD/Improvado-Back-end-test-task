import logging as log
import pandas as pd


class SaveFormat(object):

    def __init__(self, dataframe: pd.DataFrame) -> None:

        self.dataframe = dataframe

    def save(self,
             export_path: str,
             export_format: str) -> None:
        """
            export_path - > path to save file
            export_format - > format [ csv, json, tsv]
        :param export_path:
        :param export_format:
        :return:
        """

        if export_format == 'csv':
            log.info('Saving data in .csv format')
            self.dataframe.to_csv(f'{export_path}.csv', index=False)

        elif export_format == 'json':
            log.info('Saving data in .json format')
            self.dataframe.to_json(f'{export_path}.json', orient='records', force_ascii=False, indent=2)

        elif export_format == 'tsv':
            log.info('Saving data in .tsv format')
            self.dataframe.to_csv(f'{export_path}.tsv', index=False, sep='\t')

        log.info(f'Exported as {export_path}.{export_format}')
