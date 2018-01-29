const menuData = [
  {
   "name": "区域组管理",
    "icon": "fa-users",
    "path": "/group_list",
    "treeview": false,
  },
  {
    "name": "会员管理",
    "icon": "fa-users",
    "path": "/accounts",
    "treeview": true,
    "treeviews": [
      {
        "name": "会员信息",
        "path": "/accounts/user_list"
      },
      {
        "name": "角色管理",
        "path": "/accounts/role_list"
      }
    ]
  },
  {
    "name": "推介资产管理",
    "icon": "fa-dashboard",
    "path": "/assets",
    "treeview": true,
    "treeviews": [
      {
        "name": "资产信息",
        "path": "/assets/assets_list"
      },
      {
        "name": "资产种类管理",
        "path": "/assets/category_list"
      }
    ]
  },
]

export default menuData
