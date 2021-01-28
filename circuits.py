from fractions import Fraction

class Circuit:

    def __init__(self, fraction_mode=True):
        self.fraction_mode = fraction_mode

    def standard(self, x):
        if self.fraction_mode and not isinstance(x, Fraction):
            return Fraction(x)
        return x

    def pll(self, R1, R2):
        '''
        Parallel Operator
        '''
        R1, R2 = self.standard(R1), self.standard(R2)
        return (R1 * R2) / (R1 + R2)

    def v_div_gain(self, R1, R2):
        '''
        Voltage Divider Gain
        '''
        R1, R2 = self.standard(R1), self.standard(R2)
        return R2 / (R1 + R2)

    def v_div(self, R1, R2, V_s=1):
        '''
        Voltage Divider
        '''
        return V_s * self.v_div_gain(R1, R2)
