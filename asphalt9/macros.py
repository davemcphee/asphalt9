sel_car_and_start_race = """
A 0.2s
8s
"""

race_macro = """
LOOP 100
    Y 0.1s
    0.2s
    Y 0.1s
    1.6s
"""

back_to_mp_macro = """
LOOP 13
    B 0.2s
    1.8s
"""

select_mp1_and_select_prev_car = """
A 0.2s
2.5s
A 0.2s
4.5s
PLUS 0.2s
1.5s
B 0.2s
2.5s
A 0.2s
2.5s
"""

COMPLETE_MP1_LOOP = """
A 0.2s
6s
LOOP 70
    Y 0.1s
    0.2s
    Y 0.1s
    1.6s
LOOP 7
    B 0.2s
    1.8s
A 0.2s
2.5s
A 0.2s
4.5s
PLUS 0.2s
1.5s
B 0.2s
2.5s
A 0.2s
3.5s
"""