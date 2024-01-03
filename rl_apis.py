from fastapi import APIRouter
from enum import Enum
from pydantic import BaseModel

from dependencies import (
    db, collection_ticket, collection_cl1_name,
    collection_cl2_name, collection_resp, collection_val
    )

#loading the collections
ticket_collection = db.get_collection(collection_ticket)
response_collection = db.get_collection(collection_resp)
category_l1_collection = db.get_collection(collection_cl1_name)
category_l2_collection = db.get_collection(collection_cl2_name)
valid_comp_collection = db.get_collection(collection_val)

router = APIRouter()

# Defining datatypes
class Complaint(Enum):
    comp = "complete"
    incomp = "incomplete"  

class ComplaintL1(Enum):
    elec_it = "electrical_it"
    its_tech_elec = "it-support_technician_electrician"
    clean_jan = "cleaning_janitorial"
    plumber_main = "plumber_maintenance-engineer"
    build_infra = "building_infrastructure"
    sec = "security"
    fr_ff = "first-responder_fire-fighter"
    sec_g_sur_saf = "security-guard_surveillance-personnel_safety-officer"
    hm_recep_admin = "hospitality-manager_receptionist_admin"
    
class ComplaintL2(Enum):
    elec = "electrical"
    it = "it"
    it_support = "it-support"
    electrician = "electrician"
    tech = "technician"
    clean = "cleaning"
    jan = "janitorial"
    plumber = "plumber"
    maint_eng = "maintenance-engineer"
    build = "building"
    infra = "infrastructure"
    sec = "security"
    fr = "first-responder"
    ff = "fire-fighter"
    sec_guard = "security-guard"
    surv_pers = "surveillance-personnel"
    saf_off = "safety-officer"
    hosp_mng = "hospitality-manager"
    recep = "receptionist"
    adm = "admin"
    
class Ticket(Enum):
    ticket = "ticket"
    not_tick = "not_ticket"

# Defining the Input Schmas for the API
class InpComplaint(BaseModel):
    text: str
    correct_class: Complaint
    
class InpComplaintL1(BaseModel):
    text:str
    correct_class: ComplaintL1
    
    
class InpComplaintL2(BaseModel):
    text:str
    correct_class: ComplaintL2
    
class InpResp(BaseModel):
    complaint_text: str
    complaint_response: str
    complaint_class: ComplaintL2
    
class InptTicket(BaseModel):
    text: str
    correct_class: Ticket

# creating routes
@router.post("/complaint_is_complete")
async def is_complete_complaint(cmp: InpComplaint):
    """
    endpoint to update the valid complaint type(complete/incomplete)
    """
    valid_comp_collection.update_one({"cmp_id":1}, {"$push": {cmp.correct_class.value: cmp.text}}, upsert=True)
    
    return {
        "response": "updated record successfully"
    }

@router.post("/complaint_l1_type")
async def classify_complaint(cmp: InpComplaintL1):
    """
    endpoint to update the correct level 1 category of the complaint
    """
    category_l1_collection.update_one({"cmp_id":1}, {"$push": {cmp.correct_class.value: cmp.text}}, upsert=True)
    
    return {
        "response": "updated record successfully"
    }
    
@router.post("/complaint_l2_type")
async def classify_complaint2(cmp: InpComplaintL2):
    """
    endpoint to update the correct level 2 category of the complaint
    """
    category_l2_collection.update_one({"cmp_id":1}, {"$push": {cmp.correct_class.value: cmp.text}}, upsert=True)
    
    return {
        "response": "updated record successfully"
    }
    
    
@router.post("/complaint_response")
async def complaint_response(cmp: InpResp):
    """
    endpoint to update the correct response for complaint with the correct category
    """
    response_collection.update_one({"cmp_id":1},
                                   {"$push": {cmp.complaint_class.value: [cmp.complaint_text,
                                                                    cmp.complaint_response]}},
                                   upsert=True)
    
    return {
        "response": "updated record successfully"
    }
    

@router.post("/ticket_clf")
async def classify_ticket(cmp: InptTicket):
    """
    endpoint to update the correct ticket type of the complaint
    """
    ticket_collection.update_one({"cmp_id":1}, {"$push": {cmp.correct_class.value: cmp.text}}, upsert=True)
    
    return {
        "response": "updated record successfully"
    }