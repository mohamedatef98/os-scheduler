import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from ..abstractions.View import MainWindow
from .PrioritySceduler_V2 import PriorityScheduler
from processes.PriorityProcess import PriorityProcess

class PriorityMainWindow(MainWindow):
	def __init__(self, main_window):
		MainWindow.__init__(self, main_window)
		results_box = Gtk.Box()
		results_box.set_border_width(4)

		self.preemptive = Gtk.CheckButton(("Preemptive"))
		results_box.add(self.preemptive)

		self.attach(results_box, 1, 0, 1, 1)
		'''
		#for debug
		self.queue.addProcess(PriorityProcess("p0", 0, 5,5))
		self.queue.addProcess(PriorityProcess("p1", 1, 5,4))
		self.queue.addProcess(PriorityProcess("p2", 1, 5,3))
		self.queue.addProcess(PriorityProcess("p3", 3, 5,2))
		self.queue.addProcess(PriorityProcess("p4", 3, 5,1))
		self.draw_queue()
		'''

	def schedule(self, widget):
		scheduler = PriorityScheduler(self.queue)
		gantt_chart = scheduler.schedule(self.preemptive.get_active())
		self.draw_gantt(gantt_chart)
		self.setWaitingTime(scheduler.avgWait)
		
	#overwrites
	def add_process_dialog(self, widget):
		self.dialog = Gtk.Dialog('Add Process', self.main_window)
		dialog_main_window = self.dialog.get_content_area()


		#Row for the text fields
		first_row = Gtk.Box(spacing=50)

		#Row for the Add and Cancel buttons
		second_row = Gtk.Box(spacing=50)

		#Row for validation information
		third_row = Gtk.Box(spacing=50)

		dialog_main_window.add(first_row)
		dialog_main_window.add(second_row)
		dialog_main_window.add(third_row)


		#Add the text fields to the first row
		self.process_name_input = Gtk.Entry()
		self.process_name_input.set_text('Process Name')

		self.process_time_input = Gtk.Entry()
		self.process_time_input.set_text('Process Time')

		self.process_arrival_input = Gtk.Entry()
		self.process_arrival_input.set_text('Process Arrival Time')
		
		self.process_Priority = Gtk.Entry()
		self.process_Priority.set_text('Process Priority')

		first_row.pack_start(self.process_name_input, True, True, 0)
		first_row.pack_start(self.process_time_input, True, True, 0)
		first_row.pack_start(self.process_arrival_input, True, True, 0)
		first_row.pack_start(self.process_Priority, True, True, 0)

		#Add the buttons to the second row

		add_process_button = Gtk.Button('Add')
		add_process_button.connect('clicked', self.validate)

		cancel_button = Gtk.Button('Cancel')
		cancel_button.connect('clicked', self.cancel)
		second_row.pack_start(add_process_button, True, True, 0)
		second_row.pack_start(cancel_button, True, True, 0)


		#Add the validations row
		self.validations = Gtk.Label()
		third_row.pack_start(self.validations, True, True, 0)

		self.dialog.show_all()
		
	def validate(self, widget):
		process_name = self.process_name_input.get_text()
		process_time = self.process_time_input.get_text()
		process_arrival = self.process_arrival_input.get_text()
		process_priority = self.process_Priority.get_text()
		try:
		    process_time = int(process_time)
		    process_arrival = int(process_arrival)
		    process_priority = int(process_priority)
		    if(process_arrival < 0 and process_time < 0 and process_name is ''):
		        raise Exception('')
			
		    self.queue.addProcess(PriorityProcess(process_name, process_arrival, process_time,process_priority))
		except Exception as e:
		    self.validations.set_label('The Process Name is Required, and the process arrival and Time should be non-negative integers')
		else:
		    self.cancel(widget)
		    self.draw_queue()

	def draw_queue(self):
		for child in self.process_lines.get_children():
			self.process_lines.remove(child)
		for process in self.queue.processes:
			t = str(process.name) + " /// " + str(process.arrival) + " /// " + str(process.time) + " /// " + str(process.priority)
			self.process_lines.add(Gtk.Label(t))
			self.process_lines.show_all()


