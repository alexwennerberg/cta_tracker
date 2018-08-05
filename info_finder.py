import requests, json, datetime, yaml

def get_bus_times(route, stop_id):
    time_list = []
    payload = {
        "key": yaml.load(open("keys.yml"))["bus"],
        "format": "json",
        "rt": route,
        "stpid": stop_id
    }
    url = "http://www.ctabustracker.com/bustime/api/v2/getpredictions/"
    response = json.loads(requests.get(url, params=payload).text)["bustime-response"]
    if "prd" not in response:
        return []
    predictions = response["prd"]
    for prediction in predictions:
        time_list.append(wait_time(prediction["prdtm"], prediction["tmstmp"]))
    return time_list

def get_train_times(stop_id):
    time_list = []
    payload = {"key": yaml.load(open("keys.yml"))["train"],
                "outputType": "json",
                "stpid": stop_id}
    url = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx/"
    response = json.loads(requests.get(url, params=payload).text)
    for prediction in response["ctatt"]["eta"]:
        time_list.append((format_train_time(prediction["arrT"])-format_train_time(prediction["prdt"])).seconds // 60)
    return time_list

def wait_time(prediction_time, current_time):
    return (format_bus_time(prediction_time) - format_bus_time(current_time)).seconds // 60

# TODO: cleanup lol
def format_train_time(time):
    year = int(time[:4])
    month = int(time[5:7])
    day = int(time[8:10])
    hour = int(time[11:13])
    minute = int(time[14:16])
    second = int(time[17:19])
    return datetime.datetime(year, month, day, hour, minute, second)

def format_bus_time(time):
    year = int(time[:4])
    month = int(time[4:6])
    day = int(time[6:8])
    hour = int(time[9:11])
    minute = int(time[12:14])
    return datetime.datetime(year, month, day, hour, minute)
