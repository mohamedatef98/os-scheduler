import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from schedulers.FCFS.FCFSView import FCFSMainWindow
class OSWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="OS PROJECT")

        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(100)


        label = Gtk.Label()
        label.set_markup("<big>A fancy label</big>")
        stack.add_titled(label, "label", "A label")

        fcfs = FCFSMainWindow()
        stack.add_titled(fcfs, "fcfs", "FCFS")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)


        self.connect('destroy', Gtk.main_quit)
        self.show_all()


    def run(self):
        Gtk.main()