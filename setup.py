from setuptools import setup, find_packages

setup(
    name="py_email_notifier",
    version='1.0.0',
    description='Python module for sending by email the result of a long execution.',
    author="Iñigo Gabirondo López",
    author_email="igabirondo13@gmail.com",
    url="https://github.com/igabirondo16/PyEmailNotifier",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Software development'
    ],

)