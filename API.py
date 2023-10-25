import mysql.connector
from flask import request, Flask, jsonify

app = Flask(__name__)
connected_server = mysql.connector.connect(user='root', password='1234',
                                           host='localhost',
                                           database='onlinelibrary')

@app.route('/role/get', methods=['GET'])
def get_role():
    id = request.args.get('Id_role')
    if (int(id) >= 0 and not None):
        request_id = (f"SELECT * FROM roles WHERE RoleId = {id}")
        cursor_request = connected_server.cursor()
        cursor_request.execute(request_id)
        result = cursor_request.fetchall()

        return jsonify(result), 200

    else:
        return "The id you entered was not found", 404


@app.route('/role/post', methods=['POST'])
def post_role():
    title_role = request.args.get('Title_role')
    request_roles = (f"SELECT * FROM roles")
    post_cursor = connected_server.cursor()
    post_cursor.execute(request_roles)
    result = post_cursor.fetchall()

    for role in result:
        if role["RoleTitle"] == title_role:
            return f"Quote with title {title_role} already exists",401

    insert_new_role = "INSERT INTO roles (RoleId, RoleTitle) VALUES (%s, %s)"
    new_data_role = (len(result)-1, title_role)
    post_cursor.execute(insert_new_role, new_data_role)
    connected_server.commit()

    return "SUCCESSFUL", 200

@app.route('/role/put', methods=['PUT'])
def put_role():
    title_role = request.args.get('Title_role')
    id_changed_role = request.args.get('Id_role')
    request_roles = (f"SELECT * FROM roles")
    put_cursor = connected_server.cursor()
    put_cursor.execute(request_roles)
    result = put_cursor.fetchall()

    for role in result:
        if role['RoleId'] == id_changed_role:
            delete_requast = f"DELETE FROM roles WHERE RoleId == {id_changed_role}"
            put_cursor.execute(delete_requast)
            connected_server.commit
            insert_changed_role = "INSERT INTO roles (RoleId, RoleTitle) VALUES (%s, %s)"
            changed_data_role = (id_changed_role, title_role)
            put_cursor.execute(insert_changed_role, changed_data_role)
            connected_server.commit()

            return f"SUCCESSFUL change role id = {id_changed_role}", 200

    insert_changed_role = "INSERT INTO roles (RoleId, RoleTitle) VALUES (%s, %s)"
    changed_data_role = (id_changed_role, title_role)
    put_cursor.execute(insert_changed_role, changed_data_role)
    connected_server.commit()

    return "SUCCESSFUL create role", 201

@app.route('/role/delete', methods=['DELETE'])
def delete_role():
    id_delete_role = request.args.get('id_role')
    request_roles = (f"SELECT * FROM roles")
    put_cursor = connected_server.cursor()
    put_cursor.execute(request_roles)
    result = put_cursor.fetchall()
    for role in result:
        if role["RoleId"] == id_delete_role:
            delete_requast = f"DELETE FRO M roles WHERE RoleId == {id_delete_role}"
            put_cursor.execute(delete_requast)
            connected_server.commit
            return f"role has id {id_delete_role} delete", 200
    return "role not found", 404

def ApiStart():
    if __name__ == '__main__':
        app.run()

ApiStart()





