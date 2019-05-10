#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri May  3 16:16:38 2019
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from b_discriminador_frec_umd_cf import b_discriminador_frec_umd_cf  # grc-generated hier_block
from gnuradio import analog
from gnuradio import audio
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
import math
import sip
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
        self.samp_rate_audio = samp_rate_audio = 11000
        self.D = D = 15.
        self.BWm = BWm = samp_rate_audio/2.
        self.DeltaF = DeltaF = D*BWm
        self.BW = BW = 2*DeltaF+2*BWm
        self.Ap = Ap = 1.
        self.samp_rate = samp_rate = 390625
        self.run_stop = run_stop = True
        self.Kf = Kf = DeltaF/Ap
        self.Gain_Tx_precanal = Gain_Tx_precanal = 0.7
        self.Gain_Tx_USRP_max = Gain_Tx_USRP_max = 60.
        self.Gain_Tx_USRP = Gain_Tx_USRP = 0
        self.Gain_Rx_post_canal = Gain_Rx_post_canal = 1
        self.Gain_Rx_USRP_max = Gain_Rx_USRP_max = 38
        self.Gain_Rx_USRP = Gain_Rx_USRP = 0
        self.Fc = Fc = 99000000
        self.B = B = 2*BW
        self.Audio_Gain = Audio_Gain = 1.

        ##################################################
        # Blocks
        ##################################################
        self._Gain_Tx_precanal_range = Range(0, 2., 2./100., 0.7, 200)
        self._Gain_Tx_precanal_win = RangeWidget(self._Gain_Tx_precanal_range, self.set_Gain_Tx_precanal, 'Gain_Tx_precanal', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Gain_Tx_precanal_win, 1, 2, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(1,2)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(2,3)]
        self._Gain_Tx_USRP_range = Range(0, Gain_Tx_USRP_max, Gain_Tx_USRP_max/100., 0, 200)
        self._Gain_Tx_USRP_win = RangeWidget(self._Gain_Tx_USRP_range, self.set_Gain_Tx_USRP, 'Ganancia del USRP Tx', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Gain_Tx_USRP_win, 0, 3, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(3,4)]
        self._Gain_Rx_post_canal_range = Range(0, 1000., 1000./100., 1, 200)
        self._Gain_Rx_post_canal_win = RangeWidget(self._Gain_Rx_post_canal_range, self.set_Gain_Rx_post_canal, 'Gain_Rx_post_canal', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Gain_Rx_post_canal_win, 1, 3, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(1,2)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(3,4)]
        self._Gain_Rx_USRP_range = Range(0, Gain_Rx_USRP_max, Gain_Rx_USRP_max/100., 0, 200)
        self._Gain_Rx_USRP_win = RangeWidget(self._Gain_Rx_USRP_range, self.set_Gain_Rx_USRP, 'Ganancia del USRP Rx', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Gain_Rx_USRP_win, 0, 2, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(2,3)]
        self._Audio_Gain_range = Range(0, 4, 4./100., 1., 200)
        self._Audio_Gain_win = RangeWidget(self._Audio_Gain_range, self.set_Audio_Gain, 'Volumen', "dial", float)
        self.top_grid_layout.addWidget(self._Audio_Gain_win, 0, 1, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(1,2)]
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(Fc, 0)
        self.uhd_usrp_source_0.set_gain(Gain_Rx_USRP, 0)
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
        self.uhd_usrp_sink_0.set_gain(Gain_Tx_USRP, 0)
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
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=samp_rate_audio,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=samp_rate,
                decimation=samp_rate_audio,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'PSD. Salida del Filtro receptor', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['.', '', '', '', '',
                  '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 4, 2, 1, 2)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(4,5)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(2,4)]
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"PSD. Entrada del USRP", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['.', '', '', '', '',
                  '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 4, 0, 1, 2)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(4,5)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,2)]
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	1024, #size
        	'Salida del del Filtro receptor', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()

        labels = ['-', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win, 5, 1, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(5,6)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(1,2)]
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	'Entrada del Entrada del USRP', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['.', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 5, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(5,6)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	Gain_Rx_post_canal, samp_rate, BW, BW/16., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	Gain_Tx_precanal, samp_rate, BW, BW/16., firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_0_0 = blocks.wavfile_source('/home/hob/MisGITS/Libro_su_software/Flujogramas_Compartidos/bush-clinton_debate_waffle.wav', True)
        self.blocks_vco_c_0_0_0 = blocks.vco_c(samp_rate, 2*math.pi, 1)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((Kf, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((Audio_Gain, ))
        self.b_discriminador_frec_umd_cf_0 = b_discriminador_frec_umd_cf()
        self.audio_sink_0 = audio.sink(samp_rate_audio, '', True)
        self.analog_fm_preemph_0 = analog.fm_preemph(fs=samp_rate, tau=75e-6, fh=-1.0)
        self.analog_fm_deemph_0 = analog.fm_deemph(fs=samp_rate, tau=75e-6)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fm_deemph_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.analog_fm_preemph_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.b_discriminador_frec_umd_cf_0, 0), (self.analog_fm_deemph_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_vco_c_0_0_0, 0))
        self.connect((self.blocks_vco_c_0_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.b_discriminador_frec_umd_cf_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_fm_preemph_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio
        self.set_BWm(self.samp_rate_audio/2.)

    def get_D(self):
        return self.D

    def set_D(self, D):
        self.D = D
        self.set_DeltaF(self.D*self.BWm)

    def get_BWm(self):
        return self.BWm

    def set_BWm(self, BWm):
        self.BWm = BWm
        self.set_BW(2*self.DeltaF+2*self.BWm)
        self.set_DeltaF(self.D*self.BWm)

    def get_DeltaF(self):
        return self.DeltaF

    def set_DeltaF(self, DeltaF):
        self.DeltaF = DeltaF
        self.set_Kf(self.DeltaF/self.Ap)
        self.set_BW(2*self.DeltaF+2*self.BWm)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(self.Gain_Rx_post_canal, self.samp_rate, self.BW, self.BW/16., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.Gain_Tx_precanal, self.samp_rate, self.BW, self.BW/16., firdes.WIN_HAMMING, 6.76))
        self.set_B(2*self.BW)

    def get_Ap(self):
        return self.Ap

    def set_Ap(self, Ap):
        self.Ap = Ap
        self.set_Kf(self.DeltaF/self.Ap)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(self.Gain_Rx_post_canal, self.samp_rate, self.BW, self.BW/16., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.Gain_Tx_precanal, self.samp_rate, self.BW, self.BW/16., firdes.WIN_HAMMING, 6.76))

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_Kf(self):
        return self.Kf

    def set_Kf(self, Kf):
        self.Kf = Kf
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.Kf, ))

    def get_Gain_Tx_precanal(self):
        return self.Gain_Tx_precanal

    def set_Gain_Tx_precanal(self, Gain_Tx_precanal):
        self.Gain_Tx_precanal = Gain_Tx_precanal
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.Gain_Tx_precanal, self.samp_rate, self.BW, self.BW/16., firdes.WIN_HAMMING, 6.76))

    def get_Gain_Tx_USRP_max(self):
        return self.Gain_Tx_USRP_max

    def set_Gain_Tx_USRP_max(self, Gain_Tx_USRP_max):
        self.Gain_Tx_USRP_max = Gain_Tx_USRP_max

    def get_Gain_Tx_USRP(self):
        return self.Gain_Tx_USRP

    def set_Gain_Tx_USRP(self, Gain_Tx_USRP):
        self.Gain_Tx_USRP = Gain_Tx_USRP
        self.uhd_usrp_sink_0.set_gain(self.Gain_Tx_USRP, 0)


    def get_Gain_Rx_post_canal(self):
        return self.Gain_Rx_post_canal

    def set_Gain_Rx_post_canal(self, Gain_Rx_post_canal):
        self.Gain_Rx_post_canal = Gain_Rx_post_canal
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(self.Gain_Rx_post_canal, self.samp_rate, self.BW, self.BW/16., firdes.WIN_HAMMING, 6.76))

    def get_Gain_Rx_USRP_max(self):
        return self.Gain_Rx_USRP_max

    def set_Gain_Rx_USRP_max(self, Gain_Rx_USRP_max):
        self.Gain_Rx_USRP_max = Gain_Rx_USRP_max

    def get_Gain_Rx_USRP(self):
        return self.Gain_Rx_USRP

    def set_Gain_Rx_USRP(self, Gain_Rx_USRP):
        self.Gain_Rx_USRP = Gain_Rx_USRP
        self.uhd_usrp_source_0.set_gain(self.Gain_Rx_USRP, 0)


    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.uhd_usrp_source_0.set_center_freq(self.Fc, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.Fc, 0)

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B

    def get_Audio_Gain(self):
        return self.Audio_Gain

    def set_Audio_Gain(self, Audio_Gain):
        self.Audio_Gain = Audio_Gain
        self.blocks_multiply_const_vxx_0.set_k((self.Audio_Gain, ))


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
