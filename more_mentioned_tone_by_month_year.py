import mongo_connection
from matplotlib import pyplot as pl

from bson.code import Code
map = Code("""function() {
var avg_articles = [this.avg_tone, this.num_articles];
emit(this.date.getFullYear().toString()+'-'+this.date.getMonth().toString(), avg_articles);;
};
""")
reduce = Code("""function(keyCustId, values) {
var art_count = {};
max_num_art = -1;
max_avg_tone = -10;
for (var i = 0; i < values.length; i++) {art_count[values[i][0]] = 0;}
for (var i = 0; i < values.length; i++) {
var avg_tone = values[i][0];
var num_articles = values[i][1];

art_count[avg_tone]+= num_articles;

if(art_count[avg_tone]>max_num_art){
max_num_art=art_count[avg_tone];
max_avg_tone = avg_tone;
}
}
return max_avg_tone;
};
""")
events = mongo_connection.get_events_collection()

result = events.map_reduce(map,
                           reduce,
                           "myresults",
                           query={}
                           )
dates = []
avg_tones = []
for doc in result.find():
    value = doc['value']
    if isinstance(value, list):
        value=value[0]
    dates.append(doc['_id'])
    avg_tones.append(value)
    print (doc)
pl.plot(avg_tones)
pl.show()