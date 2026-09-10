class TimeMap:

    def __init__(self):
        self.TimeMap = {}
        return None

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.TimeMap.get(key) is None:
            self.TimeMap[key] = {"value": [], "timestamp": []}
        self.TimeMap[key]["value"].append(value)
        self.TimeMap[key]["timestamp"].append(timestamp)
        return None

    def get(self, key: str, timestamp: int) -> str:
        if self.TimeMap.get(key) is None:
            return ""
        vals = self.TimeMap[key]["value"]
        tstmps = self.TimeMap[key]["timestamp"]
        
        idx = self.BinarySearchIdx(tstmps, timestamp)
        return vals[idx] if idx != -1 else ""
        

    def BinarySearchIdx(self, arr, target):
        low = 0
        high = len(arr) - 1
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] <= target:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
        
