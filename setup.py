import setuptools
from setuptools import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()

# Define the Fortran extensions
extensions = [
    Extension(
        name='plancklens.wigners.wigners',
        sources=['plancklens/wigners/wigners.f90'],
        extra_link_args=['-lgomp'],
        libraries=['gomp'],
        extra_f90_compile_args=['-fopenmp', '-w'],
    ),
    Extension(
        name='plancklens.n1.n1f',
        sources=['plancklens/n1/n1f.f90'],
        extra_link_args=['-lgomp'],
        libraries=['gomp'],
        extra_f90_compile_args=['-fopenmp', '-w'],
    )
]

setup(
    name='plancklens',
    version='0.0.1',
    packages=['plancklens', 'plancklens.n1', 'plancklens.filt', 'plancklens.sims', 'plancklens.helpers',
              'plancklens.qcinv', 'plancklens.wigners', 'tests'],
    data_files=[('plancklens/data/cls', ['plancklens/data/cls/FFP10_wdipole_lensedCls.dat',
                                'plancklens/data/cls/FFP10_wdipole_lenspotentialCls.dat',
                                'plancklens/data/cls/FFP10_wdipole_params.ini'])],
    url='https://github.com/carronj/plancklens',
    author='Julien Carron',
    author_email='to.jcarron@gmail.com',
    description='Planck lensing python pipeline',
    install_requires=['numpy', 'healpy', 'six'],  # removed mpi4py for travis tests
    requires=['numpy', 'healpy', 'six', 'scipy'],
    long_description=long_description,
    ext_modules=extensions,
)
