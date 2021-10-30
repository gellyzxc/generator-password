import json
from flask import Flask
from Password import Password

app = Flask(__name__)


@app.route('/pg/<count_symbols>')
def generate_password(count_symbols):
    password = Password()
    if count_symbols.isdigit():
        password.generate(int(count_symbols))
    else:
        password.generate(None)
    
    response = app.response_class(
        response=json.dumps({
            "version": '0.0.5',
            "smblsarray": f'{len(password.get_array_symbols())}',
            "smbls": f'{password.get_array_symbols()}',
            "pwd": f'{password.password}',
        }),
        status=200,
        mimetype='application/json'

    )

    return response


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
