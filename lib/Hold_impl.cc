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
#include "Hold_impl.h"
#include <algorithm>

namespace gr {
  namespace DoA_BladeRF {

    Hold::sptr
    Hold::make(bool hold)
    {
      return gnuradio::get_initial_sptr
        (new Hold_impl(hold));
    }

    /*
     * The private constructor
     */
    Hold_impl::Hold_impl(bool hold)
      : gr::sync_block("Hold",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)))
    {
        set_hold(hold);
        d_value = 0;
}

    /*
     * Our virtual destructor.
     */
    Hold_impl::~Hold_impl()
    {
    }

    void Hold_impl::set_hold(bool new_hold) {
        if (new_hold != d_hold) {
            d_hold = new_hold;
            //printf("\nnew hold: %d\n",d_hold);
        }
    }
    int
    Hold_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];

      // Do <+signal processing+>

      if(!d_hold){
          //pass every sample through, save the last one into d_value
          memcpy(out,in,sizeof(float)*noutput_items);
          d_value = in[noutput_items-1];
      }
      else{
          //hold = true, so just return the last given value
          std::fill(out,out+noutput_items,d_value);
      }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace DoA_BladeRF */
} /* namespace gr */

