from flask import Flask
from app.utils.response_helper import success_response, fail_response, error_response
from app.routes.v1 import category_bp_v1, product_bp_v1


def create_app():
    app = Flask(__name__)

    app.register_blueprint(category_bp_v1)
    app.register_blueprint(product_bp_v1)

    @app.route("/", methods=["GET"])
    def home():
        return success_response({
            "name": "Backend Modular API",
            "version": "1.0.0",
            "api_version": "v1",
            "api_prefix": "/api/v1"
        }, "Backend API aktif dan berjalan")

    @app.errorhandler(404)
    def not_found(error):
        return fail_response({"uri": "Endpoint tidak ditemukan"}, 404)

    @app.errorhandler(405)
    def method_not_allowed(error):
        return fail_response({"method": "Metode HTTP tidak diizinkan"}, 405)

    @app.errorhandler(500)
    def internal_server_error(error):
        return error_response("Terjadi kesalahan internal server", 500)

    return app
