cmake_minimum_required(VERSION 3.12)
project(PyUtilities)

set(CMAKE_CXX_STANDARD 14)
add_subdirectory(./pybind11)
find_package(pybind11 REQUIRED)
pybind11_add_module(PyUtilities utilitypb.cc)
target_include_directories( PyUtilities PUBLIC . .. ...)#添加环境变量
target_link_libraries(PyUtilities PRIVATE TLibCommon)
target_link_libraries(PyUtilities PRIVATE TLibEncoder)
target_link_libraries(PyUtilities PRIVATE Utilities)


