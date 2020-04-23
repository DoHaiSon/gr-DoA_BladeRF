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

#ifndef INCLUDED_DOA_BLADERF_DELAY_IMPL_H
#define INCLUDED_DOA_BLADERF_DELAY_IMPL_H

#include <DoA_BladeRF/Delay.h>
#include <gnuradio/thread/thread.h>

namespace gr {
  namespace DoA_BladeRF {

    class Delay_impl : public Delay
    {
     private:
      void forecast(int noutput_items,
                    gr_vector_int &ninput_items_required);

      size_t d_itemsize;
      int d_delta;
      gr::thread::mutex d_mutex_delay;
      void handle_msg(pmt::pmt_t msg);

     public:
      Delay_impl(size_t itemsize, int delay);
      ~Delay_impl();

      int dly() const { return history()-1; }
      void set_dly(int d);

      // Where all the action really happens


      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace DoA_BladeRF
} // namespace gr

#endif /* INCLUDED_DOA_BLADERF_DELAY_IMPL_H */

