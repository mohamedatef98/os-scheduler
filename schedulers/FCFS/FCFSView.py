import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from ..abstractions.View import MainWindow
from .FCFSSceduler import FCFSScheduler

class FCFSMainWindow(MainWindow):
    def __init__(self, main_window):
        MainWindow.__init__(self, main_window)

    def schedule(self, widget):
        scheduler = FCFSScheduler(self.queue)
        gantt_chart = scheduler.schedule()
        self.draw_gantt(gantt_chart)


