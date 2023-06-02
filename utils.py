import re
import json
from datetime import datetime
from sqlalchemy import inspect


def validate_email(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pat, s):
        return True
    else:
        return False


def validate(input_data):
    if not input_data:
        return {"status": False,
                "message": "No Data found"}
    try:
        data = json.loads(input_data)
        if len(data) == 0:
            return {"status": False, "message": "No data in the array"}
    except ValueError as e:
        return {"status": False,
                "message": "Data is not valid"}
    return {"status": True,
            "message": data}


def validate_req_data(data, req_keys):
    for k in req_keys:
        if k not in data.keys():
            return {"status": False,
                    "message": str(k) + ' key is not available'}
        elif not data[k]:
            return {"status": False,
                    "message": str(k) + ' is not available'}
    return {"status": True,
            "message": data}


def date_now():
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date


def response(data, code, message, error):
    return {
        "data": data,
        "code": code,
        "message": message,
        "error": error
    }


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}
