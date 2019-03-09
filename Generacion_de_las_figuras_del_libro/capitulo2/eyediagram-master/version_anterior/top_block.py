#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Apr 26 20:23:57 2018
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from b_Eye_Diagram_simple import b_Eye_Diagram_simple  # grc-generated hier_block
from b_Nyquis_Filter_ff import b_Nyquis_Filter_ff  # grc-generated hier_block
from b_Raised_cosine_ff import b_Raised_cosine_ff  # grc-generated hier_block
from b_binary_gen_rand import b_binary_gen_rand  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import wform  # embedded python module


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, ntaps=128, rolloff=0.5):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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
        # Parameters
        ##################################################
        self.ntaps = ntaps
        self.rolloff = rolloff

        ##################################################
        # Variables
        ##################################################
        self.Sps = Sps = 8
        self.samp_rate = samp_rate = 256e3
        self.h_rrc = h_rrc = wform.rrcos(Sps,ntaps,rolloff)
        self.h_rect = h_rect = wform.rect(Sps)
        self.Rb = Rb = 32000
        self.NodB = NodB = -100
        self.Delay_rect = Delay_rect = 0
        self.Delay_RRC = Delay_RRC = 0
        self.Delay_RC = Delay_RC = 72
        self.Delay_Nyquist = Delay_Nyquist = 0

        ##################################################
        # Blocks
        ##################################################
        self._Delay_rect_range = Range(0, ntaps*2, 1, 0, 200)
        self._Delay_rect_win = RangeWidget(self._Delay_rect_range, self.set_Delay_rect, "Retraso Rect", "counter_slider", int)
        self.top_grid_layout.addWidget(self._Delay_rect_win, 1,0,1,1)
        self._Delay_RRC_range = Range(0, ntaps*10000, Sps, 0, 200)
        self._Delay_RRC_win = RangeWidget(self._Delay_RRC_range, self.set_Delay_RRC, "Retraso RRC", "counter_slider", int)
        self.top_grid_layout.addWidget(self._Delay_RRC_win, 1,3,1,1)
        self._Delay_RC_range = Range(0, ntaps*10000, Sps, 72, 200)
        self._Delay_RC_win = RangeWidget(self._Delay_RC_range, self.set_Delay_RC, "Retraso RC", "counter_slider", int)
        self.top_grid_layout.addWidget(self._Delay_RC_win, 1,2,1,1)
        self._Delay_Nyquist_range = Range(0, ntaps*10000, Sps, 0, 200)
        self._Delay_Nyquist_win = RangeWidget(self._Delay_Nyquist_range, self.set_Delay_Nyquist, "Retraso Nyq", "counter_slider", int)
        self.top_grid_layout.addWidget(self._Delay_Nyquist_win, 1,1,1,1)
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_fff(Sps, firdes.root_raised_cosine(
        	8, samp_rate, samp_rate/Sps, rolloff, ntaps))
        self.qtgui_time_sink_x_0_0_0_0_0 = qtgui.time_sink_f(
        	32*Sps, #size
        	samp_rate, #samp_rate
        	"Wave Forming", #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0.set_y_axis(-0.3, 1.2)
        
        self.qtgui_time_sink_x_0_0_0_0_0.set_y_label("RC Filter Poly", "")
        
        self.qtgui_time_sink_x_0_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0_0_0.disable_legend()
        
        labels = [" Rect", "Nyq", "RC", "RRC", "",
                  "", "", "", "", ""]
        widths = [3, 3, 3, 3, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(4):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	32, #size
        	Rb, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ["Binary source", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
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
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.interp_fir_filter_xxx_0_0_0 = filter.interp_fir_filter_fff(Sps, (Sps*[1.,] ))
        self.interp_fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self.blocks_throttle_0_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((2, ))
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, "/home/jhon/Escritorio/datos", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0_0_2 = blocks.delay(gr.sizeof_float*1, Delay_RC)
        self.blocks_delay_0_0_1 = blocks.delay(gr.sizeof_float*1, Delay_RRC)
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_float*1, Delay_Nyquist)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 121+ntaps*8+Delay_rect)
        self.b_binary_gen_rand_0 = b_binary_gen_rand()
        self.b_Raised_cosine_ff_0_0 = b_Raised_cosine_ff(
            ntaps=ntaps,
            rolloff=rolloff,
            samp_rate=samp_rate,
            sps=Sps,
        )
        self.b_Nyquis_Filter_ff_0 = b_Nyquis_Filter_ff(
            Ganancia=1.,
            Sps=Sps,
            ntaps=ntaps,
        )
        self.b_Eye_Diagram_simple_0 = b_Eye_Diagram_simple(
            AlphaLineas=0.5,
            Delay=0,
            GrosorLineas=20,
            N_eyes=2,
            Samprate=samp_rate,
            Sps=Sps,
            Title="Eye Diagramm",
            Ymax=2,
            Ymin=-2,
        )
        self.top_layout.addWidget(self.b_Eye_Diagram_simple_0)
        self._NodB_range = Range(-100, 0., 1., -100, 200)
        self._NodB_win = RangeWidget(self._NodB_range, self.set_NodB, "No (in dB for white noise)", "counter_slider", float)
        self.top_grid_layout.addWidget(self._NodB_win, 0,1,1,1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_Nyquis_Filter_ff_0, 0), (self.blocks_delay_0_0_0, 0))    
        self.connect((self.b_Raised_cosine_ff_0_0, 0), (self.blocks_delay_0_0_2, 0))    
        self.connect((self.b_binary_gen_rand_0, 0), (self.b_Nyquis_Filter_ff_0, 0))    
        self.connect((self.b_binary_gen_rand_0, 0), (self.b_Raised_cosine_ff_0_0, 0))    
        self.connect((self.b_binary_gen_rand_0, 0), (self.interp_fir_filter_xxx_0_0_0, 0))    
        self.connect((self.b_binary_gen_rand_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.b_binary_gen_rand_0, 0), (self.root_raised_cosine_filter_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_throttle_0_0_0_0, 0))    
        self.connect((self.blocks_delay_0_0_0, 0), (self.b_Eye_Diagram_simple_0, 0))    
        self.connect((self.blocks_delay_0_0_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_delay_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 1))    
        self.connect((self.blocks_delay_0_0_1, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 3))    
        self.connect((self.blocks_delay_0_0_2, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 2))    
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_delay_0_0_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_h_rrc(wform.rrcos(self.Sps,self.ntaps,self.rolloff))
        self.b_Nyquis_Filter_ff_0.set_ntaps(self.ntaps)
        self.b_Raised_cosine_ff_0_0.set_ntaps(self.ntaps)
        self.blocks_delay_0.set_dly(121+self.ntaps*8+self.Delay_rect)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(8, self.samp_rate, self.samp_rate/self.Sps, self.rolloff, self.ntaps))

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.set_h_rrc(wform.rrcos(self.Sps,self.ntaps,self.rolloff))
        self.b_Raised_cosine_ff_0_0.set_rolloff(self.rolloff)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(8, self.samp_rate, self.samp_rate/self.Sps, self.rolloff, self.ntaps))

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_h_rect(wform.rect(self.Sps))
        self.set_h_rrc(wform.rrcos(self.Sps,self.ntaps,self.rolloff))
        self.b_Eye_Diagram_simple_0.set_Sps(self.Sps)
        self.b_Nyquis_Filter_ff_0.set_Sps(self.Sps)
        self.b_Raised_cosine_ff_0_0.set_sps(self.Sps)
        self.interp_fir_filter_xxx_0_0_0.set_taps((self.Sps*[1.,] ))
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(8, self.samp_rate, self.samp_rate/self.Sps, self.rolloff, self.ntaps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_Eye_Diagram_simple_0.set_Samprate(self.samp_rate)
        self.b_Raised_cosine_ff_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0_0_0_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate(self.samp_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(8, self.samp_rate, self.samp_rate/self.Sps, self.rolloff, self.ntaps))

    def get_h_rrc(self):
        return self.h_rrc

    def set_h_rrc(self, h_rrc):
        self.h_rrc = h_rrc

    def get_h_rect(self):
        return self.h_rect

    def set_h_rect(self, h_rect):
        self.h_rect = h_rect

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.Rb)

    def get_NodB(self):
        return self.NodB

    def set_NodB(self, NodB):
        self.NodB = NodB

    def get_Delay_rect(self):
        return self.Delay_rect

    def set_Delay_rect(self, Delay_rect):
        self.Delay_rect = Delay_rect
        self.blocks_delay_0.set_dly(121+self.ntaps*8+self.Delay_rect)

    def get_Delay_RRC(self):
        return self.Delay_RRC

    def set_Delay_RRC(self, Delay_RRC):
        self.Delay_RRC = Delay_RRC
        self.blocks_delay_0_0_1.set_dly(self.Delay_RRC)

    def get_Delay_RC(self):
        return self.Delay_RC

    def set_Delay_RC(self, Delay_RC):
        self.Delay_RC = Delay_RC
        self.blocks_delay_0_0_2.set_dly(self.Delay_RC)

    def get_Delay_Nyquist(self):
        return self.Delay_Nyquist

    def set_Delay_Nyquist(self, Delay_Nyquist):
        self.Delay_Nyquist = Delay_Nyquist
        self.blocks_delay_0_0_0.set_dly(self.Delay_Nyquist)


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "", "--ntaps", dest="ntaps", type="intx", default=128,
        help="Set ntaps [default=%default]")
    parser.add_option(
        "", "--rolloff", dest="rolloff", type="eng_float", default=eng_notation.num_to_str(0.5),
        help="Set rolloff [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(ntaps=options.ntaps, rolloff=options.rolloff)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
