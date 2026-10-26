from app.repositories import catalog_repository as repo


def validate_category(data):
    if not isinstance(data, dict):
        return {"body": "Body harus berupa objek JSON"}

    errors = {}
    name = data.get("name")
    if not isinstance(name, str) or not name.strip():
        errors["name"] = "Field name wajib diisi dan harus berupa teks"

    description = data.get("description", "")
    if not isinstance(description, str):
        errors["description"] = "Field description harus berupa teks"
    return errors


def validate_product(data):
    if not isinstance(data, dict):
        return {"body": "Body harus berupa objek JSON"}

    errors = {}
    name = data.get("name")
    if not isinstance(name, str) or not name.strip():
        errors["name"] = "Field name wajib diisi dan harus berupa teks"

    price = data.get("price")
    if isinstance(price, bool) or not isinstance(price, (int, float)) or price <= 0:
        errors["price"] = "Field price harus berupa angka lebih besar dari 0"

    stock = data.get("stock")
    if isinstance(stock, bool) or not isinstance(stock, int) or stock < 0:
        errors["stock"] = "Field stock harus berupa bilangan bulat minimal 0"

    category_id = data.get("category_id")
    if isinstance(category_id, bool) or not isinstance(category_id, int) or category_id <= 0:
        errors["category_id"] = "Field category_id harus berupa bilangan bulat positif"
    elif repo.get_category(category_id) is None:
        errors["category_id"] = "Kategori tidak ditemukan"
    return errors
