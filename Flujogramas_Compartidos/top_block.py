#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Aug 22 09:14:27 2019
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import  math
import E3TRadio
import VCO_hob
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
        self.samp_rate = samp_rate = 32000
        self.run_stop = run_stop = True
        self.N = N = 256

        ##################################################
        # Blocks
        ##################################################
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
        self.qtgui_vector_sink_f_0_0_0 = qtgui.vector_sink_f(
            N,
            0,
            1.0,
            "time",
            "amplitude",
            "sample functions",
            10 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0_0.set_y_axis(-1.5, 1.5)
        self.qtgui_vector_sink_f_0_0_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_0_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0_0.set_ref_level(0)

        labels = ['sample function 0', 'sample  function1', 'sample function 2', 'sample function 3', 'sample function 4',
                  'sample function 5', 'sample function 6', 'sample function 7', 'sample function 8', 'sample function 9']
        widths = [3, 3, 3, 3, 3,
                  3, 3, 3, 3, 3]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(10):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_0_0_win)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            N,
            0,
            1.0,
            "time",
            "amplitude",
            "mean function",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-0.004, 0.004)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
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
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(N, (np.array([1]*N)))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, N)
        self.blocks_stream_to_streams_0 = blocks.stream_to_streams(gr.sizeof_float*N, 10)
        self.blocks_null_sink_0_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((math.pi, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((1/1000., ))
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.analog_random_uniform_source_x_0 = analog.random_uniform_source_i(-1000, 1001, 24)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 1, 0)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 400000)
        self.VCO_hob = VCO_hob.blk()
        self.E3TRadio_vector_average_hob_0 = E3TRadio.vector_average_hob(N, 100000000)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_vector_average_hob_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.VCO_hob, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.VCO_hob, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.VCO_hob, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_null_sink_0_1, 0))
        self.connect((self.analog_random_uniform_source_x_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.VCO_hob, 2))
        self.connect((self.blocks_stream_to_streams_0, 0), (self.qtgui_vector_sink_f_0_0_0, 0))
        self.connect((self.blocks_stream_to_streams_0, 1), (self.qtgui_vector_sink_f_0_0_0, 1))
        self.connect((self.blocks_stream_to_streams_0, 2), (self.qtgui_vector_sink_f_0_0_0, 2))
        self.connect((self.blocks_stream_to_streams_0, 3), (self.qtgui_vector_sink_f_0_0_0, 3))
        self.connect((self.blocks_stream_to_streams_0, 4), (self.qtgui_vector_sink_f_0_0_0, 4))
        self.connect((self.blocks_stream_to_streams_0, 5), (self.qtgui_vector_sink_f_0_0_0, 5))
        self.connect((self.blocks_stream_to_streams_0, 6), (self.qtgui_vector_sink_f_0_0_0, 6))
        self.connect((self.blocks_stream_to_streams_0, 7), (self.qtgui_vector_sink_f_0_0_0, 7))
        self.connect((self.blocks_stream_to_streams_0, 8), (self.qtgui_vector_sink_f_0_0_0, 8))
        self.connect((self.blocks_stream_to_streams_0, 9), (self.qtgui_vector_sink_f_0_0_0, 9))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.E3TRadio_vector_average_hob_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_stream_to_streams_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.VCO_hob, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_null_sink_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.interp_fir_filter_xxx_0.set_taps((np.array([1]*self.N)))


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
