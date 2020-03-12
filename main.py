from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/menus', methods=["POST"])
def menus():
    req_data = request.get_json(silent=True, cache=False, force=True)
    name = req_data['name']
    print(name)
    f = open("menus.txt", 'r')
    lines = f.readlines()
    menus = []

    if name == "99분식":
        search = lines[1:3]
    elif name == "뚝담":
        search = lines[5:6]
    for index, line in enumerate(search):

        line = line.split(",")
        print(line)
        menu = {}
        menu['key'] = line[0]
        menu['menu'] = line[1]
        menu['price'] = line[2]
        menu['url'] = line[3][:-1]
        menus.append(menu)

    f.close()
    print(menus)

    return jsonify(menus)


@app.route('/store', methods=["POST"])
def stores():
    stores = ['99분식', '뚝담']
    return jsonify(stores)
if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.8', threaded=True)
