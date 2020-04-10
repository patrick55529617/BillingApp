from importlib import import_module
import logging

SETTING_ABSOLUTELY_PATH = 'BillingApp.settings.{}'
SETTING_FILES = (
    'settings_default', 'settings_heroku', 'settings_local')
logging.getLogger(__name__)

for setting in SETTING_FILES:
    try:
        module = import_module(SETTING_ABSOLUTELY_PATH.format(setting))
        for variable in [v for v in dir(module) if not v.startswith('__')]:
            globals()[variable] = getattr(module, variable)
        logging.info('import setting: %s', setting)
    except ImportError:
        pass
