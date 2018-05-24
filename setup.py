from setuptools import setup

setup(name='blockchain_statistics_readout',
      version='0.3.1',
      description='Read out statistics from a blockchain',
      author='Anton von Weltzien',
      license='MIT',
      packages=['blockchain_statistics_readout'],
      url='https://github.com/BPChain/blockchain_statistics_readout.git',
      install_requires=['websocket-client==0.47.0', 'psutil==5.4.5'],
      zip_safe=False)
