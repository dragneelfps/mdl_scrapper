import re
from typing import Optional

import requests
from bs4 import BeautifulSoup, Tag

from mdl_scrapper.models.Search import SearchResult, SearchDrama


class DramaFinder:
    __baseUrlPatter = "https://mydramalist.com/search?q={}&page={}"

    def __init__(self, query: str):
        self.query = query
        self.curr_page = 1

    def find_next(self) -> SearchResult:
        url = self.__baseUrlPatter.format(self.query, self.curr_page)
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser")

        table = soup.find_all("div", id=re.compile("^mdl-"), class_="box")

        dramas = []

        for item in table:
            id = self.__get_id(item)
            title = self.__get_title(item)
            cover_url = self.__get_cover_url(item)
            ranking = self.__get_ranking(item)
            score = self.__get_score(item)
            description = self.__get_description(item)
            drama = SearchDrama(id, title, cover_url, ranking, score, description)

            dramas.append(drama)

        self.curr_page += 1

        return SearchResult(url, dramas)

    @staticmethod
    def __get_id(item: Tag) -> int:
        return item.attrs["id"].partition("mdl-")[2]

    @staticmethod
    def __get_title(item: Tag) -> str:
        return item.find("h6", class_="title").find("a").text

    @staticmethod
    def __get_cover_url(item: Tag) -> str:
        return item.find("img", class_="cover").attrs["src"]

    @staticmethod
    def __get_ranking(item: Tag) -> Optional[int]:
        node = item.find("div", class_="ranking")
        if node:
            return int(node.find("span").text.partition("#")[2])
        else:
            return None

    @staticmethod
    def __get_score(item: Tag) -> Optional[float]:
        node = item.find("span", class_="score")
        if node and len(node.text) > 0:
            return float(node.text)
        else:
            return None

    @staticmethod
    def __get_description(item: Tag) -> str:
        return item.find("div", class_="content").find_all("p")[-1].text
