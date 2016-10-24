from collections import Counter
import csv, json, urllib2

with open('2015ATP.csv', 'rb') as csvfile:
    recordReader = csv.DictReader(csvfile)

    # locations = []
    locationsTop1Win2 = []
    locationsTop1Win3 = []
    locationsTop1Win4 = []
    locationsTop1Win5 = []
    locationsTop1Lose2 = []
    locationsTop1Lose3 = []
    locationsTop1Lose4 = []
    locationsTop1Lose5 = []

    locationsTop2Win2 = []
    locationsTop2Win3 = []
    locationsTop2Win4 = []
    locationsTop2Win5 = []
    locationsTop2Lose2 = []
    locationsTop2Lose3 = []
    locationsTop2Lose4 = []
    locationsTop2Lose5 = []

    locationsTop3Win2 = []
    locationsTop3Win3 = []
    locationsTop3Win4 = []
    locationsTop3Win5 = []
    locationsTop3Lose2 = []
    locationsTop3Lose3 = []
    locationsTop3Lose4 = []
    locationsTop3Lose5 = []

    players = []

    for row in recordReader:
        # print ', '.join(row)
        # print (row['ATP'],row['Location'],row['Date'],row['Winner'],row['Loser'])
        # print type(row['Location'])

        # Create a list of all locations
        # if row['Location'] not in locations:
        #     locations.append(row['Location'])

        # Create a list of all players, both winners and losers
        players.append(row['Winner'])
        players.append(row['Loser'])

        # Top 1 player won and lost in 2,3,4,5 sets
        if row['Winner'] == "Djokovic N." and row['Wsets'] == "2":
            if row['Location'] not in locationsTop1Win2:
                locationsTop1Win2.append(row['Location'])
        if row['Winner'] == "Djokovic N." and row['Wsets'] == "3":
            if row['Location'] not in locationsTop1Win3:
                locationsTop1Win3.append(row['Location'])
        if row['Winner'] == "Djokovic N." and row['Wsets'] == "4":
            if row['Location'] not in locationsTop1Win4:
                locationsTop1Win4.append(row['Location'])
        if row['Winner'] == "Djokovic N." and row['Wsets'] == "5":
            if row['Location'] not in locationsTop1Win5:
                locationsTop1Win5.append(row['Location'])

        if row['Loser'] == "Djokovic N." and row['Lsets'] == "2":
            if row['Location'] not in locationsTop1Lose2:
                locationsTop1Lose2.append(row['Location'])
        if row['Loser'] == "Djokovic N." and row['Lsets'] == "3":
            if row['Location'] not in locationsTop1Lose3:
                locationsTop1Lose3.append(row['Location'])
        if row['Loser'] == "Djokovic N." and row['Lsets'] == "4":
            if row['Location'] not in locationsTop1Lose4:
                locationsTop1Lose4.append(row['Location'])
        if row['Loser'] == "Djokovic N." and row['Lsets'] == "5":
            if row['Location'] not in locationsTop1Lose5:
                locationsTop1Lose5.append(row['Location'])

        # Top 2 player won and lost in 2,3,4,5 sets
        if row['Winner'] == "Nadal R." and row['Wsets'] == "2":
            if row['Location'] not in locationsTop2Win2:
                locationsTop2Win2.append(row['Location'])
        if row['Winner'] == "Nadal R." and row['Wsets'] == "3":
            if row['Location'] not in locationsTop2Win3:
                locationsTop2Win3.append(row['Location'])
        if row['Winner'] == "Nadal R." and row['Wsets'] == "4":
            if row['Location'] not in locationsTop2Win4:
                locationsTop2Win4.append(row['Location'])
        if row['Winner'] == "Nadal R." and row['Wsets'] == "5":
            if row['Location'] not in locationsTop2Win5:
                locationsTop2Win5.append(row['Location'])

        if row['Loser'] == "Nadal R." and row['Lsets'] == "2":
            if row['Location'] not in locationsTop2Lose2:
                locationsTop2Lose2.append(row['Location'])
        if row['Loser'] == "Nadal R." and row['Lsets'] == "3":
            if row['Location'] not in locationsTop2Lose3:
                locationsTop2Lose3.append(row['Location'])
        if row['Loser'] == "Nadal R." and row['Lsets'] == "4":
            if row['Location'] not in locationsTop2Lose4:
                locationsTop2Lose4.append(row['Location'])
        if row['Loser'] == "Nadal R." and row['Lsets'] == "5":
            if row['Location'] not in locationsTop2Lose5:
                locationsTop2Lose5.append(row['Location'])

        # Top 3 player won and lost in 2,3,4,5 sets
        if row['Winner'] == "Berdych T." and row['Wsets'] == "2":
            if row['Location'] not in locationsTop3Win2:
                locationsTop3Win2.append(row['Location'])
        if row['Winner'] == "Berdych T." and row['Wsets'] == "3":
            if row['Location'] not in locationsTop3Win3:
                locationsTop3Win3.append(row['Location'])
        if row['Winner'] == "Berdych T." and row['Wsets'] == "4":
            if row['Location'] not in locationsTop3Win4:
                locationsTop3Win4.append(row['Location'])
        if row['Winner'] == "Berdych T." and row['Wsets'] == "5":
            if row['Location'] not in locationsTop3Win5:
                locationsTop3Win5.append(row['Location'])

        if row['Loser'] == "Berdych T." and row['Lsets'] == "2":
            if row['Location'] not in locationsTop3Lose2:
                locationsTop3Lose2.append(row['Location'])
        if row['Loser'] == "Berdych T." and row['Lsets'] == "3":
            if row['Location'] not in locationsTop3Lose3:
                locationsTop3Lose3.append(row['Location'])
        if row['Loser'] == "Berdych T." and row['Lsets'] == "4":
            if row['Location'] not in locationsTop3Lose4:
                locationsTop3Lose4.append(row['Location'])
        if row['Loser'] == "Berdych T." and row['Lsets'] == "5":
            if row['Location'] not in locationsTop3Lose5:
                locationsTop3Lose5.append(row['Location'])

    print "Top1Win2", locationsTop1Win2
    print "Top1Win3", locationsTop1Win3
    print "Top1Win4", locationsTop1Win4
    print "Top1Win5", locationsTop1Win5
    print "Top1Lose2", locationsTop2Lose2
    print "Top1Lose3", locationsTop2Lose3
    print "Top1Lose4", locationsTop2Lose4
    print "Top1Lose5", locationsTop2Lose5
    print "Top2Win2", locationsTop2Win2
    print "Top2Win3", locationsTop2Win3
    print "Top2Win4", locationsTop2Win4
    print "Top2Win5", locationsTop2Win5
    print "Top2Lose2", locationsTop2Lose2
    print "Top2Lose3", locationsTop2Lose3
    print "Top2Lose4", locationsTop2Lose4
    print "Top2Lose5", locationsTop2Lose5
    print "Top3Win2", locationsTop3Win2
    print "Top3Win3", locationsTop3Win3
    print "Top3Win4", locationsTop3Win4
    print "Top3Win5", locationsTop3Win5
    print "Top3Lose2", locationsTop3Lose2
    print "Top3Lose3", locationsTop3Lose3
    print "Top3Lose4", locationsTop3Lose4
    print "Top3Lose5", locationsTop3Lose5

    # print Counter(players)


    # Output to a players file to make a frequency plot
    # output_file = open('players.csv', 'w')
    # output_file.write("Player,Frequency\n")
    # for (k,v) in sorted(Counter(players).iteritems(), key=lambda(k,v):v, reverse=True):
    #     # print k,v
    #     output_file.write(str(k)+","+str(v)+"\n")
    # output_file.close()



def requestWeather(mydata):
    ans = {}
    locationsUrl = []

    for city in mydata:
        # Replace the blank space and apostrophe to the link-readable format
        city = city.replace(" ","%20").replace("'", "%27")
        # print 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=233e1276d5bca85849d4ae1381932c25'
        locationsUrl.append('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=233e1276d5bca85849d4ae1381932c25')

    # city = 'Kuala Lumpur'
    # url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=233e1276d5bca85849d4ae1381932c25'


    for i in locationsUrl:

        url = i

        data={
            "coord":{"lon":"lonNum","lat":"latNum"},
            "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
            "base":"cmc stations",
            "main":{"temp":293.25,"pressure":1019,"humidity":83,"temp_min":289.82,"temp_max":295.37},
            "wind":{"speed":"speedNum","deg":"degNum"},
            "clouds":{"all":20},
            "dt":1435658272,
            "sys":{"type":1,"id":8166,"message":0.0166,"country":"AU","sunrise":1435610796,"sunset":1435650870},
            "id":2172797,
            "name":"Cairns",
            "cod":200
        }

        json_data = json.dumps(data)

        req = urllib2.Request(url, json_data, {'Content-Type': 'application/json', 'Content-Length': len(json_data)})
        f = urllib2.urlopen(req)
        response = json.load(f)

        # print response
        ans[response['name']] = [response['main']['temp']-273.15,response['main']['pressure'],response['main']['humidity'],response['wind']['speed']]

        # print response['name']
        # print response['main']['temp']
        # print response['main']['pressure']
        # print response['main']['humidity']

    return ans


# Test Results
# print requestWeather(locationsTop1Win2)
# print requestWeather(locationsTop1Win3)
# print requestWeather(locationsTop1Win4)
# print requestWeather(locationsTop1Win5)
# print requestWeather(locationsTop1Lose2)
# print requestWeather(locationsTop1Lose3)
# print requestWeather(locationsTop1Lose4)
# print requestWeather(locationsTop1Lose5)
# print requestWeather(locationsTop2Win2)
# print requestWeather(locationsTop2Win3)
# print requestWeather(locationsTop2Win4)
# print requestWeather(locationsTop2Win5)
# print requestWeather(locationsTop2Lose2)
# print requestWeather(locationsTop2Lose3)
# print requestWeather(locationsTop2Lose4)
# print requestWeather(locationsTop2Lose5)
# print requestWeather(locationsTop3Win2)
# print requestWeather(locationsTop3Win3)
# print requestWeather(locationsTop3Win4)
# print requestWeather(locationsTop3Win5)
# print requestWeather(locationsTop3Lose2)
# print requestWeather(locationsTop3Lose3)
# print requestWeather(locationsTop3Lose4)
# print requestWeather(locationsTop3Lose5)


# Output to a players file to make a boxplot

output_file = open('boxplot.csv', 'w')
output_file.write("Player,Result,Temp,Pressure,Humidity,WindSpeed\n")

def writeOutput(dataset, name, result):
    for i in requestWeather(dataset).values():
        output_file.write(name+","+result+"," + str(i[0]) + "," + str(i[1]) + "," + str(i[2])+ "," + str(i[3]) + "\n")


writeOutput(locationsTop1Win2, "Djokovic N.", "Win2")
writeOutput(locationsTop1Win3, "Djokovic N.", "Win3")
writeOutput(locationsTop1Win4, "Djokovic N.", "Win4")
writeOutput(locationsTop1Win5, "Djokovic N.", "Win5")
writeOutput(locationsTop1Lose2, "Djokovic N.", "Lose2")
writeOutput(locationsTop1Lose3, "Djokovic N.", "Lose3")
writeOutput(locationsTop1Lose4, "Djokovic N.", "Lose4")
writeOutput(locationsTop1Lose5, "Djokovic N.", "Lose5")

writeOutput(locationsTop2Win2, "Nadal R.", "Win2")
writeOutput(locationsTop2Win3, "Nadal R.", "Win3")
writeOutput(locationsTop2Win4, "Nadal R.", "Win4")
writeOutput(locationsTop2Win5, "Nadal R.", "Win5")
writeOutput(locationsTop2Lose2, "Nadal R.", "Lose2")
writeOutput(locationsTop2Lose3, "Nadal R.", "Lose3")
writeOutput(locationsTop2Lose4, "Nadal R.", "Lose4")
writeOutput(locationsTop2Lose5, "Nadal R.", "Lose5")

writeOutput(locationsTop3Win2, "Berdych T.", "Win2")
writeOutput(locationsTop3Win3, "Berdych T.", "Win3")
writeOutput(locationsTop3Win4, "Berdych T.", "Win4")
writeOutput(locationsTop3Win5, "Berdych T.", "Win5")
writeOutput(locationsTop3Lose2, "Berdych T.", "Lose2")
writeOutput(locationsTop3Lose3, "Berdych T.", "Lose3")
writeOutput(locationsTop3Lose4, "Berdych T.", "Lose4")
writeOutput(locationsTop3Lose5, "Berdych T.", "Lose5")

output_file.close()