from flask import Blueprint, request, jsonify
from db import session
from models.explosive_model import Explos
from models.hostage_model import Hostage
from consumer_to_mongo.all_messages import get_collection



bp_query = Blueprint("query",__name__)


@bp_query.route('/by_email',   methods=['GET'])
def get_all_messages_by_email():
    data = request.get_json()
    email = data['email']
    if not email:
        return jsonify({"error": "Email parameter is required"}), 400
    collection = get_collection()

    result = collection.find({"email": email})
    messages = []
    for message in result:
        message["_id"] = str(message["_id"])
        messages.append(message)


    return jsonify({"messages": messages}), 200


@bp_query.route("/by_froud_email", methods=["GET"])
def get_all_messages_by_forged_email():
    data = request.get_json()
    email1 = data['email']
    all_ho = session.query(Hostage).filter_by(email=email1)
    messages_ho = [message.to_dict() for message in all_ho]
    all_ex = session.query(Explos).filter_by(email=email1)
    messages_ex = [message.to_dict() for message in all_ex]
    return jsonify({"hostage_messages": messages_ho, "explos_messages": messages_ex}), 200





@bp_query.route("/world_by_email", methods=["GET"])
def get_all_messages_by_hostage_name():
    data = request.get_json()
    email = data["email"]
    my_dict = {}
    all_ho = session.query(Hostage).filter_by(email=email)
    messages_ho = [message.to_dict() for message in all_ho]
    all_ex = session.query(Explos).filter_by(email=email)
    messages_ex = [message.to_dict() for message in all_ex]
    all_messages = messages_ex + messages_ho
    sentences = [message['sentences'] for message in all_messages]
    tst = " ".join(sentences)
    cleaned_text = tst.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ')
    words = cleaned_text.split()
    for letter in words:
        if letter not in my_dict:
            my_dict[letter] = 0
        my_dict[letter] += 1
    return jsonify({"world_messages": my_dict}), 200


@bp_query.route('/world_of_all', methods=['GET'])
def get_all_messages_by_email_and_world_frequency():
    list_world_connect = ["the","what","them","to"]
    my_dict = {}
    all_ho = session.query(Hostage)
    messages_ho = [message.to_dict() for message in all_ho]

    all_ex = session.query(Explos)
    messages_ex = [message.to_dict() for message in all_ex]

    conn = get_collection()
    result = conn.find()
    messages = []
    for message in result:
        message["_id"] = str(message["_id"])
        messages.append(message['sentences'])
    mesmes = []
    for i in messages:
        for letter in i:
            s = letter.split(' ')
            for j in s:
                mesmes.append(j)
    for i in mesmes:
        if i in list_world_connect:
            mesmes.remove(i)
    for i in mesmes:
        if i not in my_dict:
            my_dict[i] = 0
        my_dict[i] += 1

    all_messages = messages_ex + messages_ho
    sentences = [message['sentences'] for message in all_messages]
    tst = " ".join(sentences)
    cleaned_text = tst.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ')
    words = cleaned_text.split()
    for i in words:
        if i in list_world_connect:
            words.remove(i)
    for letter in words:
        if letter not in my_dict:
            my_dict[letter] = 0
        my_dict[letter] += 1
    max_val = max(my_dict.values())
    res = list(filter(lambda x: my_dict[x] == max_val, my_dict))
    return jsonify({"world": res,"value":max_val}), 200

