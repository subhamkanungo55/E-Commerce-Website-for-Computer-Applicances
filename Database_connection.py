from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# from CustomLogger.logger import Logger

# logging = Logger('logFiles/test.log')

# class db():

# def __init__():
"""
:DESC: Creates connection with Database when backend thread runs.
"""
# logging.info('INFO', 'Obj created')
Client_id = 'xwlwAXRXrBUvqfEzfyMWrLqo'
print("one")
Client_secret = '3OpU2p8CthkYQnzKbISiafG9e,r8+m23fsTFLgLy-s4LP7yYZ9LuN_MkrCHIwmfS3R,+r-m0aDitnTD1MnEIA..01tWMWxp4PjwuITxr29+6o67ciXl1IOfx53FhukdT'
print("two")
cloud_config = {'secure_connect_bundle': 'secure-connect-compac-application1.zip'}
print("three")
auth_provider = PlainTextAuthProvider(Client_id, Client_secret)
print("four")
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
print("five")
session = cluster.connect()
print("six")

# row = session.execute("select release_version from system.local").one()
# print("seven")
# if row:
#     print(row[0])
# else:
#     print("An error occurred.")

# def master(self):
"""
:DESC: Creates table if not existed into database
:return:
"""
# def get_data():
session.execute("use user")
row=session.execute("select * from keyboard").one()
print(row)
# if row:
#     print(row[0])
# else:
#     print("not iterate")
# session.execute("use user")
# session.execute("CREATE TABLE Data(id uuid PRIMARY KEY,Airline text,Source text,Destination text,Total_Stops text,Total_Duration int,Journey_month int,Journey_day int);")
        # self.session.execute("select release_version from system.local")
        # self.session.execute("CREATE TABLE Data(id uuid PRIMARY KEY,Airline text,Source text,Destination text,Total_Stops text,Total_Duration int,Journey_month int,Journey_day int);")