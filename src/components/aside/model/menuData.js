const menuData = [
  {
    "name": "资产管理",
    "icon": "fa-dashboard",
    "path": "/dashboard/assets",
    "treeview": false,
  },
  {
    "name": "工作流 / 工单",
    "icon": "fa-stack-overflow",
    "path": "/workflow",
    "treeview": false
  },
  {
    "name": "值班表",
    "icon": "fa-calendar-check-o",
    "path": "/schedule",
    "treeview": false
  },
  {
    "name": "部署",
    "icon": "fa-cloud-upload",
    "path": "/deploy",
    "treeview": true,
    "treeviews": [
      {
        "name": "服务部署",
        "path": "/deploy/server_deploy"
      },
      {
        "name": "前端部署",
        "path": "/deploy/fe_deploy"
      },
      {
        "name": "其他部署",
        "path": "/deploy/other_deploy"
      },
      {
        "name": "服务打包",
        "path": "/deploy/quick_pike"
      },
      {
        "name": "文件上传",
        "path": "/deploy/fileupload"
      }
    ]
  },
  {
    "name": "服务",
    "icon": "fa-server",
    "path": "/service",
    "treeview": true,
    "treeviews": [
      {
        "name": "服务信息",
        "path": "/service/service_info"
      },
      {
        "name": "服务配置",
        "path": "/service/service_config"
      },
      {
        "name": "服务命名",
        "path": "/service/service_name"
      }
    ]
  },
  {
    "name": "数据库",
    "icon": "fa-database",
    "path": "databases",
    "treeview": true,
    "treeviews": [
      {
        "name": "mariadb权限",
        "path": "/mysql_grants"
      },
      {
        "name": "token工具",
        "path": "/mysql_tool"
      },
      {
        "name": "mariadb监控",
        "path": "/mysql_status"
      }
    ]
  },
  {
    "name": "设备",
    "icon": "fa-gears",
    "path": "/device",
    "treeview": true,
    "treeviews": [
      {
        "name": "机房信息",
        "path": "/device/server_room"
      },
      {
        "name": "设备信息",
        "path": "/device/device"
      }
    ]
  },
  {
    "name": "计划任务",
    "icon": "fa-tasks",
    "path": "crontable",
    "treeview": true,
    "treeviews": [
      {
        "name": "计划任务管理",
        "path": "/cron"
      },
      {
        "name": "日志",
        "path": "/cronlog"
      }
    ]
  },
  {
   "name": "用户",
    "icon": "fa-users",
    "path": "user",
    "treeview": true,
    "treeviews": [
      {
        "name": "用户信息",
        "path": "/user/user_info"
      },
      {
        "name": "用户管理",
        "path": "/user/user_oversea"
      }
    ]
  },
  {
   "name": "监控与通知",
    "icon": "fa-eye",
    "path": "alarm",
    "treeview": true,
    "treeviews": [
      {
        "name": "告警配置",
        "path": "/alarm_set"
      },
      {
        "name": "告警统计",
        "path": "/alarm_count"
      },
      {
        "name": "交易监控报警",
        "path": "/channelsuccrt"
      }
    ]
  },
  {
   "name": "流量查看",
    "icon": "fa-line-chart",
    "path": "flow_rate",
    "treeview": true,
    "treeviews": [
      {
        "name": "成功率",
        "path": "/succrt"
      },
      {
        "name": "nginx流量",
        "path": "/nginx"
      },
      {
        "name": "PV走势",
        "path": "/nginxpv"
      }
    ]
  },
  {
   "name": "扫码统计",
    "icon": "fa-bar-chart",
    "path": "qrcode",
    "treeview": true,
    "treeviews": [
      {
        "name": "耗时统计",
        "path": "/pay_time"
      },
      {
        "name": "其他统计",
        "path": "/pay_other"
      }
    ]
  },
  {
    "name": "日报查询",
    "icon": "fa-search",
    "path": "/report",
    "treeview": false
  },
  {
    "name": "操作日志",
    "icon": "fa-newspaper-o",
    "path": "/record",
    "treeview": false
  }
  ,
  {
    "name": "链接大全",
    "icon": "fa-link",
    "path": "/links",
    "treeview": false
  },
  {
    "name": "工作流管理",
    "icon": "fa-list-ol",
    "path": "flow",
    "treeview": true,
    "treeviews": [
      {
        "name": "模版管理",
        "path": "/flow/template"
      },
      {
        "name": "步骤管理",
        "path": "/flow/steps"
      }
    ]
  },
  {
    "name": "线下打包",
    "icon": "fa-file-zip-o",
    "path": "off_line_pike",
    "treeview": true,
    "treeviews": [
      {
        "name": "普通打包",
        "path": "/pike"
      }
    ]
  }
]

export default menuData
