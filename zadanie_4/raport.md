# Raport – Analiza metod decyzyjnych TOPSIS i SPOTIS

## 1. Dane

Analiza dotyczy 4 alternatyw ocenianych względem 3 kryteriów: koszt (min), jakość (max), czas (min).

## 2. Wagi

Wagi wyznaczono automatycznie metodą entropii na podstawie zmienności danych.

## 3. Metody

Zastosowano dwie metody wielokryterialnego podejmowania decyzji:

- **TOPSIS** – opiera się na odległości od idealnych rozwiązań.
- **SPOTIS** – minimalizuje odległość od tzw. punktu referencyjnego.

## 4. Wyniki

| Alternatywa | Wynik TOPSIS | Pozycja TOPSIS | Wynik SPOTIS | Pozycja SPOTIS |
| ----------- | ------------ | -------------- | ------------ | -------------- |
| A1          | 0.401769     | 3              | 0.489488     | 3              |
| A2          | 0.201722     | 4              | 0.497313     | 4              |
| A3          | 0.909144     | 1              | 0.410559     | 1              |
| A4          | 0.625711     | 2              | 0.421736     | 2              |

_(Dane pojawią się po uruchomieniu skryptu)_

## 5. Wnioski

- TOPSIS i SPOTIS dają podobne, ale nie identyczne rankingi.
- W analizowanym przypadku najlepiej wypada alternatywa **A3** (zgodnie z rankingiem).
- Różnice wynikają z różnych założeń metody: TOPSIS uwzględnia oba bieguny (idealny i anty-idealny), SPOTIS skupia się na referencyjnym punkcie kompromisu.
