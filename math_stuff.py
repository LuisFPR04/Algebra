import numpy as np

def rotation(alpha):
    row_1 = [np.cos(alpha), -np.sin(alpha)]
    row_2 = [np.sin(alpha), np.cos(alpha)]

    return [row_1, row_2]

#Gauss-Jordan Algorithm start
def column_sum(eq_1, eq_2):
    eq_sum = []
    for i in range(4):
        result = eq_1[i] + eq_2[i]
        eq_sum.append(result)

    return eq_sum

def column_rest(eq_1, eq_2):
    eq_res = []
    for i in range(4):
        result = eq_1[i] - eq_2[i]
        eq_res.append(result)

    return eq_res

def mult_columns(eq, scalar):
    scaled_m = []
    for i in range(4):
        scaled_m.append(eq[i]*scalar)

    return scaled_m

def row_reduction(eq_1, eq_2):
    if eq_1[0] != 1:
        eq_mult = mult_columns(eq_2, eq_1[1])
        eq_1 = column_rest(eq_mult, eq_1)
        if eq_1[1] != 0:
            eq_1 = mult_columns(eq_1,1/eq_1[0])

    return eq_1

v_1 = [3,7,5,1]
v_2 = [1,5,9,2]

print(row_reduction(v_1,v_2))
#Gauss-Jordan algorithm end