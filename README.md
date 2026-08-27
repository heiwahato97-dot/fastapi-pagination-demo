# FastAPI Pagination Demo

FastAPIでPagination、Filtering、Sortingを実装するデモです。

## 概要

商品一覧APIに対して、以下の機能を実装しています。

- Pagination（ページ分割）
- Filtering（条件による絞り込み）
- Sorting（並び替え）

大量のデータを扱うAPIでよく使われる一覧取得処理の基本を確認します。

## 使用技術

- Python
- FastAPI
- Uvicorn
- Query Parameters

## API

### GET `/products`

商品一覧を取得します。

使用できるQuery Parameter:

```text
page
limit
min_price
max_price
sort
```

## Pagination

`page` と `limit` を使用して、取得する範囲を指定します。

例:

```text
GET /products?page=2&limit=5
```

計算:

```python
start = (page - 1) * limit
end = start + limit
```

レスポンスには現在のページ情報も含めます。

```json
{
  "total": 12,
  "page": 2,
  "limit": 5,
  "items": []
}
```

## Filtering

価格の下限・上限を指定できます。

```text
GET /products?min_price=5000&max_price=10000
```

条件:

```text
price >= min_price
price <= max_price
```

`total` には絞り込み後の件数が入ります。

## Sorting

価格による並び替えができます。

昇順:

```text
sort=price_asc
```

降順:

```text
sort=price_desc
```

## 機能の組み合わせ

Pagination、Filtering、Sortingは同時に使用できます。

例:

```text
GET /products?page=1&limit=2&min_price=5000&max_price=15000&sort=price_desc
```

処理順序:

```text
全データ
   ↓
Filtering
   ↓
Sorting
   ↓
Pagination
   ↓
Response
```

FilteringをPaginationより先に行うことで、全データから条件に一致した結果を取得したあと、その結果をページ分割できます。

## Query Validation

FastAPIの `Query` を使用して値を制限しています。

```python
page: int = Query(default=1, ge=1)

limit: int = Query(
    default=5,
    ge=1,
    le=20
)
```

これにより、不正なページ番号や極端に大きなlimitを防止できます。

## セットアップ

```bash
python -m venv .venv
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 学習ポイント

- Pagination
- Filtering
- Sorting
- Query Parameters
- Query Validation
- Python List Slicing
- `sorted()`
- `lambda`
- API一覧取得設計
- Filtering → Sorting → Pagination の処理順序