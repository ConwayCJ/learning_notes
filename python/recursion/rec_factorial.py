def num_possible_orders(num_posts):
    # base case - stops if num_posts hits last number..
    # !5          1 * 2 * 3 * 4 * 5
    if num_posts <= 0:
        return 1
    
    return num_possible_orders(num_posts * (num_posts -1))
