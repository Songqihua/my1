from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse

from .. models import Users
import os

# Create your views here.
# 会员列表
def index(request):

    # 获取所有的用户数据
    userlist = Users.objects.filter()
    #获取搜索条件
    types = request.GET.get('type',None)
    keywords = request.GET.get('keywords',None)

    # 判断是否具有搜索条件
    if types:
        # 有搜索条件
            # 全条件搜索
        if types == 'all':
            from django.db.models import Q
            userlist = Users.objects.filter(
                Q(username__contains=keywords)|
                Q(age__contains=keywords)|
                Q(email__contains=keywords)|
                Q(phone__contains=keywords)|
                Q(sex__contains=keywords)
            )
            # 按照username搜索
        elif types =='username':
            userlist = Users.objects.filter(username__contains=keywords)
            # 按照age搜索
        elif types =='age':
            userlist = Users.objects.filter(age__contains=keywords)
            # 按照email搜索
        elif types =='email':
            userlist = Users.objects.filter(email__contains=keywords)
            # 按照phone搜索
        elif types =='phone':
            userlist = Users.objects.filter(phone__contains=keywords)
            # 按照sex搜索
        elif types =='sex':
            userlist = Users.objects.filter(sex__contains=keywords)



    else:
        # 获取所有的用户数据
        userlist = Users.objects.filter()

    # 导入分页类
    from django.core.paginator import Paginator
    # 实例化分页对象，参数为一，数据集合，参数为二，每页显示条数
    paginator = Paginator(userlist,10)
    
    # 获取当前页码数
    p = request.GET.get('p',1)

    # 获取当前页的数据

    ulist = paginator.page(p)



    # 分配数据
    context = {'userlist':ulist,}
    
    # 加载模板
    return render(request,'myadmin/user/list.html',context)
# 会员添加
def add(request):

    if request.method =='GET':

        # 显示添加页面
        return render(request,'myadmin/user/add.html')


    elif request.method =='POST':
        # e 
        try:
            # 接受表单的提交数据
            data = request.POST.copy().dict()
            # 删除csrf验证字段
            del data['csrfmiddlewaretoken']

            # 进行密码加密
            from django.contrib.auth.hashers import make_password, check_password
            data['password'] = make_password(data['password'], None, 'pbkdf2_sha256')

            # 进行会员头像上传
            if request.FILES.get('pic',None):
                data['pic'] = uploads(request)
                if data['pic'] == 1:
                    return HttpResponse('<script>alert("上传错误");location.href="'+reverse('myadmin_user_add')+'"</script>')
            else:
                del data['pic']



            # 执行用户的创建
            ob = Users.objects.create(**data)
            return HttpResponse('<script>alert("添加成功");location.href="'+reverse('myadmin_user_list')+'"</script>')
        except:
            return HttpResponse('<script>alert("添加失败");location.href="'+reverse('myadmin_user_add')+'"</script>')
            

def delete(request):
    try:
        uid = request.GET.get('uid',None)
        ob = Users.objects.get(id=uid)

        # 判断当前用户是否右头像,如果右则删除
        if ob.pic:
            # /static/pics/
            os.remove('.'+ob.pic)

        ob.delete()

        data = {'msg':'删除成功','code':0}
    except:
        data = {'msg':'删除失败','code':1}

    return JsonResponse(data)

# 执行文件的上传
def uploads(request):
    
    # 获取请求中的 文件 File 
    myfile = request.FILES.get('pic',None)

    # 获取上传的文件后缀名 myfile.name.split('.').pop()
    p = myfile.name.split('.').pop()
    arr = ['jpg','png','jpeg','gif']
    if p not in arr:
        return 1

    import time,random
    # 生成新的文件名
    filename = str(time.time())+str(random.randint(1,99999))+'.'+p
    
    # 打开文件
    destination = open("./static/pics/"+filename,"wb+")

    # 分块写入文件  
    for chunk in myfile.chunks():      
       destination.write(chunk)  

    # # destination.write(myfile.read()) #不推荐

    # 关闭文件
    destination.close()
    
    # return HttpResponse(filename)

    return '/static/pics/'+filename


# # 显示编辑和执行编辑
def edit(request):
    # 接受参数
    uid = request.GET.get('uid',None)
    if not uid:
        return HttpResponse('<script>alert("没有数据返回返回上一页");location.href="'+reverse('myadmin_user_list')+'"</script>')

    # 获取对象
    ob = Users.objects.get(id=uid)

    if request.method == 'GET':
       
        # 分配数据
        context = {'uinfo':ob}
        # 显示编辑页面
        return render(request,'myadmin/user/edit.html',context)

    elif request.method == 'POST':

        try:
            # 判断是否上传了新的图片
            if request.FILES.get('pic',None):
                # 判断是否使用的默认图
                if ob.pic:
                    # 如果使用的不是默认图,则删除之前上传的头像
                    os.remove('.'+ob.pic)

                # 执行上传
                ob.pic = uploads(request)
                

            ob.username = request.POST['username']
            ob.email = request.POST['email']
            ob.age = request.POST['age']
            ob.sex = request.POST['sex']
            ob.phone = request.POST['phone']
            ob.save()

            return HttpResponse('<script>alert("更新成功");location.href="'+reverse('myadmin_user_list')+'"</script>')
        except:
            return HttpResponse('<script>alert("更新失败");location.href="'+reverse('myadmin_user_edit')+'?uid='+str(ob.id)+'"</script>')

