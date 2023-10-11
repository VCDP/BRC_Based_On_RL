#!/usr/bin/env bash

git clone -b HM-9.2 https://vcgit.hhi.fraunhofer.de/jvet/HM.git ../hm-9.2
cd ../hm-9.2
patch -p0 < ../swig/swig-hm-9.2.diff
cd ./build/linux
make
cd ../../../swig

python setup.py build_ext --inplace
