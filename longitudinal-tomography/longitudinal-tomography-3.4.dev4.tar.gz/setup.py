from setuptools import setup
from os import path
import platform
from pybind11.setup_helpers import Pybind11Extension

HERE = path.split(path.abspath(__file__))[0]

extra_compile_args = []
extra_link_args = []
if platform.system() == 'Windows':
    extra_compile_args.append('-openmp')
elif platform.system() == 'Linux':
    extra_compile_args.append('-fopenmp')
    extra_compile_args.append('-ffast-math')
    extra_link_args.append('-lgomp')


cpp_routines = Pybind11Extension('tomo.cpp_routines.libtomo',
                                 cxx_std=17,
                                 sources=['tomo/cpp_routines/libtomo.cpp',
                                          'tomo/cpp_routines/reconstruct.cpp',
                                          'tomo/cpp_routines/kick_and_drift.cpp',
                                          'tomo/cpp_routines/data_treatment.cpp'],
                                 extra_compile_args=extra_compile_args,
                                 extra_link_args=extra_link_args)

setup(ext_modules=[cpp_routines])
