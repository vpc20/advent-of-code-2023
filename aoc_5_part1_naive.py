import sys


def create_map_range(input_data):
    map_ranges_txt = [item for item in input_data.split('\n') if item[0].isdigit()]
    map_ranges_array = [item.split(' ') for item in map_ranges_txt]
    return [[int(e) for e in item] for item in map_ranges_array]


def create_map(map_range):
    map = {}
    for destination, source, range_length in map_range:
        print(destination, source, range_length)
        for i in range(range_length):
            map[source + i] = destination + i
    return map


def get_map_value(key, map):
    return map[key] if key in map else key


if __name__ == '__main__':
    f = open('aoc_5_test_data1.txt')
    # f = open('aoc_5_data1.txt')
    input = f.read().split('\n\n')
    f.close()

    for e in input:
        print(e)
        print()

    seed_input = input[0]

    seed_to_soil_input = input[1]
    soil_to_fertilizer_input = input[2]
    fertilizer_to_water_input = input[3]
    water_to_light_input = input[4]
    light_to_temperature_input = input[5]
    temperature_to_humidity_input = input[6]
    humidity_to_location_input = input[7]

    split_seed_input = seed_input.split(': ')
    seeds = [int(e) for e in split_seed_input[1].split()]
    print(seeds)

    seed_to_soil_map_range = create_map_range(seed_to_soil_input)
    print(seed_to_soil_map_range)
    soil_to_fertilizer_map_range = create_map_range(soil_to_fertilizer_input)
    print(soil_to_fertilizer_map_range)
    fertilizer_to_water_map_range = create_map_range(fertilizer_to_water_input)
    print(fertilizer_to_water_map_range)
    water_to_light_map_range = create_map_range(water_to_light_input)
    print(water_to_light_map_range)
    light_to_temperature_map_range = create_map_range(light_to_temperature_input)
    print(light_to_temperature_map_range)
    temperature_to_humidity_map_range = create_map_range(temperature_to_humidity_input)
    print(temperature_to_humidity_map_range)
    humidity_to_location_map_range = create_map_range(humidity_to_location_input)
    print(humidity_to_location_map_range)

    seed_to_soil_map = create_map(seed_to_soil_map_range)
    print(seed_to_soil_map)
    soil_to_fertilizer_map = create_map(soil_to_fertilizer_map_range)
    print(soil_to_fertilizer_map)
    fertilizer_to_water_map = create_map(fertilizer_to_water_map_range)
    print(fertilizer_to_water_map)
    water_to_light_map = create_map(water_to_light_map_range)
    print(water_to_light_map)
    light_to_temperature_map = create_map(light_to_temperature_map_range)
    print(light_to_temperature_map)
    temperature_to_humidity_map = create_map(temperature_to_humidity_map_range)
    print(temperature_to_humidity_map)
    humidity_to_location_map = create_map(humidity_to_location_map_range)
    print(humidity_to_location_map)

    min_location = sys.maxsize
    for seed in seeds:
        soil = get_map_value(seed, seed_to_soil_map)
        print('soil', soil)
        fertilizer = get_map_value(soil, soil_to_fertilizer_map)
        print('fertilizer', fertilizer)
        water = get_map_value(fertilizer, fertilizer_to_water_map)
        print('water', water)
        light = get_map_value(water, water_to_light_map)
        print('light', light)
        temperature = get_map_value(light, light_to_temperature_map)
        print('temperature', temperature)
        humidity = get_map_value(temperature, temperature_to_humidity_map)
        print('humidity', humidity)
        location = get_map_value(humidity, humidity_to_location_map)
        print('location', location)
        min_location = min(min_location, location)

    print(min_location)
