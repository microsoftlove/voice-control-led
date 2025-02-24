from fastapi import FastAPI

app = FastAPI()

from led import greet,openLed,closeLed,autoLightLed
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    print(greet(name))
    return {"message": f"Hello {name}"}
@app.get("/open")
def open():
    openLed()
    return {"message": f"Hello 开灯"}

@app.get("/close")
def close():
    closeLed()
    return {"message": f"Hello 关灯"}

@app.get("/autoLight")
def autoLight():
    autoLightLed()
    return {"message": f"Hello 自动开关灯"}