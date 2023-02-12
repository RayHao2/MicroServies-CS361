# python -m grpc_tools.protoc -I./proto --python_out=. --pyi_out=. --grpc_python_out=. ./proto/zip.proto

from pyzipcode import ZipCodeDatabase
import logging
from concurrent import futures

import zip_pb2_grpc
import grpc
import zip_pb2

class zipCodeServicer(zip_pb2_grpc.ZipSearchingServicer):

    def ZipSearching(self, request, context):

        zipInput = str(request.zipCode)
        radiusInput = int(request.radius)
        zcdb = ZipCodeDatabase()
        in_radius = str([z.zip for z in zcdb.get_zipcodes_around_radius(zipInput, radiusInput)]) # ('ZIP', radius in miles)
        
        return zip_pb2.ZipOutput(output=in_radius)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    zip_pb2_grpc.add_ZipSearchingServicer_to_server(
        zipCodeServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
