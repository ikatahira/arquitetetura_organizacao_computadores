int num = 0; //Variable global que almacena el dato ingresado
			//por el monitor serial, debe estar inicializada en 0.
void setup()
{
  //Se definen los pines como salidas digitales.
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  Serial.begin(9600); //Se inicia la comunicación serial
  					//con velocidad (baudios) de transmisión
  					//de datos 9600bits/s en función setup()
}

void loop()
{ 
  if(Serial.available() > 0){ 
    //Si hay datos (bytes) disponibles en el buffer de recepción del
    //puerto serial, para ser leídos por el puerto serial... 
    //...se dan las siguientes instrucciones
  	num = Serial.readString().toInt();
    //Se usa la instrucción Serial.readString() que permite leer
    //una cadena de caracteres, lo que se ingrese por el puerto
    //serial se lee como una cadena de caracter, y luego se
    //usa la instrucción toInt() que convierte una cadena de
    //caracteres a entero.
    int cont = 9; //Se inicializa en 9, referente al pin 9.
    while(num > 0){ //num va disminuyendo su valor hasta llegar a 0.
      if(num % 2 == 0){
        //Si el residuo de dividir num por 2 es cero, ese es un bit
        //igual a cero, entonces el LED se debe mostrar apagado.
        digitalWrite(cont, LOW);
    	delay(20);//espere 0,02 segundos
        cont--;//y ahora es el siguiente LED
      }
      else if(num % 2 == 1){
        //Si el residuo de dividir num por 2 es uno, ese es un bit
        //igual a uno, entonces el LED se debe mostrar encendido.
        digitalWrite(cont, HIGH);
    	delay(20);//espere 0,02 segundos
        cont--;//y ahora es el siguiente LED
      }
      num = num / 2;//En cada ciclo la variable de control debe disminuirse
    }
    while(cont >=  2){
      //Luego de que num = 0, falta por tener en cuenta el resto
      //de bits iguales a cero, es decir, que se deben mostrar LEDS
      //apagados.
      digitalWrite(cont, LOW);
   	  delay(20);//espere 0,02 segundos
      cont--;//y ahora es el siguiente LED
    }
  }
}