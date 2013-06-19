CZDAP Tools
===========

* Decrypt FTP credentials downloaded from ICANN's CZDAP application.
* Download zone data directly using the CZDAP API.

Installation
------------

This script requires Python 2.x plus the `pycrypto` and `requests` extension libraries.

#### Mac OSX

*Tested with Snow Leopard and Mountain Lion*

OSX comes with Python preinstalled. To install the pycrypto extension, issue the following commands:

    sudo easy_install pip
    sudo pip install --upgrade pycrypto requests

#### Linux

With *Ubuntu 13.04 Raring Ringtail*:

    sudo apt-get install python-pycryptopp python-requests

#### Windows

*No steps available right now, but steps above should work with pip.*

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

1. Visit CZDAP and download your token. You can find it on your user profile page.
2. In the `credentials-decrypt` directory, make a copy of the `config.sample.json` file and name it `config.json`.
3. Edit config.json and overwrite the "token" parameter with the your unique token.
2. Copy your private key into this directory and make sure it's named `czdap.private.key`.
4. Run `python decrypt.py`.

Downloading zone data
---------------------

1. Visit CZDAP and download your token. You can find it on your user profile page.
2. In the `zonedata-download` directory, make a copy of the `config.sample.json` file and name it `config.json`.
3. Edit config.json and overwrite the "token" parameter with the your unique token.
4. Run `python download.py`

Contributing
------------

Contributions are welcome.
