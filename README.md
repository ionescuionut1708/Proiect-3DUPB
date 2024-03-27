# Proiect tabără - 3DUPB Ediția 2023

## Directorul 1

Proiectul este o aplicație web simplă care permite utilizatorilor să se înregistreze, să se conecteze și să vizualizeze scorurile pentru două jocuri: "Balloons Madness" și "Endless Runner". 

Structura proiectului:
- Pagina de autentificare (login.html): Permite utilizatorilor existenți să se conecteze folosind numele de utilizator și parola. De asemenea, oferă un link către pagina de înregistrare pentru utilizatorii noi.
- Pagina de înregistrare (signup.html): Permite utilizatorilor noi să creeze un cont furnizând un nume de utilizator, o adresă de e-mail și o parolă.
- Pagina principală (meniu.html): După autentificare, utilizatorii sunt redirecționați către această pagină, care afișează două carduri reprezentând jocurile disponibile. Fiecare card conține o imagine, un titlu și o descriere scurtă a jocului. Utilizatorii pot face clic pe un card pentru a vizualiza scorurile mari pentru jocul respectiv.
- Pagina de scoruri mari (highScores.html): Afișează o listă a utilizatorilor și scorurile lor pentru jocul selectat. De asemenea, are un buton "Back to games" care redirecționează utilizatorul înapoi la pagina principală.

Fișierul JavaScript (script.js) conține două funcții:
1. `pages(event)`: Gestionează navigarea între pagini în funcție de ID-ul butonului apăsat.
2. `highScores(game)`: Redirecționează utilizatorul către pagina de scoruri mari atunci când se face clic pe un card de joc.

## Director 2:
În directorul 2 al proiectului se află fișierul index.html, alături de alte directoare precum node_modules, public, src și fișiere de configurare precum .gitignore, package-lock.json și vite.config.js.
Prezența directorului node_modules și a fișierelor package-lock.json sugerează că proiectul utilizează Node.js și NPM pentru gestionarea dependențelor. Directorul public poate conține active statice, cum ar fi imagini sau fișiere CSS. Directorul src conține, probabil, codul sursă JavaScript și componentele Vue ale aplicației tale.

Fișierul vite.config.js indică faptul că proiectul utilizează Vite, un instrument de construcție rapidă pentru dezvoltarea web modernă.

Pentru a rula acest proiect, ar trebui să instalezi dependențele folosind `npm install`, iar apoi să pornești un server de dezvoltare folosind Vite (`npm run dev` sau `vite`, în funcție de configurația proiectului tău).

## Directorul 3:
În folderul 3 al proiectului se află fișierul DBManager.py, alături de alte fișiere precum balloons.jpg, balloons2.jpg și runner.jpg.

Fișierul DBManager.py este responsabil pentru gestionarea interacțiunilor cu baza de date MongoDB. Iată o scurtă explicație a conținutului său:

1. Se importă modulele necesare: pymongo pentru interacțiunea cu MongoDB, certifi pentru gestionarea certificatelor SSL/TLS și gridfs pentru stocarea fișierelor în baza de date.

2. Se stabilește conexiunea la baza de date MongoDB folosind un URI și se selectează baza de date "web_dev".

3. Se creează o instanță GridFS pentru stocarea fișierelor în baza de date.

4. Se definesc trei colecții: "users", "games" și "scores".

5. Se inserează documente în colecția "users" folosind `userCollection.insert_many()`. Aceasta returnează ID-uri unice pentru fiecare utilizator inserat.

6. Se definește o listă de jocuri (`gameList`) cu titluri, descrieri și imagini asociate.

7. Se încarcă imaginile jocurilor în baza de date folosind GridFS. ID-urile imaginilor încărcate sunt atribuite câmpului "image" al fiecărui joc.

8. Se inserează documentele jocurilor în colecția "games" folosind `gamesCollesction.insert_many()`.

9. Se definește o listă de scoruri înalte (`highScoresList`) care asociază fiecare scor cu un joc și un utilizator.

10. Se inserează documentele de scor înalt în colecția "scores" folosind `highScoresCollection.insert_many()`.

Codul include, de asemenea, câteva linii comentate care demonstrează cum se pot asocia ID-urile utilizatorilor și jocurilor cu documentele din colecția "scores". Cu toate acestea, această parte este comentată în codul furnizat.

Observații:
- Codul utilizează un fișier de certificat (certifi) pentru a stabili o conexiune securizată la baza de date MongoDB.
- Credențialele pentru conexiunea la baza de date (URI-ul) sunt hard-codate în cod, ceea ce nu este o practică recomandată. În schimb, ar trebui să fie stocate în variabile de mediu sau într-un fișier de configurare separat.
- Erorile la încărcarea imaginilor sunt gestionate folosind declarații try-except, iar erorile sunt afișate în consolă.

## Directorul 4:
Fișierul routes.py conține rutele și logica serverului pentru aplicația web, utilizând framework-ul Flask. 

Iată o explicație a funcționalităților principale ale acestui fișier:
1. Se importă modulele necesare, inclusiv Flask pentru crearea aplicației web, pymongo pentru interacțiunea cu MongoDB, certifi pentru gestionarea certificatelor SSL/TLS și gridfs pentru stocarea și preluarea fișierelor din baza de date.

2. Se stabilește conexiunea la baza de date MongoDB folosind un URI și se selectează baza de date "web_dev".

3. Se creează instanțe ale colecțiilor "users", "games" și "scores" din baza de date.

4. Se creează o instanță a aplicației Flask și se configurează CORS (Cross-Origin Resource Sharing) pentru a permite cereri de la origini diferite.

5. Se definește un decorator de gestionare a erorilor (`@app.errorhandler(Exception)`) pentru a prinde și a returna erorile ca răspunsuri JSON.

6. Se definesc mai multe rute pentru diferite funcționalități ale aplicației:
   - `/getGames`: Returnează o listă de jocuri din colecția "games".
   - `/getImageById/<id>`: Returnează imaginea asociată unui joc pe baza ID-ului imaginii.
   - `/getScores`: Returnează o listă de scoruri din colecția "scores".
   - `/getScoresByGameName/<game>`: Returnează scorurile pentru un anumit joc pe baza numelui jocului.
   - `/getScoreById/<id>`: Returnează un singur scor pe baza ID-ului său.
   - `/addScore`: Adaugă un nou scor în colecția "scores" folosind o cerere POST sau actualizează un scor existent folosind o cerere PUT.
   - `/login`: Gestionează autentificarea utilizatorilor pe baza numelui de utilizator și a parolei.
   - `/register`: Gestionează înregistrarea utilizatorilor noi, validând datele furnizate și verificând unicitatea numelui de utilizator și a adresei de e-mail.

7. Fiecare rută este decorată cu `@cross_origin(supports_credentials=True)` pentru a permite cereri de la origini diferite și pentru a suporta acreditările (cum ar fi cookie-urile).

8. În funcția `get_image`, ID-ul imaginii este convertit într-un obiect ObjectId și este utilizat pentru a prelua datele imaginii din GridFS. Datele imaginii sunt apoi returnate ca răspuns.

9. În funcțiile `add_scores`, `login` și `register`, datele cererii sunt extrase din obiectul `request.json` și sunt validate pentru a se asigura că sunt furnizate toate câmpurile necesare.

10. Funcția `register` verifică, de asemenea, unicitatea numelui de utilizator și a adresei de e-mail înainte de a insera un nou utilizator în colecția "users".

11. Dacă fișierul este rulat direct (`if __name__ == "__main__"`), serverul Flask este pornit prin apelarea metodei `app.run()`.

Acest fișier servește ca backend pentru aplicația web, gestionând interacțiunile cu baza de date, autentificarea utilizatorilor, înregistrarea și furnizarea de date pentru frontend prin intermediul API-urilor RESTful.

##Bug-uri și vulnerabilități:
1. Parole în text simplu:
   - În fișierul `DBManager.py`, parolele utilizatorilor sunt stocate în text simplu în baza de date. Aceasta este o practică nesigură, deoarece oricine cu acces la baza de date poate vedea parolele. În schimb, ar trebui să folosești o funcție de hashing criptografică puternică (cum ar fi bcrypt) pentru a stoca hash-urile parolelor.

2. Lipsa validării datelor de intrare:
   - În fișierul `routes.py`, în funcțiile precum `add_scores`, `login` și `register`, datele primite de la client sunt folosite direct fără o validare adecvată. Aceasta poate duce la probleme de securitate, cum ar fi injecția SQL sau injecția NoSQL, dacă datele de intrare conțin caractere sau șabloane malițioase.
   - Ar trebui să implementezi o validare riguroasă a datelor de intrare, cum ar fi curățarea și validarea datelor înainte de a le folosi în interogările bazei de date.

3. Gestionarea erorilor și mesajele de eroare:
   - În fișierul `routes.py`, erorile sunt capturate și returnate ca răspunsuri JSON folosind `@app.errorhandler(Exception)`. Cu toate acestea, returnarea directă a mesajelor de eroare ca răspuns poate dezvălui detalii sensibile despre aplicația ta, cum ar fi stiva de apeluri sau informații de depanare.
   - În schimb, ar trebui să folosești mesaje de eroare generice în răspunsurile către client și să înregistrezi erorile detaliate în fișierele jurnal pe server pentru depanare.

4. Lipsa autorizării:
   - În fișierul `routes.py`, nu există o verificare a autorizării pentru rutele sensibile, cum ar fi `/addScore` sau `/getScoreById/<id>`. Orice client autentificat poate accesa și modifica scorurile altor utilizatori.
   - Ar trebui să implementezi o autorizare adecvată, cum ar fi verificarea dacă utilizatorul autentificat are permisiunea de a efectua acțiuni specifice sau de a accesa anumite resurse.

5. Credențiale hard-codate:
   - În fișierele `DBManager.py` și `routes.py`, credențialele bazei de date (URI-ul) sunt hard-codate direct în cod. Aceasta este o practică nesigură, deoarece oricine cu acces la codul sursă poate vedea credențialele.
   - Ar trebui să stochezi credențialele sensibile în variabile de mediu sau într-un fișier de configurare separat care nu este comis în sistemul de control al versiunilor.

6. CORS permisiv:
   - În fișierul `routes.py`, CORS este configurat folosind `CORS(app)` fără a specifica origini permise specifice. Aceasta permite oricărui domeniu să facă cereri către aplicația ta.
   - Ar trebui să restricționezi CORS pentru a permite cereri doar de la originile de încredere și necesare.

7. Lipsa protecției CSRF:
   - Nu există o protecție împotriva falsificării cererilor între site-uri (CSRF) implementată în aplicație. Aceasta poate permite atacatorilor să efectueze acțiuni nedorite în numele utilizatorilor autentificați.
   - Ar trebui să implementezi un mecanism de protecție CSRF, cum ar fi tokenuri CSRF, pentru a preveni atacurile CSRF.

## Contribuții:

Contribuțiile sunt binevenite! Dacă găsiți alte bug-uri, aveți sugestii de îmbunătățire sau doriți să adăugați noi funcționalități, vă rugăm să deschideți un issue sau să trimiteți un pull request.
