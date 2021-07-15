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

<details>
<summary>Store(GET)</summary>

- 獲取所有店家及店家菜單

| 項目 | 說明 |
|------|-----|
| API URL | {server_domain}/store/api/store/ |
| method | GET(階層資料) |

- Request
1. JWT token

- Response

| 欄位 | 名稱 | 資料類型 | 說明 |
|------|-----|---------|------|
| id | 店家ID | integer | |
| name | 店家名稱 | string | |
| notes | 店家說明 | string | |
| owner | 使用者ID | integer | |
| menu_items | 菜單清單 | array | |
| menu_items.name | 菜單名稱 | string | |
| menu_items.price | 菜單價格 | integer | |

</details>

### 待解決事項
1. rest api post
    - [Writable nested serializers](https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers)
2. bug
