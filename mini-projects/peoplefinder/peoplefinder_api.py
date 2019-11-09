'''
The module contains REST API definition and implementation of a simple 
peoplefinder along with server that works both on HTTP and HTTPS. The 
implementation is based on Flask and has CRUD operations (create, read, 
update and delete). A search interface that searches a set of attributes
is given
'''
from flask import Flask, jsonify

peoplefinder = Flask(__name__)
peoplefinder_port = 8000
peoplefinder_api_name = 'peoplefinder'
peoplefinder_desc = 'A Simple People Finder'
peoplefinder_api_version = '1.0'
peoplefinder_root_url = '/peoplefinder'


@peoplefinder.route(f'{peoplefinder_root_url}/{peoplefinder_api_version}', methods=['GET'])
def peoplefinder_description():
    return jsonify({'app_name': peoplefinder_api_name,
                    'description': peoplefinder_desc,
                    'version': peoplefinder_api_version})

if __name__ == '__main__':
    print(f'Running Server {peoplefinder}')
    peoplefinder.run(port=peoplefinder_port)