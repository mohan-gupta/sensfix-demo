from fastapi import FastAPI

import clf_api
import rl_apis

#initializing the app
# app = FastAPI(openapi_prefix="/sensfix_demo")
app = FastAPI()

#adding endpoints from clf_api.py
app.include_router(clf_api.router, prefix="/sensfix", tags=['Classifier'])
#adding endpoints from rl_apis.py
app.include_router(rl_apis.router, prefix="/sensfix", tags=['RL Feedback'])
