CZDAP Tools
===========

Some registries allow users to download zone data directly from CZDAP, and others provide FTP credentials that you can use to login to their servers. These tools allow you to programatically perform these two tasks:

* Decrypt FTP credentials downloaded from ICANN's CZDAP application.
* Download zone data directly using the CZDAP API.

Installation
------------

This script requires Python 2.x plus the `pycrypto` and `requests` extension libraries.

#### Mac OSX

*Tested with Snow Leopard and Mountain Lion*

OSX comes with Python preinstalled. To install the required extensions, issue the following commands:

    sudo easy_install pip
    sudo pip install --upgrade pycrypto requests

#### Linux

With *Ubuntu 13.04 Raring Ringtail*:

    sudo apt-get install python-pycryptopp python-requests

#### Windows

*Tested on Windows 7*

Download and configure the Python environment:

* Download Python version 2.7.x from [the main download page](http://python.org/download/).
* Run the installer and follow the installation instructions.

Install `pycrypto` and `requests`:

* Pycrypto: [pre-built binary](http://www.voidspace.org.uk/python/modules.shtml#pycrypto).
* Requests: [pre-built binary](http://www.lfd.uci.edu/~gohlke/pythonlibs/)

Decrypting credentials
----------------------

To confirm that you've installed the dependencies correctly, simply run the test and it should process the example data successfully:

    cd credentials-decrypt/test
    python test-decrypt.py

You should get the following sample output in basic CSV format:

    server,username,password
    ftp.download.com,com_ftp_access,specialpassword__22
    ftp.download.biz,sally,password12345$
    ftp.download.net,net_access,secretpassword456

To decrypt your own FTP credentials:

1. Visit CZDAP and copy your token. You can find it on your user profile page, under the tab "API".
2. In the `/credentials-decrypt` directory, make a copy of the `config.sample.json` file and name it `config.json`.
3. Edit config.json and overwrite the "token" parameter with the your unique token.
2. Copy your private key into this directory and make sure it's named `czdap.private.key`.
4. Run `python decrypt.py`.

Downloading zone data
---------------------

1. Visit CZDAP and copy your token. You can find it on your user profile page.
2. In the `/zonedata-download` directory, make a copy of the `config.sample.json` file and name it `config.json`.
3. Edit config.json and overwrite the "token" parameter with the your unique token.
4. Run `python download.py`

Contributing
------------

Contributions are welcome.
