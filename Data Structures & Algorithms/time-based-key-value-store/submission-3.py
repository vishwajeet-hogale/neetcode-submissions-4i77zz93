import heapq
class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(lambda: defaultdict(str))

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Check if the key exists 
        self.hash_map[key][timestamp] = value
        return

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hash_map:
            all_values = list(self.hash_map[key].items())
            for i in range(len(all_values)-1,-1,-1):
                if all_values[i][0] <= timestamp:
                    return all_values[i][1]
        return ""
            



