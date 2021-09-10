# JSONStorageAPI
This is a useful library for python3 which focuses on storing data using JSON and simplifying multilayer keysets.

This API has the ability to set keysets using dot notationts instead of the annoying brackets you have to normally use in python. It also features the ability to have unlimited keyset layers, do don't worry about a limit to your database needs!

To get started create a new python file and insert at the top of your project "from JSONStorageAPI import jsonfile".

To write data to a file use:
jsondb.set("filename.json", "firstkeylayer.secondkeylayer", "keyvalue")

To get data from a file use:
jsondb.get("filename.json", "firstkeylayer.secondkeylayer")

To remove a keyset use:
jsondb.remove("filename.json", "firstkeylayer.secondkeylayer")
