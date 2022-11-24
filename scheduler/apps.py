import os

from django.apps import AppConfig


class SchedulerConfig(AppConfig):
    name = 'scheduler'
    
    def ready(self):
        if os.environ.get('RUN_MAIN', None) != 'true':
            from . import updater
            updater.start()