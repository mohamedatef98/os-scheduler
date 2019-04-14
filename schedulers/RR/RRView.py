import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from ..abstractions.View import MainWindow
from .RRSceduler import RRScheduler
from .RRSceduler import RRScheduler
from ..abstractions.NumberEntry import NumberEntry

class RRMainWindow(MainWindow):
	def __init__(self, main_window):
		MainWindow.__init__(self, main_window)
		results_box = Gtk.Box()
		results_box.set_border_width(4)
		
		self.process_Quantum_input = NumberEntry('Quantum time')
		results_box.add(self.process_Quantum_input)

		self.attach(results_box, 1, 0, 1, 1)

	def schedule(self, widget):
		scheduler = RRScheduler(self.queue)
		gantt_chart = scheduler.schedule(int(self.process_Quantum_input.get_text()))
		self.draw_gantt(gantt_chart)
		
	