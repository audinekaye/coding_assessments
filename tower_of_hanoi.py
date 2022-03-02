# Tower of Hanoi
# Calculation
# -----------
# 2^(n-1) - (E.G. n = 3 Discs, 7 Moves)
# -------------------------------------

# Attempt 3 - Recursive Function
# - - - - -
input_num_of_discs = int(input("Please enter the number of discs: "))


def tower_of_hanoi(num_of_discs, starting_rod, final_rod, transfer_rod):
    if num_of_discs == 0:
        return 1

    tower_of_hanoi(num_of_discs - 1, starting_rod, transfer_rod, final_rod)
    print("moved disk", num_of_discs, "from", starting_rod,"to", final_rod)
    tower_of_hanoi(num_of_discs - 1, transfer_rod, final_rod, starting_rod)
    # Call the function twice in a different order to continue the transfer


# Call the recursive function (Parameters are number of discs & the Rod names)
tower_of_hanoi(input_num_of_discs, 'rod a', 'rod c', 'rod b')
