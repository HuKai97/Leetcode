class Solution:
    def canWinNim(self, n: int) -> bool:
        # 如果石头数目是4的倍数，无论你选1、2、3块石头，对上都可以让剩余石头数是4的倍数
        # 比如有8个石头，你选1/2/3块石头，对手就选3/2/1块石头  最终肯定会剩下4块石头
        # 你再选1/2/3块石头，最终对手就选3/2/1块石头，最后一块石头肯定会再对上手中，对手必赢
        return n % 4 != 0
