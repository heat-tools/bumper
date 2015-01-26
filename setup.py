from distutils.core import setup

setup(name='bumper',
      description='manipulate tags on Github hosted repos',
      version='0.1.4',
      author='Rackspace',
      author_email='jason@duncancreek.net',
      license='Apache License (2.0)',
      classifiers=["Programming Language :: Python"],
      url='https://github.com/JasonBoyles/bumper',
      scripts=['bumper'],
      install_requires=['click==3.3',
                        'PyGithub==1.25.2',
                        'hot>=0.5.0',
                        'requests==2.4.3']
      )
