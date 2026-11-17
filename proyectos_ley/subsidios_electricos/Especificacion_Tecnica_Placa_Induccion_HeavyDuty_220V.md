# Especificación Técnica de Ingeniería y Diseño Industrial: Placa de Inducción Heavy-Duty 220V (2 Quemadores)

> **Consorcio Industrial Kronos — Paquete de Propiedad Intelectual y Fabricación OEM/ODM**  
> *Módulo de Eficiencia Energética y Cocción Limpia — Subproyecto Subsidios Eléctricos*  
> *Código de Especificación:* `KRN-IND-220V-2Q-HD-2026`  
> *Sujeto a la Doctrina Mandatoria de Operación (AGENTS.md) — Mandamientos 1, 3, 5, 6 y 8.*

---

## 1. Justificación de Ingeniería: Por qué este Diseño es Indispensable y Único

### 1.1. Diagnóstico del Vacío Tecnológico en el Mercado
Las cocinas de inducción disponibles en el mercado latinoamericano se dividen en dos extremos disfuncionales para el contexto rural y popular:
1. **Placas de sobremesa de 110V/120V:** Pensadas para solteros o camping. Están limitadas a 1,500–1,800 W en total debido a la capacidad de los tomacorrientes domésticos estándar (15 A). No tienen potencia para hervir agua con rapidez en una hornilla mientras se fríe en la otra. Además, su corriente elevada a 120V ($I \approx 15\text{ A}$) recalienta cables de entrada precarios.
2. **Cocinas empotrables de 4 quemadores a 220V (6,000–7,200 W):** Formatos de 300 a 500 USD diseñados para mesones de granito en departamentos urbanos. En el campo, su demanda de 7 kW quema los transformadores de distribución rurales de 15 a 25 kVA, y sus cubiertas delgadas de vidrio desnudas se astillan ante el primer impacto de una olla campesina de 15 kg.

### 1.2. Propuesta de Valor y Diferenciadores Exclusivos de la IP Kronos

```
                     ARQUITECTURA DE LA PLACA KRONOS HEAVY-DUTY
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. Chasis y Marco: Acero Inoxidable Austenítico NO Magnético (AISI 304)    │
│    -> Soporta ollas de 35 kg sin calentamiento parásito ni pérdidas Joule   │
│ 2. Superficie Protegida: Borde sobre-elevado 2.5 mm sobre vitrocerámica     │
│ 3. Alimentación: 220V Bifásica (15.9 A) -> 75% menos pérdidas que 120V     │
│ 4. Potencia: 3,500 W nominales con Limitador Dinámico (Power Sharing 2,800W)│
│ 5. Controles: Perillas rotativas encoder IP54 (inmunes a vapor, grasa/harina)│
│ 6. Protección Eléctrica: Varistores MOV de 450 Joules contra rayos andinos │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. El Soporte Estructural: Acero Inoxidable Austenítico No Magnético

### 2.1. El Reto Físico de la Inducción Electromagnética
En una cocina de inducción, la bobina de cobre genera un campo magnético alterno de alta frecuencia ($f \approx 20\text{ a }40\text{ kHz}$). Si el chasis o marco estructural está fabricado en hierro o acero al carbono ferromagnético ($\mu_r \gg 1$), el campo magnético inducirá corrientes de Foucault (*Eddy currents*) en el propio marco de la cocina:
* El marco se calentaría peligrosamente (riesgo de quemaduras graves).
* Se disiparía energía útil en el marco en lugar de la olla, degradando la eficiencia térmica del 88% a menos del 60%.
* Se dispararían las protecciones de sobretemperatura del circuito resonante.

### 2.2. La Solución Kronos: Acero Austenítico AISI 304 / AISI 316
Para dotar al equipo de una resistencia mecánica extrema sin interferir con el campo electromagnético, el marco perimetral superior y el subchasis estructural de soporte de carga se fabrican exclusivamente en **acero inoxidable austenítico grado AISI 304 (o AISI 316)**:
* **Permeabilidad Magnética Relativa:** $\mu_r \approx 1.002\text{ a }1.008$ (virtualmente transparente al flujo magnético, idéntico al aire o al vacío).
* **Ausencia de Calentamiento Parásito:** No interactúa con las líneas de inducción de las bobinas toroidales de litz.
* **Capacidad de Carga Estática y Dinámica:** Espesor de chapa de **1.5 mm estampada con nervaduras de refuerzo**, capaz de soportar cargas verticales de hasta **35.0 kg por hornilla (70.0 kg en total)** y absorber caídas accidentales de ollas llenas de maíz o papas sin flectar.
* **Borde Perimetral Sobre-Elevado (Crown Rim):** El marco de acero inoxidable sobresale **2.5 mm verticalmente por encima de la placa de vitrocerámica**. Cuando se desliza o asienta una paila pesada de hierro, el impacto es absorbido mecánicamente por el acero inoxidable, impidiendo el choque directo contra el filo del cristal.

---

## 3. Justificación Termodinámica y Eléctrica: 220V Bifásico y 2 Hornillas

### 3.1. Por qué 220V y no 120V

1. **Reducción del 75% en Pérdidas por Efecto Joule en la Vivienda:**  
   La potencia disipada en forma de calor residual en los cables de la instalación doméstica se rige por:

$$P_{\text{pérdida}} = I^2 \times R$$

   Para suministrar una potencia nominal de 3,500 W:
   * A 120V: $I = 3,500\text{ W} / 120\text{ V} \approx 29.17\text{ A}$. Exigiría cable calibre 8 AWG o 6 AWG, imposible de instalar en chozas campesinas.
   * A 220V: $I = 3,500\text{ W} / 220\text{ V} \approx 15.91\text{ A}$. Se utiliza conductor convencional calibre 12 AWG con un breaker bipolar de 20 A.  
   Dado que la corriente se reduce a la mitad ($I_{220} \approx 0.54 \times I_{120}$), las pérdidas térmicas en los cables caen a:

$$\left(\frac{15.91}{29.17}\right)^2 \approx 0.297 \approx 30\%$$

   Es decir, una reducción de más del **70% al 75% en calor disipado y caída de tensión**.

2. **Equilibrio Simétrico en el Transformador Rural de Distribución:**  
   Al ser una carga bifásica pura conectada entre fases vivas ($L_1$ y $L_2$), la corriente tomada del transformador del poste es simétrica, eliminando la corriente de desbalance por el neutro que recalienta los transformadores rurales de CNEL.

3. **Sinergia con el Medidor Electrónico AMI de la Fase 2:**  
   En la Fase 2 de la reforma, CNEL EP instala medidores bifásicos a 220V para individualizar los solares rurales. La acometida a 220V ya se encuentra instalada en el predio sin costo de inversión adicional para el usuario.

### 3.2. Por qué 2 Hornillas y no 4 ni 1

| Configuración | Potencia Nominal | Impacto en Red Rural | Costo Equipo | Funcionalidad en Hogar Rural | Veredicto Kronos |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1 Hornilla (120V)** | 1,500 W a 1,800 W | Nulo (baja demanda) | 35 a 45 USD | Insuficiente: no se puede preparar arroz y sopa a la vez. | **Descartada por disfuncional** |
| **4 Hornillas (220V)** | 6,000 W a 7,200 W | Crítico: quema transformadores | 300 a 500 USD | Excesivo: exige mesón empotrado de granito y sobreendeuda. | **Descartada por inviable (Error 2014)** |
| **2 Hornillas Heavy-Duty (220V)** | **3,500 W (con limitador)** | **Controlado y estable** | **75 a 85 USD** | **Óptimo: cocina completa de sobremesa para dos ollas grandes.** | **APROBADA (IP OFICIAL)** |

---

## 4. Especificaciones Técnicas y Lista de Materiales (BOM)

### 4.1. Parámetros Eléctricos y Electrónicos

| Parámetro | Valor Especificado | Tolerancia / Norma |
| :--- | :--- | :--- |
| **Tensión de Operación Nominal** | 220 V AC bifásica (L1 + L2 + PE) | Rango dinámico operativo: 175 V a 250 V AC |
| **Frecuencia de Red** | 60 Hz | ±3 Hz |
| **Potencia Nominal Hornilla A (Principal)** | 2,000 W | Diámetro de bobina: 200 mm (Ollas de 18 a 28 cm) |
| **Potencia Nominal Hornilla B (Auxiliar)** | 1,500 W | Diámetro de bobina: 160 mm (Ollas de 12 a 20 cm) |
| **Potencia Máxima Simultánea con Power Sharing** | **2,800 W** *(Modo Rural por defecto)* | Limitador dinámico firmware para proteger postes |
| **Potencia Máxima Modo Pleno (Desbloqueable)** | **3,500 W** | Seleccionable mediante microswitch interno |
| **Eficiencia Energética de Conversión** | Mayor o igual a 88.5% | Según ensayo IEC 60335-2-6 |
| **Frecuencia de Conmutación de Inversores** | 20 kHz a 35 kHz | Control PWM por resonancia cuasi-resonante |
| **Protección contra Sobretensiones (Rayos)** | Varistor de Óxido Metálico (MOV) de 450 J | Con supresor TVS de respuesta en < 25 ns |
| **Grado de Aislamiento y Puesta a Tierra** | Clase I | Resistencia de aislamiento > 100 MΩ a 500V DC |

### 4.2. Componentes Críticos del Circuito Electrónico (Hardware)

1. **Semiconductores de Potencia (IGBTs):**  
   Dos transistores IGBT de 1,200 V / 40 A en encapsulado TO-247 (tipo Infineon IHW40N120R3 o equivalente homologado), sobredimensionados para operar a menos del 60% de su capacidad térmica máxima.
2. **Disipador Térmico Masivo:**  
   Bloque de aluminio extruido anodizado de **$220 \times 80 \times 40\text{ mm}$** con túnel de tiro forzado.
3. **Ventilación con Rodamientos Sellados:**  
   Doble ventilador tipo *Brushless DC* de 18V / 0.20 A con **doble rodamiento de bolas (Dual Ball Bearing)** vida útil nominal de 50,000 horas, protegido contra polvo y ceniza con filtro lavable inferior.
4. **Bobinas de Inducción de Hilo Litz:**  
   Bobinas planas devanadas con hilo Litz de cobre electrolítico de alta pureza (mínimo 120 hebras de 0.1 mm), con 8 barras de ferrita de alta permeabilidad magnética en base para confinar el flujo hacia arriba.
5. **Sensores de Temperatura:**  
   Termistores NTC de precisión en contacto directo con el centro del cristal vitrocerámico para corte automático por sobretemperatura ($T_{\text{corte}} = 240^\circ\text{C}$) o ebullición seca.

---

## 5. Diseño Mecánico, Ergonomía y Controles Físicos

### 5.1. Dimensiones y Planos de Envolvente
* **Ancho:** 590 mm.
* **Profundidad:** 360 mm.
* **Altura Total:** 75 mm (incluyendo patas de goma de amortiguación de 15 mm).
* **Peso Neto:** 5.80 kg.
* **Material del Chasis Inferior:** Chapa de acero galvanizado electrocincado de 0.8 mm con ranuras de ventilación tipo persiana anti-goteo.

### 5.2. Interfaz de Usuario a Prueba de Campo (Anti-Táctil Frágil)
* **El Problema del Touch Digital en el Campo:**  
  Las amas de casa campesinas cocinan con harina, masa de maíz, agua o manteca en las manos. Los paneles táctiles capacitivos de vidrio se bloquean, pitan o no responden con dedos mojados o sucios.
* **La Solución Kronos:** **Perillas Mecánicas Rotativas Selladas (Encoder Digital Óptico / Potenciómetro IP54):**
  * Control por perilla de giro continuo con pasos táctiles audibles (9 niveles de potencia claramente diferenciados).
  * Display LED rojo de 7 segmentos de alta luminosidad (visible bajo luz solar directa en cocinas rurales abiertas) que muestra el nivel de potencia (1 a 9) y códigos de diagnóstico de error claros (E1: bajo voltaje, E2: sobrecalentamiento, E3: sin olla).
  * Presionar la perilla enciende/apaga el quemador.

---

## 6. Algoritmo de Firmware y Limitador Dinámico (*Power Sharing*)

El firmware embebido en el microcontrolador (arquitectura 32-bit ARM Cortex-M0) ejecuta la subrutina de gestión de demanda comunitaria:

```
                  ALGORITMO DE GESTIÓN DE POTENCIA DINÁMICA
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. Hornilla A encendida sola -> Rango: 200 W a 2,000 W (Potencia Plena)     │
│ 2. Hornilla B encendida sola -> Rango: 200 W a 1,500 W (Potencia Plena)     │
│ 3. Ambas Hornillas activadas simultáneamente:                               │
│    IF Selector_Rural == TRUE:                                               │
│       Potencia_Total = Potencia_A + Potencia_B                              │
│       IF Potencia_Total > 2,800 W:                                          │
│          Potencia_A = 1,800 W (Fija prioritaria para hervir)                │
│          Potencia_B = Modulada dinámicamente a 1,000 W (Tope 2,800 W)       │
│    ELSE:                                                                    │
│       Potencia_Total = 3,500 W (Modo Urbano de Red Robusta)                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

Este limitador garantiza que la placa **nunca sobrepase los 12.7 A** en el modo rural, permitiendo que 15 o 20 placas funcionen al unísono en el mismo alimentador comunal sin provocar caídas de tensión ni cortes en el transformador.

---

## 7. Modelo Financiero y Costo Industrial de Fabricación (BOM)

*(Valores en USD por unidad para lote industrial de 50,000 unidades)*

| Subensamble / Componente | Descripción Técnica | Costo FOB Fabricación (USD) |
| :--- | :--- | :--- |
| **Chasis y Marco AISI 304** | Chapa acero inox no magnético 1.5 mm estampada | 14.50 USD |
| **Vidrio Vitrocerámico** | Cristal vitrocerámico negro 550 x 320 x 4 mm resistente a 700 °C | 12.80 USD |
| **Bobinas Inducción Litz (2x)** | Hilo Litz cobre puro con 8 ferritas y soporte mica | 9.20 USD |
| **Tarjeta Electrónica de Potencia** | PCB FR4 con 2x IGBTs Infineon 40A, puente rectificador y MOV 450J | 16.50 USD |
| **Tarjeta de Control y Display** | Microcontrolador ARM, perillas rotativas IP54 y LEDs | 5.80 USD |
| **Disipación y Ventilación** | Disipador aluminio extruido masivo y 2x ventiladores Dual Ball | 6.40 USD |
| **Cable de Poder y Conector** | 1.8 m cable encauchetado 3x12 AWG con enchufe NEMA 6-20P | 4.20 USD |
| **Empaque Reforzado y Manual** | Caja cartón corrugado triple con amortiguación EPE para camino rural | 2.60 USD |
| **COSTO TOTAL INDUSTRIAL FOB** | **Placa completa terminada y embalada** | **72.00 USD** |
| *Logística, Arancel 0% y Margen* | *Flete marítimo, distribución cantonal y margen de percha (15%)* | *11.00 USD* |
| **PVP FINAL AL PÚBLICO** | **Precio de venta sugerido en almacenes y cooperativas** | **83.00 USD** |

---

## 8. Normas Técnicas y Protocolos de Ensayo para Homologación

Para el licenciamiento y fabricación masiva, el prototipo debe certificar en laboratorios acreditados del INEN las siguientes pruebas:

1. **IEC 60335-2-6 / NTE INEN 2260:** Ensayos de seguridad en aparatos electrodomésticos de cocción.
2. **Prueba de Impacto Mecánico (Impact Drop Test):** Ensayo con esfera de acero de 500 g dejada caer desde 1.0 metro de altura sobre el centro del cristal y sobre el marco de acero inoxidable (sin fracturas ni astillamiento).
3. **Prueba de Resistencia de Carga Continua:** Sometimiento a 40.0 kg de peso estático sobre cada hornilla durante 72 horas consecutivas sin deformación permanente de chasis.
4. **Ensayo de Sobretensión y Descarga Transitoria (Surge Test):** IEC 61000-4-5 nivel 3 (inyección de pulso transitorio de $2\text{ kV} / 1\text{ kA}$ entre fases y tierra sin degradación de los varistores MOV ni parada del firmware).
5. **Ensayo de Inmunidad Térmica y Trabajo Continuo:** Operación a potencia máxima continua durante 8 horas en cámara ambiental a $40^\circ\text{C}$ y 85% de humedad relativa sin disparo térmico.

---

## 9. Cláusulas de Licenciamiento de Propiedad Intelectual (IP)

El diseño industrial, esquemas esquemáticos de PCB, archivos Gerber, planos CAD en formato STEP y código fuente de firmware contenidos bajo la especificación `KRN-IND-220V-2Q-HD-2026` quedan registrados bajo los siguientes términos de explotación:

1. **Licencia de Fabricación Nacional Preferente (Ecuador):** Cero regalías para fabricantes ecuatorianos de línea blanca (Indurama, Fibroacero, Mabe Ecuador) bajo el compromiso de garantizar un PVP final al usuario no mayor a **85.00 USD**.
2. **Contratos de Fabricación ODM/OEM Internacional:** Autorización a importadores y mayoristas para encargar lotes industriales a fábricas certificadas en el extranjero cumpliendo estrictamente con el BOM y las pruebas IEC/INEN descritas en este documento.
3. **Cesión de Uso a Entidades Estatales:** Licencia perpetua y gratuita a favor del Ministerio de Energía y Minas, CNEL EP y BanEcuador para planes sociales de electrificación rural sin intermediarios comerciales privados.
