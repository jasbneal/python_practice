# The Question class holds data for a triva question: question, possible answers
# (A, B, C, or D), and the correct answer.

class Question:

    def __init__(self, quest, A, B, C, D, correct_ans):
        self.__quest = quest
        self.__A = A
        self.__B = B
        self.__C = C
        self.__D = D
        self.__correct_ans = correct_ans

    def set_quest(self, quest):
        self.__quest = quest

    def set_As(elf, A):
        self.__A = A

    def set_B(self, B):
        self.__B = B

    def set_C(self, C):
        self.__C = C
    
    def set_D(self, D):
        self.__D = D

    def set_correct_ans(self, correct_ans):
        self.__correct_ans = correct_ans

    def get_quest(self):
        return self.__quest

    def get_ans_1(self):
        return self.__A
    
    def get_B(self):
        return self.__B

    def get_C(self):
        return self.__C

    def get_D(self):
        return self.__D

    def get_correct_ans(self):
        return self.__correct_ans

    def __str__(self):
    # Displays the question and possible answers. 
        return '\nQuestion: ' + self.__quest + \
        '\nA: ' + self.__A +  \
        '\nB: ' + self.__B + \
        '\nC: ' + self.__C + \
        '\nD: ' + self.__D