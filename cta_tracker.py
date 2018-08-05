import yaml
from info_finder import get_bus_times, get_train_times

def get_config_data():
    with open("config.yml") as f:
        return yaml.load(f)

def print_times():
    return formatted_bus_times() + formatted_train_times()
    
def formatted_bus_times():
    output_times = []
    config_data = get_config_data()
    for stop in config_data["buses"]:
        route = stop["route"]
        id = stop["id"]
        bus_string = (" ".join([str(route), 
                            stop["direction"], 
                            stop["label"], 
                            ", ".join(str(x) for x in get_bus_times(route, id))]))
        bus_string = bus_string + " minutes"
        output_times.append(bus_string)
    return output_times

def formatted_train_times():
    output_times = []
    config_data = get_config_data()
    for stop in config_data["trains"]:
        station_id = stop["id"]
        bus_string = (" ".join([stop["route"],
                            stop["label"], 
                            "towards", 
                            stop["direction"], 
                            ", ".join(str(x) for x in get_train_times(station_id))]))
        bus_string = bus_string + " minutes"
        output_times.append(bus_string)
    return output_times

# 16x2 LCD screen
# O XX XX F XX XX BLUE LINE
# E XX XX W XX XX 74 BUS

if __name__ == "__main__":
    for time in print_times():
        print(time)
