from fastapi import FastAPI

import urls
import rl_apis

app = FastAPI()

app.include_router(urls.router, prefix="/sensfix", tags=['Classifier'])
app.include_router(rl_apis.router, prefix="/sensfix", tags=['RL Feedback'])