def read_and_calculate(fileName):
    file = open(fileName)
    horizontal = 0
    depth = 0

    for line in file:
        step = line.split()
        movement = step[0]
        positions = int(step[1])
        
        if movement=='forward': horizontal+=positions
        if movement=='down': depth+=positions
        if movement=='up': depth-=positions
    
    file.close();
    print('horizontal: '+str(horizontal))
    print('depth: '+str(depth))
    print('result: '+str(horizontal*depth))


def read_and_calculate_aim(fileName):
    file = open(fileName)
    horizontal = 0
    depth = 0
    aim = 0

    for line in file:
        step = line.split()
        movement = step[0]
        positions = int(step[1])
        
        if movement=='down': aim+=positions
        if movement=='up': aim-=positions
        if movement=='forward': 
            horizontal+=positions
            depth= depth + (aim*positions)
    
    file.close();
    print('horizontal: '+str(horizontal))
    print('depth: '+str(depth))
    print('result: '+str(horizontal*depth))


# puzzle1
read_and_calculate('data.txt')
# puzzle1
read_and_calculate_aim('data.txt')