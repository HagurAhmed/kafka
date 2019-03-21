from time import sleep
from json import dumps
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


print("producer is okey ........")

# for e in range(1):
#     data = {'number' : e}
#     producer.send('numtest', value=data)
#     sleep(1)

# l= []
# l.append({'a':1,"b":2})
# l.append([9,10,25])

# for e in l:
#     data = e #{'number' : e}
#     producer.send('numtest', value=data)
#     sleep(1)