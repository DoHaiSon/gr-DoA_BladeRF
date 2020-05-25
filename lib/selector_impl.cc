/* -*- c++ -*- */
/* MIT License
 * 
 * Copyright (c) 2020 Do Hai Son
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "selector_impl.h"

namespace gr {
  namespace DoA_BladeRF {

    selector::sptr
    selector::make(bool input_port)
    {
      return gnuradio::get_initial_sptr
        (new selector_impl(input_port));
    }

    /*
     * The private constructor
     */
    selector_impl::selector_impl(bool input_port)
      : gr::sync_block("selector",
              gr::io_signature::make(2, 2, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)))
    {

	set_port(input_port);
	//d_input_port = 0;

}

    /*
     * Our virtual destructor.
     */
    selector_impl::~selector_impl()
    {
    }

    void selector_impl::set_port(bool new_input_port) {
        if (d_input_port != new_input_port) {
            d_input_port = new_input_port;
        }
    }

    int
    selector_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in0 = (const float *) input_items[0];
      const float *in1 = (const float *) input_items[1];
      float *out = (float *) output_items[0];
      // Do <+signal processing+>
      
      if (!d_input_port) {
	memcpy(out, in0, sizeof(float) * noutput_items);

      }
      else {
	memcpy(out, in1, sizeof(float) * noutput_items);
      }
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace DoA_BladeRF */
} /* namespace gr */

