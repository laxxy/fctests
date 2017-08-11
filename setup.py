from setuptools import setup, find_packages


def get_requirements():
    """Reads the installation requirements from test-requirements.pip"""
    with open("test-requirements.pip") as f:
        lines = f.read().split("\n")
        lines_without_comments = [line for line in lines if not line.startswith('#') and not line == '']
        return lines_without_comments

setup(name='selenium_t',
      version='0.0.1',
      description='selenium tests',
      author='',
      author_email='',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={},
      install_requires=get_requirements(),
      )
