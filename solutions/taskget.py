from flask import Flask, request

app = Flask(__name__)

@app.route('/testfun')
def test():
    return "this is my first funtion for get"

@app.route('/testfun1')
def test1():
    get_name = request.args.get("get_name") # http://127.0.0.1:5002/testfun1?get_name=shabarish
    mobile_num = request.args.get('mobile')
    mail_id = request.args.get('mail_id')
    return "this is my first funtion for get {} {} {}".format(get_name,mobile_num,mail_id)
    # http://127.0.0.1:5002/testfun1?get_name=shabarish&mobile=12345&mail_id=shabari@mail.com


if __name__=="__main__":
    app.run(port=5002)