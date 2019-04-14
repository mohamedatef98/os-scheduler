import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from queue.queue import Queue
from processes.NormalProcess import NormalProcess

class MainWindow(Gtk.Grid):
    def __init__(self, main_window):
        Gtk.Grid.__init__(self)
        self.main_window = main_window
        self.set_column_homogeneous = True

        self.queue = Queue()

        self.set_column_spacing(100)

        results_box = Gtk.ListBox()
        self.results_line = Gtk.ListBox()
        results_box.set_border_width(4)
        results_box.add(self.results_line)

        schedule_button = Gtk.Button('Schedule')
        schedule_button.connect('clicked', self.schedule)

        results_box.set_hexpand(True)
        results_box.add(schedule_button)

        self.attach(results_box, 0, 0, 1, 1)

        processes_box = Gtk.ListBox()
        self.process_lines = Gtk.ListBox()
        processes_box.add(self.process_lines)
        add_process_button = Gtk.Button('Add Process')
        add_process_button.connect('clicked', self.add_process_dialog)

        processes_box.set_hexpand(True)
        processes_box.set_border_width(5)
        processes_box.add(add_process_button)


        self.attach(processes_box, 3, 0, 1, 1)

        self.gantt_chart_box = Gtk.Box()
        self.gantt_chart_box.add(Gtk.Label('GANTT CHART GOES HERE'))
        self.attach(self.gantt_chart_box, 0, 1, 3, 1)


        self.waitTimelabel = Gtk.Label()
        self.waitTimelabel.set_text("Average Waiting Time: ")
        self.attach(self.waitTimelabel, 0, 2, 3, 1)

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
        self.process_arrival_input.set_text('Process Arrival')

        first_row.pack_start(self.process_name_input, True, True, 0)
        first_row.pack_start(self.process_time_input, True, True, 0)
        first_row.pack_start(self.process_arrival_input, True, True, 0)


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


    def cancel(self, widget):
        self.dialog.close()


    def validate(self, widget):
        process_name = self.process_name_input.get_text()
        process_time = self.process_time_input.get_text()
        process_arrival = self.process_arrival_input.get_text()

        try:
            process_time = int(process_time)
            process_arrival = int(process_arrival)
            if(process_arrival < 0 and process_time < 0 and process_name is ''):
                raise Exception('')
            self.queue.addProcess(NormalProcess(process_name, process_arrival, process_time))
        except Exception as e:
            self.validations.set_label('The Process Name is Required, and the process arrival and Time should be non-negative integers')
        else:
            self.cancel(widget)
            self.draw_queue()

    def draw_queue(self):
        for child in self.process_lines.get_children():
            self.process_lines.remove(child)
        for process in self.queue.processes:
            t = str(process.name) + " /// " + str(process.arrival) + " /// " + str(process.time)
            self.process_lines.add(Gtk.Label(t))
            self.process_lines.show_all()


    def schedule(self, widget):
        pass


    def draw_gantt(self, gantt_chart):
        for child in self.gantt_chart_box.get_children():
            self.gantt_chart_box.remove(child)

        for process in gantt_chart.chart:
            l = 'X'
            if process is not None:
                l = process.name
            l = Gtk.Button(l)
            self.gantt_chart_box.add(l)
            self.gantt_chart_box.show_all()

    def setWaitingTime(self, waitTime):
        self.waitTimelabel.set_text("Average Waiting Time: " + str(waitTime))

