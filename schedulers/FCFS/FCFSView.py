import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from ..abstractions.View import MainWindow

class FCFSMainWindow(MainWindow):
    def __init__(self):
        MainWindow.__init__(self)