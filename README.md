# PROJECT NOT UNDER ACTIVE MANAGEMENT #  
This project will no longer be maintained by Intel.  
Intel has ceased development and contributions including, but not limited to, maintenance, bug fixes, new releases, or updates, to this project.  
Intel no longer accepts patches to this project.  
 If you have an ongoing need to use this project, are interested in independently developing it, or would like to maintain patches for the open source software community, please create your own fork of this project.  
  

testtest

# BRC_Based_On_RL
## why pybind11

https://zyxin.xyz/blog/2019-08/glue-python-cpp/  
https://github.com/tensorflow/community/blob/master/rfcs/20190208-pybind11.md#replace-swig-with-pybind11   

## pybind11 example

https://www.jianshu.com/p/5dc844002d72  

## HM repo: 
https://vcgit.hhi.fraunhofer.de/jvet/HM.git

## pybind11 install way on LINUX:
dependency(centos): python3-devel libffi-devel  
```
$ git clone https://github.com/pybind/pybind11  
$ mkdir build  
$ cd build  
$ cmake ..  
$ make check -j 4  
$ make install //将pybind11的头文件拷贝到系统目录下  
```

### 手动设置python环境变量
```
$ export PYTHONPATH=$PYTHONPATH:/home/gemfield/github/prototype/pybind11/  
```
### 使用下面命令来得到所要包含的头文件的路径
```
$ python3 -m pybind11 --includes
``` 
例如：[root@media-zwj-dg1-c74 HM]# python3 -m pybind11 --includes  
-I/usr/include/python3.6m -I/usr/local/lib/python3.6/site-packages/pybind11-2.12.0.dev1-py3.6.egg/pybind11/include  


###  将这些文件如下放置：
```
[root@media-zwj-dg1-c74 pb]# pwd
/home/media/RL/repo/HM/source/Lib/pb
[root@media-zwj-dg1-c74 pb]# ls
CMakeLists.txt  pybind11  utilitypb.cc
```
