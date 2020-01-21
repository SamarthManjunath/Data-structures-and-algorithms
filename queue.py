#learning queues

from collections import deque

#create a queue
queue = deque()

#add elements to queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

#print queue
print(queue)

#delete queue, first element added
x = queue.popleft()
print(x)
print(queue)