import redis as Redis
from redisQueue import RedisQueue
import config
import json

redis = Redis.StrictRedis(host=config.CF_SERVER_IP, port=6379, db=0)

def queueMessage(queueName, msg):
    q = RedisQueue(queueName, host=config.CF_SERVER_IP)
    q.put(msg)

def getMessage(queueName):
    q = RedisQueue(queueName, host=config.CF_SERVER_IP)
    msg = q.get()
    return msg



class RedisObj:

    def __init__(self, key, initdict = {}):
        self.key = key
        self.dict = initdict


    def __setitem__(self, key, val):
        self.pull()
        self.dict[key] = val
        self.push()

    def __getitem__(self, key):
        self.pull()
        return self.dict.get(key, None)

    def keys(self):
        self.pull()
        return self.dict.keys()

    def get(self, key, defVal):
        self.pull()
        return self.dict.get(key, defVal)

    def push(self):
        strOut = json.dumps(self.dict)
        redis.set(self.key, strOut)

    def pull(self):
        try:
            strInp = redis.get(self.key)
            self.dict = json.loads(strInp)
        except:
            self.dict = {}
            pass

    def merge(self, otherDict):
        self.pull()

        for k in otherDict:
            self.dict[k] = otherDict[k]

        self.push()
