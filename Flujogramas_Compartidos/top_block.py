#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu May 16 18:11:56 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import e_Accum_ff
import e_VCO_fase_fc_0
import math
import sip
import sys
import time
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

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 64000
        self.Kd = Kd = 128
        self.samp_rate_out = samp_rate_out = samp_rate/Kd
        self.run_stop = run_stop = True
        self.r = r = 0.0
        self.Tupdate = Tupdate = 1./100.
        self.P = P = 0.
        self.Fc = Fc = 88000000
        self.F = F = 0.
        self.Ar = Ar = 0.
        self.A = A = 1.

        ##################################################
        # Blocks
        ##################################################
        self.menu = Qt.QTabWidget()
        self.menu_widget_0 = Qt.QWidget()
        self.menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_0)
        self.menu_grid_layout_0 = Qt.QGridLayout()
        self.menu_layout_0.addLayout(self.menu_grid_layout_0)
        self.menu.addTab(self.menu_widget_0, 'Transmisor')
        self.menu_widget_1 = Qt.QWidget()
        self.menu_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_1)
        self.menu_grid_layout_1 = Qt.QGridLayout()
        self.menu_layout_1.addLayout(self.menu_grid_layout_1)
        self.menu.addTab(self.menu_widget_1, 'Receptor')
        self.top_layout.addWidget(self.menu)
        self._P_range = Range(-2.*math.pi, 2.*math.pi, (4.*math.pi)/360., 0., 200)
        self._P_win = RangeWidget(self._P_range, self.set_P, 'Fase', "counter_slider", float)
        self.top_grid_layout.addWidget(self._P_win, 1, 1, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(1,2)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(1,2)]
        self._F_range = Range(-2.4, 2.4, (2*2.4)/1000., 0., 200)
        self._F_win = RangeWidget(self._F_range, self.set_F, 'Frecuencia', "counter_slider", float)
        self.top_grid_layout.addWidget(self._F_win, 1, 2, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(1,2)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(2,3)]
        self._A_range = Range(-1.5, 1.5, (1.5)/100., 1., 200)
        self._A_win = RangeWidget(self._A_range, self.set_A, 'A', "counter_slider", float)
        self.top_grid_layout.addWidget(self._A_win, 1, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(1,2)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(Fc, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(Fc, 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate,
                decimation=390625,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=390625,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=Kd,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=Kd,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=Kd,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=Kd,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=Kd,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_c(
        	1024, #size
        	(samp_rate/Kd), #samp_rate
        	"Senal Modulada", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(Tupdate)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1.5, 1.5)

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

        labels = ['Re', 'Im', '', '', '',
                  '', '', '', '', '']
        widths = [3, 3, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_1_win, 4, 1, 1, 2)
        [self.menu_grid_layout_1.setRowStretch(r,1) for r in range(4,5)]
        [self.menu_grid_layout_1.setColumnStretch(c,1) for c in range(1,3)]
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	(samp_rate/Kd), #samp_rate
        	"Nivel de Amplitud", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(Tupdate)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_0_0.set_y_label('Amplitud', 'volts')

        self.qtgui_time_sink_x_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0_0.disable_legend()

        labels = ['.', '', '', '', '',
                  '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_0_0_win, 3, 0, 1, 1)
        [self.menu_grid_layout_0.setRowStretch(r,1) for r in range(3,4)]
        [self.menu_grid_layout_0.setColumnStretch(c,1) for c in range(0,1)]
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	(samp_rate/Kd), #samp_rate
        	"Nivel de Fase", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(Tupdate)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-2*math.pi, 2*math.pi)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Fase', 'radianes')

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

        labels = ['.', '', '', '', '',
                  '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
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
        self.menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_0_win, 3, 1, 1, 1)
        [self.menu_grid_layout_0.setRowStretch(r,1) for r in range(3,4)]
        [self.menu_grid_layout_0.setColumnStretch(c,1) for c in range(1,2)]
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	(samp_rate/Kd), #samp_rate
        	"Nivel de frecuencia", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(Tupdate)
        self.qtgui_time_sink_x_0_0.set_y_axis(-2.5, 2.5)

        self.qtgui_time_sink_x_0_0.set_y_label('Frecuencia', 'Hz')

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['.', '', '', '', '',
                  '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
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
        self.menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_win, 3, 2, 1, 1)
        [self.menu_grid_layout_0.setRowStretch(r,1) for r in range(3,4)]
        [self.menu_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	(samp_rate/Kd), #samp_rate
        	"Senal Modulada", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(Tupdate)
        self.qtgui_time_sink_x_0.set_y_axis(-1.5, 1.5)

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

        labels = ['Re', 'Im', '', '', '',
                  '', '', '', '', '']
        widths = [3, 3, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
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
        self.menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_win, 4, 1, 1, 2)
        [self.menu_grid_layout_0.setRowStretch(r,1) for r in range(4,5)]
        [self.menu_grid_layout_0.setColumnStretch(c,1) for c in range(1,3)]
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	8, #size
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(Tupdate)
        self.qtgui_const_sink_x_0_0.set_y_axis(-1.5, 1.5)
        self.qtgui_const_sink_x_0_0.set_x_axis(-1.5, 1.5)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()

        labels = ['.', '', '', '', '',
                  '', '', '', '', '']
        widths = [4, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_1.addWidget(self._qtgui_const_sink_x_0_0_win, 4, 0, 1, 1)
        [self.menu_grid_layout_1.setRowStretch(r,1) for r in range(4,5)]
        [self.menu_grid_layout_1.setColumnStretch(c,1) for c in range(0,1)]
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	8, #size
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(Tupdate)
        self.qtgui_const_sink_x_0.set_y_axis(-1.5, 1.5)
        self.qtgui_const_sink_x_0.set_x_axis(-1.5, 1.5)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['.', '', '', '', '',
                  '', '', '', '', '']
        widths = [4, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_0.addWidget(self._qtgui_const_sink_x_0_win, 4, 0, 1, 1)
        [self.menu_grid_layout_0.setRowStretch(r,1) for r in range(4,5)]
        [self.menu_grid_layout_0.setColumnStretch(c,1) for c in range(0,1)]
        self.e_VCO_fase_fc_0 = e_VCO_fase_fc_0.blk()
        self.e_Accum_ff = e_Accum_ff.blk()
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0_0_0_1_0_0 = blocks.multiply_const_vff((2*math.pi/samp_rate, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, A)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, P)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, F)
        self._Ar_range = Range(0, 4., (4.)/50., 0., 200)
        self._Ar_win = RangeWidget(self._Ar_range, self.set_Ar, 'Ruido', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Ar_win, 2, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(2,3)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.e_Accum_ff, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.e_VCO_fase_fc_0, 1))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.rational_resampler_xxx_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.e_VCO_fase_fc_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_1_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.e_Accum_ff, 0), (self.blocks_multiply_const_vxx_0_0_0_1_0_0, 0))
        self.connect((self.e_VCO_fase_fc_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.e_VCO_fase_fc_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.rational_resampler_xxx_0_1, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.rational_resampler_xxx_1_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.set_samp_rate_out(self.samp_rate/self.Kd)
        self.qtgui_time_sink_x_0_1.set_samp_rate((self.samp_rate/self.Kd))
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate((self.samp_rate/self.Kd))
        self.qtgui_time_sink_x_0_0_0.set_samp_rate((self.samp_rate/self.Kd))
        self.qtgui_time_sink_x_0_0.set_samp_rate((self.samp_rate/self.Kd))
        self.qtgui_time_sink_x_0.set_samp_rate((self.samp_rate/self.Kd))
        self.blocks_multiply_const_vxx_0_0_0_1_0_0.set_k((2*math.pi/self.samp_rate, ))

    def get_Kd(self):
        return self.Kd

    def set_Kd(self, Kd):
        self.Kd = Kd
        self.set_samp_rate_out(self.samp_rate/self.Kd)
        self.qtgui_time_sink_x_0_1.set_samp_rate((self.samp_rate/self.Kd))
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate((self.samp_rate/self.Kd))
        self.qtgui_time_sink_x_0_0_0.set_samp_rate((self.samp_rate/self.Kd))
        self.qtgui_time_sink_x_0_0.set_samp_rate((self.samp_rate/self.Kd))
        self.qtgui_time_sink_x_0.set_samp_rate((self.samp_rate/self.Kd))

    def get_samp_rate_out(self):
        return self.samp_rate_out

    def set_samp_rate_out(self, samp_rate_out):
        self.samp_rate_out = samp_rate_out

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_r(self):
        return self.r

    def set_r(self, r):
        self.r = r

    def get_Tupdate(self):
        return self.Tupdate

    def set_Tupdate(self, Tupdate):
        self.Tupdate = Tupdate
        self.qtgui_time_sink_x_0_1.set_update_time(self.Tupdate)
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(self.Tupdate)
        self.qtgui_time_sink_x_0_0_0.set_update_time(self.Tupdate)
        self.qtgui_time_sink_x_0_0.set_update_time(self.Tupdate)
        self.qtgui_time_sink_x_0.set_update_time(self.Tupdate)
        self.qtgui_const_sink_x_0_0.set_update_time(self.Tupdate)
        self.qtgui_const_sink_x_0.set_update_time(self.Tupdate)

    def get_P(self):
        return self.P

    def set_P(self, P):
        self.P = P
        self.analog_const_source_x_0_0.set_offset(self.P)

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.uhd_usrp_source_0.set_center_freq(self.Fc, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.Fc, 0)

    def get_F(self):
        return self.F

    def set_F(self, F):
        self.F = F
        self.analog_const_source_x_0.set_offset(self.F)

    def get_Ar(self):
        return self.Ar

    def set_Ar(self, Ar):
        self.Ar = Ar

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A
        self.analog_const_source_x_0_0_0.set_offset(self.A)


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
