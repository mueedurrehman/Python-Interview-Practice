def jumpingOnClouds(c):
    min_jumps = 0
    current_position = 0
    length = len(c)
    while current_position < length - 1:
        print(current_position)
        if current_position + 2 == length or c[current_position + 2] == 1 :
            current_position += 1
            min_jumps += 1
        else:
            current_position +=2
            min_jumps += 1
    return min_jumps

print(jumpingOnClouds([0,0,1,0,0,1,0]))