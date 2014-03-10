__author__ = 'Administrator'
#coding=utf-8
from Tkinter import *
import tkMessageBox
import time
import socket
import win32api
import win32con
import os
import re
#----------------------------------------------Functions--------------------------------------------------------
#服务器连接
ip={}
port={}

type=sys.getfilesystemencoding()
#连接服务器
def ss(command):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((address))
    sock.send(command)
    result=sock.recv(2048)
    #sock.settimeout(5)
    sock.close()
    return result

#获取选中服务器名-连接服务器
def plist():
    sel=lb.get(lb.curselection())
    address=ip[sel.encode('gbk')],int(port[sel.encode('gbk')])
    global address
    #print address
    #发送
    mes=ss('time')
    #print mes
    tsert.delete('1.0','2.0')
    tsert.insert(INSERT,mes)

#查连服状态
def lf(conty):
    config='open("config/lianfu.txt")'
    cof=ss('%s')%(config)
    print cof.readline()

#检查输入时间
def keycheck(event):
    if 0<len(eyear.get()) and n==0:
        l=len(eyear.get())
        if not(48 <= ord(eyear.get()[l-1:l]) <= 57):
            eyear.delete(l-1,l)
            eyear.index(l-1)
        elif eyear.get().isdigit and l==4:
            n+=1
            global n
            win32api.keybd_event(9,0,0,0)
            win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)

    elif 0<len(elist[n].get()):
        l=len(elist[n].get())
        if not(48 <= ord(elist[n].get()[l-1:l]) <= 57):
           elist[n].delete(l-1,l)
        elif elist[n].get().isdigit and l==2:
           n+=1
           global n
           win32api.keybd_event(9,0,0,0)
           win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)

#发送改时间消息
def gettime():
    timeset=''
    for i in range(0,5):
        timeset+=elist[i].get()
        if i<=1:
            timeset+='-'
        elif i==2:
            timeset+=' '
        else:
            timeset+=':'
    timeset+=esec.get()
    #print timeset
    jindu.delete('1.0','2.0')
    jindu.insert(INSERT,ss(timeset))
    tsert.delete('1.0','2.0')
    tsert.insert(INSERT,timeset)
    #tset=time.mktime(time.strptime(timeset,'%Y-%m-%d %H:%M:%S'))
    #print '设置时间：',tset
    #print int(tset)
    #tsert=ss('date')
    #print tsert
    #tsert=filter(str.isdigit,tsert)
    #tsert=list(tsert)
    #tp=''
    #for i in range(len(tsert)):
    #    tp+=tsert[i]
    #    if i in (3,5):
    #        tp+='-'
    #    if i==7:
    #        tp+=' '
    #    if i in (9,11):
    #        tp+=':'
    #tsert=time.mktime(time.strptime(tp,'%Y-%m-%d %H:%M:%S'))
    #print tsert
#判断
    #if tset>tsert:
    #    jd=ss('date -s "%s"'%timeset)
    #    jindu.insert(INSERT,jd)
    #else:
    #    flag=tkMessageBox.askokcancel(title='Warning',message='设定时间早于服务器时间，需要重启，请确认')
    #    if flag==True:
    #        print ss('cd /data/game/qmrserver10002/qmrserver && /bin/sh stop.sh') #关闭服务器
    #        time.sleep(10)
    #        print ss('date -s "%s"'%timeset)
    #        print ss('cd /data/game/qmrserver10002/qmrserver && /bin/sh start.sh') #开启服务器
    #        time.sleep(15)
    #        print ss('cd /data/game/qmrserver10002/qmrserver && /bin/sh checkserver.sh -ct')#检查是否开启成功

#重启服务器
def reboot():
    jindu.delete('1.0','2.0')
    jindu.insert(INSERT,ss('reboot'))
    #print ss('cd /data/game/qmrserver10002/qmrserver && /bin/sh stop.sh') #关闭服务器
    #time.sleep(10)
    #print ss('cd /data/game/qmrserver10002/qmrserver && /bin/sh start.sh') #开启服务器
    #time.sleep(15)
    #print ss('cd /data/game/qmrserver10002/qmrserver && /bin/sh checkserver.sh -ct')#检查是否开启成功

#弹出确认窗口
def callback():
    if len(elist[0].get())!=4:
        elist[6]=1
    for i in range(1,5):
        if len(elist[i].get())>0:
            elist[6]=0
        else:
            elist[6]=1
    if elist[6]==1:
        flag=tkMessageBox.showinfo(title='Warning',message='时间输入有误，请检查后再试')
    else:
        gettime()

#重启确认窗口
def callbackre():
    flagre=tkMessageBox.askokcancel(title='Warning',message='是否确定重启服务器？')
    if flagre==True:
        reboot()


#-------------------------------增加服务器列表--------------------------------------------------------------------
#coding=utf-8
path = "C:\Users\Administrator\Documents"
title = "Server Control"
new_path = os.path.join(path, title)
if not os.path.isdir(new_path):
    os.makedirs(new_path)
    f=open('C:\Users\Administrator\Documents\Server Control\Server Info.txt','w')
    f.write('越南测试服'+':'+'49.213.70.62'+';'+'6666')
    f.close()

#write
def writ(a,b,c):
    if len(a)==0 or len(b)==0 or len(c)==0:
        flagins=tkMessageBox.showinfo(title='Warning',message='输入信息有为空项，请检查后再试')
    else:
      stri=''
      stri+=a
      stri+=':'
      stri+=b
      stri+=';'
      stri+=c
      stri=stri
      f=open('C:\Users\Administrator\Documents\Server Control\Server Info.txt','a')
      f.write('\n'+stri)
      f.close()
      os.system('taskkill /FI "WINDOWTITLE eq Ser-Control"')
      lb.delete(0,END)
      readinfo()

#增加服务器UI
def ins():
#增加弹窗
    top=Toplevel()
    top.title('Ser-Control')
    top.geometry('200x135+800+500')
#服务器名
    ftop=Frame(top,height='135',width='200',bg='aliceblue')
    ftop.pack()
    lawarning=Label(top,text='Warning:请先与运维沟通后再增加',fg='maroon',bg='aliceblue',width=27)
    lawarning.place(x=0,y=0)
    lasname=Label(top,text='服务器名称:',bg='aliceblue')
    lasname.place(x=0,y=25)
    esname=Entry(top,width='16')
    esname.place(x=80,y=25)
    lasip=Label(top,text='Socket IP:',bg='aliceblue')
    lasip.place(x=0,y=50)
    esip=Entry(top,width='16')
    esip.place(x=80,y=50)
    lasport=Label(top,text='Socket Port:',bg='aliceblue')
    lasport.place(x=0,y=75)
    esport=Entry(top,width='5')
    esport.place(x=80,y=75)
    btokt=Button(top,text='OK',fg='dodgerblue',bg='ivory',activebackground='lightblue',width='18',
                 command=lambda:writ(a=esname.get(),b=esip.get(),c=esport.get()))
    btokt.place(x=30,y=100)

#read
def readinfo():
    f=open('C:\Users\Administrator\Documents\Server Control\Server Info.txt','r')
    for ff in f:
        #print len(ff)
        if len(ff)>1:
            ff=ff.encode(type)
            nameget=ff.split(':')[0].strip('?') #服务器名
            ipget=ff.split(':')[1].split(';')[0] #IP
            portget=ff.split(';')[1] #PORT
            ip[nameget]=ipget
            port[nameget]=portget
            lb.insert(0,nameget.decode(type).encode('utf-8'))

#-----------------------Edit--------------------
def editinfo(a,b,c):
    #print a,b,c
    tempname=''
    tempname+=a
    tempname+=':'
    tempname+=b
    tempname+=';'
    tempname+=c.strip()
    f=open('C:\Users\Administrator\Documents\Server Control\Server Info.txt','r')
    array=[0]*10
    i=0
    for ff in f:
        #print ff
        if len(ff)>1:
            #ff=ff.encode(type)
            if ff.split(':')[1].split(';')[0]==b:
                array[i]=re.sub('\n','',tempname.strip('?'))
            else:
                array[i]=re.sub('\n','',ff.strip('?'))

            i+=1
    f.close()
    #print array
    f=open('C:\Users\Administrator\Documents\Server Control\Server Info.txt','w')
    f.close()
    f=open('C:\Users\Administrator\Documents\Server Control\Server Info.txt','w')
    for j in range(i):
        f.write(array[j]+'\n')
    f.close()
    os.system('taskkill /FI "WINDOWTITLE eq Ser-Edit"')
    lb.delete(0,END)
    readinfo()

#修改服务器UI
def judgeedi():
    if len(lb.curselection())>0:
        edi()
    else:
        flagjudgeedi=tkMessageBox.showinfo(title='Warning',message='未选择有效服务器，请检查后再试')
def edi():
#修改弹窗
    top1=Toplevel()
    top1.title('Ser-Edit')
    top1.geometry('200x135+800+500')
#服务器名
    ftop1=Frame(top1,height='135',width='200',bg='aliceblue')
    ftop1.pack()
    lawarning1=Label(top1,text='Warning:请先与运维沟通后再更改',fg='maroon',bg='aliceblue',width=27)
    lawarning1.place(x=0,y=0)
    lasname1=Label(top1,text='服务器名称:',bg='aliceblue')
    lasname1.place(x=0,y=25)
    esname1=Entry(top1,width='16')
    tempname=lb.get(lb.curselection())
    #print tempname
    esname1.insert(0,tempname.encode('utf-8'))
    esname1.place(x=80,y=25)
    lasip1=Label(top1,text='Socket IP:',bg='aliceblue')
    lasip1.place(x=0,y=50)
    esip1=Entry(top1,width='16')
    #print ip
    #print ip[tempname.encode('GBK')]
    esip1.insert(0,ip[tempname.encode('gbk')])
    esip1.place(x=80,y=50)
    lasport1=Label(top1,text='Socket Port:',bg='aliceblue')
    lasport1.place(x=0,y=75)
    esport1=Entry(top1,width='5')
    esport1.insert(0,port[tempname.encode('gbk')])
    esport1.place(x=80,y=75)
    btokt1=Button(top1,text='OK',fg='dodgerblue',bg='ivory',activebackground='lightblue',width='18',
                 command=lambda:editinfo(a=esname1.get(),b=esip1.get(),c=esport1.get().strip('\n')))
    btokt1.place(x=30,y=100)

#增加服务器UI
def callbackins():
    lb.insert(END,esname.get())

#---------------
def judgedele():
    if len(lb.curselection())>0:
        dele()
    else:
        flagjudgedele=tkMessageBox.showinfo(title='Warning',message='未选择有效服务器，请检查后再试')
def dele():
    temp=lb.get(lb.curselection())
    flagdel=tkMessageBox.askokcancel(title='Warning',message='是否确定删除\'%s\'配置信息？'%temp)
    if flagdel==True:
        f=open('C:\Users\Administrator\Documents\Server Control\Server Info.txt','r')
        array=[0]*10
        i=0
        for ff in f:
            if len(ff)>1:
                #ff=ff.encode(type)
                if ff.split(':')[1].split(';')[0]==ip[temp.encode('GBK')]:
                    array[i]=1
                else:
                    array[i]=ff.strip('?')
                i+=1
        f.close()
        #print array
        f=open('C:\Users\Administrator\Documents\Server Control\Server Info.txt','w')
        f.close()
        f=open('C:\Users\Administrator\Documents\Server Control\Server Info.txt','w')
        for j in range(i):
            if array[j]!=1:
                #print array[j]
                f.write(array[j]+'\n')
        f.close()
        lb.delete(0,END)
        readinfo()

#更新脚本
def updatejava():
    jindu.delete('1.0','2.0')
    jindu.insert(INSERT,ss('banben'))

def helpinfo():
    flaghelp=tkMessageBox.showinfo(title='Help',message='制作者：罗国林(服务器) 李若昊(前端). \n\r遇到bug、使用不便需要修改、甚至想加新功能请联系: 李若昊 \n\r若需要新加本脚本支持的服务器，需要运维支持请联系: 罗国林')




#-----------------------------------------------UI-------------------------------------------------------------------------

root = Tk(className=" Server Control ")
root.geometry('405x163+700+400')
#服务器列表
fser=Frame(root,height='160',width='125',bg='Ivory')
fser.place(x=0,y=0)
lb = Listbox(root,height='7',width='11',bg='ghostwhite')
#for item in ['版署服','台湾测试1服','泰国测试服','马来测试服','韩国测试服','欧美测试服','越南测试服']:
#    lb.insert(END,item)
readinfo()
lb.place(x=18,y=0)
#滚动条
slist=Scrollbar(root)
slist.pack(side=LEFT,fill=Y)
lb['yscrollcommand']=slist.set
slist.config(command=lb.yview)
lb.see(50)
#OK按钮
btok=Button(root,text='OK',fg='dodgerblue',bg='ivory',activebackground='lightblue',height='8',width='2',command=plist)
btok.place(x=100,y=6)
#增加修改删除按钮
btins=Button(root,text='+',fg='dodgerblue',bg='ivory',activebackground='lightblue',anchor='n',command=ins)
btins.place(x=20,y=130)
bted=Button(root,text='Edit',fg='dodgerblue',bg='ivory',activebackground='lightblue',anchor='n',command=judgeedi)
bted.place(x=44,y=130)
btdel=Button(root,text='-',fg='dodgerblue',bg='ivory',activebackground='lightblue',anchor='n',command=judgedele)
btdel.place(x=82,y=130)

#-------服务器状态栏-------------
#状态栏区域
fser=Frame(root,height='51',width='280',bg='Ivory')
fser.place(x=125,y=0)
#服务器时间
lasert=Label(root,text='选中服务器当前时间:',bg='Ivory')
lasert.place(x=127,y=0)
tsert=Text(root,height=1,width=19)
tsert.place(x=245,y=2)
#本地服状态
#labenfu=Label(root,text='本地服:',bg='Ivory')
#labenfu.place(x=125,y=25)
#tbenfu=Text(root,height=1,width=5)
#tbenfu.place(x=170,y=27)
#连服状态
#lalianfu=Label(root,text='连服:',bg='Ivory')
#lalianfu.place(x=230,y=25)
#tlianfu=Text(root,height=1,width=5)
#tlianfu.place(x=265,y=27)
#跨服状态
#lakuafu=Label(root,text='跨服:',bg='Ivory')
#lakuafu.place(x=325,y=25)
#tkuafu=Text(root,height=1,width=5)
#tkuafu.place(x=355,y=27)
#-------设置栏--------
#重启栏区域
fset=Frame(root,height='138',width='280',bg='aliceblue')
fset.place(x=125,y=23)
#更新脚本
laupd=Label(root,text='更新java脚本',bg='aliceblue')
laupd.place(x=125,y=28)
btupd=Button(root,text='更新脚本',fg='dodgerblue',bg='ivory',activebackground='lightblue',height='1',width='10',command=updatejava)
btupd.place(x=320,y=25)
#重启
larst=Label(root,text='重启所选服务器,自动关闭-->启动',bg='aliceblue')
larst.place(x=125,y=58)
btrst=Button(root,text='重启服务器',fg='dodgerblue',bg='ivory',activebackground='lightblue',height='1',width='10',command=callbackre)
btrst.place(x=320,y=56)
#--------改时间区域-----------
fset2=Frame(root,height='64',width='280',bg='aliceblue')
fset2.place(x=125,y=88)
#改时间
laset=Label(root,text='!直接填入时间,自动判断是否需要重启,并完成重启!',fg='maroon',bg='aliceblue')
laset.place(x=128,y=86)
#年月日
eyear=Entry(root,width='4')
eyear.bind('<KeyRelease>',keycheck)
eyear.place(x=128,y=108)
layear=Label(root,text='年',bg='aliceblue')
layear.place(x=159,y=108)
emonth=Entry(root,width='2')
emonth.bind('<KeyRelease>',keycheck)
emonth.place(x=175,y=108)
lamonth=Label(root,text='月',bg='aliceblue')
lamonth.place(x=193,y=108)
eday=Entry(root,width='2')
eday.bind('<KeyRelease>',keycheck)
eday.place(x=208,y=108)
laday=Label(root,text='日',bg='aliceblue')
laday.place(x=225,y=108)
#时分秒
ehour=Entry(root,width='2')
ehour.bind('<KeyRelease>',keycheck)
ehour.place(x=240,y=108)
lahour=Label(root,text='时',bg='aliceblue')
lahour.place(x=257,y=108)
emin=Entry(root,width='2')
emin.bind('<KeyRelease>',keycheck)
emin.place(x=272,y=108)
lamin=Label(root,text='分',bg='aliceblue')
lamin.place(x=289,y=108)
esec=Entry(root,width='2')
esec.bind('<KeyRelease>',keycheck)
esec.place(x=304,y=108)
lasec=Label(root,text='秒',bg='aliceblue')
lasec.place(x=321,y=108)
elist=[eyear,emonth,eday,ehour,emin,esec,0]
#按钮
btts=Button(root,text='修改时间',bg='ivory',fg='dodgerblue',command=callback)
btts.place(x=340,y=104)
#帮助
bthelp=Button(root,text='help',fg='red',width='3',bg='ivory',command=helpinfo)
bthelp.place(x=368,y=134)
#--------进度栏---------
jindu=Text(root,width=25,height=1,bg='aliceblue',bd=0)
jindu.place(x=128,y=135)

n=0
root.mainloop()



