import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='wfm.py',
    version='0.0.1',
    author='dsluo',
    author_email='mail@dsluo.me',
    license='MIT',
    description='A Python wrapper for warframe.market.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dsluo/wfm.py',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Games/Entertainment',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries'
    ]
)
