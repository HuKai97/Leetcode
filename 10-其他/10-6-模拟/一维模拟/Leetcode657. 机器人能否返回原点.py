class Solution:
    def judgeCircle(self, moves: str) -> bool:
        X = 0
        Y = 0
        for i in range(len(moves)):
            if moves[i] == 'R':
                X += 1
            elif moves[i] == 'L':
                X -= 1
            elif moves[i] == 'U':
                Y += 1
            elif moves[i] == 'D':
                Y -= 1
        return X == 0 and Y == 0