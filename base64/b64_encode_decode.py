#! /usr/bin/env python

import base64


info = "tz: miss you so bad !!"

encoded = base64.b64encode(info)
decoded = base64.b64decode(encoded)

print "encoded: ", encoded
print "decoded: ", decoded

