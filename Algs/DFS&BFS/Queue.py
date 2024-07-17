#FIFO 구조
#collections 모듈에서 제공하는 deque 자료구조 활용.
#deque(양방향 큐)는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue라이브러리를 이용하는 것보다 더 간단.

from collections import deque

queue = deque()

queue.append(5)
queue.append(3)
queue.append(2)
queue.popleft()
queue.pop()

print(queue)
#deque([5])