from fastapi import HTTPException, Request
from jwt import encode,decode
from fastapi.security import HTTPBearer

class JWTbearer(HTTPBearer):
  async  def __call__(self, request:Request):
        auth= await super().__call__(request)
        data =validate_token(auth.credentials)
        if data['email']!='admin@gmail.com':
            raise HTTPException(status_code=403, detail='las credenciales son incorrectas')
         
    
def create_token(data:dict):
   token:str= encode(payload=data,key="my_secret_key",algorithm="HS256")
   return token

def validate_token(token:str)->dict:
    data: dict =decode(token,key="my_secret_key",algorithms=["HS256"])
    return data