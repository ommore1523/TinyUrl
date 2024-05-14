import config
import redis

class RedisCacheStore:
    """
        Class Name: RedisCacheStore
        Description: Used for read , update , delete and create redis data.
        Author: Omkar More
        On Failure: Raise Exception
            Written By: Omkar
        Version: 1.0
    """
    
    def __init__(self) -> None:
        self.redis_store = redis.StrictRedis(
            host=config.REDIS_HOST, port=config.REDIS_PORT, db=0, decode_responses=True
        )
    
    def set_value(self, key, value, expiry) -> None:
        """Set value and permissions object"""
        self.redis_store.set(key, value, expiry)
    
    def update_expiry(self, key, prolongation) -> None:
        """Update expiry of key"""
        self.redis_store.expire(key, prolongation)
    
    def get_value(self, key):
        """Get value of key"""
        return self.redis_store.get(key)
    
    def get_ttl(self, key):
        """Get time to left of key"""
        return self.redis_store.ttl(key)
    
    def delete(self, key):
        """Delete the keys from redis store"""
        self.redis_store.delete(key)
    

    