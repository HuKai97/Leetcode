class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 美元10只能给账单20找零，而美元5可以给账单10和账单20找零，美元5更万能
        # 局部最优：遇到账单20，优先消耗美元10，完成本次找零。全局最优：完成全部账单的找零
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else: return False
            elif b == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True