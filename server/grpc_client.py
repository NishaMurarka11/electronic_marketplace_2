import grpc
import database_pb2
import database_pb2_grpc
import traceback


class GRPCClient():
    
    def exists(server,key):
        try :
            url = '{}:50051'.format(server)
            with grpc.insecure_channel(url) as channel:
                stub = database_pb2_grpc.redisOperationsStub(channel)
                data = database_pb2.Request(message=key)
                response = stub.exists(data)
                return response.message        
        except Exception as e:
            print("EXCEPTION"+str(e))
            return ("Error has occured "+str(e))
        
        
    def set(server,key,value):
        try :
            url = '{}:50051'.format(server)
            with grpc.insecure_channel(url) as channel:
                stub = database_pb2_grpc.redisOperationsStub(channel)
                data = database_pb2.Request(message=key,val=value)
                response = stub.set(data)
                return response.message    
        except Exception as e:
            traceback.print_exc()
            return ("Error has occured "+str(e))
        
    def get(server,key):
        try :
            url = '{}:50051'.format(server)
            with grpc.insecure_channel(url) as channel:
                stub = database_pb2_grpc.redisOperationsStub(channel)
                data = database_pb2.Request(message=key)
                response = stub.get(data)
                return response.message        
        except Exception as e:
            return ("Error has occured "+str(e))
        
    def delete(sever,key):
        try :
            url = '{}:50051'.format(server)
            with grpc.insecure_channel(url) as channel:
                stub = database_pb2_grpc.redisOperationsStub(channel)
                data = database_pb2.Request(message=key)
                response = stub.delete(data)
                return response.message        
        except Exception as e:
            return ("Error has occured "+str(e))
