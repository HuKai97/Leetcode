class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 先确定一边，再确定另外一边
        # 1.先从左到右，当右边的大于左边的就加1
        # 2.再从右到左，当左边的大于右边的就再加1
        count = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                count[i] = count[i-1] + 1
        # print(count)
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                count[j] = max(count[j+1] + 1, count[j])
        # print(count)
        return sum(count)