void setup ()
{
  Serial.begin (115200);
  Serial.println ( "Ready" );
}
void loop ()
{
  char ch;
  if (Serial.available())
  {
    ch = Serial.read();
    Serial.print ( ch );
  }
}
