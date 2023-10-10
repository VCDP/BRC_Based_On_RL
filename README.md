![image](https://github.com/VCDP/BRC_Based_On_RL/assets/105685839/9981c5d3-24e2-4a6d-b15d-f5f10b27a113)# BRC_Based_On_RL

HM repo: 
https://vcgit.hhi.fraunhofer.de/jvet/HM.git

pybind11 install way on LINUX:
  dependency(centos): python3-devel libffi-devel
  $ git clone https://github.com/pybind/pybind11
  $ mkdir build
  $ cd build
  $ cmake ..
  $ make check -j 4
  $ make install //将pybind11的头文件拷贝到系统目录下

  手动设置python环境变量
  $ export PYTHONPATH=$PYTHONPATH:/home/gemfield/github/prototype/pybind11/
  
  使用下面命令来得到所要包含的头文件的路径
  $ python3 -m pybind11 --includes 
  例如：[root@media-zwj-dg1-c74 HM]# python3 -m pybind11 --includes
  -I/usr/include/python3.6m -I/usr/local/lib/python3.6/site-packages/pybind11-2.12.0.dev1-py3.6.egg/pybind11/include


  将这些文件如下放置：
[root@media-zwj-dg1-c74 pb]# pwd
/home/media/RL/repo/HM/source/Lib/pb
[root@media-zwj-dg1-c74 pb]# ls
CMakeLists.txt  pybind11  utilitypb.cc
