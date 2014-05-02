# -*- coding:utf8 -*-
import urllib,urllib2,cookielib
import getpass
cj = cookielib.CookieJar();
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
urllib2.install_opener(opener);
print '''
██╗   ██╗ ██████╗ ████████╗███████╗    ███████╗ ██████╗ ██████╗     ██╗   ██╗███████╗
██║   ██║██╔═══██╗╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗    ██║   ██║██╔════╝
██║   ██║██║   ██║   ██║   █████╗      █████╗  ██║   ██║██████╔╝    ██║   ██║███████╗
╚██╗ ██╔╝██║   ██║   ██║   ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗    ██║   ██║╚════██║
 ╚████╔╝ ╚██████╔╝   ██║   ███████╗    ██║     ╚██████╔╝██║  ██║    ╚██████╔╝███████║
  ╚═══╝   ╚═════╝    ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝
                                                                                     
                                                                                     '''

username = raw_input('输入学号和密码可直接为我们投票哦～\n学号:')
password = getpass.getpass('身份证后六位:')
data = urllib.urlencode({'username':username,
	'password':password})
req = urllib2.Request(url='http://buptvote.com/vote/index.php/site/login',data=data)
urllib2.urlopen(req)
data2 = urllib.urlencode({'project_id':'91'})
req2 = urllib2.Request(url='http://buptvote.com/vote/index.php/vote/create',data=data2)
res = urllib2.urlopen(req2).read()
print eval(res)['state']
print "END"