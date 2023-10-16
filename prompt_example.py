import re

from dependencies import (
    db, collection_val, collection_cl1_name,
    collection_cl2_name, collection_ticket, collection_resp
    )

cl1 = db.get_collection(collection_cl1_name)
cl2 = db.get_collection(collection_cl2_name)
ticket = db.get_collection(collection_ticket)
response = db.get_collection(collection_resp)
valid_complaint = db.get_collection(collection_val)

def convert_data_to_str(data):
    template = """
{label}:
{data}
"""
    
    prmpt_text = []
    for k,v in data.items():
        label = "/".join(k.split("_"))
        data = "\n".join(v)
        res = template.format(label=label, data=data)
        prmpt_text.append(res)
        
    return ("\n".join(prmpt_text))

def convert_ticket_data_to_str(data):
    template = """
    {label}:
    {data}
    """
    
    prmpt_text = []
    for k,v in data.items():
        data = "\n".join(v)
        res = template.format(label=k, data=data)
        prmpt_text.append(res)
        
    return ("\n".join(prmpt_text))

def convert_response_data_to_str(data):
    template = """
    Complaint: {complaint}:
    Response: {response}
    """
    
    prmpt_text = []
    for cmp, resp in data:
        res = template.format(complaint=cmp, response=resp)
        prmpt_text.append(res)
        
    return ("\n".join(prmpt_text))

def get_valid():
    data = valid_complaint.find(projection={"_id":0, "cmp_id":0})
    data = data[0]

    return convert_data_to_str(data)
    

def get_category_l1():
    data = cl1.find(projection={"_id":0, "cmp_id":0})
    data = data[0]

    return convert_data_to_str(data)

def get_category_l2(category_lst):
    data = cl2.find(projection={"_id":0, "cmp_id":0})    
    data = data[0]
    
    res = ""
    for cat in category_lst:
        cat = re.sub("[^a-zA-Z]*", "", cat)
        cat_ex = data[cat.lower()]
        res += convert_data_to_str({cat: cat_ex})
    
    return res

def get_ticket():
    data = ticket.find(projection={"_id":0, "cmp_id":0})
    data = data[0]
    return convert_ticket_data_to_str(data)

def get_response(category):
    data = response.find(projection={"_id":0, "cmp_id":0})
    data = data[0]
    
    category = category.lower()
    res = convert_response_data_to_str(data[category])
    return res


def get_category_l1_cat(category):
    data = cl1.find(projection={"_id":0, "cmp_id":0})
    data = data[0]
    return data[category]