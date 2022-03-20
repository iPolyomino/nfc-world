#!/usr/bin/env python3
import nfc


def connected(tag):
    print(tag)
    try:
        print(('  ' + '\n  '.join(tag.dump())))
    except Exception as e:
        print('error: %s' % e)


clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})
