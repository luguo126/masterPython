#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import threading
import time

lock = threading.Lock()

class CreateListThread(threading.Thread):
	def run(self):
		self.entries = []
		for i in range(300):
			time.sleep(0.01)
			self.entries.append(i)
		lock.acquire()
		print self.entries
		lock.release()

def use_create_list_thread():
	for i in range(3):
		t = CreateListThread()
		t.start()

use_create_list_thread()
