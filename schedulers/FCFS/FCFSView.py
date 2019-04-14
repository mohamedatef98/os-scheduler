import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from processes.NormalProcess import NormalProcess

from ..abstractions.View import MainWindow
from .FCFSSceduler import FCFSScheduler

class FCFSMainWindow(MainWindow):
	def __init__(self, main_window):
		MainWindow.__init__(self, main_window)

		'''
		#for debug
		self.queue.addProcess(NormalProcess("p0", 0, 5))
		self.queue.addProcess(NormalProcess("p1", 1, 1))
		self.queue.addProcess(NormalProcess("p2", 2, 1))
		#self.queue.addProcess(NormalProcess("p3", 3, 5,2))
		#self.queue.addProcess(NormalProcess("p4", 3, 5,1))
		self.draw_queue()
		'''

	def schedule(self, widget):
		scheduler = FCFSScheduler(self.queue)
		gantt_chart = scheduler.schedule()
		self.draw_gantt(gantt_chart)
		self.setWaitingTime(scheduler.avgWait)

