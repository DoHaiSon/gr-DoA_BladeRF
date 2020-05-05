#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/haison98/gr-DoA_BladeRF/lib
export PATH=/home/haison98/gr-DoA_BladeRF/build/lib:$PATH
export LD_LIBRARY_PATH=/home/haison98/gr-DoA_BladeRF/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-DoA_BladeRF 
