from flask import Flask, request, redirect, jsonify
from urllib.parse import urlparse
from app.cache_store import RedisCacheStore as cache
from app.dbpool import DB
from app.url_generator import URLGenerator

import config


app = Flask(__name__)



@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form.get('url')

    # Check if URL already in cache
    short_url = cache().get_value(original_url)


    if short_url is  None:
        resp = DB().get_tiny_url(original_url)
        if resp['success']:
            short_url = cache().set_value(original_url, resp['message'], config.EXPIRY)
        else:
            resp = URLGenerator().generate_short_code(original_url, config.CONVERSION_METHOD)
            if resp['success']:
                short_url = resp['message']
                resp = DB().save_tiny_url(long_url=original_url, short_url=resp['message'])
                if not resp['success']:
                    return f"Error : {resp['message']}", 500
                cache().set_value(original_url, resp['message'], config.EXPIRY)
            else:
                return f"Error : {resp['message']}", 500
            
    return jsonify({'short_url': short_url})




@app.route('/<short_code>', methods=['GET'])
def redirect_to_original(short_code):
    original_url = cache().get_value(short_code)

    if original_url is  None:
        resp = DB().get_long_url(short_code)

        if resp['success']:
            original_url = cache().set_value(short_code, resp['message'], config.EXPIRY)
            original_url = resp['message']
        else:
            return "URL not found", 404

    if original_url:
        return redirect(original_url, code=302)
    else:
        return "URL not found", 404



@app.route('/metrics/top_domains', methods=['GET'])
def top_domains():
    resp = DB().get_top_three_api()
    if resp['success']:
        data = resp['message'].most_common(3)
        result = {domain: count for domain, count in data}
        return jsonify(result)
    else:
        return jsonify(resp['message'])



@app.route('/original',  methods=['POST','GET'])
def origional_url():
    return jsonify({"message":"Response from original url from same domain"})