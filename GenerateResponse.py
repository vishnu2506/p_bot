from flask import jsonify


def generateResponse(data, msg):
    response_data = {}
    data_list = []
    try:
        for i in data:
            temp = {}
            temp["ord_id"] = i[0]
            temp["p_var"] = i[1]
            temp["p_size"] = i[2]
            temp["addr"] = i[3]
            temp["ph_no"] = i[4]
            temp["status"] = i[5]
            data_list.append(temp)
            response_data["data"] = data_list

        response_data["msg"] = msg
        print(f"Respone data : {response_data}")
        return jsonify(response_data)
    except IndexError as e:
        print(e)
        return str(e)

