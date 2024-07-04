from typing  import List

from fastapi import BackgroundTasks, FastAPI
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse

class EmailSchema(BaseModel):
    email: List[EmailStr]

config = ConnectionConfig(
    MAIL_USERNAME="rakesrcciit@gmail.com",
    MAIL_PASSWORD="rakesh@1227",
    MAIL_FROM="rakesrcciit@gmail.com",
    MAIL_PORT="1227",
    MAIL_SERVER="mail server",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

app : FastAPI = FastAPI(
    title="FastAPi email verification system",
    version="0.1.0"
)

html = """
    <p> Thanks for subscribe</p>
"""

@app.get("/", name="root")
def root():
    return {"message": f"Hello World {app.version}"}