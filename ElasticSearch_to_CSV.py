from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import json
import csv

ES_Client = Elasticsearch([{'host': 'Enter ES Host',
                     'port': 'Enter ES PORT',
                     'use_ssl': True,
                     'http_auth': ['Enter ES Username', 'Enter ES Password']}]
            )


CSV_header = ['Name', 'data']                   #add whatever field you need to write
with open('data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(CSV_header)

    for hit in scan(ES_Client, index="Enter Index Name", query={"query":{"match_all" : {}}}):
        data = [hit['name'], hit['data']]
        writer.writerow(data)