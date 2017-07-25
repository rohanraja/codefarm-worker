import redis as Redis
from redisQueue import RedisQueue
import config

# redis = Redis.StrictRedis(host=config.CF_SERVER_IP, port=6379, db=0)
#

def queueMessage(queueName, msg):
    q = RedisQueue(queueName, host=config.CF_SERVER_IP)
    q.put(msg)

def getMessage(queueName):
    q = RedisQueue(queueName, host=config.CF_SERVER_IP)
    msg = q.get()
    return msg
