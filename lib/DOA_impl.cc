/* -*- c++ -*- */
/* 
 * Copyright 2020 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "DOA_impl.h"
#include <algorithm>
#include <numeric>
#include <cmath>

namespace gr {
  namespace DoA_BladeRF {

    DOA::sptr
    DOA::make(int vector_size, float spacing, int num_input, int gain)
    {
      return gnuradio::get_initial_sptr
        (new DOA_impl(vector_size, spacing, num_input, gain));
    }

    /*
     * The private constructor
     */
    DOA_impl::DOA_impl(int vector_size, float spacing, int num_input, int gain)
      : gr::sync_block("DOA",
              gr::io_signature::make(num_input, num_input, sizeof(gr_complex) * vector_size),
              gr::io_signature::make(1, 1, sizeof(float) * vector_size)),
        d_vector_size(vector_size),
	d_spacing(spacing)
    {}

    /*
     * Our virtual destructor.
     */
    DOA_impl::~DOA_impl()
    {
    }

    void DOA_impl::direction(const gr_complex* in0, const gr_complex* in1, float *P) {
        // put in0 and in1 into vectors x1 and x2
        std::vector<gr_complex> x1(in0, in0+d_vector_size);
        std::vector<gr_complex> x2(in1, in1+d_vector_size);

        // find average value of each one
        gr_complex x1_avg = accumulate(x1.begin(), x1.end(), gr_complex(0,0)) / gr_complex(d_vector_size,0);
        gr_complex x2_avg = accumulate(x2.begin(), x2.end(), gr_complex(0,0)) / gr_complex(d_vector_size,0);
        // subtract the average value from each element
        for (int i=0; i<d_vector_size; ++i) { x1[i] -= x1_avg; }
        for (int i=0; i<d_vector_size; ++i) { x2[i] -= x2_avg; }
        // find conjugates of x1 and x2
        std::vector<gr_complex> x1_c, x2_c;
        x1_c.reserve(d_vector_size);
        x2_c.reserve(d_vector_size);
        for (int i=0; i<d_vector_size; ++i) { x1_c.push_back(conj(x1[i])); }
        for (int i=0; i<d_vector_size; ++i) { x2_c.push_back(conj(x2[i])); }
        // multiply vectors together
        std::vector<gr_complex> c11, c12, c22;
        c11.reserve(d_vector_size);
        c12.reserve(d_vector_size);
        c22.reserve(d_vector_size);
        transform(x1.begin(), x1.end(), x1_c.begin(), back_inserter(c11), std::multiplies<gr_complex>());
        transform(x1.begin(), x1.end(), x2_c.begin(), back_inserter(c12), std::multiplies<gr_complex>());
        transform(x2.begin(), x2.end(), x2_c.begin(), back_inserter(c22), std::multiplies<gr_complex>());
        // make covariance matrix
        std::vector<std::vector<gr_complex> > covar(2, std::vector<gr_complex>(2, 0));
        covar[0][0] = accumulate(c11.begin(), c11.end(), gr_complex(0,0)) / gr_complex(d_vector_size,0);
        covar[0][1] = accumulate(c12.begin(), c12.end(), gr_complex(0,0)) / gr_complex(d_vector_size,0);
        covar[1][1] = accumulate(c22.begin(), c22.end(), gr_complex(0,0)) / gr_complex(d_vector_size,0);
        covar[1][0] = conj(covar[0][1]);

        // find eigenvalues
        gr_complex lambda0 = (covar[0][0]+covar[1][1]+sqrt(pow((covar[0][0]+covar[1][1]),2)-gr_complex(4,0)*(covar[0][0]*covar[1][1]-covar[0][1]*covar[1][0])))/gr_complex(2,0);
        gr_complex lambda1 = (covar[0][0]+covar[1][1]-sqrt(pow((covar[0][0]+covar[1][1]),2)-gr_complex(4,0)*(covar[0][0]*covar[1][1]-covar[0][1]*covar[1][0])))/gr_complex(2,0);
        //gr_complex max_lambda = (abs(lambda0) > abs(lambda1)) ? abs(lambda0) : abs(lambda1);

	gr_complex min_lambda = (abs(lambda0) < abs(lambda1)) ? abs(lambda0) : abs(lambda1);
	
	//find eigVectorNoise
	std::vector<std::vector<gr_complex> > eigVectorNoise(2, std::vector<gr_complex>(1, 0));
	eigVectorNoise[0][0] = -covar[0][1];
	eigVectorNoise[1][0] = covar[0][0] - min_lambda;
	if ( eigVectorNoise[0][0] == gr_complex(0, 0) && eigVectorNoise[1][0] == gr_complex(0, 0) )	{
		eigVectorNoise[0][0] = covar[1][1] - min_lambda;
		eigVectorNoise[1][0] = -covar[1][0];
	}
	
	//MUSIC P
	std::vector<std::vector<gr_complex> > A0(2, std::vector<gr_complex>(1, 0));
	std::vector<std::vector<gr_complex> > A0_conj_T(1, std::vector<gr_complex>(2, 0));
	std::vector<std::vector<gr_complex> > eigVectorNoise_conj_T(1, std::vector<gr_complex>(2, 0));
	eigVectorNoise_conj_T[0][0] = gr_complex(eigVectorNoise[0][0].real(), -eigVectorNoise[0][0].imag());
	eigVectorNoise_conj_T[0][1] = gr_complex(eigVectorNoise[1][0].real(), -eigVectorNoise[1][0].imag());
	gr_complex tmp1(0, 0);
	//float P[181];

	for(int theta = 0; theta <= 180; theta++){
		A0[0][0] = std::exp(0);
		A0[1][0] = std::exp(gr_complex(0, 1)  * gr_complex(2 * M_PI * d_spacing * std::cos(theta * M_PI / 180), 0));
		A0_conj_T[0][0] = gr_complex(A0[0][0].real(), - A0[0][0].imag());
		A0_conj_T[0][1] = gr_complex(A0[1][0].real(), - A0[1][0].imag());
		tmp1 = (A0_conj_T[0][0] * A0[0][0] + A0_conj_T[0][1] * A0[1][0]) / ((A0_conj_T[0][0] * eigVectorNoise[0][0] + A0_conj_T[0][1]
			* eigVectorNoise[1][0]) * (eigVectorNoise_conj_T[0][0] * A0[0][0] + eigVectorNoise_conj_T[0][1] * A0[1][0]));
		P[theta] = log10(tmp1.real());
	}
    }

void DOA_impl::scale(float *out,  float *in, int size){
	int new_size = size - 1;
	int ratio = (new_size + 1) / 181;
	for (int i = 0; i < 181; i ++) {
		for (int j = 0; j < ratio; j ++) {
			if( i != 180)
				out[i * ratio + j] = in[i] + ((in[i+1] - in[i]) / ratio) * j;
			else
				out[i * ratio + j] = in[i] + ((in[i] - in[i-1]) / ratio) * j;
		}
	}
	out[new_size] = in[180];
    }

    int
    DOA_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const gr_complex *in0 = (const gr_complex *) input_items[0];
      const gr_complex *in1 = (const gr_complex *) input_items[1];
      float *out = (float *) output_items[0]; 
      int size = int(d_vector_size / 181) * 181 ;
      float P[181], new_arr[size];

      // Do <+signal processing+>
      for (int i=0; i<noutput_items; ++i) {
          direction(in0, in1, P);
	  scale(new_arr, P, size);
	  for(int j =0; j<size; j++)
	  	out[j] = new_arr[j];
	  out += d_vector_size;
          in0 += d_vector_size;
          in1 += d_vector_size;
      }
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace DoA_BladeRF */
} /* namespace gr */

