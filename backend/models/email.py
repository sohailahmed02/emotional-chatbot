from pydantic import BaseModel, Field, EmailStr


class emailid(BaseModel):
    emailid  : EmailStr = Field(...) 