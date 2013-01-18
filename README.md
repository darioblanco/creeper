creeper
=======

Play with `ghost.py`, and creep the web servers. This project is just a basic set up of `Ghost.py`, with an example script. Check the [Ghost.py documentation](http://carrerasrodrigo.github.com/Ghost.py/) for further information.

## Dependencies
Python 2.6 or greater

Ubuntu packages
* python-qt4
* qt4-dev-tools

Pip packages
* argparse (only needed if running Python 2.6)
* Ghost.py
* PyQt
* SIP

Just create a virtualenv and install the pip packages with `pip install -r requirements.txt`.

`Ghost.py` needs `PyQt`. For installing it, run `pip install -r pyqt-requirements.txt`. `PyQt` and `SIP` will fail to install, which is expected because the source is downloaded but pip can't install it (yeah I hate that). But don't worry, there is a workaround: go to the place in which pip has downloaded `SIP` and `PyQt` packages and execute the following commands (the Ubuntu package dependencies are needed for `PyQt`):

> cd ~/build/SIP
python configure.py
make
sudo make install 

> cd ~/build/PyQt
python configure.py
make
sudo make install

Be patient, it takes a while (compiling `PyQt` is funny). You should remind that being a creeper is not an easy business.
