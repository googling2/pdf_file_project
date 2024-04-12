
from datetime import date, datetime
from fastapi import FastAPI, Depends, HTTPException, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session
from database import SessionLocal, engine
import uvicorn
import models

# models에 정의한 모든 클래스, 연결한 DB엔진에 테이블로 생성
models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

def parse_date(date_str):
    if isinstance(date_str, date):
        return date_str
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Incorrect date format, should be YYYY-MM-DD")       

@app.get("/")
async def home(req: Request, db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    return templates.TemplateResponse("base.html", { "request": req, "todo_list": todos })

@app.post("/add")
def add(req: Request, title: str = Form(...), date: date = Form(None), db: Session = Depends(get_db)):
    print(f"Received date: {date}, type: {type(date)}")  # 디버깅을 위한 로그 추가
    date_obj = parse_date(date) if date else None
    new_todo = models.Todo(title=title, date=date_obj)
    db.add(new_todo)
    print("저장========================================")
    db.commit()
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/update/{todo_id}")
def update(req: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/delete/{todo_id}")
def delete(req: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

# @app.get("/modify/{todo_id}")
# def update2(req: Request, todo_id: int, )

if __name__ == "__main__":
	  uvicorn.run('app:app', 
              host='localhost', port=8000, reload=True)
