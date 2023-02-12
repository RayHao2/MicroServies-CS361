from pyzipcode import ZipCodeDatabase


zcdb = ZipCodeDatabase()
in_radius = str([z.zip for z in zcdb.get_zipcodes_around_radius('97015', 5)]) # ('ZIP', radius in miles)
radius_utf = [x.encode('UTF-8') for x in in_radius] # unicode list to utf list

print(type(in_radius))
print(in_radius)



# https://realpython.com/python-microservices-grpc/#why-rpc-and-protocol-buffers
