import pymongo

myclient = pymongo.MongoClient("mongodb://172.16.66.141:27017/")

mydb = myclient["mydatabase"]



# 创建集合
mycol = mydb["customers"]

# 插入记录
mydict = {"name": "莹莹", "address": "灵宝"}

x = mycol.insert_one(mydict)

print(x.inserted_id)
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")
else:
    print('nothing')

y = mycol.find_one()
print("first doc:",y)
