import time
import redis

import database_pb2
import database_pb2_grpc


class RedisOperations(database_pb2_grpc.redisOperationsServicer):
    
    def __init__(self):
        self.redis_client = redis.Redis(
            host='myapp-redis',
            port=6379,
            db=0,
            password='password',
            socket_timeout=None
        )
    
    def exists(self, request, context):
        print(request.message, flush=True)
        key = request.message
        val =  self.redis_client.exists(key)
        print(f'received request: {request} with context {context}', flush=True)
        return redisDatabase_pb2.Reply(message=val)
    
    def get(self, request, context):
        print(request.message, flush=True)
        key = request.message
        val = self.redis_client.get(key)
        print(f'received request: {request} with context {context}', flush=True)
        return redisDatabase_pb2.Reply(message=val)
    
    def set(self, request, context):
        print(request.message, flush=True)
        key = request.message
        val = self.redis_client.set(key)
        print(f'received request: {request} with context {context}', flush=True)
        return redisDatabase_pb2.Reply(message=val)
