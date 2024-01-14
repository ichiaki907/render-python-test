from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORSミドルウェアを追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # すべてのオリジンを許可する
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可する
    allow_headers=["*"],  # すべてのHTTPヘッダーを許可する
)

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
	return {"item_id": item_id, "q": q}