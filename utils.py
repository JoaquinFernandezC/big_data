import mongo_connection
from matplotlib import pyplot as plt
events = mongo_connection.get_events_collection()
pipeline = [
    {"$group":{"_id": {"year": {"$year": "$date"}, "month": {"$month":"$date"}},"avgTone": { "$avg": "$avg_tone" }}},
    {"$sort": {"_id.year":1, "_id.month": 1}}]
agg = list(events.aggregate(pipeline).limit(10))
all_years = list(map(lambda x: x['_id']['year'], agg))
years =set(all_years)
labels_indexes =list( map(lambda year: all_years.index(year),years))

dates = list(map(lambda x: "{0}-{1}".format(x['_id']['year'], x['_id']['month']) if x['_id']['month'] == 1 else None, agg))

tones = list(map(lambda x: x['avgTone'], agg))
plt.plot(tones)
plt.xticks(labels_indexes,years)

plt.show()
for i in zip(tones):
    print (i)