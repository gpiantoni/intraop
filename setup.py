from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).resolve().parent
with (here / 'intraop' / 'VERSION').open() as f:
    VERSION = f.read().strip('\n')

with (here / 'README.rst').open(encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='intraop',
    version=VERSION,
    description='Tools to analyze intraop data in Python',
    long_description=long_description,
    url='https://github.com/gpiantoni/intraop',
    author="Gio Piantoni",
    author_email='intraop@gpiantoni.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ],
    keywords='intraop',
    packages=find_packages(exclude=('test', )),
    install_requires=[
        'nibabel',
        'nipype',
        ],
    extras_require={
        'test': [  # to run tests
            'pytest',
            'pytest-cov',
            ],
        },
    package_data={
        'intraop': [
            'VERSION',
            ],
    },
    )
