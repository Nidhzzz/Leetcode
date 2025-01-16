class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            max_heap.append(-stone)
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if x < y:
                new_stone = y-x
                heapq.heappush(max_heap, -new_stone)
            
        if len(max_heap) == 1:
            return -heapq.heappop(max_heap)
        else:
            return 0