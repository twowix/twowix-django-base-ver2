from config.settings.base import *
import json

env_json = os.path.join(BASE_DIR, 'env.json')

if SERVER_ENV == 'local':
    with open(env_json) as f:
        env_json = json.loads(f.read())['local']

    try:
        INSTALLED_APPS.append('debug_toolbar')
        MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

        def custom_show_toolbar(self):
            return True

        DEBUG_TOOLBAR_CONFIG = {
            'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
            'RENDER_PANELS': True
        }
    except:
        pass
else:
    with open(env_json) as f:
        env_json = json.loads(f.read())['development']

INSTALLED_APPS.append('model.user')

SECRET_KEY = env_json['SECRET_KEY']