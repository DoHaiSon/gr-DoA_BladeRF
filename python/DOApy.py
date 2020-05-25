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
from gnuradio import gr
import math
from numpy import linalg as LA
import scipy as sp

class DOApy(gr.sync_block):
    """
    docstring for block DOApy
    """
    def __init__(self, num_in, veclen, gain, algorithm, k):
        gr.sync_block.__init__(self,
            name="DOApy",
            in_sig=[(np.complex64, veclen)] * num_in,
            out_sig=[(np.float32, veclen)])
	self.num_in = num_in
	self.veclen = veclen
	self.gain = gain
	self.algorithm = algorithm
	self.k = k


    def work(self, input_items, output_items):
	Nb = self.veclen
	in0 = input_items[0][0]
	for i in range (1, self.num_in):
		in0 = np.vstack((in0, input_items[i][0]))
	if self.algorithm == True:
		P = DOA_MuSIC(in0, Nb, self.num_in, self.gain, self.k)
	if self.algorithm == False:
		P = DOA_CAPON(in0, Nb, self.num_in, self.gain, self.k)
	if self.algorithm == None:
		P = DOA_Bartlett(in0, Nb, self.num_in, self.gain, self.k)
	theta = np.arange(0, 181, 1)

	new_size = self.veclen - 1
	new_arr = np.zeros((1, int(new_size + 1)), dtype = float)
	for i in range (len(P)):
	  for j in range (int(new_size / len(P))):
		if(i != len(P) - 1):
	      		new_arr[0][(i) * int((new_size / len(P))) + j] = P[i] + ((P[i+1] - P[i]) / (new_size / len(P))) * j
	    	else:
	      		new_arr[0][(i) * int((new_size / len(P))) + j] = P[i] + ((P[i] - P[i - 1]) / (new_size / len(P))) * j
			last = (i) * int((new_size / len(P))) + j
	new_arr[0][last + 1] = P[len(P) - 1]
	new_arr[0][last + 2: self.veclen] = np.min(P)

	out = np.zeros((1, 1, self.veclen), dtype = float)	
	out[0] = new_arr
	output_items[0][:] = out[:]

	#for i in range (self.num_in):
	#	self.consume_each(len(input_items[i]))

        return len(output_items[0])


def DOA_MuSIC(U, Nb, M, gain, k):

    # Covar matrix:
    Ruu = np.dot(U, U.conj().T) / Nb

    # Xac dinh gia tri rieng va vector rieng cua covarian cua tin hieu loi vao
    eigValue, eigVector = LA.eigh(Ruu,UPLO= 'U')

    eigValue = sp.diag(eigValue)
    #print(eigValue)

    signals = 1

    # Xac dinh so nguon tin hieu den
    D = signals

    # Khong gian con nhieu
    eigVectorNoise = eigVector[:, 0: M -signals].copy()
    #print(eigVectorNoise)

    # Pho khong gian cua tin hieu
    A0_tmp = np.zeros((D, M), dtype = complex)
    P = np.zeros((181))
    for theta in range (0, 181):
        for reci in range (0, M):
            A0_tmp[D-1][reci] = pow(10, gain/10) * pow(math.e, complex(0, 2 * math.pi * k * (reci -0.5) * math.cos((theta)*math.pi/180)))
        A0 = A0_tmp.transpose()

        tmp = (np.dot(A0.conj().T, A0)) / (np.dot(np.dot(A0.conj().T,eigVectorNoise), np.dot(eigVectorNoise.conj().T, A0)))
        P[theta] = math.log(np.float(tmp.real))

    return P

def DOA_CAPON(U, Nb, M, gain, k):

    # Covar matrix
    Ruu = np.dot(U, U.conj().T) / Nb

    signals = 1

    D = signals

    # Pho khong gian cua tin hieu
    A0_tmp = np.zeros((D, M), dtype = complex)
    P = np.zeros((181))
    for theta in range (0, 181):
	for reci in range (0, M):
		A0_tmp[D-1][reci] = pow(10, gain/10) * pow(math.e, complex(0, 2 * math.pi * k * reci * math.cos(theta*math.pi/180)))
    	A0 = A0_tmp.transpose()
	try:
    		tmp = np.dot(A0.conj().T, A0) / np.dot(np.dot(A0.conj().T, LA.inv(Ruu)), A0)
	except np.linalg.LinAlgError as e:
		if 'Singular matrix' in str(e):
			return P
		else:
			raise
	if ( np.float(tmp.real) > 0.0 ):
		P[theta] = np.log10(np.float(tmp.real))
	else:
		P[theta] = 0.0
    return P

def DOA_Bartlett(U, Nb, M, gain, k):

    # Covar matrix
    Ruu = np.dot(U, U.conj().T) / Nb

    signals = 1

    D = signals

    # Pho khong gian cua tin hieu
    A0_tmp = np.zeros((D, M), dtype = complex)
    P = np.zeros((181))
    for theta in range (0, 181):
	for reci in range (0, M):
		A0_tmp[D-1][reci] = pow(10, gain/10) * pow(math.e, complex(0, 2 * math.pi * k * reci * math.cos(theta*math.pi/180)))
    	A0 = A0_tmp.transpose()
	tmp = np.dot(np.dot(A0.conj().T, Ruu), A0) / np.dot(A0.conj().T, A0)
	P[theta] = np.log10(np.float(np.real(tmp)))
    return P
