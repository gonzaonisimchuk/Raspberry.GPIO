from pymongo import MongoClient
import datetime

class LocalDataBase:
    client = MongoClient()
    db = client.raspberry

    def GetAllEvents(self):
        return self.db.events.find()

    def AddEvent(self, dispositivo, pin, estado):
        data = { "dispositivo": dispositivo, "pin": pin, "estado": estado, "fecha": str(datetime.datetime.now())}
        return self.db.events.insert_one(data)