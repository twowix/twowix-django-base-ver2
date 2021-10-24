from config.settings.base import *
import json

env_json = os.path.join(BASE_DIR, 'env.json')

with open(env_json) as f:
    env_json = json.loads(f.read())['product']

SECRET_KEY = env_json['SECRET_KEY']