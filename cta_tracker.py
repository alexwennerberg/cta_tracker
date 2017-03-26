from tkinter import *
from tkinter import ttk
import yaml
from info_finder import get_times

def get_bus_times():
	output_times = []
	with open("config.yml") as f:
		config_data = yaml.load(f)
	for stop in config_data["buses"]:
		route = stop["route"]
		id = stop["id"]
		bus_string = (" ".join([str(route), 
							stop["direction"], 
							stop["label"], 
							", ".join(str(x) for x in get_times(route, id))]))
		bus_string = bus_string + " minutes"
		output_times.append(bus_string)
	return output_times

if __name__ == "__main__":
	root = Tk()
	for i in get_bus_times():	
		w = Label(root, text=i, font=("Helvetica", 30), borderwidth=1, relief="solid")
		w.pack()
	root.mainloop()