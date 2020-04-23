# Copyright 2011,2012,2016 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

list(APPEND DoA_BladeRF_sources
    mess_sink_f_impl.cc
    multi_exp_impl.cc
    PCA_impl.cc
    Hold_impl.cc
    vector_steering_impl.cc
    DOA_impl.cc
    sample_offset_impl.cc
    Delay_impl.cc
)

set(DoA_BladeRF_sources "${DoA_BladeRF_sources}" PARENT_SCOPE)
if(NOT DoA_BladeRF_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT DoA_BladeRF_sources)

add_library(gnuradio-DoA_BladeRF SHARED ${DoA_BladeRF_sources})
target_link_libraries(gnuradio-DoA_BladeRF ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-DoA_BladeRF PROPERTIES DEFINE_SYMBOL "gnuradio_DoA_BladeRF_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-DoA_BladeRF PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
include(GrMiscUtils)
GR_LIBRARY_FOO(gnuradio-DoA_BladeRF RUNTIME_COMPONENT "DoA_BladeRF_runtime" DEVEL_COMPONENT "DoA_BladeRF_devel")

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_DoA_BladeRF_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_DoA_BladeRF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_DoA_BladeRF.cc
)

add_executable(test-DoA_BladeRF ${test_DoA_BladeRF_sources})

target_link_libraries(
  test-DoA_BladeRF
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-DoA_BladeRF
)

GR_ADD_TEST(test_DoA_BladeRF test-DoA_BladeRF)

########################################################################
# Print summary
########################################################################
message(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Building for version: ${VERSION} / ${LIBVER}")

