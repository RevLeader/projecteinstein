from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()



# people = {
#     1: {
#         "name": "Alice Johnson",
#         "age": 28,
#         "city": "New York",
#         "hometown": "Boston",
#         "profile_image": "https://i.pravatar.cc/150?img=1"
#     },
#     2: {
#         "name": "Carlos Rivera",
#         "age": 34,
#         "city": "Los Angeles",
#         "hometown": "Miami",
#         "profile_image": "https://i.pravatar.cc/150?img=2"
#     },
#     3: {
#         "name": "Priya Patel",
#         "age": 25,
#         "city": "Chicago",
#         "hometown": "Houston",
#         "profile_image": "https://i.pravatar.cc/150?img=3"
#     },
#     4: {
#         "name": "James O'Brien",
#         "age": 41,
#         "city": "Seattle",
#         "hometown": "Dublin",
#         "profile_image": "https://i.pravatar.cc/150?img=4"
#     },
#     5: {
#         "name": "Yuki Tanaka",
#         "age": 30,
#         "city": "San Francisco",
#         "hometown": "Tokyo",
#         "profile_image": "https://i.pravatar.cc/150?img=5"
#     },
#     6: {
#         "name": "Amara Osei",
#         "age": 27,
#         "city": "Atlanta",
#         "hometown": "Accra",
#         "profile_image": "https://i.pravatar.cc/150?img=6"
#     },
#     7: {
#         "name": "Lena Müller",
#         "age": 36,
#         "city": "Austin",
#         "hometown": "Berlin",
#         "profile_image": "https://i.pravatar.cc/150?img=7"
#     },
#     8: {

#         "name": "Tariq Hassan",
#         "age": 22,
#         "city": "Houston",
#         "hometown": "Cairo",
#         "profile_image": "https://i.pravatar.cc/150?img=8"
#     },
#     9: {
#         "name": "Sofia Martínez",
#         "age": 31,
#         "city": "Phoenix",
#         "hometown": "Mexico City",
#         "profile_image": "https://i.pravatar.cc/150?img=9"
#     },
#     10: {
#         "name": "David Kim",
#         "age": 45,
#         "city": "Denver",
#         "hometown": "Seoul",
#         "profile_image": "https://i.pravatar.cc/150?img=10"
#     }
# }
    
people = [
    {
        "name": "Alice Johnson",
        "age": 28,
        "city": "New York",
        "hometown": "Boston",
        "profile_image": "https://i.pravatar.cc/150?img=1"
    },
    {
        "name": "Carlos Rivera",
        "age": 34,
        "city": "Los Angeles",
        "hometown": "Miami",
        "profile_image": "https://i.pravatar.cc/150?img=2"
    },
    {
        "name": "Priya Patel",
        "age": 25,
        "city": "Chicago",
        "hometown": "Houston",
        "profile_image": "https://i.pravatar.cc/150?img=3"
    },
    {
        "name": "James O'Brien",
        "age": 41,
        "city": "Seattle",
        "hometown": "Dublin",
        "profile_image": "https://i.pravatar.cc/150?img=4"
    },
    {
        "name": "Yuki Tanaka",
        "age": 30,
        "city": "San Francisco",
        "hometown": "Tokyo",
        "profile_image": "https://i.pravatar.cc/150?img=5"
    },
    {
        "name": "Amara Osei",
        "age": 27,
        "city": "Atlanta",
        "hometown": "Accra",
        "profile_image": "https://i.pravatar.cc/150?img=6"
    },
    {
        "name": "Lena Müller",
        "age": 36,
        "city": "Austin",
        "hometown": "Berlin",
        "profile_image": "https://i.pravatar.cc/150?img=7"
    },
    {
        "name": "Tariq Hassan",
        "age": 22,
        "city": "Houston",
        "hometown": "Cairo",
        "profile_image": "https://i.pravatar.cc/150?img=8"
    },
    {
        "name": "Sofia Martínez",
        "age": 31,
        "city": "Phoenix",
        "hometown": "Mexico City",
        "profile_image": "https://i.pravatar.cc/150?img=9"
    },
    {
        "name": "David Kim",
        "age": 45,
        "city": "Denver",
        "hometown": "Seoul",
        "profile_image": "https://i.pravatar.cc/150?img=10"
    },
]

class CreateUser(BaseModel):
    name: str
    age: int
    city: str
    hometown: str
    profile_image: str

@app.get("/")
def main():
    return people

@app.get("/info")
def show_part(skip: int = 0, limit: int = 5):
    items_list = list(people.items())
    sliced_items = items_list[skip: skip + limit]

    return dict(sliced_items)

@app.get("/data/{person_id}")
def show_person(person_id: str):

    search_term = person_id.strip().title()
    for person in people:
        if search_term in person["name"]:
            return person
    return {"Error": "User not found"}

@app.post("/create/{person_id}")
def create_person(person_id: int, person: CreateUser):
    people[person_id] = person
    return people[person_id]