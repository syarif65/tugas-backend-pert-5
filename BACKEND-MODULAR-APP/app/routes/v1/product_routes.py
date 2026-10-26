from flask import Blueprint, request
from app.utils.response_helper import success_response, fail_response
from app.repositories import catalog_repository as repo
from app.services.catalog_service import validate_product

product_bp_v1 = Blueprint("products_v1", __name__, url_prefix="/api/v1/products")


@product_bp_v1.route("", methods=["GET"])
def get_products():
    category_value = request.args.get("category_id")
    category_id = None
    if category_value is not None:
        try:
            category_id = int(category_value)
            if category_id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return fail_response({"category_id": "Field category_id harus berupa bilangan bulat positif"}, 400)
        if repo.get_category(category_id) is None:
            return fail_response({"category_id": "Kategori tidak ditemukan"}, 404)
    products = repo.get_products(category_id)
    return success_response({"products": products, "total": len(products)})


@product_bp_v1.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = repo.get_product(product_id)
    if product is None:
        return fail_response({"product_id": "Produk tidak ditemukan"}, 404)
    return success_response({"product": product})


@product_bp_v1.route("", methods=["POST"])
def create_product():
    if not request.is_json:
        return fail_response({"content_type": "Header harus application/json"}, 415)
    data = request.get_json(silent=True)
    errors = validate_product(data)
    if errors:
        return fail_response(errors, 400)
    product = repo.create_product(data)
    return success_response({"product": product}, "Produk berhasil dibuat", 201)


@product_bp_v1.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    if not request.is_json:
        return fail_response({"content_type": "Header harus application/json"}, 415)
    data = request.get_json(silent=True)
    errors = validate_product(data)
    if errors:
        return fail_response(errors, 400)
    product = repo.update_product(product_id, data)
    if product is None:
        return fail_response({"product_id": "Produk tidak ditemukan"}, 404)
    return success_response({"product": product}, "Produk berhasil diperbarui")


@product_bp_v1.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    deleted = repo.delete_product(product_id)
    if not deleted:
        return fail_response({"product_id": "Produk tidak ditemukan"}, 404)
    return success_response({"product_id": product_id}, "Produk berhasil dihapus")
