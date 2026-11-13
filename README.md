# Śmieci kosmiczne według właściciela

## Zespół

- Analiza — [imię i nazwisko]
- CLI — [imię i nazwisko]
- Zapis i uruchomienie — [imię i nazwisko]

## Uruchomienie startera

W katalogu repozytorium wykonaj:

```text
poetry install
poetry run python main.py --help
poetry run python main.py --preview 3
```

## Opis rozwiązania

[Uzupełnijcie opis, polecenie report zapisujące CSV i polecenie summary zapisujące PNG.]

## Zależności

[Wpiszcie wymagania dotyczące Pythona i Poetry oraz opiszcie użyte pakiety.]

## Konfiguracja Poetry

Skonfigurujcie projekt w dostarczonym `pyproject.toml`. Uzupełnijcie opis i autorów oraz sprawdźcie zakres wersji Pythona.

W terminalu, w katalogu zawierającym `pyproject.toml`, dodajcie wymagane biblioteki:

```
poetry add pandas matplotlib
```

Aby dodać kolejny pakiet, wpiszcie `poetry add NAZWA_PAKIETU`, np. `poetry add numpy`, jeśli używacie NumPy bezpośrednio w kodzie. Polecenie instaluje pakiet i aktualizuje `pyproject.toml` oraz `poetry.lock`. Zapiszcie oba pliki w Git. Po sklonowaniu repozytorium zależności instaluje się poleceniem `poetry install`.

Zakres konfiguracji znajdziecie w dokumentacji https://python-poetry.org/docs/pyproject/ oraz w wykładzie dostępnym na Classroomie.

