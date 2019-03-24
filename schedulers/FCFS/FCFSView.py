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
        for child in self.gantt_chart_box.get_children():
            self.gantt_chart_box.remove(child)

        for process in gantt_chart.chart:
            l = 'X'
            if process is not None:
                l = process.name
            l = Gtk.Button(l)
            self.gantt_chart_box.add(l)
            self.gantt_chart_box.show_all()


