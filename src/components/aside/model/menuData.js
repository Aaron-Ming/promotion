const menuData = [
  {
   "name": "区域组管理",
    "icon": "fa-users",
    "path": "/group_list",
    "treeview": false,
    "roleLevel": 1
  },
  {
    "name": "会员管理",
    "icon": "fa-users",
    "path": "/accounts",
    "treeview": true,
    "roleLevel": 3,
    "treeviews": [
      {
        "name": "会员信息",
        "path": "/accounts/user_list",
        "roleLevel": 3
      }
    ]
  },
  {
    "name": "推介资产管理",
    "icon": "fa-dashboard",
    "path": "/assets",
    "treeview": true,
    "roleLevel": 3,
    "treeviews": [
      {
        "name": "资产信息",
        "path": "/assets/assets_list",
        "roleLevel": 3
      },
      {
        "name": "资产种类管理",
        "path": "/assets/category_list",
        "roleLevel": 3
      }
    ]
  },
]

export default menuData
