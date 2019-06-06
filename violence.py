import mongo_connection
from mrjob.job import MRJob
from bson.code import Code
map = Code("function () {"
           "    emit(this.event_code, this.num_articles);"
           "}")
reduce = Code("function (key, values) {"
               "  var total = 0;"
               "  for (var i = 0; i < values.length; i++) {"
               "    total += values[i];"
               "  }"
               "  return total;"
               "}")
events = mongo_connection.get_events_collection()

result = events.map_reduce(map,
                           reduce,
                           "myresults",
                           query={"event_code": {"$regex": '20.'}}
                           )
for doc in result.find():
    print (doc)
