from fastapi import FastAPI, Query


app = FastAPI()


products = [
    {"id": 1, "name": "Keyboard", "price": 5000},
    {"id": 2, "name": "Mouse", "price": 3000},
    {"id": 3, "name": "Monitor", "price": 25000},
    {"id": 4, "name": "USB Cable", "price": 1000},
    {"id": 5, "name": "Webcam", "price": 8000},
    {"id": 6, "name": "Headset", "price": 6000},
    {"id": 7, "name": "Laptop Stand", "price": 4500},
    {"id": 8, "name": "Microphone", "price": 12000},
    {"id": 9, "name": "Speaker", "price": 7000},
    {"id": 10, "name": "Desk Light", "price": 3500},
    {"id": 11, "name": "Docking Station", "price": 15000},
    {"id": 12, "name": "External SSD", "price": 18000},
]


@app.get("/products")
def get_products(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=5, ge=1, le=20),
    min_price: int | None = Query(default=None, ge=0),
    max_price: int | None = Query(default=None, ge=0),
    sort: str | None = Query(default=None)
):
    filtered_products = products

    if min_price is not None:
        filtered_products = [
            product
            for product in filtered_products
            if product["price"] >= min_price
        ]

    if max_price is not None:
        filtered_products = [
            product
            for product in filtered_products
            if product["price"] <= max_price
        ]

    if sort == "price_asc":
        filtered_products = sorted(
            filtered_products,
            key=lambda product: product["price"]
        )

    elif sort == "price_desc":
        filtered_products = sorted(
            filtered_products,
            key=lambda product: product["price"],
            reverse=True
        )

    start = (page - 1) * limit
    end = start + limit

    items = filtered_products[start:end]

    return {
        "total": len(filtered_products),
        "page": page,
        "limit": limit,
        "items": items
    }