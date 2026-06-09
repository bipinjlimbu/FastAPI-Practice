from fastapi import FastAPI, Depends, Header, HTTPException, status

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
    
def verify_token(token: str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return {
        "user": "Authorized User"
    }
    
@app.get("/secure-data")
def read_secure_data(user = Depends(verify_token)):
    return {
        "message": f"Here is your secure data!",
        "user": user['user']
    }
    