__author__ = "0x1un"

from flask import Flask, make_response


app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])
@app.route('/hello')
def hello():
    # the function will return status code and content-type<http, headers>
    # content-type default return text/html
    headers = {
            #  'content-type': 'text/plain',
            'content-type': 'application/json',
            'location': 'https://google.com'
            }
    #  response = make_response('<html></html>', 404)
    #  response.headers = headers
    return "<h1>Hello, Flask.</h1>", 301, headers
    #  return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5001)
