import logging

import grpc
import zip_pb2
import zip_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = zip_pb2_grpc.ZipSearchingStub(channel)

        zipCodeInput = input("Please input your zip code here: ")
        

        radiusInput = int(input("Please input your radius here: "))
        

        response = stub.ZipSearching(zip_pb2.ZipInput(zipCode = zipCodeInput, radius=radiusInput))


        print(response.output)




        
        
        


if __name__ == '__main__':
    logging.basicConfig()
    run()