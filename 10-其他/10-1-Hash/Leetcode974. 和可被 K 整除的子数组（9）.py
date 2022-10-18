class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mapp = defaultdict(int)   # key: 余数  val: 余数出现的次数
        mapp[0] = 1
        total = 0
        res = 0
        for i in range(len(nums)):
            total += nums[i]
            mod = total % k
            if mod in mapp:   # start: mod=0  res=0+1=1
                res += mapp[mod]
            mapp[mod] += 1
        return res