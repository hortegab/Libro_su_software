#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Lab Total
# Generated: Tue Mar  5 16:59:50 2019
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
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import E3TRadio
import cmath
import math
import numpy
import random
import sip
import sys
from gnuradio import qtgui


class Lab_total(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Lab Total")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lab Total")
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

        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.Constelacion = Constelacion = digital.constellation_qpsk().points()
        self.samp_rate_audio = samp_rate_audio = 11000
        self.NbpS = NbpS = 8
        self.M = M = len(Constelacion)
        self.Rb = Rb = NbpS*samp_rate_audio
        self.BpS = BpS = int(math.log(M,2))
        self.run_stop = run_stop = True
        self.Vp = Vp = 0.6
        self.Tmax_scope = Tmax_scope = 16./samp_rate_audio
        self.Sps = Sps = 8
        self.Rs = Rs = Rb/BpS
        self.NnivelesQ = NnivelesQ = math.pow(2,NbpS)
        self.N = N = 1024

        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((Constelacion), (), 4, 1).base()

        self.Fc = Fc = 80e6
        self.Ensayos = Ensayos = 1000000

        ##################################################
        # Blocks
        ##################################################
        self.menu = Qt.QTabWidget()
        self.menu_widget_0 = Qt.QWidget()
        self.menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_0)
        self.menu_grid_layout_0 = Qt.QGridLayout()
        self.menu_layout_0.addLayout(self.menu_grid_layout_0)
        self.menu.addTab(self.menu_widget_0, 'Tab 0')
        self.top_grid_layout.addWidget(self.menu)
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.menu_grid_layout_0.addWidget(_run_stop_check_box, 0, 0, 1, 2)
        for r in range(0, 1):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	16*Sps, #size
        	Rs*Sps, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1.5, M)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()

        labels = ["M-PAM", 'Codigo', 'Con Scrambling', '', '',
                  '', '', '', '', '']
        widths = [4, 4, 4, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 0, 3, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, 0, 0, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_1_win, 5, 0, 1, 1)
        for r in range(5, 6):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	16*BpS*Sps, #size
        	Rb*Sps, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

        labels = ['Binaria', 'Codigo', 'Con Scrambling', '', '',
                  '', '', '', '', '']
        widths = [4, 4, 4, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 0, 3, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, 0, 0, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_0_win, 4, 0, 1, 1)
        for r in range(4, 5):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	16*BpS, #size
        	Rb, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['Binaria', 'Codigo', 'Con Scrambling', '', '',
                  '', '', '', '', '']
        widths = [4, 4, 4, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 0, 3, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, 0, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	16, #size
        	Rs, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1.5, M)

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

        labels = ["M-PAM", 'Codigo', 'Con Scrambling', '', '',
                  '', '', '', '', '']
        widths = [4, 4, 4, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 0, 3, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, 0, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	Rb*Sps, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['Binaria', 'M-PAM', '', '', '',
                  '', '', '', '', '']
        widths = [4, 4, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.blocks_vector_source_x_0 = blocks.vector_source_b((6,55), True, 1, [])
        self.blocks_unpack_k_bits_bb_0_1_1 = blocks.unpack_k_bits_bb(NbpS)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(BpS, gr.GR_MSB_FIRST)
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(NbpS)
        self.blocks_char_to_float_2_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_2 = blocks.char_to_float(1, 1)
        self.E3TRadio_Zero_Order_Hold_0_0_0 = E3TRadio.Zero_Order_Hold(BpS)
        self.E3TRadio_Zero_Order_Hold_0_0 = E3TRadio.Zero_Order_Hold(Sps)
        self.E3TRadio_Zero_Order_Hold_0 = E3TRadio.Zero_Order_Hold(Sps)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_Zero_Order_Hold_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.E3TRadio_Zero_Order_Hold_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.E3TRadio_Zero_Order_Hold_0_0, 0), (self.E3TRadio_Zero_Order_Hold_0_0_0, 0))
        self.connect((self.E3TRadio_Zero_Order_Hold_0_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.E3TRadio_Zero_Order_Hold_0_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_char_to_float_2, 0), (self.E3TRadio_Zero_Order_Hold_0_0, 0))
        self.connect((self.blocks_char_to_float_2, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_char_to_float_2_0, 0), (self.E3TRadio_Zero_Order_Hold_0, 0))
        self.connect((self.blocks_char_to_float_2_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.blocks_char_to_float_2, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_1_1, 0), (self.blocks_char_to_float_2_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_1_1, 0), (self.blocks_pack_k_bits_bb_0_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_unpack_k_bits_bb_0_1_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio
        self.set_Rb(self.NbpS*self.samp_rate_audio)
        self.set_Tmax_scope(16./self.samp_rate_audio)

    def get_NbpS(self):
        return self.NbpS

    def set_NbpS(self, NbpS):
        self.NbpS = NbpS
        self.set_Rb(self.NbpS*self.samp_rate_audio)
        self.set_NnivelesQ(math.pow(2,self.NbpS))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_BpS(int(math.log(self.M,2)))
        self.qtgui_time_sink_x_0_1.set_y_axis(-1.5, self.M)
        self.qtgui_time_sink_x_0.set_y_axis(-1.5, self.M)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_Rs(self.Rb/self.BpS)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.Rb*self.Sps)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.Rb)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.Rb*self.Sps)

    def get_BpS(self):
        return self.BpS

    def set_BpS(self, BpS):
        self.BpS = BpS
        self.set_Rs(self.Rb/self.BpS)
        self.E3TRadio_Zero_Order_Hold_0_0_0.set_retardo(self.BpS)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        self._run_stop_callback(self.run_stop)
        if self.run_stop: self.start()
        else: self.stop(); self.wait()

    def get_Vp(self):
        return self.Vp

    def set_Vp(self, Vp):
        self.Vp = Vp

    def get_Tmax_scope(self):
        return self.Tmax_scope

    def set_Tmax_scope(self, Tmax_scope):
        self.Tmax_scope = Tmax_scope

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.Rs*self.Sps)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.Rb*self.Sps)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.Rb*self.Sps)
        self.E3TRadio_Zero_Order_Hold_0_0.set_retardo(self.Sps)
        self.E3TRadio_Zero_Order_Hold_0.set_retardo(self.Sps)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.Rs*self.Sps)
        self.qtgui_time_sink_x_0.set_samp_rate(self.Rs)

    def get_NnivelesQ(self):
        return self.NnivelesQ

    def set_NnivelesQ(self, NnivelesQ):
        self.NnivelesQ = NnivelesQ

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc

    def get_Ensayos(self):
        return self.Ensayos

    def set_Ensayos(self, Ensayos):
        self.Ensayos = Ensayos


def main(top_block_cls=Lab_total, options=None):

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
