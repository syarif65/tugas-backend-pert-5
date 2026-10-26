from flask import Blueprint, request
from app.utils.response_helper import success_response, fail_response
from app.repositories import catalog_repository as repo
from app.services.catalog_service import validate_category

category_bp_v1 = Blueprint("categories_v1", __name__, url_prefix="/api/v1/categories")


@category_bp_v1.route("", methods=["GET"])
def get_categories():
    categories = repo.get_categories()
    return success_response({"categories": categories, "total": len(categories)})


@category_bp_v1.route("/<int:category_id>", methods=["GET"])
def get_category(category_id):
    category = repo.get_category(category_id)
    if category is None:
        return fail_response({"category_id": "Kategori tidak ditemukan"}, 404)
    return success_response({"category": category})


@category_bp_v1.route("", methods=["POST"])
def create_category():
    if not request.is_json:
        return fail_response({"content_type": "Header harus application/json"}, 415)
    data = request.get_json(silent=True)
    errors = validate_category(data)
    if errors:
        return fail_response(errors, 400)
    category = repo.create_category(data)
    return success_response({"category": category}, "Kategori berhasil dibuat", 201)


@category_bp_v1.route("/<int:category_id>", methods=["PUT"])
def update_category(category_id):
    if not request.is_json:
        return fail_response({"content_type": "Header harus application/json"}, 415)
    data = request.get_json(silent=True)
    errors = validate_category(data)
    if errors:
        return fail_response(errors, 400)
    category = repo.update_category(category_id, data)
    if category is None:
        return fail_response({"category_id": "Kategori tidak ditemukan"}, 404)
    return success_response({"category": category}, "Kategori berhasil diperbarui")


@category_bp_v1.route("/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    result = repo.delete_category(category_id)
    if result is False:
        return fail_response({"category_id": "Kategori tidak ditemukan"}, 404)
    if result is None:
        return fail_response({"category_id": "Kategori masih memiliki produk dan tidak dapat dihapus"}, 409)
    return success_response({"category_id": category_id}, "Kategori berhasil dihapus")


@category_bp_v1.route("/<int:category_id>/products", methods=["GET"])
def get_category_products(category_id):
    category = repo.get_category(category_id)
    if category is None:
        return fail_response({"category_id": "Kategori tidak ditemukan"}, 404)
    products = repo.get_products(category_id)
    return success_response({
        "category": category,
        "products": products,
        "total": len(products)
    })
