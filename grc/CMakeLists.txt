# Copyright 2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

install(FILES
    DoA_BladeRF_DOApy.xml
    DoA_BladeRF_matlab_file.xml
    DoA_BladeRF_mess_sink_f.xml
    DoA_BladeRF_multi_exp.xml
    DoA_BladeRF_PCA.xml
    DoA_BladeRF_Hold.xml
    DoA_BladeRF_vector_steering.xml
    DoA_BladeRF_DOA.xml
    DoA_BladeRF_sample_offset.xml
    DoA_BladeRF_Delay.xml DESTINATION share/gnuradio/grc/blocks
)
