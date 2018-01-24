const menuData = [
  {
    "name": "资产管理",
    "icon": "fa-dashboard",
    "path": "/assets",
    "treeview": false,
  },
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
]

export default menuData
