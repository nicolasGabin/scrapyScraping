import scrapy

class topScorers(scrapy.Spider):
    name = "topAssists"

    def start_requests(self):
        urls = [
                "https://www.bbc.com/sport/football/champions-league/top-scorers/assists"
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rowList = response.css("tr > td::text").getall()
        nameList = response.css("tr > td:nth-child(2) > div > div > span:nth-child(1) > span::text").getall()
        groupedNameList = [nameList[n:n+4] for n in range(0, len(nameList), 4)]
        groupedRowList = [rowList[n:n+10] for n in range(0, len(rowList), 10)]
        for number, row in enumerate(groupedRowList):
            yield {
                    "rank":row[0],
                    "playerName":groupedNameList[number][0],
                    "teamName":groupedNameList[number][2],
                    "assists":row[1],
                    "goals":row[2],
                    "played":row[3],
                    "chancesCreated":row[4],
                    "chancesPer90":row[5],
                    "totalPasses":row[6],
                    "passesComplete":row[7],
                    "passesIncomplete":row[8],
                    "passAccuracy":row[9]
                    }