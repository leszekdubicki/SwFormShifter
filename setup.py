from distutils.core import setup
import py2exe

setup(options = {'py2exe': {'excludes':['_ssl', 'pyreadline', 'difflib', 'doctest', 'optparse', 'pickle', 'calendar'], 'compressed':True}}, windows=['formatki.py'], console=['cmd.py'], zipfile = None)
#setup(options = {'py2exe': {'bundle_files': 1, 'compressed':True}}, console=['e2s.py'], zipfile = None)
