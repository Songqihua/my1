from django.db import models

# Create your models here.
# 会员模型
class Users(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=80)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11,null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=1,null=True)
    pic = models.CharField(max_length=100,null=True)
    # 0 正常  1禁用 
    status = models.IntegerField(default=0)
    addtime = models.DateTimeField(auto_now_add=True)
    class Meta:
    # 指定生成权限
        permissions = (
            ("show_users", "查看会员管理"),
            ("insert_users", "添加会员"),
            ("edit_users", "修改会员"),
            ("del_users", "删除会员"),
        )
# 会员地址
class Address(models.Model):
    uid =  models.ForeignKey(to="Users", to_field="id")
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=20)
    xiangxi = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
    class Meta:
        # 指定生成权限
        permissions = (
            ("show_address", "查看地址管理"),
            ("insert_address", "添加地址"),
            ("edit_address", "修改地址"),
            ("del_address", "删除地址"),
        )

# 商品分类模型
class Classify(models.Model):
    '''
    无限分类
        classify
            id   name  pid  path
            1     服装  0    0,
            2     男装  1    0,1,
            3     西服  2    0,1,2,
            4     西裤  3    0,1,2,3,
    '''
    name = models.CharField(max_length=20)
    pid = models.IntegerField()
    path = models.CharField(max_length=50)

    class Meta:
        # 指定生成权限
        permissions = (
            ("show_cslassify", "查看商品分类管理"),
            ("insert_cslassify", "添加商品分类"),
            ("edit_cslassify", "修改商品分类"),
            ("del_cslassify", "删除商品分类"),
        )
# 商品模型
class  Goods(models.Model):
    # 一对多
    typeid =  models.ForeignKey(to="Classify", to_field="id")#类别id
    title = models.CharField(max_length=255)#商品名称
    descr = models.CharField(max_length=255,null=True)#简介
    info = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)#价格
    pics = models.CharField(max_length=100)#图片名
    # 0 新发布,1下架
    status = models.CharField(max_length=50,default='在售')#状态
    store = models.IntegerField(default=0)#库存量
    num = models.IntegerField(default=0)#被购买数量
    clicknum = models.IntegerField(default=0)#点击次数
    addtime = models.DateTimeField(auto_now_add=True)#添加时间
    class Meta:
        # 指定生成权限
        permissions = (
            ("show_goods", "查看商品管理"),
            ("insert_goods", "添加商品"),
            ("edit_goods", "修改商品"),
            ("del_goods", "删除商品"),
        )

# 订单模型
class Orders(models.Model):
    uid = models.ForeignKey(to="Users", to_field="id")
    addressid = models.ForeignKey(to="Address", to_field="id")
    totalprice = models.FloatField()
    totalnum = models.IntegerField()
    status = models.CharField(max_length=50)
    addtime = models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
        # 指定生成权限
        permissions = (
            ("show_orders", "查看订单管理"),
            ("insert_orders", "添加订单"),
            ("edit_orders", "修改订单"),
            ("del_orders", "删除订单"),
        )

# 订单详情
class OrderInfo(models.Model):
    orderid = models.ForeignKey(to="Orders", to_field="id")
    gid = models.ForeignKey(to="Goods", to_field="id")
    num = models.IntegerField()





class Citys(models.Model):
    # id name upid 
    name = models.CharField(max_length=100)
    upid = models.IntegerField()

    # myhome_citys
    class Meta():
        db_table = 'citys'