from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

from dependencies import (
    db, collection_ticket, collection_cl1_name,
    collection_cl2_name, collection_resp, collection_val
    )

ticket_collection = db.get_collection(collection_ticket)
response_collection = db.get_collection(collection_resp)
category_l1_collection = db.get_collection(collection_cl1_name)
category_l2_collection = db.get_collection(collection_cl2_name)
valid_comp_collection = db.get_collection(collection_val)

app = FastAPI()

router = APIRouter()

class Complaint(BaseModel):
    text: str
    correct_classification: str
    
class Complaint2(BaseModel):
    text: str
    base_type: str

@router.post("/complaint_is_complete")
async def is_complete_complaint(cmp: Complaint):
    correct_class = cmp.correct_classification.lower()
    valid_comp_collection.update_one({"cmp_id":1}, {"$push$": {correct_class: cmp.text}}, upsert=True)
    
    return {
        "response": "updated record successfully"
    }

@router.post("/complaint_type")
async def classify_complaint(cmp: Complaint):
    correct_class = cmp.correct_classification.lower()
    category_l1_collection.update_one({"cmp_id":1}, {"$push$": {correct_class: cmp.text}}, upsert=True)
    
    return {
        "response": "updated record successfully"
    }
    
@router.post("/complaint_type2")
async def classify_complaint2(cmp: Complaint2):
    correct_class = cmp.correct_classification.lower()
    category_l2_collection.update_one({"cmp_id":1}, {"$push$": {correct_class: cmp.text}}, upsert=True)
    
    return {
        "response": "updated record successfully"
    }
    
    
@router.post("/complaint_response")
async def complaint_response(cmp: Complaint2):
    correct_class = cmp.correct_classification.lower()
    response_collection.update_one({"cmp_id":1}, {"$push$": {correct_class: cmp.text}}, upsert=True)
    
    return {
        "response": "updated record successfully"
    }
    

@router.post("/ticket_clf")
async def classify_ticket(cmp: Complaint):
    correct_class = cmp.correct_classification.lower()
    ticket_collection.update_one({"cmp_id":1}, {"$push$": {correct_class: cmp.text}}, upsert=True)
    
    return {
        "response": "updated record successfully"
    }
    
app.include_router(router, prefix="/sensfix", tags=['Sensfix'])