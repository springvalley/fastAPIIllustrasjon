from fastapi import FastAPI
from starlette.responses import FileResponse 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

#Modell som representerer et nytt todo item
class Todo(BaseModel):
    id: int
    item: str

#Lager en ny instans av fastAPI
app = FastAPI()


#Middelware er så vi ikke får feilmeldinger, hvis du vil lese mer kan du google "CORS middleware"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Midlertidig "database" som egt. bare er et python array, vi trenger bare et sted å lagre data midlertidig 
todos = []
#Legger til et element i den "databasen"
todos.append(Todo(id=0, item="test-item"))


#Dette er hvordan man definerer en rute i fastAPI. 
#Hvor endepunktet til ruten er, i dette tilfellet er det urlen til nettsiden (localhost:8000) + "(/)" så localhost:8000/
@app.get("/")
async def root():
    #Returnerer en HTML fil
    return FileResponse("./frontend/index.html")


#Rute for å hente alle todos i "databasen".
#Som du kan se er ruten definert med "localhost:8000/todo" og vi returnerer bare todo python arrayet
@app.get("/todo")
async def getTodos():
     #returnerer arrayet
     return{"todos": todos}

#Rute for å legge til ny todo i "databasen"
#Her bruker vi app.post istedenfor app.get fordi vi vil lage en post request.
#Ruten for å hente og lage en ny todo er den samme, det er bare lov hvis man har forskjellige typer requests
@app.post("/todo")
async def create_todo(todo: Todo):
     #Legger til en ny todo i "databasen" (Arrayet)
     todos.append(todo)
     
