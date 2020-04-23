/* -*- c++ -*- */

#define DOA_BLADERF_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "DoA_BladeRF_swig_doc.i"

%{
#include "DoA_BladeRF/mess_sink_f.h"
#include "DoA_BladeRF/multi_exp.h"
#include "DoA_BladeRF/PCA.h"
#include "DoA_BladeRF/Hold.h"
#include "DoA_BladeRF/vector_steering.h"
#include "DoA_BladeRF/DOA.h"
#include "DoA_BladeRF/sample_offset.h"
#include "DoA_BladeRF/Delay.h"
%}


%include "DoA_BladeRF/mess_sink_f.h"
GR_SWIG_BLOCK_MAGIC2(DoA_BladeRF, mess_sink_f);
%include "DoA_BladeRF/multi_exp.h"
GR_SWIG_BLOCK_MAGIC2(DoA_BladeRF, multi_exp);
%include "DoA_BladeRF/PCA.h"
GR_SWIG_BLOCK_MAGIC2(DoA_BladeRF, PCA);
%include "DoA_BladeRF/Hold.h"
GR_SWIG_BLOCK_MAGIC2(DoA_BladeRF, Hold);
%include "DoA_BladeRF/vector_steering.h"
GR_SWIG_BLOCK_MAGIC2(DoA_BladeRF, vector_steering);
%include "DoA_BladeRF/DOA.h"
GR_SWIG_BLOCK_MAGIC2(DoA_BladeRF, DOA);
%include "DoA_BladeRF/sample_offset.h"
GR_SWIG_BLOCK_MAGIC2(DoA_BladeRF, sample_offset);
%include "DoA_BladeRF/Delay.h"
GR_SWIG_BLOCK_MAGIC2(DoA_BladeRF, Delay);
