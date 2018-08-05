import yaml
from info_finder import get_bus_times, get_train_times

def get_config_data():
    with open("config.yml") as f:
        return yaml.load(f)

    
def formatted_bus_times():
    output_times = []
    config_data = get_config_data()
    bus_string = ""
    for stop in config_data["buses"]:
        route = stop["route"]
        id = stop["id"]
        bus_string += (" ".join([stop["direction"][0],
                                " ".join(str(x).rjust(2) for x in get_bus_times(route, id)[:2])])).ljust(7)
        bus_string += "|"
    return bus_string[:len(bus_string)-1]

def formatted_train_times():
    config_data = get_config_data()
    train_string = ""
    for stop in config_data["trains"][0]["stops"]:
        station_id = stop["id"]
        train_string += (" ".join([
            stop["direction"][0],
            " ".join(str(x).rjust(2) for x in get_train_times(station_id)[:2])])).ljust(7)
        train_string += "|"
    return train_string[:len(train_string)-1]

# 16x2 LCD screen
# O XX XX F XX XX BLUE LINE
# E XX XX W XX XX 74 BUS

if __name__ == "__main__":
    for line in formatted_train_times(), formatted_bus_times():
        print(line)
