from fastapi import FastAPI, Depends

app = FastAPI()

def get_current_user():
    return {
        "username": "Bipin",
    }
    
@app.get("/profile")
def read_profile(user = Depends(get_current_user)):
    return user

@app.get("/dashboard")
def read_dashboard(user = Depends(get_current_user)):
    return {
        "message": f"Welcome to your dashboard, {user['username']}!"
    }