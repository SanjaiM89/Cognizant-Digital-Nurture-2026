from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)

SERVICES = {
    'courses': 'http://127.0.0.1:5001',
    'students': 'http://127.0.0.1:5002',
}


@app.route(
    '/api/<resource>',
    defaults={'path': ''},
    methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
    strict_slashes=False,
)
@app.route('/api/<resource>/<path:path>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def proxy(resource, path):
    if resource not in SERVICES:
        return jsonify({'error': f'Unknown service for resource: {resource}'}), 404

    target_url = f'{SERVICES[resource]}/api/{resource}/{path}'

    headers = {}
    if 'Content-Type' in request.headers:
        headers['Content-Type'] = request.headers['Content-Type']

    try:
        response = requests.request(
            method=request.method,
            url=target_url,
            headers=headers,
            json=request.get_json(silent=True),
            params=request.args,
            timeout=5,
        )
    except requests.exceptions.ConnectionError:
        return jsonify({'error': f'{resource} service is unavailable'}), 503

    return Response(
        response.content,
        status=response.status_code,
        content_type=response.headers.get('Content-Type', 'application/json'),
    )


if __name__ == '__main__':
    app.run(port=5000)
