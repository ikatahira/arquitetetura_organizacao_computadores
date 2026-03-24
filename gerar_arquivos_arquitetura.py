#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Estrutura completa do curso
semanas = [
    # Módulo 1
    {
        "num": 1,
        "titulo": "Apresentação e Fundamentos",
        "conteudo": [
            "História da Computação",
            "Evolução dos Computadores",
            "Componentes básicos de hardware",
            "Conceitos fundamentais de arquitetura"
        ],
        "objetivos": [
            "Compreender a evolução histórica dos computadores",
            "Identificar os principais componentes de hardware",
            "Entender os conceitos básicos de arquitetura de computadores"
        ],
        "atividades": [
            {
                "titulo": "Pesquisa sobre Gerações de Computadores",
                "objetivo": "Investigar e apresentar a evolução tecnológica",
                "duracao": 30
            },
            {
                "titulo": "Identificação de Componentes",
                "objetivo": "Reconhecer componentes em um computador real",
                "duracao": 35
            },
            {
                "titulo": "Diagrama de Blocos",
                "objetivo": "Criar diagrama de arquitetura básica",
                "duracao": 25
            }
        ]
    },
    {
        "num": 2,
        "titulo": "Sistemas Numéricos",
        "conteudo": [
            "Sistema Binário",
            "Sistema Octal e Hexadecimal",
            "Conversões entre bases",
            "Aritmética binária",
            "Complemento de 2"
        ],
        "objetivos": [
            "Dominar conversões entre diferentes bases numéricas",
            "Realizar operações aritméticas em binário",
            "Compreender representação de números negativos"
        ],
        "atividades": [
            {
                "titulo": "Conversões Numéricas",
                "objetivo": "Praticar conversão entre bases",
                "duracao": 30
            },
            {
                "titulo": "Calculadora Binária",
                "objetivo": "Implementar operações binárias",
                "duracao": 35
            },
            {
                "titulo": "Representação de Dados",
                "objetivo": "Codificar informações em binário",
                "duracao": 25
            }
        ]
    },
    {
        "num": 3,
        "titulo": "Portas Lógicas e Álgebra Booleana",
        "conteudo": [
            "Portas AND, OR, NOT",
            "Portas NAND, NOR, XOR",
            "Álgebra Booleana",
            "Teoremas de De Morgan",
            "Simplificação de expressões",
            "Tabelas verdade"
        ],
        "objetivos": [
            "Compreender o funcionamento das portas lógicas",
            "Aplicar álgebra booleana para simplificação",
            "Construir e analisar tabelas verdade"
        ],
        "atividades": [
            {
                "titulo": "Simulação de Portas Lógicas",
                "objetivo": "Usar simulador para testar circuitos",
                "duracao": 30
            },
            {
                "titulo": "Simplificação de Expressões",
                "objetivo": "Aplicar teoremas de simplificação",
                "duracao": 35
            },
            {
                "titulo": "Projeto de Circuito Lógico",
                "objetivo": "Criar circuito a partir de especificação",
                "duracao": 25
            }
        ]
    },
    {
        "num": 4,
        "titulo": "Circuitos Combinacionais",
        "conteudo": [
            "Multiplexadores e Demultiplexadores",
            "Codificadores e Decodificadores",
            "Somadores (Half e Full Adder)",
            "Subtratores",
            "Comparadores",
            "ALU básica"
        ],
        "objetivos": [
            "Projetar circuitos combinacionais básicos",
            "Compreender o funcionamento da ALU",
            "Implementar somadores e subtratores"
        ],
        "atividades": [
            {
                "titulo": "Projeto de Somador Completo",
                "objetivo": "Implementar somador de 4 bits",
                "duracao": 30
            },
            {
                "titulo": "Multiplexador 4x1",
                "objetivo": "Criar circuito seletor",
                "duracao": 35
            },
            {
                "titulo": "Mini ALU",
                "objetivo": "Desenvolver ALU com operações básicas",
                "duracao": 25
            }
        ]
    },
    {
        "num": 5,
        "titulo": "Circuitos Sequenciais",
        "conteudo": [
            "Flip-Flops (SR, D, JK, T)",
            "Registradores",
            "Contadores",
            "Máquinas de estado",
            "Memórias básicas"
        ],
        "objetivos": [
            "Compreender elementos de memória",
            "Projetar contadores e registradores",
            "Implementar máquinas de estado finito"
        ],
        "atividades": [
            {
                "titulo": "Análise de Flip-Flops",
                "objetivo": "Estudar comportamento temporal",
                "duracao": 30
            },
            {
                "titulo": "Contador de 8 bits",
                "objetivo": "Implementar contador crescente",
                "duracao": 35
            },
            {
                "titulo": "Máquina de Estados",
                "objetivo": "Criar FSM para controle",
                "duracao": 25
            }
        ]
    },
    # Módulo 2
    {
        "num": 6,
        "titulo": "Arquitetura de von Neumann",
        "conteudo": [
            "Conceito de programa armazenado",
            "Componentes: CPU, Memória, I/O",
            "Barramento de dados e endereços",
            "Ciclo Fetch-Decode-Execute",
            "Arquitetura Harvard vs von Neumann"
        ],
        "objetivos": [
            "Entender o conceito de programa armazenado",
            "Compreender o ciclo de execução de instruções",
            "Comparar diferentes arquiteturas"
        ],
        "atividades": [
            {
                "titulo": "Simulação de Execução",
                "objetivo": "Simular ciclo fetch-decode-execute",
                "duracao": 30
            },
            {
                "titulo": "Diagrama de von Neumann",
                "objetivo": "Criar diagrama detalhado",
                "duracao": 35
            },
            {
                "titulo": "Comparativo de Arquiteturas",
                "objetivo": "Analisar vantagens e desvantagens",
                "duracao": 25
            }
        ]
    },
    {
        "num": 7,
        "titulo": "Introdução ao Arduino - Hardware",
        "conteudo": [
            "Componentes da placa Arduino",
            "Microcontrolador ATmega328P",
            "Pinos digitais e analógicos",
            "Alimentação e tensões",
            "Protoboard e jumpers",
            "Componentes básicos: LEDs, resistores, botões"
        ],
        "objetivos": [
            "Conhecer os componentes do Arduino Uno",
            "Compreender a função dos pinos",
            "Montar circuitos básicos em protoboard"
        ],
        "atividades": [
            {
                "titulo": "Identificação de Componentes",
                "objetivo": "Reconhecer partes do Arduino",
                "duracao": 30
            },
            {
                "titulo": "Circuito LED Piscante",
                "objetivo": "Montar primeiro circuito com LED",
                "duracao": 35
            },
            {
                "titulo": "Teste de Botões",
                "objetivo": "Criar circuito com entrada digital",
                "duracao": 25
            }
        ]
    },
    {
        "num": 8,
        "titulo": "Programação Arduino - Básico",
        "conteudo": [
            "IDE Arduino",
            "Estrutura de um sketch",
            "Funções setup() e loop()",
            "pinMode, digitalWrite, digitalRead",
            "Controle de tempo: delay e millis",
            "Serial Monitor"
        ],
        "objetivos": [
            "Escrever e carregar programas no Arduino",
            "Controlar pinos digitais",
            "Usar comunicação serial para debug"
        ],
        "atividades": [
            {
                "titulo": "Blink Personalizado",
                "objetivo": "Programar padrões de pisca-pisca",
                "duracao": 30
            },
            {
                "titulo": "Botão com LED",
                "objetivo": "Controlar LED através de botão",
                "duracao": 35
            },
            {
                "titulo": "Semáforo Simples",
                "objetivo": "Criar lógica de semáforo",
                "duracao": 25
            }
        ]
    },
    {
        "num": 9,
        "titulo": "Sensores e Atuadores",
        "conteudo": [
            "Sensores de temperatura (DHT11/DHT22)",
            "Sensor ultrassônico (HC-SR04)",
            "Potenciômetros e entradas analógicas",
            "Displays LCD 16x2",
            "Servomotores",
            "Buzzer e sons"
        ],
        "objetivos": [
            "Integrar sensores ao Arduino",
            "Processar dados analógicos",
            "Controlar atuadores diversos"
        ],
        "atividades": [
            {
                "titulo": "Termômetro Digital",
                "objetivo": "Ler e exibir temperatura",
                "duracao": 30
            },
            {
                "titulo": "Medidor de Distância",
                "objetivo": "Usar sensor ultrassônico",
                "duracao": 35
            },
            {
                "titulo": "Sistema de Alerta",
                "objetivo": "Criar alarme com buzzer e LED",
                "duracao": 25
            }
        ]
    },
    {
        "num": 10,
        "titulo": "Projeto Prático Arduino 1",
        "conteudo": [
            "Planejamento de projeto",
            "Integração de múltiplos componentes",
            "Debugging e testes",
            "Documentação de código",
            "Apresentação de resultados"
        ],
        "objetivos": [
            "Desenvolver projeto completo com Arduino",
            "Integrar conhecimentos adquiridos",
            "Documentar e apresentar solução"
        ],
        "atividades": [
            {
                "titulo": "Sistema de Monitoramento",
                "objetivo": "Criar sistema com múltiplos sensores",
                "duracao": 40
            },
            {
                "titulo": "Automação Residencial Simples",
                "objetivo": "Controlar dispositivos automaticamente",
                "duracao": 40
            },
            {
                "titulo": "Apresentação do Projeto",
                "objetivo": "Demonstrar funcionamento e explicar código",
                "duracao": 10
            }
        ]
    },
    # Módulo 3
    {
        "num": 11,
        "titulo": "CPU e Ciclo de Instrução",
        "conteudo": [
            "Componentes da CPU: UC e ALU",
            "Registradores internos",
            "Ciclo de instrução detalhado",
            "Pipeline de instruções",
            "Hazards e dependências"
        ],
        "objetivos": [
            "Compreender o funcionamento interno da CPU",
            "Entender o conceito de pipeline",
            "Identificar problemas de dependência"
        ],
        "atividades": [
            {
                "titulo": "Simulação de Pipeline",
                "objetivo": "Simular execução com pipeline",
                "duracao": 30
            },
            {
                "titulo": "Análise de Desempenho",
                "objetivo": "Calcular CPI e throughput",
                "duracao": 35
            },
            {
                "titulo": "Identificação de Hazards",
                "objetivo": "Detectar e resolver dependências",
                "duracao": 25
            }
        ]
    },
    {
        "num": 12,
        "titulo": "Conjunto de Instruções (ISA)",
        "conteudo": [
            "RISC vs CISC",
            "Tipos de instruções",
            "Modos de endereçamento",
            "Assembly básico",
            "Exemplos: ARM, x86, MIPS"
        ],
        "objetivos": [
            "Compreender diferentes filosofias de ISA",
            "Programar em assembly básico",
            "Analisar eficiência de instruções"
        ],
        "atividades": [
            {
                "titulo": "Programação em Assembly",
                "objetivo": "Escrever programas simples",
                "duracao": 30
            },
            {
                "titulo": "Análise RISC vs CISC",
                "objetivo": "Comparar implementações",
                "duracao": 35
            },
            {
                "titulo": "Otimização de Código",
                "objetivo": "Reduzir número de instruções",
                "duracao": 25
            }
        ]
    },
    {
        "num": 13,
        "titulo": "Hierarquia de Memória",
        "conteudo": [
            "Princípio da localidade",
            "Registradores, Cache, RAM, Disco",
            "Tempo de acesso e capacidade",
            "Trade-offs de desempenho",
            "Memórias voláteis e não-voláteis"
        ],
        "objetivos": [
            "Entender a organização hierárquica",
            "Compreender trade-offs custo-desempenho",
            "Analisar impacto no desempenho"
        ],
        "atividades": [
            {
                "titulo": "Diagrama de Hierarquia",
                "objetivo": "Criar representação visual",
                "duracao": 30
            },
            {
                "titulo": "Cálculo de Tempos",
                "objetivo": "Determinar tempo médio de acesso",
                "duracao": 35
            },
            {
                "titulo": "Análise de Localidade",
                "objetivo": "Identificar padrões de acesso",
                "duracao": 25
            }
        ]
    },
    {
        "num": 14,
        "titulo": "Memória Cache",
        "conteudo": [
            "Funcionamento da cache",
            "Mapeamento direto, associativo e conjunto",
            "Políticas de substituição (LRU, FIFO)",
            "Write-through e write-back",
            "Cache hit e miss",
            "Cálculo de taxa de acerto"
        ],
        "objetivos": [
            "Compreender organização da cache",
            "Calcular taxas de hit e miss",
            "Avaliar impacto das políticas"
        ],
        "atividades": [
            {
                "titulo": "Simulação de Cache",
                "objetivo": "Simular operações de cache",
                "duracao": 30
            },
            {
                "titulo": "Cálculo de Desempenho",
                "objetivo": "Determinar taxa de acerto",
                "duracao": 35
            },
            {
                "titulo": "Comparação de Políticas",
                "objetivo": "Avaliar diferentes estratégias",
                "duracao": 25
            }
        ]
    },
    {
        "num": 15,
        "titulo": "Entrada e Saída (I/O)",
        "conteudo": [
            "Dispositivos de I/O",
            "I/O programado, por interrupção e DMA",
            "Barramentos de I/O",
            "Controladores de dispositivos",
            "Interfaces seriais e paralelas"
        ],
        "objetivos": [
            "Compreender técnicas de I/O",
            "Entender o papel das interrupções",
            "Analisar eficiência do DMA"
        ],
        "atividades": [
            {
                "titulo": "Comparação de Técnicas",
                "objetivo": "Avaliar I/O programado vs interrupção vs DMA",
                "duracao": 30
            },
            {
                "titulo": "Simulação de Interrupções",
                "objetivo": "Implementar tratamento de IRQ",
                "duracao": 35
            },
            {
                "titulo": "Projeto de Interface",
                "objetivo": "Especificar controlador de dispositivo",
                "duracao": 25
            }
        ]
    },
    # Módulo 4
    {
        "num": 16,
        "titulo": "Introdução ao ESP32",
        "conteudo": [
            "Características do ESP32",
            "Arquitetura dual-core",
            "Comparação com Arduino",
            "Configuração do ambiente",
            "Pinout e recursos",
            "Primeiros programas"
        ],
        "objetivos": [
            "Conhecer as capacidades do ESP32",
            "Configurar ambiente de desenvolvimento",
            "Programar o ESP32 usando Arduino IDE"
        ],
        "atividades": [
            {
                "titulo": "Setup do ESP32",
                "objetivo": "Configurar Arduino IDE para ESP32",
                "duracao": 30
            },
            {
                "titulo": "Blink com ESP32",
                "objetivo": "Testar primeiro programa",
                "duracao": 35
            },
            {
                "titulo": "Exploração de Recursos",
                "objetivo": "Testar diferentes periféricos",
                "duracao": 25
            }
        ]
    },
    {
        "num": 17,
        "titulo": "WiFi e IoT com ESP32",
        "conteudo": [
            "Conexão WiFi",
            "Modos AP e Station",
            "Protocolos HTTP e MQTT",
            "Requisições Web",
            "APIs REST",
            "Integração com nuvem"
        ],
        "objetivos": [
            "Conectar ESP32 à rede WiFi",
            "Fazer requisições HTTP",
            "Implementar comunicação IoT"
        ],
        "atividades": [
            {
                "titulo": "Cliente HTTP",
                "objetivo": "Buscar dados de API externa",
                "duracao": 30
            },
            {
                "titulo": "Servidor Web",
                "objetivo": "Criar página de controle",
                "duracao": 35
            },
            {
                "titulo": "Dashboard IoT",
                "objetivo": "Enviar dados para plataforma",
                "duracao": 25
            }
        ]
    },
    {
        "num": 18,
        "titulo": "Bluetooth e Comunicação",
        "conteudo": [
            "Bluetooth Classic e BLE",
            "Pareamento de dispositivos",
            "Comunicação serial via BT",
            "App mobile para controle",
            "Outros protocolos: I2C, SPI, UART"
        ],
        "objetivos": [
            "Implementar comunicação Bluetooth",
            "Controlar ESP32 via smartphone",
            "Usar protocolos de comunicação"
        ],
        "atividades": [
            {
                "titulo": "Bluetooth Serial",
                "objetivo": "Comunicação com app mobile",
                "duracao": 30
            },
            {
                "titulo": "Controle Remoto",
                "objetivo": "Comandar dispositivos via BT",
                "duracao": 35
            },
            {
                "titulo": "Rede de Sensores",
                "objetivo": "Comunicação entre ESP32s",
                "duracao": 25
            }
        ]
    },
    {
        "num": 19,
        "titulo": "Projeto Integrador",
        "conteudo": [
            "Definição do projeto final",
            "Requisitos e especificação",
            "Arquitetura do sistema",
            "Desenvolvimento e integração",
            "Testes e validação"
        ],
        "objetivos": [
            "Desenvolver projeto IoT completo",
            "Integrar todos os conhecimentos",
            "Documentar projeto profissionalmente"
        ],
        "atividades": [
            {
                "titulo": "Planejamento do Projeto",
                "objetivo": "Definir escopo e requisitos",
                "duracao": 30
            },
            {
                "titulo": "Implementação",
                "objetivo": "Desenvolver sistema completo",
                "duracao": 40
            },
            {
                "titulo": "Testes e Refinamento",
                "objetivo": "Validar e otimizar solução",
                "duracao": 20
            }
        ]
    },
    {
        "num": 20,
        "titulo": "Apresentação dos Projetos",
        "conteudo": [
            "Preparação de apresentação",
            "Demonstração ao vivo",
            "Documentação técnica",
            "Discussão de resultados",
            "Avaliação final"
        ],
        "objetivos": [
            "Apresentar projeto desenvolvido",
            "Demonstrar funcionamento",
            "Defender escolhas técnicas"
        ],
        "atividades": [
            {
                "titulo": "Apresentação Formal",
                "objetivo": "Apresentar projeto para turma",
                "duracao": 30
            },
            {
                "titulo": "Demo ao Vivo",
                "objetivo": "Demonstrar funcionamento",
                "duracao": 30
            },
            {
                "titulo": "Q&A e Feedback",
                "objetivo": "Responder perguntas e receber feedback",
                "duracao": 30
            }
        ]
    }
]

def gerar_aula(semana):
    num = semana['num']
    titulo = semana['titulo']
    conteudo = semana['conteudo']
    objetivos = semana['objetivos']
    atividades = semana['atividades']
    
    # Determinar navegação
    prev_num = num - 1 if num > 1 else None
    next_num = num + 1 if num < 20 else None
    
    prev_disabled = ' disabled' if prev_num is None else ''
    prev_link = '#' if prev_num is None else f'arquitetura_semana{prev_num:02d}_aula.html'
    next_link = f'arquitetura_semana{next_num:02d}_aula.html' if next_num else '#'
    next_disabled = ' disabled' if next_num is None else ''
    
    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Semana {num:02d} - {titulo}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;line-height:1.6;background:#f0f2f5}}
.header{{background:linear-gradient(135deg,#1e3c72 0%,#2a5298 100%);color:white;padding:20px 0;box-shadow:0 2px 10px rgba(0,0,0,0.2)}}
.header-content{{max-width:1400px;margin:0 auto;padding:0 20px}}
.header h1{{font-size:1.8em;margin-bottom:5px}}
.container{{max-width:1400px;margin:20px auto;padding:0 20px}}
.section{{background:white;border-radius:12px;padding:30px;margin-bottom:25px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}}
.section h2{{color:#1e3c72;font-size:1.8em;margin-bottom:20px;padding-bottom:10px;border-bottom:3px solid #2a5298}}
ul{{margin-left:20px;margin-top:10px}}
li{{margin-bottom:8px}}
.objetivos{{background:#e6f2ff;padding:20px;border-radius:8px;border-left:5px solid #2a5298}}
.activity-card{{background:#f8f9fa;border-left:5px solid#1e3c72;padding:20px;margin:15px 0;border-radius:8px}}
.nav-buttons{{display:flex;gap:15px;margin-top:20px}}
.nav-btn{{padding:12px 24px;background:linear-gradient(135deg,#1e3c72 0%,#2a5298 100%);color:white;text-decoration:none;border-radius:8px;font-weight:bold;transition:all 0.3s}}
.nav-btn:hover{{transform:translateY(-2px);box-shadow:0 5px 15px rgba(30,60,114,0.3)}}
.nav-btn.disabled{{opacity:0.5;pointer-events:none}}
</style>
</head>
<body>
<div class="header">
<div class="header-content">
<h1>⚙️ Semana {num:02d} - {titulo}</h1>
<p>Arquitetura e Organização de Computadores</p>
</div>
</div>
<div class="container">
<div class="section">
<h2>🎯 Objetivos</h2>
<div class="objetivos">
<ul>
'''
    
    for obj in objetivos:
        html += f'<li>{obj}</li>\n'
    
    html += '''</ul>
</div>
</div>
<div class="section">
<h2>📖 Conteúdo</h2>
<ul>
'''
    
    for item in conteudo:
        html += f'<li>{item}</li>\n'
    
    html += '''</ul>
</div>
<div class="section">
<h2>✏️ Atividades Práticas</h2>
'''
    
    for i, ativ in enumerate(atividades, 1):
        html += f'''<div class="activity-card">
<h3>Exercício {i}: {ativ['titulo']}</h3>
<p><strong>Objetivo:</strong> {ativ['objetivo']}</p>
<p><strong>Duração:</strong> {ativ['duracao']} minutos</p>
</div>
'''
    
    html += f'''</div>
<div class="nav-buttons">
<a href="{prev_link}" class="nav-btn{prev_disabled}">⬅️ Anterior</a>
<a href="index_arquitetura.html" class="nav-btn">📚 Índice</a>
<a href="arquitetura_semana{num:02d}_guia.html" class="nav-btn">✏️ Guia</a>
<a href="{next_link}" class="nav-btn{next_disabled}">Próxima ➡️</a>
</div>
</div>
</body>
</html>'''
    
    return html

def gerar_guia(semana):
    num = semana['num']
    titulo = semana['titulo']
    atividades = semana['atividades']
    
    # Determinar navegação
    prev_num = num - 1 if num > 1 else None
    next_num = num + 1 if num < 20 else None
    
    prev_disabled = ' disabled' if prev_num is None else ''
    prev_link = '#' if prev_num is None else f'arquitetura_semana{prev_num:02d}_guia.html'
    next_link = f'arquitetura_semana{next_num:02d}_guia.html' if next_num else '#'
    next_disabled = ' disabled' if next_num is None else ''
    
    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Guia - Semana {num:02d}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;line-height:1.6;background:linear-gradient(135deg,#1e3c72 0%,#2a5298 100%);min-height:100vh;padding:20px}}
.container{{max-width:1200px;margin:0 auto}}
.header{{background:white;border-radius:15px;padding:30px;margin-bottom:25px;box-shadow:0 10px 30px rgba(0,0,0,0.3)}}
.header h1{{color:#1e3c72;font-size:2.2em;margin-bottom:10px}}
.nav-buttons{{display:flex;gap:15px;margin-top:20px}}
.nav-btn{{padding:12px 24px;background:linear-gradient(135deg,#1e3c72 0%,#2a5298 100%);color:white;text-decoration:none;border-radius:8px;font-weight:bold;transition:all 0.3s}}
.nav-btn.disabled{{opacity:0.5;pointer-events:none}}
.section{{background:white;border-radius:12px;padding:30px;margin-bottom:25px;box-shadow:0 5px 20px rgba(0,0,0,0.2)}}
.section h2{{color:#1e3c72;font-size:1.8em;margin-bottom:20px;padding-bottom:10px;border-bottom:3px solid #2a5298}}
.rubric-table{{width:100%;border-collapse:collapse;margin:20px 0;background:white;box-shadow:0 2px 8px rgba(0,0,0,0.1);border-radius:8px;overflow:hidden}}
.rubric-table th{{background:linear-gradient(135deg,#1e3c72 0%,#2a5298 100%);color:white;padding:15px;text-align:left}}
.rubric-table td{{padding:12px 15px;border-bottom:1px solid #e0e0e0}}
.rubric-table tr:hover{{background:#f5f5f5}}
.criterion{{font-weight:bold;color:#1e3c72}}
.solution-box{{background:linear-gradient(to right,#e8f5e9,#f1f8e9);border-left:5px solid #4caf50;padding:25px;margin:20px 0;border-radius:8px}}
.solution-box h3{{color:#2e7d32;margin-bottom:15px}}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>📚 Guia - Semana {num:02d}</h1>
<p>{titulo}</p>
<div class="nav-buttons">
<a href="{prev_link}" class="nav-btn{prev_disabled}">⬅️ Anterior</a>
<a href="index_arquitetura.html" class="nav-btn">📚 Índice</a>
<a href="arquitetura_semana{num:02d}_aula.html" class="nav-btn">📖 Aula</a>
<a href="{next_link}" class="nav-btn{next_disabled}">Próxima ➡️</a>
</div>
</div>
'''
    
    for i, ativ in enumerate(atividades, 1):
        html += f'''<div class="section">
<h2>✏️ Exercício {i}: {ativ['titulo']}</h2>
<p><strong>📋 Objetivo:</strong> {ativ['objetivo']}</p>
<p><strong>⏱️ Duração:</strong> {ativ['duracao']} minutos</p>
<h3>📊 Rubrica de Avaliação</h3>
<table class="rubric-table">
<thead><tr>
<th>Critério</th>
<th>Insuficiente (0-5)</th>
<th>Básico (6-7)</th>
<th>Proficiente (8-9)</th>
<th>Excelente (10)</th>
</tr></thead>
<tbody>
<tr>
<td class="criterion">Compreensão</td>
<td>Não compreendeu conceitos</td>
<td>Compreensão básica</td>
<td>Boa compreensão</td>
<td>Compreensão completa e profunda</td>
</tr>
<tr>
<td class="criterion">Implementação</td>
<td>Não implementou</td>
<td>Implementação parcial</td>
<td>Bem implementado</td>
<td>Implementação exemplar</td>
</tr>
<tr>
<td class="criterion">Funcionalidade</td>
<td>Não funciona</td>
<td>Funciona parcialmente</td>
<td>Funciona bem</td>
<td>Funciona perfeitamente</td>
</tr>
<tr>
<td class="criterion">Qualidade Técnica</td>
<td>Baixa qualidade</td>
<td>Qualidade básica</td>
<td>Boa qualidade</td>
<td>Qualidade profissional</td>
</tr>
<tr>
<td class="criterion">Documentação</td>
<td>Sem documentação</td>
<td>Documentação básica</td>
<td>Bem documentado</td>
<td>Documentação completa</td>
</tr>
<tr>
<td class="criterion">Criatividade</td>
<td>Sem criatividade</td>
<td>Pouco criativo</td>
<td>Criativo</td>
<td>Muito criativo e inovador</td>
</tr>
</tbody>
</table>
<div class="solution-box">
<h3>💡 Orientações e Dicas</h3>
<p><strong>Passo a passo sugerido:</strong></p>
<ol>
<li>Analise cuidadosamente o problema proposto</li>
<li>Identifique os conceitos teóricos envolvidos</li>
<li>Planeje sua solução antes de implementar</li>
<li>Execute com atenção aos detalhes técnicos</li>
<li>Teste extensivamente sua solução</li>
<li>Documente o processo e resultados</li>
<li>Prepare uma apresentação clara dos resultados</li>
</ol>
<p><strong>💡 Dica Importante:</strong> Consulte o material da aula teórica, datasheet dos componentes (quando aplicável) e não hesite em pedir ajuda ao professor durante a atividade!</p>
</div>
</div>
'''
    
    html += f'''<div class="nav-buttons">
<a href="{prev_link}" class="nav-btn{prev_disabled}">⬅️ Guia Anterior</a>
<a href="index_arquitetura.html" class="nav-btn">📚 Índice</a>
<a href="{next_link}" class="nav-btn{next_disabled}">Próximo Guia ➡️</a>
</div>
</div>
</body>
</html>'''
    
    return html

# Gerar todos os arquivos
print("Gerando arquivos...")
for semana in semanas:
    num = semana['num']
    
    # Gerar arquivo de aula
    aula_html = gerar_aula(semana)
    with open(f'arquitetura_semana{num:02d}_aula.html', 'w', encoding='utf-8') as f:
        f.write(aula_html)
    print(f"✓ Gerado: arquitetura_semana{num:02d}_aula.html")
    
    # Gerar arquivo de guia
    guia_html = gerar_guia(semana)
    with open(f'arquitetura_semana{num:02d}_guia.html', 'w', encoding='utf-8') as f:
        f.write(guia_html)
    print(f"✓ Gerado: arquitetura_semana{num:02d}_guia.html")

print(f"\n✅ Gerados {len(semanas) * 2} arquivos com sucesso!")
print("   - 20 arquivos de aula")
print("   - 20 arquivos de guia")
