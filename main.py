import json
from fastapi import FastAPI
from supabase import create_client, Client

app = FastAPI()

url: str = "https://wijashggfgbvwgbwzemd.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndpamFzaGdnZmdidndnYnd6ZW1kIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NDc5NzI1ODYsImV4cCI6MTk2MzU0ODU4Nn0.D3ZMH507iZXgO3hvVTY6rZAXuC9iUfGb25j7YUiuy5I"
supabase: Client = create_client(url, key)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/singup")
async def singup(data: dict):
    email = supabase.table("user").select("*").eq("email", data["email"]).execute()
    username = supabase.table("user").select("*").eq("username", data["username"]).execute()
    if email.data:
        return {"message": "Email already exists"}
    elif username.data:
        return {"message": "Username already exists"}
    result, error = supabase.table("user").insert(
        {"username": data["username"], "password": data["password"], "email": data['email'],
         "weight": data["weight"]}).execute()
    if error:
        return {"message": error}
    return {"message": "Success"}


@app.post("/login")
async def login(data: dict):
    result = supabase.table("user").select("*").eq("email", data["email"]).execute()
    if result.data:
        if result.data[0]["password"] == data["password"]:
            return {"message": "Success", "uuid": result.data[0]["id"]}
        else:
            return {"message": "Wrong password"}
    else:
        return {"message": "Email not found"}


@app.post('/add_glucose_record')
async def add_gluco(data: dict):
    uuid = data["uuid"]
    result = supabase.table("user").select("*").eq("id", uuid).execute()
    if not result.data:
        return {"message": "User not found"}
    result, error = supabase.table("glucose_record").insert(
        {"user_id": uuid, "taux": data["taux"], "created_at": data["created_at"]}).execute()
    if error:
        return {"message": error}
    return {"message": "Success"}


@app.post('/get_glucose_records')
async def get_gluco(data: dict):
    uuid = data["uuid"]
    result = supabase.table("user").select("*").eq("id", uuid).execute()
    if not result.data:
        return {"message": "User not found"}
    result = supabase.table("glucose_record").select("*").eq("user_id", uuid).gte('created_at', data["date1"]).lte(
        'created_at', data["date2"]).execute()
    print(result)
    return {"message": "Success", "data": result.data}

