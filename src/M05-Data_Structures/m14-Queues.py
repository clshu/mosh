from collections import deque

# Create a new empty deque object that will function as a queue
queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if queue:
    queue.popleft()
print(queue)
if not queue:
    print("empty queue")
