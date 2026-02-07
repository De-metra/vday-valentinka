from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="app/static"))
templates = Jinja2Templates(directory='app/templates') 

QUESTIONS = [
    {
        "id": 1,
        "question": "Кто САМЫЙ милый?",
        "answers": [
            {"text": "ТЫ", "correct": True, "image": "you.png"},
            {"text": "Котёнок", "correct": False, "image": "kitten.jpg"},
        ]
    },
    {
        "id": 2,
        "question": "Кто САМЫЙ умный?",
        "answers": [
            {"text": "ТЫ", "correct": True, "image": "you.png"},
            {"text": "Умный человек в очках", "correct": False, "image": "bill.jpg"},
        ] 
    }, 
    {
        "id": 3,
        "question": "Кого я БОЛЬШЕ всего люблю?",
        "answers": [
            {"text": "ТЕБЯ", "correct": False, "image": "you.png"},
            {"text": "Леона", "correct": True, "image": "leon.jpg"},
        ]
    },
]


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        name='index.html', context={'request': request}
    )

@app.get("/question/{question_id}")
async def get_question(request: Request, question_id: int):
    if 1 <= question_id <= len(QUESTIONS):
        return templates.TemplateResponse(
            name='question.html',
            context={
                'request': request,
                'question': QUESTIONS[question_id - 1],
                'total_questions': len(QUESTIONS)
            }
        )
    return templates.TemplateResponse(
        name='error.html', context={'request': request}
    )

@app.get("/threat")
async def get_threat(request: Request):
    return templates.TemplateResponse(
        name='threat.html',
        context={'request': request}
    )

@app.get("/final")
async def final_page(request: Request):
    return templates.TemplateResponse(
        name='final.html',
        context={'request': request}
    )

