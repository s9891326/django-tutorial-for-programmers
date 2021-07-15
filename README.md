# 午餐系統

## outline
1. [說明需求](說明需求)
1. [Require](require)
1. [架構說明](架構說明)
1. [Heroku部屬](heroku部屬)
1. [重新上板步驟](重新上板步驟)
1. [API文件](api文件)
1. [待解決事項](待解決事項)

### 說明需求

### require

### 架構說明
#### Django rest framework
- 本專案使用Django rest framework進行開發
#### JWT Token
- 為登入驗證機制。保存期限為1天，提供token刷新功能。
- 登入成功後要在Header內帶入`Authorization: JWT <token>`，才能順利完成後續API呼叫
- `api-token-auth/`: 登入token驗證接口
- `api-token-refresh/`: token刷新接口

### Heroku部屬
- [參考](https://github.com/s9891326/django-tutorial-for-programmers-uranusjr/blob/1.8/24-deploy-to-heroku.md)

#### 重新上板步驟
- `git add -u`(把更新的東西都加進來) 
- `git commit -m "message"`
- `heroku login`: 會跳出一個UI介面讓你登入
- `git push heroku master`
- `heroku open`

### API文件
- 皆須在Header內加入JWT token(`Authorization: JWT <token>`)

<details>
<summary>Store(GET)</summary>

- 獲取所有店家及店家菜單

    | 項目 | 說明 |
    |------|-----|
    | API URL | {server_domain}/store/api/store/ |
    | method | GET(階層資料) |

- Request: 無

- Response

    | 欄位 | 資料類型 | 說明 |
    |------|---------|------|
    | id | integer | 店家ID |
    | name | string | 店家名稱 |
    | notes | string | 店家說明 |
    | owner | integer | 使用者ID |
    | menu_items | array | 菜單清單 ，包含name、price |
    | menu_items.name | string | 菜單名稱 |
    | menu_items.price | integer | 菜單價格 |

- Response Example

```json
[
    {
        "id": 1,
        "menu_items": [
            {
                "name": "大碗",
                "price": 140
            },
            {
                "name": "中碗",
                "price": 130
            },
            {
                "name": "小碗",
                "price": 120
            }
        ],
        "name": "台北-黑庄牛肉麵",
        "notes": "超好吃~ 一定要吃看看",
        "owner": 1
    }
]
```

</details>

<details>
<summary>Store(POST)</summary>

- 新增店家及店家菜單

    | 項目 | 說明 |
    |------|-----|
    | API URL | {server_domain}/store/api/store/ |
    | method | POST(階層資料) |

- Request

    | 欄位 | 資料類型 | 說明 |
    |------|---------|------|
    | name | string | 店家名稱 |
    | notes | string | 店家說明 |
    | owner | integer | 使用者ID |
    | menu_items | array | 菜單清單 ，包含name、price |
    | menu_items.name | string | 菜單名稱 |
    | menu_items.price | integer | 菜單價格 |

- Response

    | 欄位 | 資料類型 | 說明 |
    |------|---------|------|
    | id | integer | 店家ID |
    | name | string | 店家名稱 |
    | notes | string | 店家說明 |
    | owner | integer | 使用者ID |
    | menu_items | array | 菜單清單 ，包含name、price |
    | menu_items.name | string | 菜單名稱 |
    | menu_items.price | integer | 菜單價格 |

- Request Example

```json
{
    "name": "postman",
    "notes": "postman notes",
    "owner": "1",
    "menu_items": [
        {
            "name": "postman1",
            "price": 1
        },
        {
            "name": "postman2",
            "price": 2
        }
    ]
}
```

- Response Example

```json
{
    "id": 2,
    "menu_items": [
        {
            "name": "postman1",
            "price": 1
        },
        {
            "name": "postman2",
            "price": 2
        }
    ],
    "name": "postman",
    "notes": "postman notes",
    "owner": 1
}
```

</details>

<details>
<summary>Store(PUT)</summary>

- 新增店家及店家菜單

    | 項目 | 說明 |
    |------|-----|
    | API URL | {server_domain}/store/api/store/ |
    | method | POST(階層資料) |

- Request

    | 欄位 | 資料類型 | 說明 |
    |------|---------|------|
    | name | string | 店家名稱 |
    | notes | string | 店家說明 |
    | owner | integer | 使用者ID |
    | menu_items | array | 菜單清單 ，包含name、price |
    | menu_items.name | string | 菜單名稱 |
    | menu_items.price | integer | 菜單價格 |

- Response

    | 欄位 | 資料類型 | 說明 |
    |------|---------|------|
    | id | integer | 店家ID |
    | name | string | 店家名稱 |
    | notes | string | 店家說明 |
    | owner | integer | 使用者ID |
    | menu_items | array | 菜單清單 ，包含name、price |
    | menu_items.name | string | 菜單名稱 |
    | menu_items.price | integer | 菜單價格 |

- Request Example

```json
{
    "name": "postman",
    "notes": "postman notes",
    "owner": "1",
    "menu_items": [
        {
            "name": "postman1",
            "price": 1
        },
        {
            "name": "postman2",
            "price": 2
        }
    ]
}
```

- Response Example

```json
{
    "id": 2,
    "menu_items": [
        {
            "name": "postman1",
            "price": 1
        },
        {
            "name": "postman2",
            "price": 2
        }
    ],
    "name": "postman",
    "notes": "postman notes",
    "owner": 1
}
```

</details>

<details>
<summary>Store(DEL)</summary>

- 刪除店家及店家菜單

    | 項目 | 說明 |
    |------|-----|
    | API URL | {server_domain}/store/api/store/{store_id}/ |
    | method | DEL |

- Request: 無

- Response: 無

</details>

### 待解決事項
1. rest api post
    - [Writable nested serializers](https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers)
2. bug
