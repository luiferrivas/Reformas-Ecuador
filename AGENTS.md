# 🏛️ AGENTS.md — DOCTRINA MANDATORIA DE OPERACIÓN DE AGENTES Y REQUERIMIENTOS TÉCNICOS

> **Consorcio Industrial Kronos — Reglas Inviolables de Ejecución aplicadas al Proyecto Reformas Ecuador**  
> *Este documento es de cumplimiento estricto e ininterrumpido para todos los agentes IA, subagentes, analistas técnicos y modelos que operen en este repositorio.*

---

## 🚨 MANDAMIENTOS INVIOLABLES DE CONDUCTA Y EVALUACIÓN

Todos los agentes IA y subagentes deberán regirse obligatoriamente bajo las siguientes 12 reglas fundamentales:

### 1. No Complacencia
Queda estrictamente prohibido emitir respuestas complacientes, condescendientes, halagadoras o diseñadas para complacer a sesgos previos. Si una propuesta, cálculo, hipótesis o especificación presenta debilidades, inconsistencias o deficiencias técnicas, **DEBE** ser señalada con absoluto rigor crítico inmediato.

### 2. Cero Positivismo Naive (Cero Maquillaje de Cifras)
Está prohibido maquillar números, forzar datos financieros/termodinámicos, inventar eficiencias mágicas o alterar parámetros para hacer que un proyecto cuadre. Si una restricción física, química o financiera limita la viabilidad o escala de un proyecto, se presentará con crudeza y exactitud matemática.

### 3. Realismo Estricto en Respuestas y Modelos
Todos los balances de masa y energía, rendimientos pirometalúrgicos, cinéticas biológicas, costos unitarios de operación (OPEX/CAPEX), tiempos de retención y plazos regulatorios deben ser calculados y evaluados bajo las leyes reales de la física, termodinámica y economía de mercado.

### 4. No Omitir la Realidad Experimental Empírica
Prohibido ignorar, desestimar o sesgar los datos empíricos de campo, resultados de ensayos de laboratorio y pruebas de concepto reales. Toda teoría o modelo predictivo debe confrontarse directamente con la realidad experimental empírica.

### 5. Compatibilidad Estricta LaTeX / KaTeX (Aislamiento de Entornos y Formato Puro)
Toda notación matemática, fórmula, ecuación o expresión formateada en LaTeX debe ser 100% compatible con KaTeX sin errores visuales:
* **Separación Estricta de Tablas y Bloques Matemáticos:** Separa estrictamente los bloques matemáticos KaTeX (`$$ ... $$`) de las tablas Markdown. No utilices sintaxis `\begin{array}` ni delimitadores `$` en celdas de tablas Markdown.
* **Formato de Tablas de Datos:** Presentar las tablas de datos en Markdown estándar con números limpios, texto plano o caracteres Unicode (ej. `3.26%`, `2,300 m`, `CO2`, `H2SO4`, `±500 kV`).
* **Ecuaciones y Fórmulas en Bloques Aislados:** Colocar todas las ecuaciones y fórmulas exclusivamente en bloques independientes `$$ ... $$` en sus propias líneas fuera de tablas y listas.
* **Sintaxis Pura de Unidades:** Exigir que todas las unidades y variables en KaTeX utilicen la sintaxis pura `\text{...}`.

### 6. Bitácora Obligatoria de Decisiones y Descartes
Todo documento, especificación técnica, informe o propuesta arquitectónica creada dentro de cualquier proyecto DEBE incluir una sección/bitácora explícita que documente el fundamento de las decisiones adoptadas (pros, contras y trade-offs) y la justificación técnica exacta del porqué ciertas alternativas o ideas fueron rechazadas o descartadas. El objetivo es preservar la memoria histórica, evitar la pérdida de información crítica y prevenir el retrabajo de evaluar nuevamente opciones que ya fueron auditadas y desestimadas con sustento real.

### 7. Cero Dependencia de Subsidios e Independencia Financiera Radical (Captura de Subsidios Externos Exclusivamente como Upside Marginal)
Queda estrictamente prohibido fundamentar la rentabilidad, viabilidad financiera o escalabilidad de cualquier proyecto, proceso industrial o "propuesta ecologista" en subsidios estatales, subvenciones gubernamentales, créditos blandos a fondo perdido o transferencias públicas (Kronos no subsidia a nadie internamente, ni el Estado ecuatoriano o gobiernos locales nos subsidiarán nada).
* **Descarte de "Ideología Verde Subvencionada":** Si un proyecto o idea ecologista requiere subsidios estatales para funcionar o ser rentable, es irrealizable para Kronos y DEBE ser declarado como no viable y descartado en la Bitácora de Decisiones.
* **Aprovechamiento Asimétrico de Subsidios Externos ("Bonos de Carbono"):** Se autoriza capturar e integrar esquemas de subsidio exógenos o incentivos internacionales de terceros (ej. bonos de carbono, créditos verdes de la UE, CBAM, tax credits extranjeros), ÚNICAMENTE bajo la condición estricta de que NUNCA sean puestos como ingreso principal, base del flujo de caja o condición de viabilidad del proyecto. Deben modelarse exclusivamente como un ingreso marginal secundario ("upside bonus") agregado a un modelo de negocio que ya es 100% rentable y autosostenible por sí solo en el mercado real.

### 8. Formato Obligatorio de Monedas y Valores Financieros (Dólares como Base + Moneda Local en Paréntesis)
En toda respuesta, informe, tabla, análisis económico o presupuesto, todo valor monetario o cifra financiera DEBE ser presentado primordialmente en **Dólares de los Estados Unidos (USD)**. Cuando la transacción, costo o mercado involucrado utilice una moneda local o extranjera distinta al dólar (ej. Euros, Pesos Colombianos, Soles Peruanos, Yenes, Reales Brasileños, Francos Suizos, etc.), dicha moneda local DEBE colocarse obligatoriamente entre paréntesis a continuación del valor en dólares (ej. `3.50 USD (3.20 EUR)`, `150 USD (600,000 COP)`, `100 USD (370 PEN)`).

### 9. Archivo SUMMARY.md Obligatorio por Subproyecto (L1 Cache Contractual, Técnico y Financiero)
Cada subproyecto dentro del Consorcio Kronos debe mantener de forma obligatoria un archivo `SUMMARY.md` en su directorio raíz como fuente primaria e inicial de consulta:
* **Propósito Contractual (L1 Cache):** Cuando un subproyecto, analista o subagente requiera consultar dependencias, especificaciones o generalidades de otro subproyecto, consultará primero `SUMMARY.md`, evitando la lectura innecesaria de documentos extensos y reduciendo el consumo de tokens.
* **Contenido Mínimo Estandarizado:** Debe contener obligatoriamente:
  1. **Misión y Estado Operativo Actual:** Objetivo concreto y fase de desarrollo (En diseño / Auditado Red Team / Congelado / Descartado).
  2. **Contrato de Interfaces (Simbiosis Industrial):** Insumos requeridos (entradas desde otros proyectos) y entregables/subproductos generados (salidas hacia otros proyectos).
  3. **Parámetros Técnicos Críticos Congelados:** 3 a 5 especificaciones numéricas innegociables (capacidades, cotas, flujos, presiones, potencias).
  4. **Modelo Financiero, Fases y Rentabilidad:**
     * **Fases de Ejecución y CAPEX:** Desglose del presupuesto de inversión por etapas o hitos constructivos expresado en USD (y moneda local en paréntesis si aplica).
     * **Estructura de OPEX:** Costo operativo recurrente anual/mensual y cuellos de botella de mantenimiento.
     * **Modelo de Ingresos y Ganancias (EBITDA / ROI / Payback):** Proyección de monetización y ganancias netas autosuficientes, cumpliendo estrictamente la prohibición de depender de subsidios.
  5. **Bitácora de Decisiones y Descartes Clave:** Justificación técnica de alternativas aprobadas y motivos explícitos de opciones rechazadas.
  6. **Índice de Documentación Profunda:** Enlaces a planos, memorias de cálculo, scripts de Python y especificaciones detalladas.
* **Regla de Cero Deriva (Zero Drift):** Es terminantemente prohibido alterar parámetros técnicos, balances de materia, rutas, cotas, fases constructivas o cifras financieras en un subproyecto sin reflejar dicho cambio de inmediato en su archivo `SUMMARY.md` en el mismo turno o commit.

### 10. Cálculo Riguroso de Payback y Doble Métrica Financiera (Payback Crudo vs. Payback Acelerado por Negociación Estatal)
Todo análisis de retorno de inversión (Payback) debe calcularse bajo estricta rigurosidad tributaria y de mercado:
* **Deducción Obligatoria de Cargas Reales (Prohibición de Payback sobre EBITDA Bruto):** Queda terminantemente prohibido calcular el período de repago dividiendo CAPEX entre EBITDA bruto simple sin descontar impuestos ni deducciones de ley. El flujo de caja debe deducir obligatoriamente: (1) Impuesto a la renta corporativo y participaciones laborales obligatorias (ej. 15% trabajadores + 25% IR en Ecuador; 35% renta corporativa en Colombia más sobretasas), (2) Regalías mineras y petroleras brutas sobre ingresos, (3) Costos adicionales no operativos (seguros de riesgo andino, capital de trabajo, contingencias, servidumbres), y (4) Presión de precios y erosión de márgenes por competencia real de mercado.
* **Doctrina de Doble Métrica de Payback:** Todo modelo financiero reportará obligatoriamente dos métricas de retorno:
  1. **Payback Crudo / Real de Resistencia (*Unshielded Payback*):** Calculado bajo el régimen fiscal ordinario severo sin beneficios fiscales ni acuerdos estatales. Esta cifra representa la solvencia base del consorcio: si el proyecto no es viable bajo este escenario crudo, queda automáticamente descartado (cumplimiento estricto del Mandamiento 7 de Cero Dependencia de Subsidios).
  2. **Payback Acelerado por Negociación Estatal (*Fast-Track / Negotiated Payback*):** Información estratégica complementaria considerando figuras legítimas de negociación soberana (ej. Contratos de Inversión con exención temporal de ISD/aranceles, esquemas de *Obras por Impuestos* para cruzar CAPEX contra tributos futuros, depreciación acelerada o diferimiento temporal de regalías preoperativas). Esta métrica se utiliza como instrumento estratégico de negociación con los Estados para pactar repagos rápidos en los primeros años críticos de la obra y mitigar el riesgo percibido por los inversionistas, sin comprometer jamás la viabilidad del proyecto si dicha negociación no se concreta.

### 11. Benchmark Obligatorio de Petróleo (WTI como Referencia Base + Spread Brent Comparativo)
En toda formulación técnica, contrato de *tolling*, análisis de sensibilidad, proyección financiera o balance económico que dependa del precio del petróleo crudo dentro del Consorcio Kronos:
* **Marcador Primario Obligatorio (WTI):** El referente mandatorio es el **West Texas Intermediate (WTI)**, cotizado en USD por barril (`USD/bbl`), por constituir el estándar físico de precios en el continente americano y el marcador natural de paridad para los crudos de Ecuador (Oriente/Napo) y Colombia (Castilla/Vasconia).
* **Mención Comparativa de Brent (Solo para Spread):** Se permite una mención secundaria y concisa al marcador **Brent** exclusivamente como referencia de mercado global para indicar el diferencial o *spread* (ej. `Brent +X.XX USD/bbl`), pero la base de cálculo de tarifas, modelos de ingresos y sensibilidades financieras debe formularse estrictamente sobre WTI.

### 12. Protocolo Mandatorio de Carpetas `historico/` y Regla de Oro de Descarte
Se creará obligatoriamente una carpeta `historico/` dentro de cada directorio de subproyecto o módulo técnico donde corresponda archivar versiones anteriores, borradores superados o propuestas que tras análisis se consideren obsoletas o fallidas:
* **Exclusividad de la Raíz Canónica:** Los documentos vigentes en la raíz de cada carpeta contendrán EXCLUSIVAMENTE las versiones y decisiones actuales oficiales cuando se realizan auditorías, correcciones o búsqueda de inconsistencias, eliminando ruido y contradicciones de diseño.
* **Regla de Oro para la Carpeta `historico/`:** Cada archivo que se mueva o cree dentro de `historico/` contendrá OBLIGATORIAMENTE en su cabecera una **Bitácora Forense de Decisión y Descarte** con enlaces directos (`file:///...`) hacia la versión canónica vigente, justificando con rigor técnico por qué se descartó, qué números o supuestos fallaban (presiones, temperaturas, balances de masa, CAPEX/OPEX, seguridad) y qué decisión lo superó.
* **Preservación Antiamnesia y Lecciones Aprendidas:** Toda propuesta evaluada queda registrada con sus causales de descarte. Si en el futuro se vuelven a suscitar las mismas dudas o ideas similares, el consorcio sabrá de inmediato qué propuestas se tuvieron antes, por qué resultaron fallidas y qué alternativa técnica consolidada las sustituyó.
