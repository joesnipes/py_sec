#!/usr/bin/env python

import sys

class Printer:

    def __init__(self, ina, inb):
        self.a = ina
        self.b = inb

    def manufacturer(self):
        return self.a

    def model(self):
        return self.b

newPrinter = Printer('HP', 'ex200')

print 'Manufacturer: %r'%newPrinter.manufacturer()
print 'Model: %r'%newPrinter.model()