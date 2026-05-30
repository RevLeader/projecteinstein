from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

new_users = [
    {"full_name": "John Doe", "username": "john_doe92", "profile_picture": "https://example.com/profile1.jpg", "password": "Pass@1234", "city": "Accra", "home": "Apartment"},
    {"full_name": "Jane Smith", "username": "jane_smith88", "profile_picture": "https://example.com/profile2.jpg", "password": "Jane@5678", "city": "Kumasi", "home": "Villa"},
    {"full_name": "Michael Brown", "username": "mike_brown45", "profile_picture": "https://example.com/profile3.jpg", "password": "Mike@2025", "city": "Tema", "home": "Duplex"},
    {"full_name": "Sarah Johnson", "username": "sarah_j22", "profile_picture": "https://example.com/profile4.jpg", "password": "Sarah#998", "city": "Tamale", "home": "Bungalow"},
    {"full_name": "Daniel Wilson", "username": "dan_wilson77", "profile_picture": "https://example.com/profile5.jpg", "password": "Dan!4455", "city": "Cape Coast", "home": "Condo"},
    {"full_name": "Emily Davis", "username": "emily_d90", "profile_picture": "https://example.com/profile6.jpg", "password": "Emily@909", "city": "Ho", "home": "Townhouse"},
    {"full_name": "Chris Evans", "username": "cevans33", "profile_picture": "https://example.com/profile7.jpg", "password": "Chris#123", "city": "Takoradi", "home": "Studio"},
    {"full_name": "Sophia Taylor", "username": "sophia_t11", "profile_picture": "https://example.com/profile8.jpg", "password": "Sophia!56", "city": "Sunyani", "home": "Penthouse"},
    {"full_name": "David Anderson", "username": "david_a55", "profile_picture": "https://example.com/profile9.jpg", "password": "David@888", "city": "Koforidua", "home": "Cottage"},
    {"full_name": "Olivia Thomas", "username": "olivia_t99", "profile_picture": "https://example.com/profile10.jpg", "password": "Olivia#202", "city": "Bolgatanga", "home": "Mansion"},
    {"full_name": "James White", "username": "jwhite12", "profile_picture": "https://example.com/profile11.jpg", "password": "James@741", "city": "Accra", "home": "Villa"},
    {"full_name": "Grace Hall", "username": "grace_h44", "profile_picture": "https://example.com/profile12.jpg", "password": "Grace!321", "city": "Tema", "home": "Apartment"},
    {"full_name": "Benjamin Lee", "username": "benlee_87", "profile_picture": "https://example.com/profile13.jpg", "password": "Ben#7788", "city": "Kumasi", "home": "Studio"},
    {"full_name": "Ava Martin", "username": "ava_m66", "profile_picture": "https://example.com/profile14.jpg", "password": "Ava@12345", "city": "Ho", "home": "Townhouse"},
    {"full_name": "Lucas Walker", "username": "lucasw_09", "profile_picture": "https://example.com/profile15.jpg", "password": "Lucas!555", "city": "Tamale", "home": "Duplex"},
    {"full_name": "Mia Young", "username": "mia_y88", "profile_picture": "https://example.com/profile16.jpg", "password": "Mia#1111", "city": "Takoradi", "home": "Condo"},
    {"full_name": "Henry King", "username": "henry_k77", "profile_picture": "https://example.com/profile17.jpg", "password": "Henry@909", "city": "Cape Coast", "home": "Apartment"},
    {"full_name": "Charlotte Scott", "username": "char_scott", "profile_picture": "https://example.com/profile18.jpg", "password": "Char!789", "city": "Sunyani", "home": "Villa"},
    {"full_name": "Ethan Green", "username": "ethangreen22", "profile_picture": "https://example.com/profile19.jpg", "password": "Ethan#456", "city": "Accra", "home": "Bungalow"},
    {"full_name": "Amelia Baker", "username": "amelia_bk", "profile_picture": "https://example.com/profile20.jpg", "password": "Amelia@10", "city": "Tema", "home": "Cottage"},
    {"full_name": "Logan Adams", "username": "logan_a33", "profile_picture": "https://example.com/profile21.jpg", "password": "Logan!303", "city": "Koforidua", "home": "Penthouse"},
    {"full_name": "Ella Nelson", "username": "ella_n55", "profile_picture": "https://example.com/profile22.jpg", "password": "Ella#9090", "city": "Bolgatanga", "home": "Studio"},
    {"full_name": "Jacob Carter", "username": "jacobc_44", "profile_picture": "https://example.com/profile23.jpg", "password": "Jacob@741", "city": "Takoradi", "home": "Condo"},
    {"full_name": "Harper Mitchell", "username": "harper_m88", "profile_picture": "https://example.com/profile24.jpg", "password": "Harper!77", "city": "Accra", "home": "Villa"},
    {"full_name": "Alexander Perez", "username": "alex_p77", "profile_picture": "https://example.com/profile25.jpg", "password": "Alex#2025", "city": "Ho", "home": "Townhouse"},
    {"full_name": "Evelyn Roberts", "username": "evelyn_r11", "profile_picture": "https://example.com/profile26.jpg", "password": "Evelyn@55", "city": "Tamale", "home": "Apartment"},
    {"full_name": "Sebastian Turner", "username": "seb_turner", "profile_picture": "https://example.com/profile27.jpg", "password": "Seb!909", "city": "Kumasi", "home": "Mansion"},
    {"full_name": "Abigail Phillips", "username": "abby_p90", "profile_picture": "https://example.com/profile28.jpg", "password": "Abby#654", "city": "Cape Coast", "home": "Bungalow"},
    {"full_name": "Matthew Campbell", "username": "matt_c01", "profile_picture": "https://example.com/profile29.jpg", "password": "Matt@123", "city": "Sunyani", "home": "Duplex"},
    {"full_name": "Sofia Parker", "username": "sofia_p77", "profile_picture": "https://example.com/profile30.jpg", "password": "Sofia!456", "city": "Tema", "home": "Penthouse"}
]

# print(users)


@app.get("/")
def main():
    return "First assignment completed"

items = {
    "items1": ["mango", "banana", "pawpaw"],
    "items2": ["cowpea"]
}

@app.get("/users/{all}")
def new(all):
    # return {"items": items}
    # return items["items1"]
    return new_users


@app.get("/new")
def come(q):
    return {"post": q}

class Status(str, Enum):
    online = "online"
    offline = "offline"
    deceased = "deceased"

@app.get("/stat")
def main(status: Status):
    if status == Status.online:
        return "ONLINE"
    elif status == Status.offline:
        return "OFFLINE"
    elif status == Status.deceased:
        return "DECEASED"

@app.get("/")
def main(skip: int = 0, limit: int = None):
    if limit is None:
        return new_users[skip:]
    
    return new_users[skip: skip + limit]





class User(BaseModel):
    name: str
    number: int
    town: str
    age: int
    password: str
    city: str | None = None

@app.post("/create/user")
def main(user: User):
    return {"user": user}


if __name__ == "__main__":
    main()