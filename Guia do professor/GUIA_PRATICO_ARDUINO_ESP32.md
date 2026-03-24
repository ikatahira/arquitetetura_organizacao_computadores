# 🔧 Guia Prático Completo - Arduino e ESP32
## Manual do Professor com Resoluções Detalhadas

---

## 📋 Índice

1. [Módulo 2: Arduino (Semanas 7-10)](#módulo-2)
2. [Módulo 4: ESP32 (Semanas 16-18)](#módulo-4)
3. [Troubleshooting Comum](#troubleshooting)
4. [Lista de Materiais](#materiais)
5. [Códigos Comentados Completos](#códigos)

---

## Módulo 2: Arduino (Semanas 7-10)

### Semana 7: Introdução ao Arduino - Hardware

#### Exercício 1: Identificação de Componentes do Arduino
**Duração:** 30 minutos | **Peso:** 10 pontos

**Componentes a identificar:**

1. **Microcontrolador ATmega328P**
   - Cérebro do Arduino
   - Clock: 16 MHz
   - Flash: 32 KB (0.5 KB usado pelo bootloader)
   - SRAM: 2 KB
   - EEPROM: 1 KB
   - Arquitetura: Harvard modificada (von Neumann + cache)

2. **Pinos Digitais (0-13)**
   - GPIO configuráveis
   - Podem ser INPUT ou OUTPUT
   - Pinos 0-1: TX/RX (comunicação serial)
   - Pinos 3,5,6,9,10,11: PWM (~)
   - Pino 13: LED onboard

3. **Pinos Analógicos (A0-A5)**
   - Entrada analógica (ADC 10 bits = 0-1023)
   - Podem ser usados como digitais também
   - Tensão: 0-5V

4. **Pinos de Alimentação**
   - 5V: saída regulada 5V
   - 3.3V: saída regulada 3.3V (máx 50mA)
   - GND: terra (referência 0V)
   - VIN: entrada não regulada (7-12V)
   - IOREF: referência de tensão dos pinos I/O

5. **Botão de Reset**
   - Reinicia o programa
   - Volta ao setup()

6. **Conector USB**
   - Alimentação (5V até 500mA)
   - Comunicação serial com computador
   - Upload de código

7. **Jack de Alimentação Externa**
   - 7-12V DC (centro positivo)
   - Regulador linear 5V onboard

8. **LED Power (verde)**
   - Indica alimentação ligada

9. **LEDs TX/RX (amarelo)**
   - Piscam durante comunicação serial

10. **LED L (pino 13)**
    - LED onboard conectado ao pino 13
    - Útil para testes rápidos

**Critérios de Avaliação:**
- Identificação correta: 5 pts (0.5 pt cada componente)
- Descrição da função: 3 pts
- Especificações técnicas: 2 pts

**Respostas Esperadas dos Alunos:**
Os alunos devem ser capazes de apontar fisicamente cada componente na placa e explicar sua função básica.

---

#### Exercício 2: Circuito LED Piscante
**(Já detalhado no Guia Mestre HTML)**

---

#### Exercício 3: Teste de Botões
**Duração:** 25 minutos | **Peso:** 10 pontos

**Objetivo:** Criar circuito com entrada digital (botão) e saída digital (LED)

**Montagem do Circuito:**

```
Arduino                    Protoboard
                           
PIN 2 ─────────┬─────── Botão ─────── 5V
               │                      
               └─── [R 10kΩ] ─── GND  (pull-down)

PIN 13 ────── [R 220Ω] ────── LED+ ────── GND
```

**Explicação dos Resistores:**
- **Pull-down 10kΩ:** Garante que pino leia 0V quando botão não pressionado
- **Limitador 220Ω:** Protege LED (já explicado no Ex. 2)

**Código Completo Comentado:**

```cpp
/*
 * Controle de LED com Botão
 * Quando botão pressionado: LED liga
 * Quando botão solto: LED desliga
 */

const int BUTTON_PIN = 2;   // Pino do botão
const int LED_PIN = 13;     // Pino do LED

void setup() {
  // Configura pinos
  pinMode(BUTTON_PIN, INPUT);   // Botão como entrada
  pinMode(LED_PIN, OUTPUT);     // LED como saída
  
  // Inicializa Serial para debug
  Serial.begin(9600);
  Serial.println("Sistema iniciado!");
  Serial.println("Pressione o botão...");
}

void loop() {
  // Lê estado do botão
  int buttonState = digitalRead(BUTTON_PIN);
  
  // Debug: mostra estado no Serial Monitor
  Serial.print("Botão: ");
  Serial.println(buttonState);  // 0=solto, 1=pressionado
  
  // Se botão pressionado (HIGH)
  if (buttonState == HIGH) {
    digitalWrite(LED_PIN, HIGH);  // Liga LED
    Serial.println("LED LIGADO");
  }
  // Se botão solto (LOW)
  else {
    digitalWrite(LED_PIN, LOW);   // Desliga LED
    Serial.println("LED DESLIGADO");
  }
  
  // Pequeno delay para evitar leituras muito rápidas
  delay(100);
}
```

**Versão Melhorada com Debounce:**

```cpp
/*
 * Controle de LED com Botão + Debounce
 * Elimina ruídos de leitura (bouncing)
 */

const int BUTTON_PIN = 2;
const int LED_PIN = 13;
const int DEBOUNCE_DELAY = 50;  // 50ms

int lastButtonState = LOW;      // Estado anterior
int buttonState;                 // Estado atual
unsigned long lastDebounceTime = 0;

void setup() {
  pinMode(BUTTON_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Lê estado atual do botão
  int reading = digitalRead(BUTTON_PIN);
  
  // Se mudou, resetar timer de debounce
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }
  
  // Se passou tempo suficiente após última mudança
  if ((millis() - lastDebounceTime) > DEBOUNCE_DELAY) {
    // Se estado é diferente do atual
    if (reading != buttonState) {
      buttonState = reading;
      
      // Atualiza LED
      digitalWrite(LED_PIN, buttonState);
      
      Serial.print("Novo estado: ");
      Serial.println(buttonState ? "PRESSIONADO" : "SOLTO");
    }
  }
  
  // Salva estado para próxima iteração
  lastButtonState = reading;
}
```

**Critérios de Avaliação:**
- Montagem do circuito: 2.5 pts
- Código básico funcional: 3 pts
- Implementação de debounce: 2 pts
- Uso de Serial Monitor: 1 pt
- Documentação: 1.5 pts

**Erros Comuns:**
- Esquecer resistor pull-down → leituras instáveis
- Usar INPUT_PULLUP sem adaptar lógica
- Não fazer debounce → múltiplas leituras erradas
- delay() muito longo → resposta lenta

**Conceitos de Arquitetura:**
- **Entrada Digital:** GPIO configurado como INPUT
- **Níveis TTL:** 0V = LOW, 5V = HIGH
- **Debouncing:** Software filtra ruído mecânico do botão
- **Polling:** CPU constantemente verifica estado (vs. interrupção)

---

### Semana 8: Programação Arduino - Básico

#### Exercício 1: Blink Personalizado
**Duração:** 30 minutos | **Peso:** 10 pontos

**Tarefa:** Criar 3 padrões diferentes de pisca-pisca

**Resolução Completa:**

```cpp
/*
 * Três Padrões de Pisca-Pisca
 * Padrão 1: Rápido (200ms on/off)
 * Padrão 2: Médio (500ms on/off)  
 * Padrão 3: Lento (1000ms on/off)
 */

const int LED_PIN = 13;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("=== Padrões de Blink ===");
}

void loop() {
  // Padrão 1: RÁPIDO
  Serial.println("\n--- Padrão RÁPIDO ---");
  for(int i = 0; i < 10; i++) {  // 10 piscadas rápidas
    digitalWrite(LED_PIN, HIGH);
    delay(200);
    digitalWrite(LED_PIN, LOW);
    delay(200);
  }
  delay(1000);  // Pausa entre padrões
  
  // Padrão 2: MÉDIO
  Serial.println("\n--- Padrão MÉDIO ---");
  for(int i = 0; i < 5; i++) {   // 5 piscadas médias
    digitalWrite(LED_PIN, HIGH);
    delay(500);
    digitalWrite(LED_PIN, LOW);
    delay(500);
  }
  delay(1000);
  
  // Padrão 3: LENTO
  Serial.println("\n--- Padrão LENTO ---");
  for(int i = 0; i < 3; i++) {   // 3 piscadas lentas
    digitalWrite(LED_PIN, HIGH);
    delay(1000);
    digitalWrite(LED_PIN, LOW);
    delay(1000);
  }
  delay(2000);  // Pausa maior antes de recomeçar
}
```

**Versão Avançada com Funções:**

```cpp
/*
 * Padrões Modulares com Funções
 */

const int LED_PIN = 13;

// Função genérica para piscar
void blink(int times, int onTime, int offTime) {
  for(int i = 0; i < times; i++) {
    digitalWrite(LED_PIN, HIGH);
    delay(onTime);
    digitalWrite(LED_PIN, LOW);
    delay(offTime);
  }
}

// Função para fade in/out (PWM)
void fade() {
  // Fade in
  for(int brightness = 0; brightness <= 255; brightness++) {
    analogWrite(LED_PIN, brightness);
    delay(10);
  }
  // Fade out
  for(int brightness = 255; brightness >= 0; brightness--) {
    analogWrite(LED_PIN, brightness);
    delay(10);
  }
}

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  Serial.println("Padrão 1: Rápido");
  blink(10, 100, 100);
  delay(1000);
  
  Serial.println("Padrão 2: Médio");
  blink(5, 300, 300);
  delay(1000);
  
  Serial.println("Padrão 3: Lento");
  blink(3, 800, 800);
  delay(1000);
  
  Serial.println("Padrão 4: Fade");
  fade();
  delay(1000);
}
```

**Critérios de Avaliação:**
- 3 padrões implementados: 6 pts (2 pts cada)
- Uso de funções: 2 pts
- Clareza do código: 1 pt
- Comentários: 1 pt

---

#### Exercício 2: Botão com LED (Toggle)
**Duração:** 35 minutos | **Peso:** 10 pontos

**Tarefa:** Cada pressão do botão alterna estado do LED (liga/desliga)

**Código Completo:**

```cpp
/*
 * Toggle LED com Botão
 * Cada pressão alterna entre ON e OFF
 */

const int BUTTON_PIN = 2;
const int LED_PIN = 13;

// Estados
bool ledState = false;               // Estado atual do LED
bool lastButtonState = LOW;          // Último estado do botão
bool buttonState;                    // Estado atual do botão

// Debounce
unsigned long lastDebounceTime = 0;
const unsigned long DEBOUNCE_DELAY = 50;

void setup() {
  pinMode(BUTTON_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("Toggle LED iniciado!");
  Serial.println("Pressione o botão para alternar");
}

void loop() {
  // Lê botão
  int reading = digitalRead(BUTTON_PIN);
  
  // Verifica se mudou (e resetar debounce)
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }
  
  // Se passou tempo de debounce
  if ((millis() - lastDebounceTime) > DEBOUNCE_DELAY) {
    // Se estado mudou
    if (reading != buttonState) {
      buttonState = reading;
      
      // Se botão foi PRESSIONADO (transição LOW→HIGH)
      if (buttonState == HIGH) {
        // Alterna estado do LED
        ledState = !ledState;
        digitalWrite(LED_PIN, ledState);
        
        Serial.print("LED agora está: ");
        Serial.println(ledState ? "LIGADO" : "DESLIGADO");
      }
    }
  }
  
  lastButtonState = reading;
}
```

**Versão com Contador:**

```cpp
/*
 * Toggle com Contador de Pressões
 */

const int BUTTON_PIN = 2;
const int LED_PIN = 13;

bool ledState = false;
bool lastButtonState = LOW;
bool buttonState;
unsigned long lastDebounceTime = 0;
const unsigned long DEBOUNCE_DELAY = 50;

int pressCount = 0;  // Contador de pressões

void setup() {
  pinMode(BUTTON_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("=== Contador de Pressões ===");
}

void loop() {
  int reading = digitalRead(BUTTON_PIN);
  
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }
  
  if ((millis() - lastDebounceTime) > DEBOUNCE_DELAY) {
    if (reading != buttonState) {
      buttonState = reading;
      
      if (buttonState == HIGH) {
        ledState = !ledState;
        digitalWrite(LED_PIN, ledState);
        pressCount++;
        
        Serial.print("Pressão #");
        Serial.print(pressCount);
        Serial.print(" - LED: ");
        Serial.println(ledState ? "ON" : "OFF");
      }
    }
  }
  
  lastButtonState = reading;
}
```

**Critérios de Avaliação:**
- Lógica de toggle correta: 4 pts
- Debounce implementado: 2 pts
- Detecção de borda (edge detection): 2 pts
- Feedback via Serial: 1 pt
- Código limpo: 1 pt

**Erros Comuns:**
- Toggle acontece enquanto botão pressionado (sem edge detection)
- Múltiplos toggles por pressão (sem debounce)
- Usar delay() dentro da lógica principal
- Não salvar lastButtonState

**Conceitos de Arquitetura:**
- **State Machine:** LED e botão representam estados
- **Edge Detection:** Detectar transição LOW→HIGH
- **Debouncing:** Filtro de software para ruído de hardware
- **Boolean Logic:** Operador NOT (!) para alternar

---

### Semana 9: Sensores e Atuadores

#### Exercício 1: Termômetro Digital (DHT11/DHT22)
**Duração:** 30 minutos | **Peso:** 10 pontos

**Material Necessário:**
- 1x Sensor DHT11 ou DHT22
- 1x Resistor 10kΩ (pull-up)
- Biblioteca: DHT sensor library by Adafruit

**Montagem:**

```
DHT11/DHT22                Arduino
┌─────────┐
│  1 2 3  │
└─────────┘
  │ │ │
  │ │ └──── PIN 2 (Data)
  │ │   ┌─[R 10kΩ]─ 5V
  │ └──────────────── 5V
  └────────────────── GND
```

**Código Completo:**

```cpp
/*
 * Termômetro Digital com DHT11
 * Lê temperatura e umidade
 * Exibe no Serial Monitor
 */

#include <DHT.h>

#define DHTPIN 2        // Pino de dados do DHT
#define DHTTYPE DHT11   // Tipo de sensor (ou DHT22)

// Cria objeto DHT
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println("=== Termômetro Digital ===");
  Serial.println("Inicializando sensor DHT11...");
  
  dht.begin();
  delay(2000);  // Aguarda estabilização
  
  Serial.println("Sensor pronto!");
  Serial.println("Formato: Temp(°C) | Umid(%)");
  Serial.println("─────────────────────────");
}

void loop() {
  // Lê dados do sensor
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  
  // Verifica se leitura foi bem-sucedida
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("❌ Erro ao ler sensor!");
    delay(2000);
    return;
  }
  
  // Calcula índice de calor (sensação térmica)
  float heatIndex = dht.computeHeatIndex(temperature, humidity, false);
  
  // Exibe resultados
  Serial.print("🌡️  Temperatura: ");
  Serial.print(temperature, 1);  // 1 casa decimal
  Serial.print(" °C");
  
  Serial.print("  |  💧 Umidade: ");
  Serial.print(humidity, 1);
  Serial.print(" %");
  
  Serial.print("  |  🔥 Sensação: ");
  Serial.print(heatIndex, 1);
  Serial.println(" °C");
  
  // Aguarda 2 segundos antes da próxima leitura
  delay(2000);
}
```

**Versão com Alertas:**

```cpp
/*
 * Termômetro com Sistema de Alertas
 * LED vermelho: temperatura alta (>30°C)
 * LED amarelo: temperatura normal (20-30°C)
 * LED azul: temperatura baixa (<20°C)
 * Buzzer: dispara se temperatura crítica (>35°C)
 */

#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

#define LED_RED 10       // Temperatura alta
#define LED_YELLOW 11    // Temperatura normal
#define LED_BLUE 12      // Temperatura baixa
#define BUZZER_PIN 9     // Alarme crítico

DHT dht(DHTPIN, DHTTYPE);

// Limiares de temperatura
const float TEMP_LOW = 20.0;
const float TEMP_HIGH = 30.0;
const float TEMP_CRITICAL = 35.0;

void setup() {
  Serial.begin(9600);
  dht.begin();
  
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  
  Serial.println("Sistema de Monitoramento Térmico");
  Serial.println("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
  delay(2000);
}

void loop() {
  float temp = dht.readTemperature();
  float humid = dht.readHumidity();
  
  if (isnan(temp) || isnan(humid)) {
    Serial.println("Erro de leitura!");
    blinkError();
    delay(2000);
    return;
  }
  
  // Atualiza display
  displayStatus(temp, humid);
  
  // Atualiza LEDs e buzzer
  updateIndicators(temp);
  
  delay(1000);
}

void displayStatus(float temp, float humid) {
  Serial.print("Temp: ");
  Serial.print(temp, 1);
  Serial.print("°C  |  Umid: ");
  Serial.print(humid, 1);
  Serial.print("%  |  Status: ");
  
  if (temp < TEMP_LOW) {
    Serial.println("❄️  FRIO");
  } else if (temp < TEMP_HIGH) {
    Serial.println("✅ NORMAL");
  } else if (temp < TEMP_CRITICAL) {
    Serial.println("🔥 QUENTE");
  } else {
    Serial.println("⚠️  CRÍTICO!");
  }
}

void updateIndicators(float temp) {
  // Desliga todos LEDs
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_YELLOW, LOW);
  digitalWrite(LED_BLUE, LOW);
  noTone(BUZZER_PIN);
  
  // Liga LED apropriado
  if (temp < TEMP_LOW) {
    digitalWrite(LED_BLUE, HIGH);
  } else if (temp < TEMP_HIGH) {
    digitalWrite(LED_YELLOW, HIGH);
  } else {
    digitalWrite(LED_RED, HIGH);
    
    // Se crítico, ativa buzzer
    if (temp >= TEMP_CRITICAL) {
      tone(BUZZER_PIN, 1000);  // 1000 Hz
      delay(100);
      noTone(BUZZER_PIN);
      delay(100);
    }
  }
}

void blinkError() {
  // Pisca todos LEDs em erro
  for(int i = 0; i < 3; i++) {
    digitalWrite(LED_RED, HIGH);
    digitalWrite(LED_YELLOW, HIGH);
    digitalWrite(LED_BLUE, HIGH);
    delay(200);
    digitalWrite(LED_RED, LOW);
    digitalWrite(LED_YELLOW, LOW);
    digitalWrite(LED_BLUE, LOW);
    delay(200);
  }
}
```

**Critérios de Avaliação:**
- Montagem do circuito: 2 pts
- Instalação e importação da biblioteca: 1 pt
- Leitura correta: 3 pts
- Formatação da saída: 1 pt
- Sistema de alertas (opcional): +3 pts extra
- Documentação: 1 pt

**Troubleshooting Comum:**
- **Leitura NaN:** Cabo de dados solto ou resistor pull-up faltando
- **Valores errados:** Tipo de sensor incorreto (DHT11 vs DHT22)
- **Travamento:** delay() muito curto entre leituras (min 2s DHT11, 1s DHT22)
- **Biblioteca não encontrada:** Instalar via Library Manager

**Conceitos de Arquitetura:**
- **ADC (Analog-to-Digital Converter):** Sensor envia sinal analógico
- **Protocolo de Comunicação:** DHT usa protocolo proprietário de 1-Wire
- **Timing Crítico:** Sensor precisa de delays específicos
- **Ponto Flutuante:** float usa 4 bytes (32 bits) no ATmega328P

---

## 🧰 Troubleshooting Comum

### Problema: Arduino não é reconhecido pelo PC
**Possíveis causas:**
1. Cabo USB defeituoso ou apenas de carregamento
2. Driver CH340/CH341 não instalado (clones chineses)
3. Porta USB sem energia suficiente
4. Arduino com bootloader corrompido

**Soluções:**
1. Testar com cabo USB conhecido (dados + energia)
2. Instalar driver: https://sparks funfun.github.io/CH340-Drivers/
3. Usar porta USB diferente ou hub powered
4. Regravar bootloader com ISP programmer

### Problema: Upload falha com erro "avrdude: stk500_recv()"
**Causas:**
- Placa errada selecionada em Tools → Board
- Porta COM errada selecionada
- Algo conectado aos pinos 0 e 1 (TX/RX)
- Arduino travado

**Soluções:**
- Selecionar "Arduino Uno" em Board
- Verificar porta correta em Tools → Port
- Desconectar tudo dos pinos 0 e 1 durante upload
- Pressionar reset enquanto faz upload

### Problema: LED não acende
**Checklist:**
1. LED invertido? (perna longa no +)
2. Resistor presente?
3. Conexão de GND?
4. Código correto (pinMode OUTPUT)?
5. LED queimado? (testar outro)

---

## 📦 Lista de Materiais Completa

### Kit Básico por Aluno/Dupla:
- 1x Arduino Uno R3
- 1x Cabo USB A-B
- 1x Protoboard 830 pontos
- 40x Jumpers macho-macho (variados)
- 20x Jumpers macho-fêmea

### Componentes Eletrônicos:
**LEDs:**
- 10x LED vermelho 5mm
- 5x LED verde 5mm
- 5x LED amarelo 5mm
- 5x LED azul 5mm

**Resistores (1/4W):**
- 10x 220Ω (vermelho-vermelho-marrom)
- 10x 1kΩ (marrom-preto-vermelho)
- 10x 10kΩ (marrom-preto-laranja)
- 5x 100kΩ (marrom-preto-amarelo)

**Entrada:**
- 5x Push button (tátil)
- 2x Potenciômetro 10kΩ

**Sensores:**
- 1x DHT11 ou DHT22 (temperatura/umidade)
- 1x HC-SR04 (ultrassônico)
- 1x LDR (sensor de luz)
- 1x Sensor PIR (movimento)

**Displays:**
- 1x LCD 16x2 com interface I2C
- 1x Display 7 segmentos (ânodo comum)

**Atuadores:**
- 2x Buzzer passivo
- 1x Servo motor 9g (SG90)
- 1x Motor DC 3-6V
- 1x Driver L298N

**Comunicação:**
- 1x Módulo Bluetooth HC-05 ou HC-06

### Ferramentas de Bancada:
- Multímetro digital
- Fonte de alimentação variável (opcional)
- Alicate de corte
- Alicate de ponta fina
- Ferro de solda (para projetos avançados)

---

## 💡 Dicas Finais para o Professor

1. **Organize kits em caixas plásticas** numeradas
2. **Faça inventário antes e depois** de cada aula
3. **Tenha componentes sobressalentes** (LEDs e resistores)
4. **Documente montagens com fotos** para correção posterior
5. **Use simuladores online** quando kits insuficientes (Tinkercad)
6. **Crie biblioteca de códigos** testados e funcionais
7. **Estabeleça regras de lab** desde o início
8. **Ensine debug básico:** Serial Monitor é essencial!

---

**Este guia será continuado com:**
- Módulo 4: ESP32 (Semanas 16-18)
- Projetos Integradores (Semanas 19-20)
- Banco de Exercícios Extras
- Questões de Prova Teórica

---

📘 **Guia Prático Arduino/ESP32**  
Centro Estadual de Educação Tecnológica Paula Souza | 2026
