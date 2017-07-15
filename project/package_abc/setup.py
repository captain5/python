from setuptools import setup

setup(name='abc_test',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['abc_test'],
	  install_requires=['requests', 'xxhash'],
	  entry_points={
        'console_scripts': ['funniest-joke=abc_test.command_line:main'],
		
      },
      zip_safe=False)