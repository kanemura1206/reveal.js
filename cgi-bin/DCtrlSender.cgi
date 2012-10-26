#! /usr/bin/env python
# -*- coding:utf-8 -*-

# ------------------------------------------------------------------------------
# This script is made for ET 2012 Demo. (2012/10/25)
# This script gets D-Control script from client and sends it to D-Controller.
# ------------------------------------------------------------------------------

import urllib, urllib2
import cgi, uuid, sys, os, json

### Config
DCtrl_ip = 'http://192.168.59.150'
DCtrl_url = DCtrl_ip + '/reveal/cgi-bin/dse_dummy.cgi'

def request_addCid():
	form = cgi.FieldStorage()
	req = ({
			'CId': createCId(),
			'Method': form.getvalue('Method'),
			'Script': form.getvalue('Script'),
			'Option': form.getvalue('Option')
		})
	return req

def sendRequest(req):
	params = urllib.urlencode(req)
	return urllib2.urlopen(DCtrl_url, params)

def returnClient(req, res):
	print "Content-Type: application/json"
	print ''
	#print res
	print json.dumps({
			'CId': req['CId'],
			'Result': 'success',
			'Method': 'ResponseDSE'
	})

def createCId():
	return str(uuid.uuid4())

if __name__ == '__main__':
	req = request_addCid()
	res = sendRequest(req)
	returnClient(req, res.read());
