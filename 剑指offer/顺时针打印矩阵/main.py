# -*- coding:utf-8 -*-


class Solution:

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return None
        height = len(matrix)
        width = len(matrix[0])
        cnt = height * width
        res = []
        hs = 0
        he = height
        ws = 0
        we = width
        while True:
            for i in xrange(ws, we):
                res.append(matrix[hs][i])
            hs += 1
            if len(res) == cnt:
                return res
            for i in xrange(hs, he):
                res.append(matrix[i][we-1])
            we -= 1
            if len(res) == cnt:
                return res
            for i in xrange(we-1, ws-1, -1):
                res.append(matrix[he-1][i])
            he -= 1
            if len(res) == cnt:
                return res
            for i in xrange(he-1, hs-1, -1):
                res.append(matrix[i][ws])
            ws += 1
            if len(res) == cnt:
                return res
