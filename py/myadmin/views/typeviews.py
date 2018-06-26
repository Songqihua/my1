from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from .. models import Classify
import os

# Create your views here.
def getclassifyorder():
    # 获取所有的分类信息
    # tlist = classify.objects.all()

    # select *,concat(path,id) as paths from myadmin_classify order by paths;
    tlist = Classify.objects.extra(select = {'paths':'concat(path,id)'}).order_by('paths')

    for x in tlist:
        if x.pid == 0:
            x.pname = '顶级分类'
        else:
            t = Classify.objects.get(id=x.pid)
            x.pname = t.name
        num  = x.path.count(',')-1
        x.name = (num*'|----')+x.name


    return tlist




def add(request):
    if request.method == 'GET':
        # 返回一个添加的页面

        tlist = getclassifyorder()

        context = {'tlist':tlist}

        return render(request,'myadmin/classify/add.html',context)

    elif request.method == 'POST':
        # 执行分类的添加
        ob = Classify()
        ob.name = request.POST['name']
        ob.pid = request.POST['pid']
        if ob.pid == "0":
            ob.path = '0,'
        else:
            # 根据当前父级id获取path,在添加当前父级id
            t = Classify.objects.get(id=ob.pid)
            ob.path = t.path+str(ob.pid)+','
        ob.save()
        return HttpResponse('<script>alert("添加成功");location.href="'+reverse('myadmin_classify_list')+'"</script>')


        

def index(request):

    

    # 获取搜索条件
    types = request.GET.get('type',None)

    keywords = request.GET.get('keywords',None)
  
    # 判断是否具有搜索条件

    if types:
        # 有搜索条件
        if types == 'all':
            # 全条件搜索
            # select * from user where username like '%aa%' 
            from django.db.models import Q
            tlist = Classify.objects.filter(
                Q(name__contains=keywords)|
                Q(pid__contains=keywords)
            )
        elif types == 'name':
            # 按照分类名搜索
            tlist = Classify.objects.filter(name__contains=keywords)
        
        elif types == 'pid':
            # 按照所属父级搜索
            tlist = Classify.objects.filter(pid__contains=keywords)

    else:
        # 获取所有的用户数据
        tlist = Classify.objects.all()



    for x in tlist:
        if x.pid ==0:
            x.pname = '顶级分类'
        else:
            # print(x.pid,type(x.pid))
            t = Classify.objects.get(id=x.pid)
            x.pname = t.name
    num  = x.path.count(',')-1
    print(num)
    x.name = (num*'|----')+x.name

    # 导入分页类
    from django.core.paginator import Paginator
    # 实例化分页对象,参数1,数据集合,参数2 每页显示条数
    paginator = Paginator(tlist, 10)
    # 获取当前页码数
    p = request.GET.get('p',1)
    # 获取当前页的数据
    t_list = paginator.page(p)

    # tlist=getclassifyorder()
    # 分配数据
    context = {'tlist':t_list,'tl':tlist}

    return render(request,'myadmin/classify/list.html',context)



def delete(request):

    tid = request.GET.get('uid',None)

    # 判断当前类下是否子类
    num = Classify.objects.filter(pid=tid).count()

    if num != 0:
         data = {'msg':'当前类下有子类,不能删除','code':1}
    else:
        # 判断当前类下是否商品,
        ob = Classify.objects.get(id=tid)
        ob.delete()

        data = {'msg':'删除成功','code':0}



    return JsonResponse(data)









# 显示编辑和执行编辑
def edit(request):
    # 接受参数
    uid = request.GET.get('uid',None)
     # 获取对象
    print(uid)
    ob = Classify.objects.get(id=uid)

    if request.method == 'GET':
       
        # 分配数据
        context = {'uinfo':ob}
        # 显示编辑页面
        return render(request,'myadmin/classify/edit.html',context)

    elif request.method == 'POST':
        ob.name = request.POST['name']
        # a=request.POST['name']
        # print(ob.name)
        # return HttpResponse(a)

        ob.save()
        return HttpResponse('<script>alert("更新成功");location.href="'+reverse('myadmin_classify_list')+'"</script>')
   