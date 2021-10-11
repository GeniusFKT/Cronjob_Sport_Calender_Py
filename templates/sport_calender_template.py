def get_database_template(title_text: str, parent_page_id: str):
    body = {
        "icon": {
            "type": "emoji",
            "emoji": "👟"
        },
        "title": [
            {
                "type": "text",
                "text": {
                    "content": title_text,
                },
                "plain_text": title_text,
            }
        ],
        "properties": {
            "Date": {
                "date": {}
            },
            "👟你今天运动了吗": {
                "checkbox": {}
            },
            "yc早起否": {
                "checkbox": {}
            },
            "yc早睡否": {
                "checkbox": {}
            },
            "penny早起否": {
                "checkbox": {}
            },
            "penny早睡否": {
                "checkbox": {}
            },
            "运动类型": {
                "multi_select": {
                    "options": [
                        {
                            "name": "乒乓球",
                            "color": "yellow"
                        },
                        {
                            "name": "台球",
                            "color": "pink"
                        },
                        {
                            "name": "走路",
                            "color": "orange"
                        },
                        {
                            "name": "剧本杀",
                            "color": "gray"
                        },
                        {
                            "name": "跑步",
                            "color": "brown"
                        },
                        {
                            "name": "健身",
                            "color": "red"
                        },
                        {
                            "name": "游泳",
                            "color": "green"
                        }
                    ]
                }
            },
            "备注": {
                "title": {}
            }
        },
        "parent": {
            "type": "page_id",
            "page_id": parent_page_id
        }
    }

    return body


def get_item_template(database_id: str, start_date: str):
    body = {
        "parent": {
            "database_id": database_id
        },
        "properties": {
            "Date": {
                "date": {
                    "start": start_date
                }
            }
        }
    }

    return body
