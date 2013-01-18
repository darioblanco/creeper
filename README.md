creeper
=======

Play with ghost.py, and creep the web servers.

## Dependencies
Python 2.6 or greater

Ubuntu packages
* python-qt4
* qt4-dev-tools

Pip packages
* argparse
* Ghost.py
* PyQt
* SIP

Just create a virtualenv and install the pip packages with `pip install -r requirements.txt`.

`Ghost.py` needs `PyQt`. For installing it, run `pip install -r pyqt-requirements.txt`. `PyQt` and `SIP` will fail to install, which is expected because the source is downloaded but pip can't install it.
Go to the place in which pip has downloaded `SIP` and `PyQt` packages and execute the following commands (the Ubuntu package dependencies are needed for `PyQt`):

For `SIP`
> cd ~/build/SIP
>
> python configure.py
>
> make
>
> sudo make install 

For `PyQt`
> cd ~/build/PyQt
>
> python configure.py
>
> make
>
> sudo make install

Be patient, it takes a while. Being a creeper is not an easy business.
