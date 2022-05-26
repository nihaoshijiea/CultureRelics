from flask import Flask, request
import json
from flask import jsonify
from Entity.Suggestion import Suggestion as Suggestion
from Dao.SuggestionDao import Suggestion_Dao
import time
from flask_cors import *


app = Flask(__name__)

CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/send_suggestion', methods=['POST'])
def add_suggestion():
    suggestion = Suggestion()
    suggestion_dao = Suggestion_Dao()
    json_data = request.json

    suggestion.letter_headline = json_data['Letter_headLine']
    suggestion.letter_information = json_data['Letter_information']
    suggestion.letter_type = json_data['Letter_type']
    suggestion.occupation = json_data['Occupation']
    suggestion.subdistrict = json_data['Subdistrict']
    suggestion.telephone = json_data['Telephone']
    suggestion.user_id = json_data['User_ID']
    suggestion.user_name = json_data['User_name']
    suggestion.user_sex = json_data['User_sex']
    suggestion.Id = str(time.time())
    suggestion.set_param_dict()
    suggestion_dao.save_entity(suggestion)
    res = jsonify(
        {'code' : 0,
         'msg' : "success",
         "id" : str(suggestion.Id)
         })
    # print(request.headers)
    # print(request.form)
    # print(request.form['name'])
    # print(request.form.getlist('name'))
    # print(request.form.get('nickname', default='little apple'))
    # do something else
    #
    #
    return res

@app.route('/get_suggestion', methods=['POST'])
def get_suggestion():
    # suggestion = Suggestion()
    suggestion_dao = Suggestion_Dao()
    json_data = request.json
    Id = json_data["Id"]
    suggestion = suggestion_dao.get_entity_rewrite(Id)

    return suggestion

@app.route('/get_suggestion_count', methods=['POST'])
def get_suggestion_count():
    suggestion_dao = Suggestion_Dao()
    print(suggestion_dao.get_count())
    return suggestion_dao.get_count()

@app.route('/get_rand_suggestion', methods=['POST'])
def get_rand_suggestion():
    suggestion_dao = Suggestion_Dao()
    res = suggestion_dao.rand_get()
    return res


@app.route('/get_all_suggestion', methods=['POST'])
def get_all_suggestion():
    suggestion_dao = Suggestion_Dao()
    res = suggestion_dao.get_all()
    return res


@app.route('/get_suggestion_by_key', methods=['POST'])
def get_suggestion_by_key():
    json_data = request.json
    key = json_data['key']
    key_value = json_data['key_value']
    suggestion_dao = Suggestion_Dao()
    res = suggestion_dao.get_by_key(key=key, key_value=key_value)
    return res


@app.route('/delete_suggestion_by_id', methods=['POST'])
def delete_suggestion_by_id():
    json_data = request.json
    Id = json_data['Id']
    suggestion_dao = Suggestion_Dao()
    res = suggestion_dao.delete_by_id(Id)
    res = jsonify(
        {'code': res,
         'msg': "success",
         })
    return res


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=9999, debug=True)

