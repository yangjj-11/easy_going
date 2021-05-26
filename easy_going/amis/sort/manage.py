PAGE = {
    "$schema": "http://amis.baidu.com/v1/schemas/page.json#",
    "title": "ADRevenueMonthly",
    "subTitle": "",
    "body": [
        {
            "type": "crud",
            "keepItemSelectionOnPageChange": True,
            "headerToolbar": [
                "filter-toggler",
                "bulkActions",
                {"type": "tpl", "tpl": "当前有 ${count} 条数据。", "className": "v-middle"},
                {"type": "columns-toggler", "align": "right"},
                {"type": "drag-toggler", "align": "right"},
                {"type": "pagination", "align": "right"},
            ],
            "footerToolbar": ["statistics", "switch-per-page", "pagination"],
            "rows": [{"a": "a"}, {"b": "b"}],
            "columns": [
                {
                    "name": "_id",
                    "label": "ID",
                    "sortable": True,
                    "type": "text",
                    "remark": "ID",
                },
                {
                    "name": "channel",
                    "label": "渠道",
                    "sortable": True,
                    "type": "text",
                },
                {
                    "name": "date",
                    "label": "日期",
                    "sortable": True,
                    "type": "text",
                },
                {
                    "name": "revenue",
                    "label": "收入",
                    "sortable": True,
                    "type": "text",
                },
                {
                    "name": "updated_text",
                    "label": "更新时间",
                    "sortable": True,
                    "type": "text",
                    "toggled": True,
                },
                {
                    "name": "created_at",
                    "label": "创建时间",
                    "sortable": True,
                    "type": "datetime",
                    "toggled": True,
                },
            ],
        }
    ],
}
