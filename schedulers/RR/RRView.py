import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from ..abstractions.View import MainWindow
from .RRSceduler import RRScheduler


class RRMainWindow(MainWindow):
	def __init__(self, main_window):
		MainWindow.__init__(self, main_window)

	def schedule(self, widget):
		scheduler = RRScheduler(self.queue)
		gantt_chart = scheduler.schedule()
		self.draw_gantt(gantt_chart)
		
	
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
		
		self.process_Quantum = Gtk.Entry()
		self.process_Quantum.set_text('Quantum time')

		first_row.pack_start(self.process_name_input, True, True, 0)
		first_row.pack_start(self.process_time_input, True, True, 0)
		first_row.pack_start(self.process_arrival_input, True, True, 0)
		first_row.pack_start(self.process_Quantum, True, True, 0)

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
