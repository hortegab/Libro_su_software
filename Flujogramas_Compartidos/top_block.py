#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon May  6 21:17:04 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import e_signal  # embedded python module
import numpy as np
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.N = N = 32
        self.samp_rate = samp_rate = 32000
        self.run_stop = run_stop = True
        self.retraso = retraso = 0
        self.M = M = N*8

        ##################################################
        # Blocks
        ##################################################
        self._retraso_range = Range(0, N, 1, 0, 200)
        self._retraso_win = RangeWidget(self._retraso_range, self.set_retraso, 'Atrasar senal', "counter_slider", int)
        self.top_grid_layout.addWidget(self._retraso_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_vector_sink_f_0_0_0_0 = qtgui.vector_sink_f(
            M,
            -samp_rate/2,
            (samp_rate)/M,
            "Frecuencia",
            "Amplitud",
            'Fase',
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0_0_0.set_y_axis(0., 1.)
        self.qtgui_vector_sink_f_0_0_0_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0_0_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0_0_0.set_x_axis_units("Hz")
        self.qtgui_vector_sink_f_0_0_0_0.set_y_axis_units("Volt")
        self.qtgui_vector_sink_f_0_0_0_0.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_0_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_0_0_0_win)
        self.qtgui_vector_sink_f_0_0_0 = qtgui.vector_sink_f(
            M,
            -samp_rate/2,
            (samp_rate)/M,
            "Frecuencia",
            "Amplitud",
            'Im',
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0_0.set_y_axis(0., 1.)
        self.qtgui_vector_sink_f_0_0_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0_0.set_x_axis_units("Hz")
        self.qtgui_vector_sink_f_0_0_0.set_y_axis_units("Volt")
        self.qtgui_vector_sink_f_0_0_0.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_0_0_win, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_vector_sink_f_0_0 = qtgui.vector_sink_f(
            M,
            -samp_rate/2,
            (samp_rate)/M,
            "Frecuencia",
            "Amplitud",
            'Re',
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0.set_y_axis(0., 1.)
        self.qtgui_vector_sink_f_0_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0.set_x_axis_units("Hz")
        self.qtgui_vector_sink_f_0_0.set_y_axis_units("Volt")
        self.qtgui_vector_sink_f_0_0.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_0_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            M,
            -samp_rate/2,
            (samp_rate)/M,
            "Frecuencia",
            "Amplitud",
            'magnitud',
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(0., 1.)
        self.qtgui_vector_sink_f_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("Hz")
        self.qtgui_vector_sink_f_0.set_y_axis_units("Volt")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	N*4, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fft_vxx_0 = fft.fft_vcc(M, True, (), True, 1)
        self.blocks_vector_source_x_0 = blocks.vector_source_c(e_signal.pulse_rect(N,N/4), True, 1, [])
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, M)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1./(e_signal.pulse_delta(M)*2+1)))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, retraso)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(M)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(M)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(M)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_arg_0, 0), (self.qtgui_vector_sink_f_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.qtgui_vector_sink_f_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.qtgui_vector_sink_f_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_M(self.N*8)
        self.blocks_vector_source_x_0.set_data(e_signal.pulse_rect(self.N,self.N/4), [])

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_vector_sink_f_0_0_0_0.set_x_axis(-self.samp_rate/2, (self.samp_rate)/self.M)
        self.qtgui_vector_sink_f_0_0_0.set_x_axis(-self.samp_rate/2, (self.samp_rate)/self.M)
        self.qtgui_vector_sink_f_0_0.set_x_axis(-self.samp_rate/2, (self.samp_rate)/self.M)
        self.qtgui_vector_sink_f_0.set_x_axis(-self.samp_rate/2, (self.samp_rate)/self.M)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        self._run_stop_callback(self.run_stop)

    def get_retraso(self):
        return self.retraso

    def set_retraso(self, retraso):
        self.retraso = retraso
        self.blocks_delay_0.set_dly(self.retraso)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.qtgui_vector_sink_f_0_0_0_0.set_x_axis(-self.samp_rate/2, (self.samp_rate)/self.M)
        self.qtgui_vector_sink_f_0_0_0.set_x_axis(-self.samp_rate/2, (self.samp_rate)/self.M)
        self.qtgui_vector_sink_f_0_0.set_x_axis(-self.samp_rate/2, (self.samp_rate)/self.M)
        self.qtgui_vector_sink_f_0.set_x_axis(-self.samp_rate/2, (self.samp_rate)/self.M)
        self.blocks_multiply_const_vxx_0.set_k((1./(e_signal.pulse_delta(self.M)*2+1)))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
