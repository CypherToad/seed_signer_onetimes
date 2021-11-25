#!/usr/bin/env python3

# Built in python libraries
import base64
from io import BytesIO

# Trusting Trezor's for randopm wallet creations
from mnemonic import Mnemonic

# Trusting qrcode library as offline qr code creation
import qrcode

# Trusting Flask as simple web interface which can be easily printed or stored as pdf
from flask import Flask, render_template


app = Flask(__name__)
mnemo = Mnemonic("english")

# load our words.txt which was fetched from Trezor's github
# https://github.com/trezor/python-mnemonic/blob/master/src/mnemonic/wordlist/english.txt
with open('words.txt') as f:
    words = [ i for i in f.read() if i ]


def seed_qr_string(words):
    """
    Return a string representation of our words for seed_signer
    """

    return ''.join([ words[i:i+4] for i in range(0, len(words), 4) ])


def seed_qr_base64(words):
    """
    Return a base64 PNG encoding of our seed_qr.
    """

    # create a qrcode of our seed_qr_string
    img = qrcode.make(
        seed_qr_string(words))

    # generate a
    # https://jdhao.github.io/2020/03/17/base64_opencv_pil_image_conversion/
    im_file = BytesIO()
    img.save(im_file, format="PNG")
    im_b64 = base64.b64encode(im_file.getvalue())

    return im_b64.decode()


@app.route("/")
def home():
    """
    Main home page which generates random wallets
    """

    # going to store our wallets and qr codes in a list of tuples
    word_bundle = []

    # generate 5 wallets per run
    for i in range(5):

        words = mnemo.generate(strength=256)
        word_bundle.append((words, seed_qr_base64(words)))

    return render_template('index.html', word_bundle=word_bundle)


if __name__ == "__main__":
    app.run()
