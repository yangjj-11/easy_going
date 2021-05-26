PAGE = {
    "type": "page",
    "title": "YJJ Management",
    "subTitle": "这是子标题",
    "remark": "这是小提示信息",
    "aside": {
        "type": "wrapper",
        "size": "xs",
        "className": "",
        "body": {
            "type": "nav",
            "stacked": True,
            "links": [
                {
                    "label": "SORT",
                    "children": [
                        {"label": "Activity", "to": "/admin/app/activity"},
                        {"label": "Debugger", "to": "/admin/app/debugger"},
                        {"label": "Release", "to": "/admin/app/release"},
                    ],
                },
            ],
        },
    },
}
