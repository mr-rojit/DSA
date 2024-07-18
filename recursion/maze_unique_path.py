"""

(1,1)

S  #  #  #  #  #
#  #  #  #  #  #
#  #  #  #  #  #
#  #  #  #  #  #
#  #  #  #  #  #
#  #  #  #  #  F (6,6)



"""

def count_ways(start, dest, path=""):

    if start == dest:
        print(path)
        return 1
    
    if start[0] > dest[0] or start[1] > dest[1]:
        return 0
    

    # going right
    right = count_ways((start[0], start[1]+1), dest, path+'R')

    # going down
    down = count_ways((start[0]+1, start[1]), dest, path+'D')

    return right + down

initial_position = 0,0
destination = 2,2

print(count_ways(initial_position, destination))