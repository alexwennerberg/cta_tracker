import requests, json, datetime, yaml

def get_times(route, stop_id):
	time_list = []
	payload = {"key": yaml.load(open("keys.yml"))["bus"],
				"format": "json",
				"rt": route,
				"stpid": stop_id }
	url = "http://www.ctabustracker.com/bustime/api/v2/getpredictions/"
	response = json.loads(requests.get(url, params=payload).text)["bustime-response"]
	if "prd" not in response:
		return []
	predictions = response["prd"]
	for prediction in predictions:
		time_list.append(wait_time(prediction["prdtm"], prediction["tmstmp"]))
	return time_list

def wait_time(prediction_time, current_time):
	return (format_time(prediction_time) - format_time(current_time)).seconds // 60

def format_time(time):
	year = int(time[:4])
	month = int(time[4:6])
	day = int(time[6:8])
	hour = int(time[9:11])
	minute = int(time[12:14])
	return datetime.datetime(year, month, day, hour, minute)