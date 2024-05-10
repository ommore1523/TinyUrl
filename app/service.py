from flask import Flask, request, redirect, jsonify
from urllib.parse import urlparse
from app.cache_store import RedisTokenStore as cache
from app.dbpool import DB
from app.url_generator import URLGenerator
import config


app = Flask(__name__)



@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('url')

    # Check if URL already in cache
    short_url = cache().get_value(original_url)

    if short_url is not None:
        short_url = short_url[original_url]
    else:
        resp = DB().get_tiny_url(original_url)
        if resp['success']:
            short_url = cache().set_value(original_url, resp['message'], config.EXPIRY)
        else:
            short_url = URLGenerator.generate_short_code(original_url)
            cache().set_value(original_url, resp['message'], config.EXPIRY)

    return jsonify({'short_url': short_url})


@app.route('/<short_code>')
def redirect_to_original(short_code):
    short_url = cache().get_value(original_url)
    if short_url is not None:
        original_url = short_url[original_url]
    else:
        resp = DB().get_long_url(short_url)

        if resp['success']:
            original_url = cache().set_value(short_url, resp['message'], config.EXPIRY)

    if original_url:
        return redirect(original_url, code=302)
    else:
        return "URL not found", 404


