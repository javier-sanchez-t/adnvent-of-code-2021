
def read_file(fileName):
    file = open(fileName)
    coordinates = []

    for line in file:
        coordinate = {
            'x1': 0,
            'y1': 0,
            'x2': 0,
            'y2': 0
        }
        data = line.replace('\n', '').split(' -> ')
        coordinate1 = data[0].split(',')
        coordinate2 = data[1].split(',')
        coordinate['x1'] = int(coordinate1[0])
        coordinate['y1'] = int(coordinate1[1])
        coordinate['x2'] = int(coordinate2[0])
        coordinate['y2'] = int(coordinate2[1])
        coordinates.append(coordinate)

    file.close();
    return coordinates;


def get_max_coordinate(array, coordinate):
    max = 0
    for item in array:
        if(item[coordinate] > max):
            max = item[coordinate]

    return max


def get_overlaping_segments():
    coordinates  = read_file('data.txt')
    max_x1 = get_max_coordinate(coordinates, 'x1')+1
    max_y1 = get_max_coordinate(coordinates, 'y1')+1
    max_x2 = get_max_coordinate(coordinates, 'x2')+1
    max_y2 = get_max_coordinate(coordinates, 'y2')+1
    max_x = max_x1 if max_x1 > max_x2 else max_x2;
    max_y = max_y1 if max_y1 > max_y2 else max_y2;

    board = [[0 for row in range(max_x)] for col in range(max_y)]
    overlaping = 0

    for cord in coordinates:
        #horizontal
        if(cord['x1']==cord['x2']):
            if(cord['y1']>cord['y2']):
                maxCoord = cord['y1']
                minCoord = cord['y2']
            else:
                maxCoord = cord['y2']
                minCoord = cord['y1']
            
            while(maxCoord>=minCoord):
                board[minCoord][cord['x1']] +=1
                minCoord += 1
            continue
        
        #vertical
        if(cord['y1']==cord['y2']):
            if(cord['x1']>cord['x2']):
                maxCoord = cord['x1']
                minCoord = cord['x2']
            else:
                maxCoord = cord['x2']
                minCoord = cord['x1']

            while(maxCoord>=minCoord):
                board[cord['y1']][minCoord] +=1
                minCoord += 1
            continue

        #diagonal
        coord1 = '';
        coord2 = '';
        if(cord['x1']>cord['x2']):
            if(cord['y1']>cord['y2']):
                coord2 = { 'x': cord['x1'], 'y': cord['y1']}
                coord1 = { 'x': cord['x2'], 'y': cord['y2']}
            else:
                coord1 = { 'x': cord['x1'], 'y': cord['y1']}
                coord2 = { 'x': cord['x2'], 'y': cord['y2']}
        else:
            if(cord['y1']>cord['y2']):
                coord2 = { 'x': cord['x1'], 'y': cord['y1']}
                coord1 = { 'x': cord['x2'], 'y': cord['y2']}
            else:
                coord1 = { 'x': cord['x1'], 'y': cord['y1']}
                coord2 = { 'x': cord['x2'], 'y': cord['y2']}
        
        if(coord1['x']>coord2['x']):
            while(coord2['y']>=coord1['y']):
                board[coord1['y']][coord1['x']]+=1
                coord1['y']+=1
                coord1['x']-=1
        else:
            while(coord2['y']>=coord1['y']):
                board[coord1['y']][coord1['x']]+=1
                coord1['y']+=1
                coord1['x']+=1

    for x in range(len(board)):
        #print(board[x])
        for y in range(len(board[x])):
            if(board[x][y]>=2):
                overlaping += 1

    print('Number of points where at least two lines overlap: '+str(overlaping))
            

# puzzle1
get_overlaping_segments()


