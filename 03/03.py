def read_file(fileName):
    file = open(fileName)
    array = []

    for line in file:
        array.append(line)

    file.close();
    return array


def get_power_consumption(fileName):
    data = read_file(fileName);
    gamma_rate = ''
    epsilon_rate = ''
    power_consumption = 0

    for bit in range(12):
        bits = {
            "zero": 0,
            "one": 0,
        }
        for number in data:
            if(number[bit]=='0'):
                bits['zero'] = bits['zero'] + 1
            if(number[bit]=='1'):
                bits['one'] = bits['one'] + 1

        print(bits)
        if(bits['zero'] > bits['one']):
            gamma_rate = gamma_rate + '0'
            epsilon_rate = epsilon_rate + '1'
        if(bits['one']>bits['zero']):
            gamma_rate = gamma_rate + '1'
            epsilon_rate = epsilon_rate + '0'
    
    gamma_rate = int(gamma_rate,2)
    epsilon_rate = int(epsilon_rate,2)
    power_consumption = gamma_rate*epsilon_rate
    print('gamma_rate: '+str(gamma_rate))
    print('epsilon_rate: '+str(epsilon_rate))
    print('Power consumption: '+str(power_consumption))



def get_rating(type, fileName):
    numbers = read_file(fileName)

    for bit in range(12):
        bits = {
            "zero": 0,
            "nums_zero": [],
            "one": 0,
            "nums_one": []
        }

        for number in numbers:
            if(number[bit]=='0'):
                bits['zero'] = bits['zero'] + 1
                bits['nums_zero'].append(number)
            if(number[bit]=='1'):
                bits['one'] = bits['one'] + 1
                bits['nums_one'].append(number)
        
        bit_criteria = 'nums_'
        if(type=='oxygen'):
            if(bits['zero'] > bits['one']):
                bit_criteria += 'zero'
            if(bits['one'] >= bits['zero']):
                bit_criteria += 'one'
        
        if(type=='CO2'):
            if(bits['one'] >= bits['zero']):
                bit_criteria += 'zero'
            if(bits['zero'] > bits['one']):
                bit_criteria += 'one'
        
        numbers = bits[bit_criteria]

        if(len(numbers)==1):
            return numbers[0]


def get_life_support_rating(fileName):
    oxygen = int(get_rating('oxygen', fileName), 2);
    Co2 = int(get_rating('CO2', fileName), 2);
    life_support_rating = oxygen*Co2
    print('oxygen: '+str(oxygen))
    print('Co2: '+str(Co2))
    print('Life support rating: '+str(life_support_rating))

# puzzle1
get_power_consumption('data.txt')

# puzzle2
get_life_support_rating('data.txt');

