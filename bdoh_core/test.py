from domain import *


location = Location(name="Paris", location=Point([0, 0]))
thing = Thing(name="Station Paris")
thing.add_location(location)

ds = Datastream(name="Temperature", thing=thing)
thing.datastreams.append(ds)

print(thing)
print(thing.datastreams[0].thing.name)
