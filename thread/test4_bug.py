#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import threading
import time

class CreateListThread (threading.Thread):
	def run(self):
		self.entries = []
		for i in range(230):
			time.sleep(0.01)
			self.entries.append(i)
		print self.entries
		print "\n"

def use_create_list_thread():
	for i in range(3):
		t = CreateListThread()
		t.start()

use_create_list_thread()

