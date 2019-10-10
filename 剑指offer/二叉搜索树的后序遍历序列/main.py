# -*- coding:utf-8 -*-


class Solution:

    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        if len(sequence) < 3:
            return True
        index = 0
        for i in sequence[:-1]:
            if i < sequence[-1]:
                index += 1
        postleft = sequence[:index]
        postright = sequence[index:-1]
        for i in postleft:
            if i > sequence[-1]:
                return False
        for i in postright:
            if i < sequence[-1]:
                return False
        return True
