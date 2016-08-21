try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Vikram Mullachery',
	'url': 'http://gitlab.com/',
	'download_url': '',
	'author_email': 'mullachv@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['calltrace'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)
