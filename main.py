import urllib.request
import threading
import random
import sys
import os
import requests
from colorama import Fore



r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=all&country=all&anonymity=all&ssl=yes")
r2 = requests.get("http://pubproxy.com/api/proxy?limit=10&format=txt&http=true&country=all&type=http")
r3 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt")
r4 = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
f = open("proxies.txt",'a+')
f.write(r.text)
f.write(r2.text)
f.write(r3.text)
f.write(r4.text)


clear()

try:
    txtfile = 'proxies.txt'
    f = open(txtfile)
except:
    sys.exit()

useragents=('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')


def checkeproxy():
	global out_file
	candidate_proxies = open(txtfile).readlines()
	filedl = open(txtfile, "w")
	filedl.close()
	out_file = open(txtfile, "a")
	threads = []
	for i in candidate_proxies:
		t = threading.Thread(target=checker, args=[i])
		t.start()
		threads.append(t)


	for t in threads:
		t.join()

	out_file.close()
	print("Checked all proxies")

def checker(i):
	proxy = i
	proxy_support = urllib.request.ProxyHandler({'http' : proxy})
	opener = urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(opener)
	req = urllib.request.Request(("http://www.google.com"))
	req.add_header("User-Agent", useragents)
	try:
		urllib.request.urlopen(req, timeout=60)
		print (Fore.GREEN + f"[Valid] {proxy}{Fore.RESET}")
		out_file.write(i)
	except:
		print(Fore.RED + f"[Invalid] {proxy}{Fore.RESET}")

checkeproxy()
