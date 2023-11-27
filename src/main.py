from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

app = FastAPI()



templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return RedirectResponse(url="/counter")

@app.get("/counter" ,response_class=HTMLResponse)
def read_counter(request: Request):
    f = open("count.txt", "r+")
    count = int(f.read())
    f.close()
    return templates.TemplateResponse("counter.html", {"request": request, "counter":count})

@app.get("/increment")
def read_counter(request: Request):
    f = open("count.txt", "r+")
    count = int(f.read())
    count +=1
    print(count)
    f.seek(0)
    f.write(str(count))
    f.truncate()
    f.close()
    return templates.TemplateResponse("counter-text.html", {"request": request, "counter": count})


@app.get("/decrement")
def read_counter(request: Request):
    f = open("count.txt", "r+")
    count = int(f.read())
    count -=1
    print(count)
    f.seek(0)
    f.write(str(count))
    f.truncate()
    f.close()
    return templates.TemplateResponse("counter-text.html", {"request": request, "counter": count})