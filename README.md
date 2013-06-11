CZDAP Decrypt
=============

Decrypt FTP credentials downloaded from ICANN's CZDAP application.

Installation
============

This script requires Python 2.x and the pycrypto extension.

Mac OSX
-------

OSX comes with Python preinstalled. To install the pycrypto extension, issue the following command:

    sudo pip install pycrypto

Usage
=====

To confirm that you've installed the dependencies correctly, simply run decrypt.py and it should process the example data successfully:

    python decrypt.py

You should get the following sample output in basic CSV format:

    server,username,password
    ftp.download.com,com_ftp_access,specialpassword__22
    ftp.download.biz,sally,password12345$
    ftp.download.net,net_access,secretpassword456

To decrypt your own FTP credentials:

1. Visit CZDAP and download the credentials.json file for your account.
2. Replace the credentials.json file you see in this directory with the one you downloaded.
3. Replace the example key `czdap.private.key` with the one associated with your CZDAP account.
4. Run `python decrypt.py`.

Contributing
============

Contributions are welcome.
