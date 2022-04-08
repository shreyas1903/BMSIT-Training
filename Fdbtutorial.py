import firebase_admin
from firebase_admin import credentials, db

GfbSdkCfgVar = credentials.Certificate('FDBkey.json')

firebase_admin.initialize_app(GfbSdkCfgVar, {
	'databaseURL': 'https://bmsit-fdb-6c062-default-rtdb.firebaseio.com/'
})

FdbRefVap = db.reference('/')
# FdbRefVap.update({"Shreyas":{"0":7776924028,"1":8605007028}})
# FdbRefVap.update({"email":"shreyaspati1l901@gmail.com"})
# FdbRefVap.update({"branch":"cse","usn":"145","sem":"6th"})
# FdbRefVap.update({"address":{
#     "area":"yelhanka",
#     "city":"bengaluru",
#     "pin":560064
# }})

FdbRefVap = FdbRefVap.get()
print("Data recevied",FdbRefVap)