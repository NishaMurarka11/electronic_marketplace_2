import time
import redis

import database_pb2
import database_pb2_grpc


class RedisOperations(database_pb2_grpc.redisOperationsServicer):
    
    def __init__(self):
        self.redis_client = redis.Redis(
            host='127.0.0.1',
            port=6379,
            db=0,
            socket_timeout=None
        )
    
    def exists(self, request, context):
        print(request.message, flush=True)
        key = request.message
        val =  self.redis_client.exists(key)
        print(f'received request: {request} with context {context}', flush=True)
        return database_pb2.Reply(message=str(val))
    
    def get(self, request, context):
        print(request.message, flush=True)
        key = request.message
        val = self.redis_client.get(key)
        print(f'received request: {request} with context {context}', flush=True)
        return database_pb2.Reply(message=str(val))
    
    def set(self, request, context):
        print(request.message, flush=True)
        key = request.message
        val = request.val 
        val = self.redis_client.set(key,val)
        print(f'received request: {request} with context {context}', flush=True)
        return database_pb2.Reply(message=str(val))
    
    def delete(self, request, context):
        print(request.message, flush=True)
        key = request.message
        val = self.redis_client.delete(key)
        print(f'received request: {request} with context {context}', flush=True)
        return database_pb2.Reply(message=str(val))
