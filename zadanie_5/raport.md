# Zadanie 5

## 1. Web Scraping

Web scraping to proces automatycznego pobierania danych z internetu, najczęściej w postaci HTML, JSON lub XML. Może być używany do ekstrakcji informacji z różnych stron internetowych, takich jak dane o produktach, ceny, artykuły, czy dane statystyczne. Web scraping jest szeroko wykorzystywany w analizach rynkowych, monitoringu cen, zbieraniu danych do badań oraz w innych dziedzinach.

## 2. Biblioteki

Dla tej dziedziny wybrałem dwie popularne biblioteki:

- **BeautifulSoup** – biblioteka, która pozwala na łatwą analizę i ekstrakcję danych z dokumentów HTML i XML.
- **Scrapy** – bardziej zaawansowane narzędzie do web scrapingu, które umożliwia tworzenie pełnych aplikacji do zbierania danych.

## 3. Opisy bibliotek

### BeautifulSoup

- [Dokumentajca](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Repozytorium](https://github.com/wention/BeautifulSoup4)

```bash
  pip3 install beautifulsoup4
  python3 beautifulsoup_example.py
```

BeautifulSoup to biblioteka Pythona służąca do parsowania dokumentów HTML i XML. Umożliwia łatwe i intuicyjne manipulowanie drzewem DOM w celu wyciągania danych ze stron internetowych.

#### Zalety

- Łatwość użycia: BeautifulSoup jest jedną z najprostszych bibliotek do scrapowania, szczególnie dla początkujących.
- Elastyczność: Można ją łatwo zintegrować z innymi narzędziami i bibliotekami, co sprawia, że jest bardzo elastyczna.
- Przyjazna dokumentacja: Dokumentacja jest bardzo przystępna i zawiera dużą ilość przykładów, które pomagają w szybkim rozpoczęciu pracy z tą biblioteką.
- Wsparcie dla różnych parserów: BeautifulSoup może działać z różnymi parserami (np. lxml, html.parser, html5lib), co daje większą kontrolę nad procesem parsowania.

#### Wady

- Wolniejsze w porównaniu do Scrapy: BeautifulSoup jest szybsze przy małych i średnich ilościach danych, ale przy dużych ilościach danych (np. setki stron internetowych) może być mniej wydajne niż Scrapy.
- Brak wbudowanego wsparcia dla asynchronicznych zapytań: BeautifulSoup nie ma wbudowanego wsparcia dla równoczesnego wykonywania zapytań HTTP, co sprawia, że w przypadku bardziej wymagających projektów trzeba ręcznie zarządzać wątkami lub procesami.
- Brak zaawansowanych funkcji: BeautifulSoup jest bardziej podstawową biblioteką i nie oferuje wszystkich funkcji, które znajdziesz w Scrapy (np. rotacja proxy, zaawansowane zarządzanie żądaniami HTTP).

### Scrapy

- [Dokumentajca](https://docs.scrapy.org/en/latest/)
- [Repozytorium](https://github.com/scrapy/scrapy)

```bash
  pip3 install scrapy
  cd scrapy_example
  python3 -m scrapy crawl quotes
```

Scrapy to framework do tworzenia aplikacji służących do scrapowania danych z internetu. Jest to potężne narzędzie do tworzenia pająków internetowych (web crawlers), które mogą zbierać dane ze stron internetowych i zapisywać je w różnych formatach (np. JSON, CSV, XML).

#### Zalety

- Prosta konfiguracja: Scrapy oferuje prostą konfigurację projektu, dzięki czemu łatwo jest rozpocząć scrapowanie. Wystarczy zainstalować Scrapy i stworzyć projekt, by zacząć zbierać dane.
- Wydajność: Scrapy jest zoptymalizowany pod kątem wydajności. Potrafi równocześnie obsługiwać setki, a nawet tysiące zapytań.
- Wsparcie społeczności: Scrapy ma bardzo dużą społeczność użytkowników i programistów, co sprawia, że łatwo znaleźć pomoc online, w tym gotowe rozwiązania, tutoriale i przykłady.
- Dobra dokumentacja: Dokumentacja Scrapy jest bogata i zawiera wiele przykładów, co ułatwia szybkie wdrożenie.

#### Wady

- Wymaga zaawansowanej konfiguracji: Dla bardziej zaawansowanych zastosowań, takich jak rozpraszanie zapytań (distributed crawling), Scrapy może wymagać bardziej zaawansowanej konfiguracji.
- Nie obsługuje JavaScript bez dodatkowych narzędzi: Scrapy nie obsługuje JavaScriptu w standardzie, więc do obsługi dynamicznych stron należy wykorzystać dodatkowe narzędzia (np. Splash lub Selenium).
- Wymaga Pythona 3.6+: Scrapy nie działa na starszych wersjach Pythona, co może być problemem w przypadku korzystania z przestarzałych wersji.
