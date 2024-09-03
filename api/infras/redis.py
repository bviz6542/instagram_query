import redis
from typing import Optional
from api.configs.settings import settings

redis_client = redis.StrictRedis(
    host=settings.REDIS_HOST, 
    port=settings.REDIS_PORT, 
    decode_responses=True
)

def get_value(key: str) -> Optional[any]:
    value = redis_client.get(key)
    if not value:
        return None
    return value

def set_value(key: str, value: any, expiration_time: int):
    redis_client.set(key, value, ex=expiration_time)

def delete_key(key: str):
    redis_client.delete(key)