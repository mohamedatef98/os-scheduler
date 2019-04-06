import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from ..abstractions.View import MainWindow
from .SJFSceduler import SJFScheduler
from queue.queue import Queue
from processes.NormalProcess import NormalProcess

class SJFMainWindow(MainWindow):
	def __init__(self, main_window):
		MainWindow.__init__(self, main_window)
		results_box = Gtk.Box()
		results_box.set_border_width(4)

		self.preemptive = Gtk.CheckButton(("Preemptive"))
		results_box.add(self.preemptive)

		self.attach(results_box, 1, 0, 1, 1)

	def schedule(self, widget):
		scheduler = SJFScheduler(self.queue)
		gantt_chart = scheduler.schedule(self.preemptive.get_active())
		self.draw_gantt(gantt_chart)
		
	
