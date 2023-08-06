# redmq

Redis message queue utils: a simple distributed lock based on redis, a simple message queue based on redis with ack feature.

## Install

```
pip install redmq
```

## Usage Examples 

### redmq.lock.RedisLock

```
import redis
from redmq.lock import RedisLock

conn = redis.Redis()
lock_name = "test01_lock"

with RedisLock(conn, lock_name) as locked:
    if lock:
        pass # do things if acquired the lock
    else:
        pass # do things if not acquired the lock
```

### redmq.message_queue.MessageQueue

*worker.py*

```
import time
import redis
from redmq.message_queue import MessageQueue

conn = redis.Redis()
mq = MessageQueue(conn)
while True:
    task = mq.pop_nowait()
    if task:
        message = task["message"]
        mq.acknowledge(task, message.upper())
    else:
        time.sleep(0.1)
```

*client.py*

```
import time
import redis
from redmq.message_queue import MessageQueue

conn = redis.Redis()
mq = MessageQueue(conn)
task1 = mq.push("task1")
task_info = None
for _ in range(100):
    task_info = mq.get_result_nowait(task1)
    if task_info:
        break
    time.sleep(0.1)
print(task_info["result"])

```

*start worker*

```
python3 worker.py
```

*start client*

```
python3 client.py
```

*client output*

```
test@test redmq % python3.9 client.py 
{'error_message': 'OK', 'result_data': 'TASK1', 'success': True, 'error_code': 0}
```

## Why NOT using blpop instead of lpop?

We do pop_nowait via LUA script, but redis is NOT allow us to use blpop in LUA script.

## Releases

### v0.1.0

- First release.

### v0.1.1

- redmq.message_queue.MessageQueue.push takes `high_priority` parameter. Normal message use FIFO rule, and `high_priority` message use LIFO rule.
