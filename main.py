from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
  "name": "Facundo Mendez",
  "role": "SRE / Backend Developer",
  "location": "Argentina 🇦🇷",
  "status": "Work in progress"
}
