#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Direction of Arrival
# Author: DoHaiSon
# Generated: Tue May  5 09:38:18 2020
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
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import DoA_BladeRF
import doa
import sip
import soapy
import sys
import threading
import time
from gnuradio import qtgui


class DOA_DVB_T2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Direction of Arrival")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Direction of Arrival")
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

        self.settings = Qt.QSettings("GNU Radio", "DOA_DVB_T2")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.variance = variance = 20
        self.delay_0 = delay_0 = 0
        self.delay = delay = 0
        self.argmax = argmax = 0
        self.variable_qtgui_label_2 = variable_qtgui_label_2 = delay_0
        self.variable_qtgui_label_1_0 = variable_qtgui_label_1_0 = variance
        self.variable_qtgui_label_1 = variable_qtgui_label_1 = argmax
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = delay
        self.samp_rate = samp_rate = 160e3 * 2
        self.pi = pi = 3.14159265
        self.num_item = num_item = 1024
        self.choose = choose = False

        ##################################################
        # Blocks
        ##################################################
        self.delay_sample = blocks.probe_signal_i()
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Sync')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'DoA')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'Demod')
        self.top_layout.addWidget(self.tab)
        self.probe65 = blocks.probe_signal_f()
        self.my_block_0 = blocks.probe_signal_f()

        def _delay_0_probe():
            while True:
                val = self.delay_sample.level()
                try:
                    self.set_delay_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _delay_0_thread = threading.Thread(target=_delay_0_probe)
        _delay_0_thread.daemon = True
        _delay_0_thread.start()

        self._choose_options = (False, True, )
        self._choose_labels = ('Sync', 'DOA', )
        self._choose_group_box = Qt.QGroupBox('State: ')
        self._choose_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._choose_button_group = variable_chooser_button_group()
        self._choose_group_box.setLayout(self._choose_box)
        for i, label in enumerate(self._choose_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._choose_box.addWidget(radio_button)
        	self._choose_button_group.addButton(radio_button, i)
        self._choose_callback = lambda i: Qt.QMetaObject.invokeMethod(self._choose_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._choose_options.index(i)))
        self._choose_callback(self.choose)
        self._choose_button_group.buttonClicked[int].connect(
        	lambda i: self.set_choose(self._choose_options[i]))
        self.top_grid_layout.addWidget(self._choose_group_box, 0, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]
        self.blocks_probe_signal_x_0 = blocks.probe_signal_f()

        def _variance_probe():
            while True:
                val = self.probe65.level()
                try:
                    self.set_variance(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variance_thread = threading.Thread(target=_variance_probe)
        _variance_thread.daemon = True
        _variance_thread.start()

        self._variable_qtgui_label_2_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_2_formatter = None
        else:
          self._variable_qtgui_label_2_formatter = lambda x: str(x)

        self._variable_qtgui_label_2_tool_bar.addWidget(Qt.QLabel('Delay Sample: '+": "))
        self._variable_qtgui_label_2_label = Qt.QLabel(str(self._variable_qtgui_label_2_formatter(self.variable_qtgui_label_2)))
        self._variable_qtgui_label_2_tool_bar.addWidget(self._variable_qtgui_label_2_label)
        self.tab_layout_0.addWidget(self._variable_qtgui_label_2_tool_bar)
        self._variable_qtgui_label_1_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_1_0_formatter = None
        else:
          self._variable_qtgui_label_1_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_1_0_tool_bar.addWidget(Qt.QLabel('Angle Variance'+": "))
        self._variable_qtgui_label_1_0_label = Qt.QLabel(str(self._variable_qtgui_label_1_0_formatter(self.variable_qtgui_label_1_0)))
        self._variable_qtgui_label_1_0_tool_bar.addWidget(self._variable_qtgui_label_1_0_label)
        self.tab_grid_layout_0.addWidget(self._variable_qtgui_label_1_0_tool_bar, 4, 0, 1, 1)
        [self.tab_grid_layout_0.setRowStretch(r,1) for r in range(4,5)]
        [self.tab_grid_layout_0.setColumnStretch(c,1) for c in range(0,1)]
        self._variable_qtgui_label_1_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_1_formatter = None
        else:
          self._variable_qtgui_label_1_formatter = lambda x: str(x)

        self._variable_qtgui_label_1_tool_bar.addWidget(Qt.QLabel('DOA'+": "))
        self._variable_qtgui_label_1_label = Qt.QLabel(str(self._variable_qtgui_label_1_formatter(self.variable_qtgui_label_1)))
        self._variable_qtgui_label_1_tool_bar.addWidget(self._variable_qtgui_label_1_label)
        self.tab_layout_1.addWidget(self._variable_qtgui_label_1_tool_bar)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: eng_notation.num_to_str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Phase OFfset: '+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.tab_layout_0.addWidget(self._variable_qtgui_label_0_tool_bar)
        self.soapy_source_0_0 = \
         soapy.source(1, 'driver=bladerf, serial=ca4c', '', samp_rate , "fc32")



        self.soapy_source_0_0.set_frequency(0, 923e6 )
        self.soapy_source_0_0.set_gain(0, 0)
        self.soapy_source_0_0.set_gain_mode(0, True)
        self.soapy_source_0_0.set_bandwidth(0, 3e6)
        self.soapy_source_0_0.set_dc_offset_mode(0, True)

        self.soapy_source_0 = \
         soapy.source(1, 'driver=bladerf, serial=2a45', '', samp_rate , "fc32")



        self.soapy_source_0.set_frequency(0, 923e6 )
        self.soapy_source_0.set_gain(0, 0)
        self.soapy_source_0.set_gain_mode(0, True)
        self.soapy_source_0.set_bandwidth(0, 3e6)
        self.soapy_source_0.set_dc_offset_mode(0, True)

        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            num_item,
            0,
            1.0 / (int(num_item/181)),
            "DOA (do)",
            "Pho khong gian DOA (dB)",
            "Direction of Arrival",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(0, 20)
        self.qtgui_vector_sink_f_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0.enable_grid(True)
        self.qtgui_vector_sink_f_0.set_x_axis_units("do")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
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
        self.tab_layout_1.addWidget(self._qtgui_vector_sink_f_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"Tin hieu thu", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Bien do', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
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
        self.tab_layout_0.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
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

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
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
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 5e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 5e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.doa_variance_ff_0 = doa.variance_ff(100)
        self.doa_unwrap_ff_0_0 = doa.unwrap_ff(100, -3.14159265, 3.14159265)

        def _delay_probe():
            while True:
                val = self.my_block_0.level()
                try:
                    self.set_delay(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _delay_thread = threading.Thread(target=_delay_probe)
        _delay_thread.daemon = True
        _delay_thread.start()

        self.dc_blocker_xx_0_0 = filter.dc_blocker_cc(1024, True)
        self.dc_blocker_xx_0 = filter.dc_blocker_cc(1024, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_2_0 = blocks.stream_to_vector(gr.sizeof_float*1, 100)
        self.blocks_stream_to_vector_1_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 8192)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 8192)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 10)
        self.blocks_stream_to_vector_0_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, num_item)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 10)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, num_item)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, int(num_item / 181))
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff(((-choose  -1) , ))
        self.blocks_keep_one_in_n_1_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, 500)
        self.blocks_keep_one_in_n_1 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, 500)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(num_item)

        def _argmax_probe():
            while True:
                val = self.blocks_probe_signal_x_0.level()
                try:
                    self.set_argmax(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _argmax_thread = threading.Thread(target=_argmax_probe)
        _argmax_thread.daemon = True
        _argmax_thread.start()

        self.DoA_BladeRF_sample_offset_0 = DoA_BladeRF.sample_offset(8192, 5)
        self.DoA_BladeRF_multi_exp_0 = DoA_BladeRF.multi_exp(0.0)
        self.DoA_BladeRF_mess_sink_f_0 = DoA_BladeRF.mess_sink_f()
        self.DoA_BladeRF_PCA_0 = DoA_BladeRF.PCA(10)
        self.DoA_BladeRF_Hold_0 = DoA_BladeRF.Hold(choose)
        self.DoA_BladeRF_Delay_1 = DoA_BladeRF.Delay(gr.sizeof_gr_complex*1, (delay_0 > 0 ) * delay_0)
        self.DoA_BladeRF_Delay_0 = DoA_BladeRF.Delay(gr.sizeof_gr_complex*1, (delay_0<0)*-delay_0)
        self.DoA_BladeRF_DOApy_0 = DoA_BladeRF.DOApy(2, 1024, 30, True, 0.5)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.DoA_BladeRF_mess_sink_f_0, 'out'), (self.DoA_BladeRF_multi_exp_0, 'arg'))
        self.connect((self.DoA_BladeRF_DOApy_0, 0), (self.blocks_argmax_xx_0, 0))
        self.connect((self.DoA_BladeRF_DOApy_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.DoA_BladeRF_Delay_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.DoA_BladeRF_Delay_1, 0), (self.DoA_BladeRF_multi_exp_0, 0))
        self.connect((self.DoA_BladeRF_Hold_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.DoA_BladeRF_PCA_0, 0), (self.DoA_BladeRF_Hold_0, 0))
        self.connect((self.DoA_BladeRF_PCA_0, 0), (self.blocks_stream_to_vector_2_0, 0))
        self.connect((self.DoA_BladeRF_multi_exp_0, 0), (self.blocks_keep_one_in_n_1, 0))
        self.connect((self.DoA_BladeRF_multi_exp_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.DoA_BladeRF_multi_exp_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.DoA_BladeRF_sample_offset_0, 0), (self.delay_sample, 0))
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_null_sink_1, 0))
        self.connect((self.blocks_argmax_xx_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_keep_one_in_n_1, 0), (self.blocks_stream_to_vector_0_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_1_0, 0), (self.blocks_stream_to_vector_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.DoA_BladeRF_mess_sink_f_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.my_block_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_probe_signal_x_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.DoA_BladeRF_DOApy_0, 1))
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.DoA_BladeRF_PCA_0, 1))
        self.connect((self.blocks_stream_to_vector_0_0_1, 0), (self.DoA_BladeRF_DOApy_0, 0))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.DoA_BladeRF_PCA_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.DoA_BladeRF_sample_offset_0, 0))
        self.connect((self.blocks_stream_to_vector_1_0, 0), (self.DoA_BladeRF_sample_offset_0, 1))
        self.connect((self.blocks_stream_to_vector_2_0, 0), (self.doa_unwrap_ff_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_keep_one_in_n_1_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_0_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.dc_blocker_xx_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.doa_unwrap_ff_0_0, 0), (self.doa_variance_ff_0, 0))
        self.connect((self.doa_variance_ff_0, 0), (self.probe65, 0))
        self.connect((self.low_pass_filter_0, 0), (self.DoA_BladeRF_Delay_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.DoA_BladeRF_Delay_1, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_stream_to_vector_1_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.soapy_source_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.soapy_source_0_0, 0), (self.dc_blocker_xx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "DOA_DVB_T2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variance(self):
        return self.variance

    def set_variance(self, variance):
        self.variance = variance
        self.set_variable_qtgui_label_1_0(self._variable_qtgui_label_1_0_formatter(self.variance))

    def get_delay_0(self):
        return self.delay_0

    def set_delay_0(self, delay_0):
        self.delay_0 = delay_0
        self.set_variable_qtgui_label_2(self._variable_qtgui_label_2_formatter(self.delay_0))
        self.DoA_BladeRF_Delay_1.set_dly((self.delay_0 > 0 ) * self.delay_0)
        self.DoA_BladeRF_Delay_0.set_dly((self.delay_0<0)*-self.delay_0)

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.delay ))

    def get_argmax(self):
        return self.argmax

    def set_argmax(self, argmax):
        self.argmax = argmax
        self.set_variable_qtgui_label_1(self._variable_qtgui_label_1_formatter(self.argmax))

    def get_variable_qtgui_label_2(self):
        return self.variable_qtgui_label_2

    def set_variable_qtgui_label_2(self, variable_qtgui_label_2):
        self.variable_qtgui_label_2 = variable_qtgui_label_2
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_2_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_2))

    def get_variable_qtgui_label_1_0(self):
        return self.variable_qtgui_label_1_0

    def set_variable_qtgui_label_1_0(self, variable_qtgui_label_1_0):
        self.variable_qtgui_label_1_0 = variable_qtgui_label_1_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_1_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_1_0))

    def get_variable_qtgui_label_1(self):
        return self.variable_qtgui_label_1

    def set_variable_qtgui_label_1(self, variable_qtgui_label_1):
        self.variable_qtgui_label_1 = variable_qtgui_label_1
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_1_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_1))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 5e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 5e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_pi(self):
        return self.pi

    def set_pi(self, pi):
        self.pi = pi

    def get_num_item(self):
        return self.num_item

    def set_num_item(self, num_item):
        self.num_item = num_item
        self.qtgui_vector_sink_f_0.set_x_axis(0, 1.0 / (int(self.num_item/181)))
        self.blocks_short_to_float_0.set_scale(int(self.num_item / 181))

    def get_choose(self):
        return self.choose

    def set_choose(self, choose):
        self.choose = choose
        self._choose_callback(self.choose)
        self.blocks_multiply_const_vxx_0_0.set_k(((-self.choose  -1) , ))
        self.DoA_BladeRF_Hold_0.set_hold(self.choose)


def main(top_block_cls=DOA_DVB_T2, options=None):

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
