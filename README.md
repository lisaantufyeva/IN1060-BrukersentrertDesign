# IN-1060_Arduino


Hjemmetrening PT er en maskin som skal guide brukere gjennom en treningsøkt. Sammen med maskinen følger det med kort som holder forskjellige treningsøkt av ulike varighet avhengig av type trening. Under prototyping hadde vi tilgang til ett kort og én tag, derfor bruker vi de i videoene. Det valgte kortet skal skannes via en kortleser og brukeren selv velger nivå avhengig av erfaringen brukeren har med trening og øvelser. Når brukeren velger nivå ved å trykke på knappen (1, 2 eller 3). Når nivået er valgt skal treningsprogrammet avspilles via en innebygd høyttaler. Hver treningsøkt består av ett sett med øvelser, og hver øvelse har består av to lydspor: en grundig forklaring av øvelsen, og en gjennomføring. Brukeren selv bestemmer når den vil ta pauser, ved å trykke på pause/resume knapp og kan gjenstarte treningen ved å klikke på samme knapp. Brukeren har også mulighet til å spille av forrige/neste lydsporet, dersom den har behov for å høre forklaring på nytt eller hoppe forbi forklaringen. I tillegg er det enkelt for brukeren å bytte mellom nivå, dersom nivået ble valgt ved en feiltakelse.

Hjemmetrening PT er laget med Arduino Uno som hovedkomponent som kontrollerer kommunikasjon med RFID/NFC leser, registrerer brukerinput og kommuniserer med Raspberry Pi.

Prosjektbeskrivelse: https://www.uio.no/studier/emner/matnat/ifi/IN1060/v20/prosjekter-20/interlinked/

Link til promovideo: ​https://vimeo.com/426578205

Tegning av kretsen:
![PT hjemmetrening_bb](https://user-images.githubusercontent.com/65827422/151951096-6fbc04ce-5131-466e-bda0-ed5ca51d9e17.png)
