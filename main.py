from typing  import List

from fastapi import BackgroundTasks, FastAPI
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse

from controller import generate_otp

class EmailSchema(BaseModel):
    # email: List[EmailStr]
    email: EmailStr

config = ConnectionConfig(
    MAIL_USERNAME="rakesrcciit",
    MAIL_PASSWORD="iqot tkho nscl frer",
    MAIL_FROM="rakesrcciit@gmail.com",
    MAIL_PORT="465",
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

app : FastAPI = FastAPI(
    title="FastAPi email verification system",
    version="0.1.0"
)

# generating otp

otp = generate_otp()

html = f"""
    <h1> Thanks for subscribed {app.version} and your OTP is {otp}</p>
"""

@app.get("/", name="root")
def root():
    return {"message": f"Hello World version-{app.version}"}

@app.post("/email")
async def sample_mail(email : EmailSchema) -> JSONResponse:
    print(f"mail is {email}")
    message = MessageSchema(
        subject="Sample mail form FastAPI",
        # recipients=email.model_dump().get("email"),  # if you want to send same email different multiple account at a time.
        recipients=[email.email],
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(config=config)
    await fm.send_message(message=message)
    return JSONResponse(
        status_code=200,
        content={
            "message" : "email has been sent..!"
        }
    )