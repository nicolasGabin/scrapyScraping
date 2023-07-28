import scrapy

class topScorers(scrapy.Spider):
    name = "table"

    def start_requests(self):
        urls = [
                "https://www.bbc.com/sport/football/champions-league/table"
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # response.css("div.qa-tables > div").getall() get all groups
        values = response.css("div.qa-tables > div > div > table > tbody > tr > td::text").getall()
        valuesTeams = [values[n:n+9] for n in range(0, len(values), 9)]
        valuesTeamsGroups = [valuesTeams[n:n+4] for n in range(0, len(valuesTeams), 4)]
        # gets all team names
        teamNames = response.css("tr > td:nth-child(3) > abbr > span::text, tr > td:nth-child(3) > a > abbr > span::text").getall()
        teamNamesGrouped = [teamNames[n:n+4] for n in range(0, len(teamNames), 4)]
        groups = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for groupNumber, row in enumerate(valuesTeamsGroups):
            for teamNumber, item in enumerate(row):
                yield {
                    "group":groups[groupNumber],
                    "rank":valuesTeamsGroups[groupNumber][teamNumber][0],
                    "teamName":teamNamesGrouped[groupNumber][teamNumber],
                    "played":valuesTeamsGroups[groupNumber][teamNumber][1],
                    "won":valuesTeamsGroups[groupNumber][teamNumber][2],
                    "drawn":valuesTeamsGroups[groupNumber][teamNumber][3],
                    "lost":valuesTeamsGroups[groupNumber][teamNumber][4],
                    "for":valuesTeamsGroups[groupNumber][teamNumber][5],
                    "against":valuesTeamsGroups[groupNumber][teamNumber][6],
                    "gd":valuesTeamsGroups[groupNumber][teamNumber][7],
                    "points":valuesTeamsGroups[groupNumber][teamNumber][8],
                }