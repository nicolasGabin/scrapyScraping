import scrapy

class topScorers(scrapy.Spider):
    name = "topScorers"

    def start_requests(self):
        urls = [
                "https://www.bbc.com/sport/football/champions-league/top-scorers"
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rowList = response.css("tr > td::text").getall()
        nameList = response.css("tr > td:nth-child(2) > div > div > span:nth-child(1) > span::text").getall()
        groupedNameList = [nameList[n:n+4] for n in range(0, len(nameList), 4)]
        groupedRowList = [rowList[n:n+9] for n in range(0, len(rowList), 9)]
        for number, row in enumerate(groupedRowList):
            yield {
                    "rank":row[0],
                    "playerName":groupedNameList[number][0],
                    "teamName":groupedNameList[number][2],
                    "goals":row[1],
                    "assists":row[2],
                    "played":row[3],
                    "goalsPer90":row[4],
                    "minutesPerGoal":row[5],
                    "totalShots":row[6],
                    "goalConversion":row[7],
                    "shotAccuracy":row[8]
                    }
        # response.css("th > span > span:nth-child(1)::text").getall() gets Goals, Assists, Played, Mins per Goal
        # response.css("th::text").getall() gets Name, Goals per 90, Total Shots, Goal Conversion, Shot accuracy
        # response.css("tr > td::text").getall() get all table items except name and teamName
        # response.css("tr > td:nth-child(2) > div > div > span:nth-child(1) > span::text").getall() get names
        #page = response.url.split("/")[-2]
        #filename = f"topScorers-{page}.html"
        #Path(filename).write_bytes(topScorers)
        #self.log(f"Saved file {filename}")
