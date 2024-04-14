from elasticsearch import Elasticsearch

# Create the client instance
client = Elasticsearch("http://localhost:9200")

# Successful response!
client.info()
# {'name': 'instance-0000000000', 'cluster_name': ...}

if client.ping():
    print("Connected OK")
else:
    print("Connected Error")
    

res = client.search(index="employees",query={
    "match_all":{}
})

print(res)