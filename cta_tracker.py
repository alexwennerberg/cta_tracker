from tkinter import *
from tkinter import ttk
import yaml
from info_finder import get_times

def config_setup():
	with open("config.yml") as f:
		config_data = yaml.load(f)
	for stop in config_data["buses"]:
		route = stop["route"]
		id = stop["id"]
		print(route, stop["direction"], stop["label"], get_times(route, id))

if __name__ == "__main__":
	config_setup()
	#root = Tk()
	#ttk.Button(root, text="Hello World").grid()
	#root.mainloop()