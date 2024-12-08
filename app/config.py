import uuid
import os

class Config:
    CASSANDRA_HOSTS = os.getenv('CASSANDRA_HOSTS', 'cassandra').split(',')
    CASSANDRA_PORT = int(os.getenv('CASSANDRA_PORT', 9042))
    NODE_ID = os.getenv('NODE_ID', str(uuid.uuid4()))
    CACHE_TYPE = os.getenv('CACHE_TYPE', 'RedisCache')
    CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL', 'redis://redis:6379/0')
