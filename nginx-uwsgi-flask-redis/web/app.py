"""Simple Flask app connected to Redis"""

from flask import Flask
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://redis:6379'

redis = FlaskRedis(app)
redis.set_response_callback('GET', int)


def get_count():
    """returns number of visitors as stored in Redis"""
    return redis.get('count')


@app.route('/')
def hello():
    """
    Root path:

    increments the visitor count
    returns welcome message along with visitor count
    """
    redis.incr('count')
    count = get_count()
    s = 's' if count != 1 else ''

    return f"Welcome! {count} whale{s} have docked here."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True, use_reloader=False,
            threaded=True)
