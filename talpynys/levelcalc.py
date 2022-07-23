from math import floor

def calculate_level(exp):
    y = 2
    x = 0.04
    level = floor(exp**(1/y)*x)
    return level

def calculate_exp(level):
    y = 2
    x = 0.04
    exp = (level/x)**y
    return exp
