#!/usr/bin/env python3

import nfc
from nfc.clf import RemoteTarget
from ndef import TextRecord

clf = nfc.ContactlessFrontend('usb')
target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'),
                   RemoteTarget('212F'))
if target is None:
    print('waiting for tag')

tag = clf.connect(rdwr={'on-connect': lambda tag: False})
if tag.ndef is not None:
    for record in tag.ndef.records:
        print(record)
    if tag.ndef.is_writeable:
        data = input('Please input the character string.\n>> ')
        tag.format(wipe=0)
        tag.ndef.records = [TextRecord(data)]
        print('Done')
