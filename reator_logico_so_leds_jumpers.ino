/*
  ============================================================
  REATOR LOGICO — versao "so LEDs, Arduino, jumpers e resistores"
  ============================================================
  Sem botao fisico e sem buzzer. As respostas 0 e 1 sao dadas
  encostando a PONTA SOLTA de um jumper no GND (o proprio fio
  funciona como um botao improvisado, usando o pull-up interno
  do Arduino).

  LIGACOES:
    LED A (entrada) .......... pino digital 2  -> resistor 220R -> GND
    LED B (entrada) .......... pino digital 3  -> resistor 220R -> GND
    LED verde (acerto) ....... pino digital 4  -> resistor 220R -> GND
    LED vermelho (erro) ...... pino digital 5  -> resistor 220R -> GND
    Fio resposta "0" .......... pino digital 8  -> jumper com ponta solta
    Fio resposta "1" .......... pino digital 9  -> jumper com ponta solta

  COMO RESPONDER:
    Para responder "0": encoste a ponta solta do jumper do
    pino 8 em qualquer ponto do trilho GND do protoboard.
    Para responder "1": faca o mesmo com o jumper do pino 9.
    Solte o fio depois — ele volta sozinho para "1" (nao
    respondido) por causa do pull-up interno.

  Acompanhe nivel, pontuacao e escudos pelo Monitor Serial
  (9600 bps). Nao ha som (sem buzzer nesta versao).
  ============================================================
*/

const int LED_A = 2, LED_B = 3, LED_OK = 4, LED_ERR = 5;
const int WIRE_0 = 8, WIRE_1 = 9;

struct Gate {
  const char* name;
  int nInputs;
  int inA[4];
  int inB[4];
  int out[4];
  int rows;
};

Gate GATES[7] = {
  { "AND",  2, {0,0,1,1}, {0,1,0,1}, {0,0,0,1}, 4 },
  { "OR",   2, {0,0,1,1}, {0,1,0,1}, {0,1,1,1}, 4 },
  { "NOT",  1, {0,1,0,0}, {0,0,0,0}, {1,0,0,0}, 2 },
  { "NAND", 2, {0,0,1,1}, {0,1,0,1}, {1,1,1,0}, 4 },
  { "NOR",  2, {0,0,1,1}, {0,1,0,1}, {1,0,0,0}, 4 },
  { "XOR",  2, {0,0,1,1}, {0,1,0,1}, {0,1,1,0}, 4 },
  { "XNOR", 2, {0,0,1,1}, {0,1,0,1}, {1,0,0,1}, 4 }
};

int LEVEL_POOL[3][7] = {
  { 0,1,2,-1,-1,-1,-1 },
  { 0,1,2,3,4,-1,-1  },
  { 0,1,2,3,4,5,6    }
};
int LEVEL_SIZE[3] = { 3, 5, 7 };
const int NEEDED_PER_LEVEL = 5;

int level = 1, score = 0, shields = 3, streak = 0, correctInLevel = 0;
int curGateIdx, curA, curB, curOut;

void setup() {
  pinMode(LED_A, OUTPUT);
  pinMode(LED_B, OUTPUT);
  pinMode(LED_OK, OUTPUT);
  pinMode(LED_ERR, OUTPUT);
  pinMode(WIRE_0, INPUT_PULLUP);
  pinMode(WIRE_1, INPUT_PULLUP);

  randomSeed(analogRead(A0));
  Serial.begin(9600);
  Serial.println(F("=== REATOR LOGICO — versao so LEDs/jumpers/resistores ==="));
  Serial.println(F("Encoste o jumper do pino 8 no GND para responder 0."));
  Serial.println(F("Encoste o jumper do pino 9 no GND para responder 1."));
  newRound();
}

void newRound() {
  int idx = random(LEVEL_SIZE[level - 1]);
  curGateIdx = LEVEL_POOL[level - 1][idx];
  Gate g = GATES[curGateIdx];
  int row = random(g.rows);
  curA = g.inA[row];
  curB = g.inB[row];
  curOut = g.out[row];

  digitalWrite(LED_A, curA);
  digitalWrite(LED_B, g.nInputs == 2 ? curB : LOW);
  digitalWrite(LED_OK, LOW);
  digitalWrite(LED_ERR, LOW);

  Serial.println();
  Serial.print(F("Nivel ")); Serial.print(level); Serial.print(F("/3   "));
  Serial.print(F("Pontos: ")); Serial.print(score); Serial.print(F("   "));
  Serial.print(F("Escudos: ")); Serial.println(shields);
  Serial.print(F("Porta: ")); Serial.print(g.name);
  Serial.print(F("   A=")); Serial.print(curA);
  if (g.nInputs == 2) { Serial.print(F("  B=")); Serial.print(curB); }
  Serial.println(F("   -> qual a saida? (encoste o fio 0 ou 1 no GND)"));
}

void loop() {
  if (digitalRead(WIRE_0) == LOW) { answer(0); delay(400); }
  if (digitalRead(WIRE_1) == LOW) { answer(1); delay(400); }
}

void answer(int val) {
  bool ok = (val == curOut);

  if (ok) {
    digitalWrite(LED_OK, HIGH);
    score += 10 * level;
    streak++;
    correctInLevel++;
    Serial.print(F(">> Correto! Saida = ")); Serial.println(curOut);
  } else {
    digitalWrite(LED_ERR, HIGH);
    shields--;
    streak = 0;
    Serial.print(F(">> Errado! A saida correta era ")); Serial.println(curOut);
  }

  delay(1000);

  if (shields <= 0) {
    shields = 3;
    correctInLevel = 0;
    Serial.println(F("!! Escudos esgotados. Progresso do nivel reiniciado."));
  } else if (correctInLevel >= NEEDED_PER_LEVEL) {
    if (level < 3) {
      level++;
      correctInLevel = 0;
      shields = 3;
      Serial.print(F("*** Nivel ")); Serial.print(level); Serial.println(F(" desbloqueado! ***"));
    } else {
      Serial.println(F("*** REATOR ESTABILIZADO! Parabens! ***"));
      Serial.print(F("Pontuacao final: ")); Serial.println(score);
      digitalWrite(LED_OK, HIGH);
      while (true) { /* fim de jogo — reinicie o Arduino para jogar de novo */ }
    }
  }

  newRound();
}
