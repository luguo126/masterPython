#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

some_var = 0

class IncrementThread (threading.Thread):
	def run(self):
		global some_var
		read_value = some_var
		print "some_var in %s is %d " % (self.name, read_value)
		some_var = read_value + 1
		print "some_var in %s after increment is %s " % (self.name, some_var)


def use_increment_thread():
	threads = []
	for i in range(100):
		t = IncrementThread()
		threads.append(t)
		t.start()
	for t in threads:
		t.join()
	2 ** 100
	print "After 50 modifications, some_var should have become 100"
	print "After 50 modifications, some_var is %d" % some_var


use_increment_thread()
