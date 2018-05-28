from setuptools import setup

setup(name='statistics_reader',
      version='0.7.1',
      description='Read out statistics from a blockchain',
      author='Anton von Weltzien',
      license='MIT',
      packages=['statistics_reader'],
      url='https://github.com/BPChain/blockchain_statistics_readout.git',
      install_requires=['websocket-client==0.47.0', 'psutil==5.4.5'],
      zip_safe=False)
