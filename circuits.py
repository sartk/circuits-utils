from fractions import Fraction

class Circuit:

    def __init__(self, fraction_mode=True):
        self.fraction_mode = fraction_mode

    def standard(self, x):
        if self.fraction_mode:
            return Fraction(x)
        return x

    def pll(self, R1, R2):
        '''
        Parallel Operator
        '''
        R1, R2 = self.standard(R1), self.standard(R2)
        return (R1 * R2) / (R1 + R2)

    def v_div(self, V_s, R1, R2):
        '''
        Voltage Divider
        '''
        R1, R2 = self.standard(R1), self.standard(R2)
        return V_s * R2 / (R1 + R2)
