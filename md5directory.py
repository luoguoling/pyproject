__author__ = 'Administrator'
#coding:utf-8
import os,smtplib,sys,filecmp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import hashlib,io
def find_ip():
    '''查出ip地址'''
    ip = os.popen("/sbin/ip a|grep 'global eth0'").readlines()[0].split()[1].split("/")[0]
    if "192.168." in ip:
        ip = os.popen("/sbin/ip a|grep 'global eth1'").readlines()[0].split()[1].split("/")[0]
    return ip
def sendMail(info):
    '''邮件发送'''
    you = "luoguoling@mokylin.com"
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
def calMd5(files):
    '''计算md5值'''
    m = hashlib.md5()
    file = io.FileIO(files,'r')
    bytes = file.read(2048)
    while(bytes != b''):
        m.update(bytes)
        bytes = file.read(1024)
    file.close()
    md5value = m.hexdigest()
    return md5value
def truncatefile():
        f = open('b.txt','w+')
        f.truncate()
        f.close()
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
#                       temp = sys.stdout
#                       sys.stdout = open('a.txt','w')
#                       f = open('b.txt','w')
#                       f.truncate()
#                       os.remove('b.txt')
#                       f.close()
#                       sys.stdout = f
                        so = file('b.txt','a+')
                        os.dup2(so.fileno(),sys.stdout.fileno())
                        print  os.path.join(root,filespath), calMd5(filepath)
def comparefile():
    flag = filecmp.cmp(r'a.txt',r'b.txt')
#       print flag
    ip = find_ip()
    if flag == False:
            sendMail('%s the file i changed' % ip)
    else:
            print "the file is change"
if __name__ == '__main__':
        path = '/data/www'
        ip = find_ip()
        truncatefile()
        findDirectory(path)
        comparefile()











