from setuptools import setup, find_packages

setup(name='process_search',
      version='0.1',
      description='Utility to search for running processes',
      long_description='Basically a wrapping for ps -ef | grep python',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Licence :: OSI Approved :: MIT Licence',
          'Programming language :: Python :: 2.7',
          'Topic :: Utilities'
      ],
      keywords='process search test utility',
      url='https://github.com/burrbank/process_search',
      author='Ryan Porter',
      author_email='ryan.j.porterr@gmail.com',
      licence='MIT',
      pagages=find_packages(),
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
