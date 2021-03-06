#! /usr/bin/env python
# -*- coding:utf-8 -*-

# ------------------------------------------------------------------------------
# This script is made for ET 2012 Demo. (2012/10/25)
# This script gets D-Control script from client and sends it to D-Controller.
# ------------------------------------------------------------------------------

import urllib, urllib2
import cgi, uuid, sys, os, json

### Config
DCtrl_ip = 'http://127.0.0.1:8080'
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
	print "Content-Type: application/json"
	print ''
	string = "{ \"Method\" : \"SendDSE\" , \"Script\" : \"System.p(123);\" , \"Name\":\"hoge.k\", \"event\":\"D-Task\", \"To\": \"127.0.0.1:8080\"}"
	params = "%22%7b%20%c2%a5%22Method%c2%a5%22%20%3a%20%c2%a5%22SendDSE%c2%a5%22%20%2c%20%c2%a5%22Script%c2%a5%22%20%3a%20%c2%a5%22System%2ep%28%c2%a5%c2%a5%c2%a5%22hello%c2%a5%c2%a5%c2%a5%22%29%3b%c2%a5%22%20%2c%20%c2%a5%22Name%c2%a5%22%3a%c2%a5%22hoge%2ek%c2%a5%22%2c%20%c2%a5%22event%c2%a5%22%3a%c2%a5%22D%2dTask%c2%a5%22%2c%20%c2%a5%22To%c2%a5%22%3a%20%c2%a5%22127%2e0%2e0%2e1%3a8080%c2%a5%22%7d%22"
	print params
	return urllib2.urlopen(DCtrl_ip, params)

def returnClient(req, res):
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
