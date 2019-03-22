import pika
from practicing.config import config
#from practicing.Scrapy import Scrapy
import json
class rabbitmouse:
 def gettingscrapyvalues(self,carddata):
    #object = config()
    #asd = object.carddata()
   #print(len(asd))
    for asd1 in carddata:
        asd2 = json.dumps(asd1.__dict__)
        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = connection.channel()
        # channel.exchange_declare(exchange="",exchange_type="")
        channel.basic_publish(exchange='', routing_key='hello', body=asd2)
        print("[x] sent hello world")
        connection.close()











