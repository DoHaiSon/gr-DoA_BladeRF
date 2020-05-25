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


#ifndef INCLUDED_DOA_BLADERF_DOA_H
#define INCLUDED_DOA_BLADERF_DOA_H

#include <DoA_BladeRF/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace DoA_BladeRF {

    /*!
     * \brief <+description of block+>
     * \ingroup DoA_BladeRF
     *
     */
    class DOA_BLADERF_API DOA : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<DOA> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of DoA_BladeRF::DOA.
       *
       * To avoid accidental use of raw pointers, DoA_BladeRF::DOA's
       * constructor is in a private implementation
       * class. DoA_BladeRF::DOA::make is the public interface for
       * creating new instances.
       */
      static sptr make(int vector_size, float spacing, int num_input, int gain);
    };

  } // namespace DoA_BladeRF
} // namespace gr

#endif /* INCLUDED_DOA_BLADERF_DOA_H */

