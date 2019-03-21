from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'NUMS',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     #consumer_timeout_ms=1000,  # after 1000ms stop 
     value_deserializer=lambda x: loads(x.decode('utf-8')))

print("consumer is okey ........")

#r = open(r'C:\Users\DELL\Desktop\KAFKA\drawing\example.txt','r').readlines()
#index = int(r[-1].[0])
#r.close()    


f = open(r'C:\Users\DELL\Desktop\KAFKA\drawing\example.txt','a+')
# f.seek(0)
# f.truncate()   




for message in consumer:
    message = message.value
    s =''  
    for m in message:
        s +=str(m)+' '
    print('{} added to here {}'.format(message,s))
    f.write( s + '\n')
    f.flush()
    
    
f.close() 