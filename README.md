# JSONStorageAPI
This is a useful library for storing data using JSON in python.



To get started create a new python file and insert at the top of your project "from JSONStorageAPI import jsonfile".

To write data to a file use:
jsondb.set("filename.json", "firstkeylayer.secondkeylayer", "keyvalue")

To get data from a file use:
jsondb.get("filename.json", "firstkeylayer.secondkeylayer")

To remove a keyset use:
jsondb.remove("filename.json", "firstkeylayer.secondkeylayer")
