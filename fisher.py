from app import create_app

__author__ = '0x1un'

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5001, threaded=True)
