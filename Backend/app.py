from flask import Flask, request, jsonify, send_from_directory, url_for
from flask_cors import CORS
import InterfaceFunctions
import os

# Initial App
app = Flask(__name__, static_folder='../Frontend', template_folder='../Frontend')
CORS(app)

#   Hosting Setting APIs
@app.route('/')
def serve_index():
    return send_from_directory(app.template_folder, 'MainPage.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

#   Frontend APIs
# route for file uploads
@app.route('/api/upload_data', methods=['POST'])
def upload_data():
    msg, index = InterfaceFunctions.upload_data()
    return jsonify(msg), index

@app.route('/api/delete_data', methods=['POST'])
def delete_data():
    msg, index = InterfaceFunctions.delete_data()
    return jsonify(msg), index

@app.route('/api/get_doc_list', methods=['POST'])
def get_doc_list():
    msg, index = InterfaceFunctions.get_doc_list()
    return jsonify(msg), index

@app.route('/api/get_doc_data', methods=['POST'])
def get_doc_data():
    msg, index = InterfaceFunctions.get_doc_data()
    return jsonify(msg), index

# Debug - check static folders
@app.route('/list-static-files', methods=['GET'])
def list_static_files():
    static_folder = app.static_folder
    file_structure = {}
    for root, dirs, files in os.walk(static_folder):
        relative_path = os.path.relpath(root, static_folder)
        folder_name = relative_path if relative_path != '.' else 'root'
        file_structure[folder_name] = {
            'folders': dirs,
            'files': files
        }
    return jsonify(file_structure)

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)