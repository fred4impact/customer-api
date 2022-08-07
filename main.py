from typing import List
from fastapi import FastAPI, HTTPException
from uuid import UUID  #uuid4
from models import Customer, CustomerUpdate

app = FastAPI()

db: List[Customer] = [
    Customer(
        customer_id = UUID("828e8662-386e-466e-8f95-a19ae9560eae"),
        first_name = "John",
        last_name = "HAAY",
        phone = "8086543900",
        city = "Essex",
        state = "London", 
        postcode = "wc1 2Ch",
        email = "joh.h@gmail.com"
    ),

    Customer(
        customer_id = UUID("59c8b180-7409-446f-87a4-18d37869aed8"),
        first_name = "Ray",
        last_name = "Joshep",
        phone = "000987654",
        city = "Canary Wahrf",
        state = "London", 
        postcode = "C1N 341",
        email = "ray@gmail.com"
    ),
]


@app.get("/")
def index():
      return{"Message": "Welcome to FASTAPI Customre Resources"}


@app.get("/api/v1/customers")
async def fetch_customers():
    return db;


@app.post("/api/v1/customers")
async def create_customer(customer: Customer):
    db.append(customer)
    return {"customerid": customer.customer_id};


@app.delete("/api/v1/customers/{customer_id}")
async def delete_customer(customer_id: UUID):
    for customer in db: 
        if customer.customer_id == customer_id:
            db.remove(customer)
            return 
    raise HTTPException(
    status_code=404,detail=f"Customer with customerId:{customer_id} does not exists"
) 

    

@app.put("/api/v1/customers/{customer_id}")
async def update_customer(customer_update: CustomerUpdate, customer_id: UUID):
   for customer in db:
        if customer.customer_id == customer_id:
           if customer_update.first_name is not None:
               customer.first_name  =  customer_update.first_name
           if customer_update.last_name is not None:
               customer.last_name = customer_update.last_name 
           if customer_update.phone is not None:
               customer.phone =customer_update.phone 
           if customer_update.city is not None:
               customer.city=customer_update.city 
           if customer_update.state is not None:
               customer.state=customer_update.state 
           if customer_update.email is not None:
               customer.email = customer_update.email 
           return 
   raise HTTPException(
    status_code=404, detail=f"Customer with customerId:{customer_id} does not exists"
)       
