categories = [
    {"id": 1, "name": "Elektronik", "description": "Produk elektronik"},
    {"id": 2, "name": "Aksesori", "description": "Aksesori komputer"},
]

products = [
    {"id": 1, "category_id": 1, "name": "Laptop Pro", "price": 15000000, "stock": 5},
    {"id": 2, "category_id": 2, "name": "Mechanical Keyboard", "price": 850000, "stock": 10},
]


def get_categories():
    return categories


def get_category(category_id):
    return next((c for c in categories if c["id"] == category_id), None)


def create_category(data):
    new_id = max((c["id"] for c in categories), default=0) + 1
    category = {
        "id": new_id,
        "name": data["name"].strip(),
        "description": data.get("description", "").strip(),
    }
    categories.append(category)
    return category


def update_category(category_id, data):
    category = get_category(category_id)
    if category is None:
        return None
    category["name"] = data["name"].strip()
    category["description"] = data.get("description", category["description"]).strip()
    return category


def delete_category(category_id):
    category = get_category(category_id)
    if category is None:
        return False
    if any(p["category_id"] == category_id for p in products):
        return None
    categories.remove(category)
    return True


def get_products(category_id=None):
    if category_id is None:
        return products
    return [p for p in products if p["category_id"] == category_id]


def get_product(product_id):
    return next((p for p in products if p["id"] == product_id), None)


def create_product(data):
    new_id = max((p["id"] for p in products), default=0) + 1
    product = {
        "id": new_id,
        "category_id": data["category_id"],
        "name": data["name"].strip(),
        "price": data["price"],
        "stock": data["stock"],
    }
    products.append(product)
    return product


def update_product(product_id, data):
    product = get_product(product_id)
    if product is None:
        return None
    product.update({
        "category_id": data["category_id"],
        "name": data["name"].strip(),
        "price": data["price"],
        "stock": data["stock"],
    })
    return product


def delete_product(product_id):
    product = get_product(product_id)
    if product is None:
        return False
    products.remove(product)
    return True
