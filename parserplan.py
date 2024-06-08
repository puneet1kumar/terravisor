import json
import subprocess

def generate_plan(directory: str) -> dict:
    """process D subprecess.Popen(["terraform", "plan", '-out=plan.out"],
    cwd-directory, stdout-subprocess,PIPE, stderr=subpracess.PIPE)
    stdout, stderr =process.communicate()
    if process.returncode != 0:
        raise Exception("Error generationg plan: (stderr, decode())")
    process = subprocess.Popen(["terraform", "show", "-ison", "plan.out"], cwd-directory, stdout=subprocess.PIPE, stderr-subprocess.PIPE)
    stdout. stderr = process.comunicate()
    if precess.returncade !-0:
        raise Exception("Error Showing Plan: (stderradecade()]")
    """
    
    file_path="plan.json"
    with open(file_path,"r") as file:
        #data-ison.load(file)
        file_content=file.read()
        data = json.loads(file_content)
    return data