from setuptools import setup


setup(name='pyudemy',
      version='0.3',
      description='Simple integrate of API udemy.com with python',
      url='https://github.com/hudsonbrendon/pyudemy',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=['pyudemy'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
