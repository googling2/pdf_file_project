from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os


# fastapi 객체생성
app = FastAPI()

abs_path = os.path.dirname(os.path.realpath(__file__))
print(abs_path)
print(f"{abs_path}/templates")

# html 템플릿 폴더를 지정하여 jinja템플릿 객체 생성
# templates = Jinja2Templates(directory="templates") doc사용시 오류날 수 있기 떄문에 아래와 같이 절대경로를 사용한다.
templates = Jinja2Templates(directory=f"{abs_path}/templates")

# app.mount("/static", StaticFiles(directory=f"static")) #상대적인 위치
app.mount("/static", StaticFiles(directory=f"{abs_path}/static")) # 절대적인 위치

@app.get("/")
def home(request: Request):
    todos = 0
    # html에 데이터 랜더링을 해서 리턴함
    # return {"todos_data": todos}
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "todos": todos})

