import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointIdx2DistMap = []
        for idx, point in enumerate(points):
            euc_dist = 0
            for coordinate in point:
                distance = math.pow(coordinate - 0, 2)
                euc_dist += distance
            point_dist = math.sqrt(euc_dist)
            heapq.heappush(pointIdx2DistMap, (point_dist, idx))
        
        res_indexes = []
        
        for _ in range(k):
            distance, index = heapq.heappop(pointIdx2DistMap)
            res_indexes.append(index)
        
        output = []
        for idx in res_indexes:
            output.append(points[idx])
        
        return output


