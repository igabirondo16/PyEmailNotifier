from setuptools import setup, find_packages

# Function to read requirements from requirements.txt
def read_requirements():
    with open('./requirements.txt') as req_file:
        return req_file.read().splitlines()

setup(
    name="py_email_notifier",
    version='1.0.0',
    description='Python module for sending by email the result of a long execution.',
    author="Iñigo Gabirondo López",
    author_email="igabirondo13@gmail.com",
    url="https://github.com/igabirondo16/PyEmailNotifier",
    packages=find_packages(),
    install_requires=read_requirements(),
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
    ],

)