#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2020 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy as np
import scipy as sp
import scipy.io
from gnuradio import gr

class matlab_file(gr.sync_block):
    """
    docstring for block matlab_file
    """
    def __init__(self, link, num_in):
        gr.sync_block.__init__(self,
            name="matlab_file",
            in_sig=None,
            out_sig=[np.complex64] * num_in)
	self.link = link
	self.num_in = num_in


    def work(self, input_items, output_items):
	mat = scipy.io.loadmat(self.link)
	U = mat['U']
	out = np.zeros((self.num_in, len(output_items[0])), dtype=np.complex)
	for i in range (self.num_in):
		for j in range (len(output_items[0])):
			out[i][j] = U[i][j]
	for i in range (self.num_in):
		output_items[i][:] = out[i][:]

        return len(output_items[0])

