# seed_signer_ontimes

> **WARNING** This project has mainly been used for local development, and creation should be ran on a air-gapped machine.

A minimal python script for generating multiple onetime use **bip39 seed phrases**, and corresponding [Seed Signer Seed](https://github.com/SeedSigner/seedsigner) seed phrase **qr code**.

![screenshot](/examples/screenshoot_v1.png)

### Dependencies

The following python project are used, and should be retrieved
before moving to the final air-gapped machine.

```
click==8.0.3
Flask==2.0.2
itsdangerous==2.0.1
Jinja2==3.0.3
MarkupSafe==2.0.1
mnemonic==0.20
Pillow==8.4.0
qrcode==7.3.1
Werkzeug==2.0.2
```

### Installation

```
$ cd seed_signer_ontimes/
$ virtualenv -p python3 venv/
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Usage

```
$ ./main.py
```

If successful you will have a local website available with your
random seed phrases.


> * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Go ahead and refresh the page to get a new set of addresses!
