import random
import time
import base64
import hashlib
from src.config.secure import ciclos

def genKey():
    key = str(random.random())+str(time.time())
    key = base64.b64encode(key)
    
    i = 0
    while(i < ciclos):
        has = hashlib.sha512()
        has.update(key)
        key = has.hexdigest()
        i += 1
    
    key = str(key).encode('utf8')
    key = key.upper()
    return key
