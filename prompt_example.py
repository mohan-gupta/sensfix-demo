import re

#importing the database and collection names
from dependencies import (
    db, collection_val, collection_cl1_name,
    collection_cl2_name, collection_ticket, collection_resp
    )

#loading the collections
cl1 = db.get_collection(collection_cl1_name)
cl2 = db.get_collection(collection_cl2_name)
ticket = db.get_collection(collection_ticket)
response = db.get_collection(collection_resp)
valid_complaint = db.get_collection(collection_val)

def l1_category_lst():
    """
    Function to get the list of level 1 categories
    """
    res = cl1.find(projection={"_id":0, "cmp_id":0})
    res = res[0]
    
    return tuple(res.keys())

def l2_category_lst():
    """
    Function to get the list of level 1 categories
    """
    res = cl2.find(projection={"_id":0, "cmp_id":0})
    res = res[0]
    
    return tuple(res.keys())

def convert_data_to_str(data):
    """
    Function to convert input data into string
    """
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
    """
    Function to convert the ticket examples into string
    """
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
    """
    Function to convert response examples into string
    """
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
    """
    Function to fetch all the examples of complete and incomplete complaints from the valid_complaint collection
    """
    data = valid_complaint.find(projection={"_id":0, "cmp_id":0})
    data = data[0]

    return convert_data_to_str(data)
    

def get_category_l1():
    """
    Function to fetch all the examples of category level 1 from the cl1 collection
    """
    data = cl1.find(projection={"_id":0, "cmp_id":0})
    data = data[0]

    return convert_data_to_str(data)

def get_category_l2():
    """
    Function to fetch all the data from the cl2 collection
    """   
    data = cl2.find(projection={"_id":0, "cmp_id":0})    
    data = data[0]
    return data

def get_category_l2_eg(l2_data, category_lst):
    """
    Function to fetch all the examples of a category from the cl2 collection
    """    
    res = ""
    for cat in category_lst:
        cat = re.sub("[^a-zA-Z]*", "", cat)
        cat_ex = l2_data[cat.lower()]
        res += convert_data_to_str({cat: cat_ex})
    
    return res

def get_ticket():
    """
    Function to fetch all the examples of ticket and not ticket from the ticket collection
    """
    data = ticket.find(projection={"_id":0, "cmp_id":0})
    data = data[0]
    return convert_ticket_data_to_str(data)

def get_response():
    data = response.find(projection={"_id":0, "cmp_id":0})
    data = data[0]
    
    return data

def get_response_eg(response_data, category):
    """
    Function to fetch all the examples of responses for a category from the response collection
    """    
    category = category.lower()
    res = convert_response_data_to_str(response_data[category])
    return res