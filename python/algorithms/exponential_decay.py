test_case = (1000,0.05,3)

def decayed_followers(initial_number, fraction_lost_daily, time):
    if initial_number <= 0:
        return 0
    if fraction_lost_daily <= 0:
        return initial_number

    remaining = initial_number *  (1 - fraction_lost_daily) ** time 

    return remaining

print(decayed_followers(1000,0.05,3)) # should be 857.>>