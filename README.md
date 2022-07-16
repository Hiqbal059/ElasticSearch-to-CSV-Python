# ElasticSearch-to-CSV-Python
Fetching more than 1000 documents at once and write them in CSV file

# Install Package
```
pip install elasticsearch 

or use command

pip install -r requirements.txt

```

# Import Packages
```
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import json
import csv
```

# Initialize ElasticSearch Client
```
ES_Client = Elasticsearch([{'host': 'Enter ES Host',
                            'port': 'Enter ES PORT',
                            'use_ssl': True,
                            'http_auth': ['Enter ES Username', 'Enter ES Password']}]
                        )
```

# Fetch Listings(10000+) and write to CSV File
```
CSV_header = ['Name', 'data']  //add whatever field you need to write
with open('data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(CSV_header)

    for hit in scan(ES_Client, index="Enter Index Name", query={"query":{"match_all" : {}}):
        data = [hit['name'], hit['data']]
        writer.writerow(data)

```


