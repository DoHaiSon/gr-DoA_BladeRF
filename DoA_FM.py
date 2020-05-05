#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Direction of Arrival
# Author: DoHaiSon
# Generated: Mon May  4 13:50:06 2020
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
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import DoA_BladeRF
import doa
import sip
import sys
import threading
import time
from gnuradio import qtgui


class DoA_FM(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "DoA_FM")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.variance = variance = 20
        self.samp_rate = samp_rate = 360e3
        self.pi = pi = 3.14159265
        self.delay_0 = delay_0 = 0
        self.delay = delay = 0
        self.argmax = argmax = 0
        self.vol = vol = 0.2
        self.variable_qtgui_label_2 = variable_qtgui_label_2 = delay_0
        self.variable_qtgui_label_1_0 = variable_qtgui_label_1_0 = variance
        self.variable_qtgui_label_1 = variable_qtgui_label_1 = argmax
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = delay * 180 / pi

        self.taps_up = taps_up = firdes.low_pass(1.0, samp_rate, 7500, 500, firdes.WIN_HAMMING, 6.76)

        self.num_item = num_item = 1024
        self.choose = choose = False
        self.angle = angle = 95.0

        ##################################################
        # Blocks
        ##################################################
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
        self.my_block_0 = blocks.probe_signal_f()
        self.delay_sample = blocks.probe_signal_i()
        self._vol_range = Range(0, 1, 0.05, 0.2, 200)
        self._vol_win = RangeWidget(self._vol_range, self.set_vol, 'Volume', "counter_slider", float)
        self.tab_layout_2.addWidget(self._vol_win)
        self.probe65 = blocks.probe_signal_f()

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
        self._angle_range = Range(0.0, 180.0, 1.0, 95.0, 181)
        self._angle_win = RangeWidget(self._angle_range, self.set_angle, 'Goc Den:', "counter_slider", float)
        self.tab_layout_1.addWidget(self._angle_win)

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
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=2,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=15,
                decimation=2,
                taps=(taps_up),
                fractional_bw=None,
        )
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            num_item,
            0,
            1.0 / (int(num_item/181)),
            "x-Axis",
            "y-Axis",
            "Direction of Arrival",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(0, 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
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
        	"Pho tin hieu thu", #name
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
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate / 3, #bw
        	"Pho tin hieu giai dieu che", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
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
        self.tab_layout_2.addWidget(self._qtgui_freq_sink_x_0_win)
        self.doa_variance_ff_0 = doa.variance_ff(100)
        self.doa_unwrap_ff_0_0 = doa.unwrap_ff(100, -3.14159265, 3.14159265)
        self.channels_fading_model_0_1 = channels.fading_model( 8, 10.0/samp_rate, False, 4.0, 1000 )
        self.channels_fading_model_0_0_0 = channels.fading_model( 8, 10.0/samp_rate, False, 4.0, 1000 )
        self.channels_channel_model_0_1 = channels.channel_model(
        	noise_voltage=0.01,
        	frequency_offset=0.01,
        	epsilon=1.0,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=1000,
        	block_tags=False
        )
        self.channels_channel_model_0_0_0 = channels.channel_model(
        	noise_voltage=0.01,
        	frequency_offset=0.01,
        	epsilon=1.0,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=1000,
        	block_tags=False
        )
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/media/haison98/Windows/Users/dohai/Desktop/My Thesis/01-Dancing-On-My-Own.wav', True)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, 753982.2369, 1)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_2_0 = blocks.stream_to_vector(gr.sizeof_float*1, 100)
        self.blocks_stream_to_vector_1_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 4096)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 4096)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 10)
        self.blocks_stream_to_vector_0_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, num_item)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 10)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, num_item)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, int(num_item / 181))
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_3_1 = blocks.multiply_const_vcc((choose, ))
        self.blocks_multiply_const_vxx_3_0_0 = blocks.multiply_const_vcc((choose, ))
        self.blocks_multiply_const_vxx_2_1 = blocks.multiply_const_vcc((1.0, ))
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_vcc((not choose, ))
        self.blocks_multiply_const_vxx_1_0_0 = blocks.multiply_const_vcc((not choose, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((vol, ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vff((0.5, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((-choose  -1, ))
        self.blocks_keep_one_in_n_1_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, 500)
        self.blocks_keep_one_in_n_1 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, 500)
        self.blocks_integrate_xx_0 = blocks.integrate_ff(1, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1000)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(num_item)
        self.blocks_add_xx_0_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0_0_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((1, ))
        self.band_pass_filter_0 = filter.fir_filter_ccf(3, firdes.band_pass(
        	1, samp_rate, 100e3, 140e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(48000, '', False)

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

        self.analog_sig_source_x_0_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 91e6, 1, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 91e6, 1, 0)
        self.analog_noise_source_x_0_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)
        self.analog_fm_demod_cf_0 = analog.fm_demod_cf(
        	channel_rate=samp_rate / 3,
        	audio_decim=1,
        	deviation=10e3,
        	audio_pass=10e3,
        	audio_stop=11e3,
        	gain=1.0,
        	tau=0,
        )
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, angle)
        self.DoA_BladeRF_vector_steering_0 = DoA_BladeRF.vector_steering(90.0)
        self.DoA_BladeRF_sample_offset_0 = DoA_BladeRF.sample_offset(4096, 5)
        self.DoA_BladeRF_multi_exp_1 = DoA_BladeRF.multi_exp(0.0)
        self.DoA_BladeRF_multi_exp_0 = DoA_BladeRF.multi_exp(45*pi/180)
        self.DoA_BladeRF_mess_sink_f_1 = DoA_BladeRF.mess_sink_f()
        self.DoA_BladeRF_mess_sink_f_0 = DoA_BladeRF.mess_sink_f()
        self.DoA_BladeRF_PCA_0 = DoA_BladeRF.PCA(10)
        self.DoA_BladeRF_Hold_0 = DoA_BladeRF.Hold(choose)
        self.DoA_BladeRF_Delay_1 = DoA_BladeRF.Delay(gr.sizeof_gr_complex*1, (delay_0 > 0 ) * delay_0)
        self.DoA_BladeRF_Delay_0 = DoA_BladeRF.Delay(gr.sizeof_gr_complex*1, (delay_0<0)*-delay_0)
        self.DoA_BladeRF_DOApy_0 = DoA_BladeRF.DOApy(2, 1024, 30, None, 0.5)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.DoA_BladeRF_mess_sink_f_0, 'out'), (self.DoA_BladeRF_vector_steering_0, 'arg'))
        self.msg_connect((self.DoA_BladeRF_mess_sink_f_1, 'out'), (self.DoA_BladeRF_multi_exp_1, 'arg'))
        self.connect((self.DoA_BladeRF_DOApy_0, 0), (self.blocks_argmax_xx_0, 0))
        self.connect((self.DoA_BladeRF_DOApy_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.DoA_BladeRF_Delay_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.DoA_BladeRF_Delay_1, 0), (self.DoA_BladeRF_multi_exp_1, 0))
        self.connect((self.DoA_BladeRF_Hold_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.DoA_BladeRF_PCA_0, 0), (self.DoA_BladeRF_Hold_0, 0))
        self.connect((self.DoA_BladeRF_PCA_0, 0), (self.blocks_stream_to_vector_2_0, 0))
        self.connect((self.DoA_BladeRF_multi_exp_0, 0), (self.DoA_BladeRF_Delay_0, 0))
        self.connect((self.DoA_BladeRF_multi_exp_0, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.DoA_BladeRF_multi_exp_1, 0), (self.blocks_keep_one_in_n_1, 0))
        self.connect((self.DoA_BladeRF_multi_exp_1, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.DoA_BladeRF_multi_exp_1, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.DoA_BladeRF_sample_offset_0, 0), (self.delay_sample, 0))
        self.connect((self.DoA_BladeRF_vector_steering_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.DoA_BladeRF_mess_sink_f_0, 0))
        self.connect((self.analog_fm_demod_cf_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.analog_fm_demod_cf_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_multiply_const_vxx_1_0_0, 0))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_multiply_const_vxx_1_1, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.band_pass_filter_0, 0), (self.analog_fm_demod_cf_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_integrate_xx_0, 0))
        self.connect((self.blocks_add_xx_0_0_0, 0), (self.DoA_BladeRF_multi_exp_0, 0))
        self.connect((self.blocks_add_xx_0_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_null_sink_1, 0))
        self.connect((self.blocks_argmax_xx_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.DoA_BladeRF_Delay_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_1_0, 0))
        self.connect((self.blocks_integrate_xx_0, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.blocks_keep_one_in_n_1, 0), (self.blocks_stream_to_vector_0_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_1_0, 0), (self.blocks_stream_to_vector_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.DoA_BladeRF_mess_sink_f_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.my_block_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_0, 0), (self.blocks_add_xx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.blocks_add_xx_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_2_1, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_3_0_0, 0), (self.blocks_add_xx_0_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_3_1, 0), (self.blocks_add_xx_0_1, 1))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.channels_channel_model_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.channels_channel_model_0_1, 0))
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
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.DoA_BladeRF_vector_steering_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_multiply_const_vxx_2_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.channels_channel_model_0_0_0, 0), (self.channels_fading_model_0_0_0, 0))
        self.connect((self.channels_channel_model_0_1, 0), (self.channels_fading_model_0_1, 0))
        self.connect((self.channels_fading_model_0_0_0, 0), (self.blocks_multiply_const_vxx_3_1, 0))
        self.connect((self.channels_fading_model_0_1, 0), (self.blocks_multiply_const_vxx_3_0_0, 0))
        self.connect((self.doa_unwrap_ff_0_0, 0), (self.doa_variance_ff_0, 0))
        self.connect((self.doa_variance_ff_0, 0), (self.probe65, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "DoA_FM")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variance(self):
        return self.variance

    def set_variance(self, variance):
        self.variance = variance
        self.set_variable_qtgui_label_1_0(self._variable_qtgui_label_1_0_formatter(self.variance))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate / 3)
        self.channels_fading_model_0_1.set_fDTs(10.0/self.samp_rate)
        self.channels_fading_model_0_0_0.set_fDTs(10.0/self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 100e3, 140e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)

    def get_pi(self):
        return self.pi

    def set_pi(self, pi):
        self.pi = pi
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.delay * 180 / self.pi))
        self.DoA_BladeRF_multi_exp_0.set_arg(45*self.pi/180)

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
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.delay * 180 / self.pi))

    def get_argmax(self):
        return self.argmax

    def set_argmax(self, argmax):
        self.argmax = argmax
        self.set_variable_qtgui_label_1(self._variable_qtgui_label_1_formatter(self.argmax))

    def get_vol(self):
        return self.vol

    def set_vol(self, vol):
        self.vol = vol
        self.blocks_multiply_const_vxx_1.set_k((self.vol, ))

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

    def get_taps_up(self):
        return self.taps_up

    def set_taps_up(self, taps_up):
        self.taps_up = taps_up
        self.rational_resampler_xxx_0.set_taps((self.taps_up))

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
        self.blocks_multiply_const_vxx_3_1.set_k((self.choose, ))
        self.blocks_multiply_const_vxx_3_0_0.set_k((self.choose, ))
        self.blocks_multiply_const_vxx_1_1.set_k((not self.choose, ))
        self.blocks_multiply_const_vxx_1_0_0.set_k((not self.choose, ))
        self.blocks_multiply_const_vxx_0_0.set_k((-self.choose  -1, ))
        self.DoA_BladeRF_Hold_0.set_hold(self.choose)

    def get_angle(self):
        return self.angle

    def set_angle(self, angle):
        self.angle = angle
        self.analog_const_source_x_0_0.set_offset(self.angle)


def main(top_block_cls=DoA_FM, options=None):

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
