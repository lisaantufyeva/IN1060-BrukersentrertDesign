#include <SPI.h>
#include <MFRC522.h>

#include <SoftwareSerial.h>
#include <DFMiniMp3.h>

SoftwareSerial mySerial(2, 3);

#define RST_PIN 9 // Configurable, see typical pin layout above
#define SS_PIN 10 // Configurable, see typical pin layout above

/* RFID/NFC */
MFRC522 rfid(SS_PIN, RST_PIN); // Create MFRC522 instance

/*KNAPPER*/

const int nivaa1 = 4;
const int nivaa2 = 3;
const int nivaa3 = 2;

const int pauseKnapp = 5;
bool paused = false;

const int prevKnapp = 6;
const int nextKnapp = 7;

unsigned long sisteKnappetrykk = 0;
const int debounceDelay = 500;
uint8_t kortSkannet;

void setup()
{

  pinMode(nivaa1, INPUT);
  digitalWrite(nivaa1, HIGH);
  pinMode(nivaa2, INPUT);
  digitalWrite(nivaa2, HIGH);
  pinMode(nivaa3, INPUT);
  digitalWrite(nivaa3, HIGH);
  pinMode(pauseKnapp, INPUT);
  digitalWrite(pauseKnapp, HIGH);
  pinMode(prevKnapp, INPUT);
  digitalWrite(prevKnapp, HIGH);
  pinMode(nextKnapp, INPUT);
  digitalWrite(nextKnapp, HIGH);
  /*RFID/NFC*/
  Serial.begin(115200);

  SPI.begin();
  rfid.PCD_Init();
  //Serial.println(F("Les kort: "));
  //Serial.println();
}

void loop()
{
  //Serial.println("loop");
  int wid = sjekkWorkoutNr();
  int niva = velgNivaa();
  int pausePlay = pauseWorkout(); // 
  int prev = playPrev();
  int next = playNext();
  String msg;

  if (wid != 0 && niva != 0)
  {
    msg = playMessageToPi(wid, niva);
    Serial.println(msg);
  }
  if (wid !=0 && next != 0)
  {
    msg = nextMessageToPi(next);
    Serial.println(msg);
  }
  if (wid != 0 && prev != 0)
  {
    msg = prevMessageToPi(prev);
    Serial.println(msg);
  }

  if (wid != 0 && pausePlay != 0)
  {
 
    paused = true;
    msg = pauseMessageToPi(pausePlay);
    Serial.println(msg);
    
  }
    while(paused)
    {
      int buttonState;
      buttonState= (digitalRead(pauseKnapp));
      
      if (buttonState == LOW)
      {
        //Serial.println(buttonState);
        delay(debounceDelay);
        paused = false;
        msg = resumeMessageToPi(pausePlay);
        Serial.println(msg);
      }
    }

}

String resumeMessageToPi(int pausePlay)
{
  String resumeMld = "RESUME ";
  resumeMld += "0 ";
  resumeMld += String(pausePlay);
  return(resumeMld);
}

String playMessageToPi(int wNr, int niva)
{
  String playMld = "PLAY ";
  playMld += String(wNr);
  playMld += " ";
  playMld += String(niva);
  return(playMld);
}

String pauseMessageToPi(int pausePlay)
{
  String pauseMld = "PAUSE ";
  pauseMld += "0 ";
  pauseMld += String(pausePlay);
  return(pauseMld);
}

String prevMessageToPi(int prev)
{
  String prevMld= "PREV ";
  prevMld += "- ";
  prevMld += String(prev);
  return(prevMld);
}

String nextMessageToPi(int next)
{
  String nextMld= "NEXT ";
  nextMld += "+ ";
  nextMld += String(next);
  return(nextMld);
}


/* PAUSER AVSPILLING*/
int pauseWorkout()
{
  int buttonState;

  buttonState = digitalRead(pauseKnapp);

  if (buttonState == LOW)
  {
    //Serial.println("Pause button")
    delay(debounceDelay);

    return 1;
  }
  return 0; 
}

/* SPILL AV NESTE*/
int playNext()
{
  int buttonState;

  buttonState = digitalRead(nextKnapp);

  if (buttonState == LOW)
  {
    //Serial.println("Play next");
    delay(debounceDelay);

    return 1;
  }
  return 0; 
}

/* SPILL AV FORRIGE*/
int playPrev()
{
  int buttonState;

  buttonState = digitalRead(prevKnapp);

  if (buttonState == LOW)
  {
    //Serial.println("Play previous");
    delay(debounceDelay);

    return 1;
  }
  return 0; 
}

/*IDENTIFISERER WORKOUT*/

int sjekkWorkoutNr()
{

  int newRead = readCard();

  if (newRead == 1)
  {
    String content = "";

    for (byte i = 0; i < rfid.uid.size; i++)
    {
      content.concat(String(rfid.uid.uidByte[i] < 0x10 ? " 0" : " "));
      content.concat(String(rfid.uid.uidByte[i], HEX));
    }

    content.toUpperCase();

    //change here the UID of the card/cards that you want to give access
    if (content.substring(1) == "66 73 9A 1F")
    {
      return 1;
    }
    else if (content.substring(1) == "A9 2F 7D 63")
    {
      return 2;
    }
    else
    {
      return 0;
    }
  }
  else
  {
    return 0;
  }
}

/*LESER KORT*/

int8_t readCard()
{
  // sjekeker om det er nye kort og velger et av kortene
  if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial())
  {
    rfid.PICC_HaltA(); // Stop reading
    return 1;
  }
  rfid.PICC_HaltA(); // Stop reading
  return 0;
}

/*SJEKKER HVILKEN NIVÅ-KNAPP */

int velgNivaa()
{
  int buttonState;

  buttonState = digitalRead(nivaa1);

  if (buttonState == LOW)
  {
    delay(debounceDelay);
    return 1;
  }

  buttonState = digitalRead(nivaa2);

  if (buttonState == LOW)
  {
    delay(debounceDelay);
    return 2;
  }

  buttonState = digitalRead(nivaa3);

  if (buttonState == LOW)
  {
    delay(debounceDelay);
    return 3;
  }

  return 0;
}
