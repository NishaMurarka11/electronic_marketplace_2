import grpc
import database_pb2
import database_pb2_grpc


class grpc_client():
    
    def exists(key):
        try :
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = database_pb2_grpc.redisOperationsStub(channel)
                data = database_pb2.Request(message=key)
                response = stub.exists(data)
                return response.message        
        except Exception as e:
            return ("Error has occured "+str(e))
        
        
    def set(key,value):
        try :
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = database_pb2_grpc.redisOperationsStub(channel)
                data = database_pb2.Request(message=key,val=value)
                response = stub.set(data)
                return response.message        
        except Exception as e:
            return ("Error has occured "+str(e))
        
    def get(key):
        try :
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = database_pb2_grpc.redisOperationsStub(channel)
                data = database_pb2.Request(message=key)
                response = stub.get(data)
                return response.message        
        except Exception as e:
            return ("Error has occured "+str(e))