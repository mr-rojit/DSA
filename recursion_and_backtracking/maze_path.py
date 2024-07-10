"""

(1,1)

S  #  #  #  #  #
#  #  #  #  #  #
#  #  #  #  #  #
#  #  #  #  #  #
#  #  #  #  #  #
#  #  #  #  #  F (6,6)



"""

def count_ways(start, dest):

    if start == dest:
        return 1
    
    if start[0] > dest[0] or start[1] > dest[1]:
        
        return 0
    

    # going right
    right = count_ways((start[0], start[1]+1), dest)

    # going down
    down = count_ways((start[0]+1, start[1]), dest)

    return right + down

initial_position = 1,1
destination = 3,3

print(count_ways(initial_position, destination))