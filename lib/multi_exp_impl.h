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

#ifndef INCLUDED_DOA_BLADERF_MULTI_EXP_IMPL_H
#define INCLUDED_DOA_BLADERF_MULTI_EXP_IMPL_H

#include <DoA_BladeRF/multi_exp.h>

namespace gr {
  namespace DoA_BladeRF {

    class multi_exp_impl : public multi_exp
    {
     private:
      // Nothing to declare in this block.
      float d_arg;
      void handle_arg(pmt::pmt_t arg);

     public:
      multi_exp_impl(float arg);
      ~multi_exp_impl();

      void set_arg(float new_arg);

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace DoA_BladeRF
} // namespace gr

#endif /* INCLUDED_DOA_BLADERF_MULTI_EXP_IMPL_H */

