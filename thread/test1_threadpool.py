#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# there are some errors !!!!

import time
import threadpool
import urllib2

urls = [
	'http://www.baidu.com',
	'http://163.com',
	'http://alibaba.com',
	'http://weibo.com'
]

def myRequest(url):
	resp = urllib2.urlopen(url)
	print url, resp.getcode()


def timeCost(request, n):
	print "Elapsed time: %s" % (time.time() - start_time)


start_time = time.time()

pool = threadpool.ThreadPool(4)
reqs = threadpool.makeRequests(myRequest, urls, timeCost)
[pool.putRequest(req) for req in reqs]
pool.wait()


