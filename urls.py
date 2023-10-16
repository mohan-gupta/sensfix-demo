from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

from dependencies import response_chain

from mongo_conn import db

ticket_collection = db["ticket"]
response_collection = db["response"]
category_l1_collection = db["category_l1"]
category_l2_collection = db["category_l2"]
valid_comp_collection = db["valid_complaint"]

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
async def complaint_response(cmp: Complaint):
    res = response_chain.run(cmp.text)
    res = res.replace("Response:", "").strip()
    
    return {
        "response": res
    }
    

@router.post("/ticket_clf")
async def classify_ticket(cmp: Complaint):
    correct_class = cmp.correct_classification.lower()
    ticket_collection.update_one({"cmp_id":1}, {"$push$": {correct_class: cmp.text}}, upsert=True)
    
    return {
        "response": "updated record successfully"
    }
    
app.include_router(router, prefix="/sensfix", tags=['Sensfix'])