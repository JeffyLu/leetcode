# -*- coding:utf-8 -*-


class Solution:

    right = 0
    down = 1
    left = 2
    up = 3

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return None

        start_x = 0
        start_y = 0
        end_x = len(matrix[0]) - 1
        end_y = len(matrix) - 1
        x = start_x
        y = start_y
        direction = self.right
        res = []
        while start_x <= end_x and start_y <= end_y:
            print(x, y)
            print("x:", start_x, end_x)
            print("y:", start_y, end_y)
            res.append(matrix[y][x])
            if direction == self.right:
                if x == end_x:
                    y += 1
                    direction = self.down
                    start_y += 1
                else:
                    x += 1
            elif direction == self.down:
                if y == end_y:
                    x -= 1
                    direction = self.left
                    end_x -= 1
                else:
                    y += 1
            elif direction == self.left:
                if x == start_x:
                    y -= 1
                    direction = self.up
                    end_y -= 1
                else:
                    x -= 1
            elif direction == self.up:
                if y == start_y:
                    x += 1
                    direction = self.right
                    start_x += 1
                else:
                    y -= 1
        return res


if __name__ == '__main__':

    print(Solution().printMatrix([
        [1, 2, 3],
        [4, 5, 6],
        #  [7, 8, 9],
    ]))
