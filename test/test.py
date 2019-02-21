from flask import Flask, current_app

app = Flask(__name__)

# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask AppContext
# Request RequestContext
#离线应用 单元测试

# this is context managers
with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']
    print(d)


class MyResource:

    def __enter__(self):
        print("connect to resource.")
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if tb:
            print('process exception.')
        else:
            print('no exception')
        print("close resource connetction.")

        return True

    def query(self):
        print("query data.")


with MyResource() as resource:
    resource.query()
