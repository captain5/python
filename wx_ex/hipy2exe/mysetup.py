# mysetup.py
from distutils.core import setup
import py2exe
#setup(console=["HelloWorld.py"])
setup(windows=["HelloWorld.py"])


#python mysetup.py py2exe