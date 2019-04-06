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
		
	
