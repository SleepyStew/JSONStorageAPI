##########################################
#                                        #
#  Made By SleepyStew (SleepyStew#7777)  #
#                                        #
##########################################

import json, os
from json.decoder import JSONDecodeError
from functools import reduce

class jsondb:
    def set(FileName, Key, Object):
        try:
            with open(FileName) as json_file:
                try:
                    JsonDecoded = json.load(json_file)
                except JSONDecodeError:
                    if os.stat(f"./{FileName}").st_size == 0:
                        with open(FileName, 'w') as json_file:
                            json_file.write("{}")
                            JsonDecoded = json.load(json_file)
                            return
                    print(f"Error while writing to {FileName}, file is broken. (While writing to {Key} : {Object})")
                    exit()

        except IOError:
            JsonDecoded = {}
        
        Path = Key.split(".")
        target = reduce(lambda d, k: d.setdefault(k, {}), Path[:-1], JsonDecoded)
        target[Path[-1]] = Object

        with open(FileName, 'w') as json_file:
            json.dump(JsonDecoded, json_file, indent = 4)

    def get(FileName, Key):
        Path = Key.split(".")

        try:
            with open(FileName) as json_file:
                try:
                    JsonDecoded = json.load(json_file)
                except JSONDecodeError:
                    print(f"Error while writing to {FileName}, file is broken. (While reading {Key})")
                    exit()

            for KeyObject in Path:
                JsonDecoded = JsonDecoded[KeyObject]

            return JsonDecoded
        except KeyError:
            return None

    def remove(FileName, Key):
        try:
            with open(FileName) as json_file:
                try:
                    JsonDecoded = json.load(json_file)
                except JSONDecodeError:
                    print(f"Error while writing to {FileName}, file is broken. (While removing {Key})")
                    exit()
                    
            Path = Key.split(".")
            target = reduce(lambda d, k: d.setdefault(k, {}), Path[:-1], JsonDecoded)
            del target[Path[-1]]

            with open(FileName, 'w') as json_file:
                json.dump(JsonDecoded, json_file, indent = 4)

        except KeyError:
            return None
