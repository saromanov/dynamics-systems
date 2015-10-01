import math

class Model:
    def __init__(self, const1, const2):
        self.const1 = const1
        self.const2 = const2

    def fit1(self, t):
        ''' Fit first table of system
        '''
        return self.const1 * math.exp(-self.const2 * t)

    def fir2(self, t):
        ''' Fit second type of system
        '''
        return self.const1 * math.exp(-t/self.const2)

