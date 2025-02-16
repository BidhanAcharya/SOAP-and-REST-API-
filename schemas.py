from pydantic import BaseModel

## define the schemas to take the input 
class Input(BaseModel):
    firstnumber:int
    secondnumber:int