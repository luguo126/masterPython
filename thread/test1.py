#!/usr/bin/env python

import time
import urllib2

def get_responses():
	urls = [
		'http://www.baidu.com',
		'http://www.163.com',
		'http://www.alibaba.com',
		'http://www.weibo.com',
	]

	start_time = time.time()
	for url in urls:
		print url
		resp = urllib2.urlopen(url)
		print resp.getcode()
	
	end_time = time.time()
	print "Elapsed time: %s" % (end_time - start_time)

get_responses()
