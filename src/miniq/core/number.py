from numba import complex128, float32

class Complex(object):

    def __init__(self, re: float32, im: float32):
        self.element = complex128(re, im)
