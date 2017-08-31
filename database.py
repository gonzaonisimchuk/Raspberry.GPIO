import pyrebase, datetime

class DataBase:
    config = {
        "apiKey": "",
        "authDomain": "",
        "databaseURL": "",
        "storageBucket": ""
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password("", "")
    db = firebase.database()

    def GetAllEvents(self):
        return self.db.child("events").get(self.user['idToken'])

    def AddEvent(self, dispositivo, pin, estado):
        data = { "dispositivo": dispositivo, "pin": pin, "estado": estado, "fecha": str(datetime.datetime.now())}
        return self.db.child("events").push(data, self.user['idToken'])