from fastapi import FastAPI
from pydantic import BaseModel
from app.services.app_launcher import launch_app
from app.services.website_launcher import open_website
from app.services.command_router import execute_command

app = FastAPI(title="Nexus Pendant Laptop Agent")


class AppRequest(BaseModel):
    app_name: str

class WebsiteRequest(BaseModel):
    url: str

class CommandRequest(BaseModel):
    command: str

@app.get("/")
def home():
    return {
        "status": "running",
        "service": "Nexus Laptop Agent"
    }


@app.post("/open_app")
def open_app(request: AppRequest):

    success = launch_app(request.app_name)

    if success:
        return {
            "status": "success",
            "app": request.app_name
        }

    return {
        "status": "error",
        "message": "App not supported"
    }

    
@app.post("/open_website")
def open_site(request: WebsiteRequest):

    open_website(request.url)

    return {
        "status": "success",
        "url": request.url
    }
@app.post("/execute_command")
def execute(request: CommandRequest):

    result = execute_command(request.command)

    return {
        "status": "success",
        "result": result
    }