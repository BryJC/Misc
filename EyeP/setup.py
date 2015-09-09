try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'EyeP is a test for lpthw46',
    'author': 'BryJC',
    'url': 'URL to get it at.',
    'download_url': 'local',
    'author_email': 'bryjc.projects@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['IProj'],
    'scripts': ['bin/testscript.py'],
    'name': 'EyeP'
}

setup(**config)
