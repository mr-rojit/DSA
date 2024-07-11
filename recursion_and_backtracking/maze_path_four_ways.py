"""

(0,0)

S  #  #  #  #  #
#  #  #  #  #  #
#  #  #  #  #  #
#  #  #  #  #  #
#  #  #  #  #  #
#  #  #  #  #  F (5,5)



"""

def count_ways(start, dest, visited=None):

    if not visited:
        visited = set()
    
    
    if start[0] > dest[0] or start[1] > dest[1]:
        return 0
    
    if start[0] < 0 or start[1] < 0:
        return 0
    
    if start == dest:
        return 1
    
    if start in visited:
        return 0
    
    visited.add(start)


    # going right
    right = count_ways((start[0], start[1]+1), dest, visited)



    left = count_ways((start[0], start[1]-1), dest, visited)

    # going down
    down = count_ways((start[0]+1, start[1]), dest, visited=visited)

    up = count_ways((start[0]-1, start[1]), dest, visited)
    
    visited.remove(start)





    return right + down + left + up

initial_position = 0,0
destination = 2,2

print(count_ways(initial_position, destination))