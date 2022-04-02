from flask import Flask, request, jsonify
from flask_restful import Resource
from middleware import checkAuth


class WakeUp(Resource):
    path = '/wake-up'

    def get(self):
        authResponse = checkAuth(request)
        if (not authResponse['ok']):
            return authResponse, 401
        response = jsonify({})

        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
