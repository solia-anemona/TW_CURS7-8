# Student Directory — proiect inițial

Exercițiu de aprofundare pentru cursurile 7 și 8 de Tehnologii Web, anul universitar 2026–2027.

Proiectul oferă structura inițială a aplicației Student Directory și permite obținerea listei studenților din exemplul prezentat la curs. Completați cele șase secțiuni marcate `TODO` în cod și răspunsurile din acest fișier, conform enunțului exercițiului și materialelor de curs.

## Instalare și pornire

Utilizați Python 3.10 sau o versiune ulterioară compatibilă cu Django 5.2. Verificați versiunea instalată prin comanda `python3 --version` pe macOS/Linux sau `py --version` pe Windows.

Dezarhivați fișierul `student-directory-starter.zip` și deschideți un terminal în directorul care conține folderul extras. Executați comenzile corespunzătoare sistemului de operare. Dacă terminalul este deja deschis în folderul `student-directory-starter`, omiteți comanda `cd student-directory-starter`.

macOS / Linux:

```sh
cd student-directory-starter
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py check
python manage.py migrate
python manage.py test students
python manage.py runserver
```

Windows PowerShell:

```powershell
cd student-directory-starter
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py check
python manage.py migrate
python manage.py test students
python manage.py runserver
```

Dacă activarea mediului virtual este blocată în PowerShell, omiteți comanda de activare și utilizați `.\.venv\Scripts\python.exe` în loc de `python` în comenzile ulterioare.

După pornirea serverului, deschideți <http://127.0.0.1:8000/api/students/>. Răspunsul trebuie să conțină lista celor doi studenți, în format JSON. Opriți serverul cu Ctrl+C.

Ruta `/` nu este definită în proiect; accesarea adresei <http://127.0.0.1:8000/> returnează codul HTTP 404.

Datele despre studenți sunt fictive și sunt păstrate în lista Python `STUDENTS`. Comanda `migrate` creează tabelele standard Django în baza SQLite. Datele din `STUDENTS` nu sunt salvate în această bază.

Configurația proiectului și valoarea demonstrativă a parametrului `SECRET_KEY` sunt destinate exclusiv rulării locale.

## Structura proiectului

```text
student-directory-starter/
├── manage.py
├── requirements.txt
├── README.md
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── students/
    ├── __init__.py
    ├── apps.py
    ├── admin.py
    ├── models.py
    ├── migrations/__init__.py
    ├── urls.py
    ├── views.py
    └── tests.py
```

## E1 — Analiza structurii proiectului

Explicați pe scurt, cu propriile cuvinte, rolul fiecărui fișier:

| Fișier | Rol |
| --- | --- |
| `config/settings.py` | Configurația proiectului: aplicații instalate, middleware, baza de date, `ROOT_URLCONF`. |
| `config/urls.py` | Rutarea principală: trimite `api/` către rutele aplicației `students`. |
| `students/urls.py` | Leagă fiecare adresă a aplicației de funcția potrivită din `views.py`. |
| `students/views.py` | Funcțiile care primesc cererea și returnează răspunsul JSON; conține lista `STUDENTS`. |
| `students/tests.py` | Testele automate, care trimit cereri simulate și verifică răspunsul. |

Cererea ajunge la serverul Django, care creează un obiect `HttpRequest`. Aceasta trece prin middleware, apoi Django caută adresa în `config/urls.py` (via `ROOT_URLCONF`) și mai departe în `students/urls.py`. Funcția găsită din `views.py` este apelată cu cererea și cu parametrii din URL și returnează un răspuns (`JsonResponse`). Răspunsul trece înapoi prin middleware și ajunge la client. Dacă nicio rută nu se potrivește, rezultatul este 404.

## E2 — Completarea serviciului REST

Completați secțiunile marcate `TODO 1`–`TODO 5` în fișierele `students/views.py` și `students/urls.py`:

| Marcaj | Fișier | Sarcină | Cerință |
| --- | --- | --- | --- |
| `TODO 1` | `students/views.py` | Permiteți numai cereri GET pentru lista studenților, folosind decoratorul `require_GET`. | E2.c |
| `TODO 2` | `students/views.py` | Returnați datele studentului solicitat în format JSON, cu codul HTTP 200, sau un răspuns 404 dacă studentul nu există. Utilizați lista `STUDENTS`. | E2.a |
| `TODO 3` | `students/views.py` | Implementați verificarea stării serviciului: codul HTTP 200 și răspunsul JSON `{"status": "ok"}`. | E2.b |
| `TODO 4` | `students/urls.py` | Adăugați ruta pentru obținerea datelor unui student pe baza identificatorului său. | E2.d |
| `TODO 5` | `students/urls.py` | Adăugați ruta pentru verificarea stării serviciului, accesibilă la `/api/health/`. | E2.d |

În proiectul inițial, funcțiile `student_detail` și `health` returnează provizoriu codul HTTP 501. Rutele corespunzătoare nu sunt încă definite, astfel încât cererile către aceste adrese primesc răspunsul 404. Înlocuiți răspunsurile provizorii și adăugați rutele conform cerințelor.

## E3 — Testarea serviciului REST

### Verificarea răspunsurilor HTTP

Verificați cele cinci cereri din tabel. Coloana a doua descrie comportamentul proiectului inițial, iar coloana a treia indică rezultatele cerute după completarea exercițiului.

| Cerere | În proiectul inițial | După completarea exercițiului |
| --- | --- | --- |
| GET `/api/students/` | 200, lista celor doi studenți | 200, lista studenților |
| GET `/api/students/2/` | 404, rută nedefinită | 200, datele studentului Radu Ionescu |
| GET `/api/students/999/` | 404, rută nedefinită | 404, student inexistent |
| GET `/api/health/` | 404, rută nedefinită | 200, `{"status": "ok"}` |
| POST `/api/students/` prin Django Test Client | 200, metoda nu este încă restricționată | 405, metodă nepermisă |

Mențineți serverul pornit în primul terminal. Dacă l-ați oprit, porniți-l din nou prin comanda `python manage.py runserver`, din folderul proiectului, cu mediul virtual activat. Deschideți un al doilea terminal și executați următoarele comenzi pentru cererile GET:

```sh
curl -i http://127.0.0.1:8000/api/students/
curl -i http://127.0.0.1:8000/api/students/2/
curl -i http://127.0.0.1:8000/api/students/999/
curl -i http://127.0.0.1:8000/api/health/
```

Pe Windows, utilizați `curl.exe` în loc de `curl`.

Pentru verificarea cererii POST, accesați folderul `student-directory-starter` în al doilea terminal și activați mediul virtual:

macOS / Linux:

```sh
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Apoi deschideți consola Django:

```sh
python manage.py shell
```

Executați în consolă:

```python
from django.test import Client, override_settings

with override_settings(ALLOWED_HOSTS=["testserver"]):
    response = Client().post("/api/students/")
    print(response.status_code)
```

În consola interactivă standard, apăsați Enter pe o linie goală pentru a executa blocul. După aplicarea decoratorului `require_GET`, rezultatul trebuie să fie 405. Închideți consola prin comanda `exit()`.

Django Test Client nu verifică implicit protecția CSRF. O cerere POST trimisă prin curl poate primi codul 403 din cauza acestei protecții, înainte de executarea funcției care tratează cererea.

### Testul automat

În `students/tests.py`, completați secțiunea `TODO 6` prin adăugarea unui test pentru `/api/health/`. Testul trebuie să verifice atât codul HTTP 200, cât și conținutul JSON `{"status": "ok"}`.

Din folderul proiectului, cu mediul virtual activat, executați:

```sh
python manage.py test students
```

Proiectul inițial conține un singur test, pentru lista studenților. Acest test este deja implementat; executarea sa cu succes nu confirmă îndeplinirea celorlalte cerințe.

### Rezultatele verificărilor

Versiunile Python și Django utilizate: *De completat.*

Rezultatul executării testelor automate: *De completat cu rezultatul obținut.*

Dovezi pentru cele cinci cereri din tabel: *De completat cu rezultatele comenzilor sau cu capturi de ecran.*

## E4 — Explicarea soluției

1. De ce este utilizată metoda HTTP GET pentru obținerea informațiilor despre studenți?

   *Răspuns propriu: de completat.*

2. Care este diferența dintre `HttpResponse` și `JsonResponse` în Django?

   *Răspuns propriu: de completat.*

3. Cum identifică Django funcția care trebuie executată pentru un anumit URL?

   *Răspuns propriu: de completat.*

4. De ce este potrivit codul HTTP 404 atunci când studentul solicitat nu există?

   *Răspuns propriu: de completat.*

## Declararea utilizării instrumentelor de inteligență artificială

Dacă ați folosit instrumente de inteligență artificială, precizați care au fost acestea, pentru ce le-ați folosit și cum ați verificat rezultatele, conform fișei disciplinei. Dacă nu ați folosit astfel de instrumente, menționați acest lucru.

*Declarație individuală: de completat.*

## Predare

Includeți în arhiva cu rezolvarea individuală codul sursă, fișierul `README.md` cu răspunsurile și rezultatele verificărilor, testele și `requirements.txt`.

Înainte de arhivare, excludeți directoarele `.venv` și `__pycache__`, baza locală `db.sqlite3` și fișierele temporare. Nu includeți parole, token-uri sau chei API.
