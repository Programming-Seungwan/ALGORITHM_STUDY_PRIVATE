class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for n in nums:
            my_dict[n] = my_dict.get(n, 0) + 1

        # 등장 횟수로 정렬 (내림차순)
        sorted_items = sorted(my_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

        return [item[0] for item in sorted_items[:k]]