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


#ifndef INCLUDED_DOA_BLADERF_SELECTOR_H
#define INCLUDED_DOA_BLADERF_SELECTOR_H

#include <DoA_BladeRF/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace DoA_BladeRF {

    /*!
     * \brief <+description of block+>
     * \ingroup DoA_BladeRF
     *
     */
    class DOA_BLADERF_API selector : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<selector> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of DoA_BladeRF::selector.
       *
       * To avoid accidental use of raw pointers, DoA_BladeRF::selector's
       * constructor is in a private implementation
       * class. DoA_BladeRF::selector::make is the public interface for
       * creating new instances.
       */
      static sptr make(bool input_port);
      virtual void set_port(bool new_input_port) = 0;
      virtual bool get_port() const = 0;
    };

  } // namespace DoA_BladeRF
} // namespace gr

#endif /* INCLUDED_DOA_BLADERF_SELECTOR_H */

