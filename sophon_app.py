import json
import os

from flask import Flask
import redis

app = Flask(__name__)

REDIS_KEY = os.environ.get('REDIS_KEY', 'echo')
REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def only_route(path):
    client = redis.Redis(
        host=REDIS_HOST,
        port=6379
    )
    payload = json.loads(client.get(REDIS_KEY))
    return json.dumps(payload)


if __name__ == '__main__':
    app.run()
