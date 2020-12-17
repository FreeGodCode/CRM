# url: /customer/list/
def customer_list(request):
    """客户列表"""
    pass


# url: /customer/add/
def customer_add(request):
    """添加客户"""
    pass


# url: /customer/edit/(?P<cid>\d+)/
def customer_edit(request):
    """修改客户"""
    pass


# url: /customer/del/(?P<cid>\d+)/
def customer_del(request):
    """删除客户"""
    pass


# url: /customer/import/
def customer_import(request):
    """批量导入"""
    pass


# url: /customer_tp/
def customer_tpl(request):
    """下载模板"""
    pass