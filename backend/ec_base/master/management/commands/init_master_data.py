import logging
import pathlib

from django.core import serializers
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    @staticmethod
    def __insert_data(folder):
        for file in pathlib.Path(folder).rglob('*.json'):
            logger.debug(f'File: {file}')
            if file.is_file():
                with file.open() as f:
                    data = f.read()

                for item in serializers.deserialize('json', data):
                    item.save()

    def handle(self, *args, **options):
        logger.debug("Master data initializing called.")

        try:
            self.__insert_data('ec_base/master/assets')

            logger.debug('Master data initializing success.')
        except Exception as e:
            logger.error('Master data initializing failed', exc_info=e)
