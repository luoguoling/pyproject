#author:luoguoling
#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
import socket,time,sys,os,commands

from models import Blog
from forms import AddForm
def register(request):
    pass
def socket_send(ip,command):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,1003))
    sock.send(command)
    result = sock.recv(2048)
    sock.close()
    return result
def submit(request):
    if request.method == 'POST':
#        a = request.POST['ip']
        b = request.POST['value']
#        b = u'b'
        print b
        if b == u'更新版本':
            value = 'banben'
            print value
            socket_send(request.POST['ip'],'banben')
            result = socket_send(request.POST['ip'],'banben')
   #     sql = 'C:\Program Files\MySQL\MySQL Server 5.6\bin\mysql.exe -h 120.138.75.88 -P 5849 -u qmrgame -pQmrgame925833 serverlist -e "select * from gameserverinfo"'
   #     result1 = os.popen3(sql)
#        html = '状态%s' % result
            return render_to_response('blog/submit.html',RequestContext(request,{'result':result}))
        elif b == u'重启游戏':
            socket_send(request.POST['ip'],'reboot')
            result = socket_send(request.POST['ip'],'reboot')
            return render_to_response('blog/submit.html',RequestContext(request,{'result':result}))
        elif b == u'当前时间':
            socket_send(request.POST['ip'],'time')
            result = socket_send(request.POST['ip'],'time')
            return render_to_response('blog/submit.html',RequestContext(request,{'result':result}))
        else:
            socket_send(request.POST['ip'],b)
            result = socket_send(request.POST['ip'],b)
            return render_to_response('blog/submit.html',RequestContext(request,{'result':result}))







    return render_to_response('blog/submit.html',RequestContext(request))

def list(request):
    list = Blog.objects.all()
    return render_to_response('blog/list.html',RequestContext(request,{'list':list}))
def add(request):
    if request.method=='POST':
        form = AddForm(request.POST)
        print form
        if form.is_valid():
            blog = form.save()
            return HttpResponseRedirect(reverse('blog_list'))
    return render_to_response('blog/add.html',RequestContext(request,{'form':AddForm()}))
def update(request,id):
    blog = get_object_or_404(Blog,pk=int(id))
    if request.method == 'POST':
        form = AddForm(request.POST,instance=blog)
        if form.is_valid():
            blog = form.save()
            return HttpResponseRedirect(reverse("blog_list"))
    return render_to_response('blog/add.html',RequestContext(request,{'form':AddForm(instance=blog)}))
def delete(request,id):
    blog = get_object_or_404(Blog,pk=int(id))
    blog.delete()
    return HttpResponseRedirect(reverse('blog_list'))




