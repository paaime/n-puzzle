import heapq
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class QueueItem:
    priority: int
    value: Any = field(compare=False)

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.peak_size = 0

    def __len__(self):
        return len(self.queue)

    def add(self, item, priority):
        if not isinstance(priority, int):
            raise ValueError('Priority must be an integer')
        if item is None:
            raise ValueError('Item cannot be None')
            
        entry = QueueItem(priority=priority, value=item)
        heapq.heappush(self.queue, entry)
        
        if len(self.queue) > self.peak_size:
            self.peak_size = len(self.queue)

    def extract(self):
        try:
            wrapper = heapq.heappop(self.queue)
            return wrapper.value
        except IndexError:
            return None