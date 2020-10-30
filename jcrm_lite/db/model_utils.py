
from flask import jsonify


def jsonify_list(model_list):
    result = list(map(lambda c: c.to_dict(), model_list))
    return jsonify(result)


def jsonify_one(model):
    return jsonify(model.to_dict())
