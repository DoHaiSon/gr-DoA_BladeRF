# Install script for directory: /home/haison98/gr-DoA_BladeRF/grc

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/haison98/gr-DoA_BladeRF/grc/DoA_BladeRF_DOApy.xml"
    "/home/haison98/gr-DoA_BladeRF/grc/DoA_BladeRF_matlab_file.xml"
    "/home/haison98/gr-DoA_BladeRF/grc/DoA_BladeRF_mess_sink_f.xml"
    "/home/haison98/gr-DoA_BladeRF/grc/DoA_BladeRF_multi_exp.xml"
    "/home/haison98/gr-DoA_BladeRF/grc/DoA_BladeRF_PCA.xml"
    "/home/haison98/gr-DoA_BladeRF/grc/DoA_BladeRF_Hold.xml"
    "/home/haison98/gr-DoA_BladeRF/grc/DoA_BladeRF_vector_steering.xml"
    "/home/haison98/gr-DoA_BladeRF/grc/DoA_BladeRF_DOA.xml"
    "/home/haison98/gr-DoA_BladeRF/grc/DoA_BladeRF_sample_offset.xml"
    "/home/haison98/gr-DoA_BladeRF/grc/DoA_BladeRF_Delay.xml"
    )
endif()

