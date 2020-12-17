### CRM系统:
    - 权限
    - stark组件
    - crm业务
客户管理系统:

- 客户管理
  
    - 客户列表: /customer/list/
    - 添加客户: /customer/add/
    - 删除客户: /customer/del/(?P<cid>\d+)/
    - 修改客户: /customer/edit/(?P<cid>\d+)/
    - 批量导入: /customer/import/
    - 下载模板: /customer/tpl/

- 账单管理

    - 账单列表: /payment/list/
    - 添加账单: /payment/add/
    - 删除账单: /payment/del/(?P<pid>\d+)/
    - 修改账单: /payment/edit/(?P<pid>\d+)/
    
权限信息的录入:

基本权限控制:
  - 登录页面
  - post请求,用户登录检验
  - 获取用户权限存session
  - 中间件对用户权限进行判断,去session中验证,不直接操作数据库,减轻数据库压力
