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
#include "Delay_impl.h"
#include <string.h>

namespace gr {
  namespace DoA_BladeRF {

    Delay::sptr
    Delay::make(size_t itemsize, int delay)
    {
      return gnuradio::get_initial_sptr
        (new Delay_impl(itemsize, delay));
    }

    /*
     * The private constructor
     */
    Delay_impl::Delay_impl(size_t itemsize, int delay)
      : gr::block("Delay",
                 io_signature::make(1, -1, itemsize),
                 io_signature::make(1, -1, itemsize)),
        d_itemsize(itemsize)
    {
      if(delay < 0) {
        throw std::runtime_error("delay: Cannot initialize block with a delay < 0.");
      }
      set_dly(delay);
      d_delta = 0;

      message_port_register_in(pmt::mp("msg"));
      set_msg_handler(pmt::mp("msg"), boost::bind(&Delay_impl::handle_msg, this, _1));
}

    /*
     * Our virtual destructor.
     */
    Delay_impl::~Delay_impl()
    {
    }

    void
    Delay_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      unsigned ninputs = ninput_items_required.size();
      for(unsigned i = 0; i < ninputs; i++)
        ninput_items_required[i] = noutput_items;
    }

void
    Delay_impl::set_dly(int d)
    {
      // only set a new delta if there is a change in the delay; this
      // protects from quickly-repeated calls to this function that
      // would end with d_delta=0.
      if(d != dly()) {
        gr::thread::scoped_lock l(d_mutex_delay);
        int old = dly();
        set_history(d+1);
        declare_sample_delay(history()-1);
        d_delta += dly() - old;
        printf("delay set to %d\n", d);
      }
    }

    void
    Delay_impl::handle_msg(pmt::pmt_t msg) {
        if (pmt::is_number(msg)) {
            int value = pmt::to_long(msg);
            set_dly(value);
        } else {
            GR_LOG_WARN(d_logger, boost::format("Delay message must be a number"));
        }
    }

    int
    Delay_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      gr::thread::scoped_lock l(d_mutex_delay);
      assert(input_items.size() == output_items.size());

      const char *iptr;
      char *optr;
      int cons, ret;

      // No change in delay; just memcpy ins to outs
      if(d_delta == 0) {
        for(size_t i = 0; i < input_items.size(); i++) {
          iptr = (const char *)input_items[i];
          optr = (char *)output_items[i];
          std::memcpy(optr, iptr, noutput_items*d_itemsize);
        }
        cons = noutput_items;
        ret = noutput_items;
      }

      // Skip over d_delta items on the input
      else if(d_delta < 0) {
        int n_to_copy, n_adj;
        int delta = -d_delta;
        n_to_copy = std::max(0, noutput_items-delta);
        n_adj = std::min(delta, noutput_items);
        for(size_t i = 0; i < input_items.size(); i++) {
          iptr = (const char *) input_items[i];
          optr = (char *) output_items[i];
          std::memcpy(optr, iptr+delta*d_itemsize, n_to_copy*d_itemsize);
        }
        cons = noutput_items;
        ret = n_to_copy;
        delta -= n_adj;
        d_delta = -delta;
      }

      //produce but not consume (inserts zeros)
      else {  // d_delta > 0
        int n_from_input, n_padding;
        n_from_input = std::max(0, noutput_items-d_delta);
        n_padding = std::min(d_delta, noutput_items);
        for(size_t i = 0; i < input_items.size(); i++) {
          iptr = (const char *) input_items[i];
          optr = (char *) output_items[i];
          std::memset(optr, 0, n_padding*d_itemsize);
          std::memcpy(optr, iptr, n_from_input*d_itemsize);
        }
        cons = n_from_input;
        ret = noutput_items;
        d_delta -= n_padding;
      }

      consume_each(cons);
      return ret;
    }

  } /* namespace DoA_BladeRF */
} /* namespace gr */

