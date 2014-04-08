#python2.4
import os,sys,filecmp,smtplib
#from email.mime.multipart import MIMEMultipart
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
#from email.mime.text import MIMEText
from pickle import dump
#import io
try:
	from hashlib import md5
except:
	from md5 import md5
def find_ip():
    ip = os.popen("/sbin/ip a|grep 'global eth0'").readlines()[0].split()[1].split("/")[0]
    if "192.168." in ip:
        ip = os.popen("/sbin/ip a|grep 'global eth1'").readlines()[0].split()[1].split("/")[0]
    return ip
def calMd5(files):
    m = md5()
#    file = io.FileIO(files,'r')
    file1 = file(files,'r')
    bytes = file1.read(2048)
    while(bytes != ''):
        m.update(bytes)
        bytes = file1.read(1024)
    file1.close()
    md5value = m.hexdigest()
    return md5value
def sendMail(info):
    you = "992975991@qq.com"
    me = 'lgl15984@163.com'
    mail_host = "smtp.163.com"
    mail_user = 'lgl15984'
    mail_pass = '15984794312'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Warning"
    msg['From'] = me
    msg['To'] = you
    part1 = MIMEText(info, 'plain')
    msg.attach(part1)
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(mail_user,mail_pass)
    s.sendmail(me, you, msg.as_string())
    s.quit()
def truncatefile():
	f = open('b.txt','w+')
	f.truncate()
	f.close()
def findDirectoryOld(path):
        for root,subFolders,files in os.walk(path):
                if 'weblog' in subFolders:
                        subFolders.remove('weblog')
                for filespath in files:
                        if 'laodao_ynvng_config.php' in files:
                                files.remove('laodao_ynvng_config.php')
#                       print os.path.join(root,filespath)
                        filepath = os.path.join(root,filespath)
#                       return filepath
#                       if not os.path.isdir(filepath):
#                       temp = sys.stdout
#                       sys.stdout = open('a.txt','w')
                        f = open('a.txt','a+')
#                       dump(os.path.join(root,filespath),f)
#                       f.close()
#                       a = []
#                       b = []
                        for i in os.path.join(root,filespath).split('\n'):
                                f.write(i),
                                for j in calMd5(filepath).split('\n'):
                                        f.write('\t')
                                        f.write(j),
                                        f.write('\n')
                                        f.close()
def createtxt():
    if os.path.isfile('a.txt'):
	pass
    else:
        findDirectoryOld(path)
def findDirectory(path):
        for root,subFolders,files in os.walk(path):
                if 'weblog' in subFolders:
                        subFolders.remove('weblog')
                for filespath in files:
                        if 'laodao_ynvng_config.php' in files:
                                files.remove('laodao_ynvng_config.php')
#                       print os.path.join(root,filespath)
                        filepath = os.path.join(root,filespath)
#                       return filepath
#                       if not os.path.isdir(filepath):
#			temp = sys.stdout
#			sys.stdout = open('a.txt','w')
			f = open('b.txt','a+')
#			dump(os.path.join(root,filespath),f)
#			f.close()
#			a = []
#			b = []
			for i in os.path.join(root,filespath).split('\n'):
				f.write(i),
				for j in calMd5(filepath).split('\n'):
					f.write('\t')
					f.write(j),
					f.write('\n')
					f.close()
#			f.truncate()
#			os.remove('b.txt')
#			f.close()
#			sys.stdout = f
#			so = file('b.txt','w+')
#			os.dup2(so.fileno(),sys.stdout.fileno())
#                        print  os.path.join(root,filespath), calMd5(filepath)
#			so.close()

def comparefile():
	flag = filecmp.cmp(r'a.txt',r'b.txt')
#	print flag
#	print flag
#	print flag
	ip = find_ip()
	if flag == False:
#		pass
		sendMail('%s the file i changed' % ip)
	else:
#		sendMail('%s the file not changed' % ip)
		pass
if __name__ == '__main__':
	path = '/data/www'
	ip = find_ip()
	createtxt()
	truncatefile()
	findDirectory(path)
	comparefile()
