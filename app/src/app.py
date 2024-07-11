# from flask import Flask, request, make_response

# app = Flask(__name__)


# @app.route('/')
# def index():
#     content = "It's easier to ask forgiveness than it is to get permission."
#     fwd_for = "X-Forwarded-For: {}".format(
#         request.headers.get('X-Forwarded-For', None)
#     )
#     real_ip = "X-Real-IP: {}".format(
#         request.headers.get('X-Real-IP', None)
#     )
#     fwd_proto = "X-Forwarded-Proto: {}".format(
#         request.headers.get('X-Forwarded-Proto', None)
#     )

#     output = "\n".join([content, fwd_for, real_ip, fwd_proto])
#     response = make_response(output, 200)
#     response.headers["Content-Type"] = "text/plain"

#     return response


###########################################################################


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    It's easier to ask forgiveness than it is to get permission.<br>
    X-Forwarded-For: {request.headers.get('X-Forwarded-For')}<br>
    X-Real-IP: {request.headers.get('X-Real-IP')}<br>
    X-Forwarded-Proto: {request.headers.get('X-Forwarded-Proto')}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
