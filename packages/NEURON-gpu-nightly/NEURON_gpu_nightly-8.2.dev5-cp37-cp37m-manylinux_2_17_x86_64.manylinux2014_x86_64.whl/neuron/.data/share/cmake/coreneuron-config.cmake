# =============================================================================
# Copyright (C) 2016-2021 Blue Brain Project
#
# See top-level LICENSE file for details.
# =============================================================================

# coreneuron-config.cmake - package configuration file

get_filename_component(CONFIG_PATH "${CMAKE_CURRENT_LIST_FILE}" PATH)

set(CORENRN_ENABLE_GPU ON)
set(CORENRN_ENABLE_NMODL OFF)
set(CORENRN_ENABLE_REPORTING OFF)
set(CORENEURON_LIB_LINK_FLAGS "-cuda -gpu=cuda11.5,lineinfo,cc60,cc70,cc80 -acc -rdynamic -lrt -Wl,--whole-archive -Lx86_64 -lcorenrnmech -L$(libdir) -lcoreneuron -Wl,--no-whole-archive -ldl")

find_path(CORENEURON_INCLUDE_DIR "coreneuron/coreneuron.h" HINTS "${CONFIG_PATH}/../../include")
find_path(
  CORENEURON_LIB_DIR
  NAMES libcoreneuron.a libcoreneuron.so libcoreneuron.dylib
  HINTS "${CONFIG_PATH}/../../lib")

include(${CONFIG_PATH}/coreneuron.cmake)
