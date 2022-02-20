
   
import grpc

import database_pb2
import database_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = database_pb2_grpc.redisOperationsStub(channel)
        data = database_pb2.Request(message="productDB")
        response = stub.get(data)
    print("Client received: " + response.message)


if __name__ == '__main__':
    run()