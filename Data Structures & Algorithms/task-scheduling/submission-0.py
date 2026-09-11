import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        hq = [-c for c in counts.values()]
        heapq.heapify(hq)

        time = 0
        while hq:
            temp = []
            done = 0

            for _ in range(n + 1):
                if hq:
                    cnt = heapq.heappop(hq) + 1
                    done += 1
                    if cnt < 0:
                        temp.append(cnt)
            
            for cnt in temp:
                heapq.heappush(hq, cnt)
            
            if hq:
                time += n + 1
            else:
                time += done
            
        return time
                



        
        