#!/usr/bin/env python3

import binascii
import nfc


class CardReader(object):
    def on_connect(self, tag):
        print('touched')
        self.idm = binascii.hexlify(tag.idm)
        print(self.idm)
        return True

    def read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect': self.on_connect})
        finally:
            clf.close()
            print('released')


if __name__ == '__main__':
    cr = CardReader()
    while True:
        cr.read_id()
