from flask import jsonify


def success_response(data=None, message=None, code=200):
    response = {"status": "success"}
    if message:
        response["message"] = message
    if data is not None:
        response["data"] = data
    return jsonify(response), code


def fail_response(errors, code=400):
    return jsonify({"status": "fail", "errors": errors}), code


def error_response(message="Terjadi kesalahan internal server", code=500):
    return jsonify({"status": "error", "message": message}), code
