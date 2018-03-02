import redis
from luffy_django.settings import LUFFY_REDIS

POOL = redis.ConnectionPool(host=LUFFY_REDIS['IP_ADDR'],port=LUFFY_REDIS['PORT'])