from fastapi import FastAPI
from schemas import Input
app = FastAPI()

## Add two numbers
@app.post("/add_two_numbers")
async def rest_implementation(input : Input):
    a=input.firstnumber
    b=input.secondnumber
    c=a+b
    print("The sum of two number is ",c)
    return {
        "sum of two number is ":c
    }

    



