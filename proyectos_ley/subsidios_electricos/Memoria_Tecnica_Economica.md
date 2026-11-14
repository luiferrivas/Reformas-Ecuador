# MEMORIA TÉCNICA, ECONÓMICA Y TARIFARIA

## PROYECTO DE LEY REFORMATORIA A LA LOSPEE: ASIGNACIÓN PRIORITARIA DE ENERGÍA DE MENOR COSTO Y RÉGIMEN ANTE CONTINGENCIAS CLIMÁTICAS

---

### 1. INTRODUCCIÓN Y DIAGNÓSTICO ESTRUCTURAL

El sistema eléctrico ecuatoriano ha operado históricamente bajo una paradoja: cuenta con una capacidad hidroeléctrica instalada capaz de abastecer más del 80% de la demanda en épocas de pluviosidad normal a costos marginales sumamente reducidos (1.5 a 3.5 ¢USD/kWh en operación y mantenimiento), pero sucumbe cíclicamente ante los periodos de estiaje (octubre a marzo) debido a la falta de diversificación firme, la obsolescencia del parque térmico de respaldo y un modelo tarifario que acumuló un déficit financiero multimillonario.

El esquema tradicional de subsidios eléctricos en el Ecuador adolecía de tres fallas críticas de diseño:
1. **Regresividad distributiva:** Las tarifas planas o subvencionadas sin topes técnicos reales beneficiaban desproporcionadamente a usuarios de ingresos medios-altos y altos con alto consumo de energía (aires acondicionados intensivos, piscinas temperadas, grandes residencias), desviando recursos del fisco que debían proteger a los quintiles más vulnerables.
2. **Ausencia de incentivos para el ahorro en periodos de crisis:** Al no existir una señal de precio real para los consumos no esenciales, la demanda residencial y comercial no se moderaba durante los estiajes, agravando el déficit de potencia.
3. **Déficit tarifario y degradación de activos:** Al congelarse las tarifas por razones políticas durante las sequías, las empresas públicas (CELEC EP y Distribuidoras) debían asumir los altos costos de importar electricidad (hasta 30-50 ¢USD/kWh desde Colombia) y de quemar diésel/fuel oil, generando una asfixia de liquidez que impedía dar mantenimiento al parque existente.

Esta propuesta legislativa resuelve estructuralmente estos tres problemas mediante una arquitectura técnica basada en:
- Bloques de subsistencia preferenciales con asignación contable de la energía más barata;
- Tarifa a costo real pleno para consumos no preferentes y excedentes;
- Orden de mérito en cascada y factor de ajuste temporal por estiaje con garantía de no déficit;
- Creación de un fondo intangible para reinversión eléctrica con los excedentes recaudados.

---

### 2. DETERMINACIÓN Y MODELADO DE LOS UMBRALES DE CONSUMO

```
+---------------------------------------------------------------------------------------------------+
|                                  ARQUITECTURA DE CONSUMO Y TARIFAS                                |
+------------------------------------+--------------------------------------------------------------+
| CATEGORÍA                          | TRATAMIENTO TARIFARIO                                        |
+------------------------------------+--------------------------------------------------------------+
| Residencial (0 a 250 kWh/mes)      | Tarifa Más Barata Posible (Asignación prioritaria de hidro/  |
|                                    | eólica/solar de menor costo según región)                    |
+------------------------------------+--------------------------------------------------------------+
| Residencial (> 250 kWh/mes)        | Tarifa a Costo Real Pleno sobre el excedente consumido       |
+------------------------------------+--------------------------------------------------------------+
| Alimentación Popular y Tiendas     | Tarifa Más Barata Posible (Asignación prioritaria)           |
| (0 a 500 kWh/mes)                  |                                                              |
+------------------------------------+--------------------------------------------------------------+
| Alimentación Popular y Tiendas     | Tarifa a Costo Real Pleno sobre el excedente consumido       |
| (> 500 kWh/mes)                    |                                                              |
+------------------------------------+--------------------------------------------------------------+
| Comercial General, Gran Industria, | 100% Tarifa a Costo Real Pleno (Sin subsidio público)        |
| Sector Público, Grandes Usuarios   |                                                              |
+------------------------------------+--------------------------------------------------------------+
```

#### 2.1. Bloque Residencial Familiar: Umbral de 250 kWh/mes
- **Fundamento Demográfico y Estadístico:**
  - El consumo promedio de un hogar ecuatoriano de 4 habitantes en la región Sierra (Quito, Cuenca, Ambato) se sitúa entre **120 y 160 kWh/mes**, destinado principalmente a iluminación LED, refrigeradora eficiente, televisión, pequeños electrodomésticos y computación.
  - En la región Costa y Amazonía (Guayaquil, Manta, Machala, Lago Agrio), el uso estacional de ventilación o un equipo de aire acondicionado de bajo consumo (inverter) eleva el promedio de los hogares típicos a un rango de **180 a 230 kWh/mes**.
  - Por ende, el umbral de **250 kWh/mes** cubre holgadamente el consumo vital y de confort básico de aproximadamente el **78% de la población residencial ecuatoriana**.
- **Mecánica del Cobro Excedente:**
  - A diferencia de esquemas punitivos de corte abrupto (donde pasarse de 1 kWh eliminaba todo el subsidio hacia atrás), la reforma establece un cobro marginal por tramos:
    $$\text{Factura Residencial} = (C_{\text{preferente}} \times \min(\text{Consumo}, 250)) + (C_{\text{real}} \times \max(0, \text{Consumo} - 250)) + \text{Cargos de Red y Alumbrado}$$
  - Esto protege el presupuesto familiar básico mientras penaliza de forma transparente los consumos suntuarios o ineficientes.

#### 2.2. Bloque de Soberanía Alimentaria y Cadena Popular de Frío: Análisis Técnico (500 kWh vs. 800 kWh)

- **¿Es suficiente 500 kWh/mes para panaderías? Diagnóstico de Carga Electromecánica:**
  A fin de responder con rigor técnico a los requerimientos energéticos reales de la cadena popular de alimentos, se levantó el inventario de consumo de potencia y factor de uso en dos tipologías clave de establecimientos de la economía popular ecuatoriana:

  ```
  +-------------------------------------------------------------------------------------------------------+
  |              CURVA DE CARGA TÍPICA: COMERCIO MINORISTA vs. PANADERÍA CON OBRADOR                     |
  +-------------------------------------------+---------------------+---------------+---------------------+
  | EQUIPO ELECTROMECÁNICO                    | POTENCIA NOMINAL    | USO DIARIO    | CONSUMO ESTIMADO    |
  |                                           | (kW / HP)           | ESTIMADO      | MENSUAL (kWh/mes)   |
  +-------------------------------------------+---------------------+---------------+---------------------+
  | **A. TIENDA DE BARRIO / MICROMERCADO:**                                                               |
  | 1-2 Vitrinas refrigeradas (bebidas/lácteos)| 0.25 kW c/u         | 24 h (ciclos) | 160 - 220 kWh/mes   |
  | Congelador horizontal (helados/carnes)    | 0.20 kW             | 18 h (ciclos) | 90 - 120 kWh/mes    |
  | Iluminación LED, punto de venta y router  | 0.15 kW             | 14 h          | 60 - 80 kWh/mes     |
  | Balanza digital y rebanadora básica       | 0.10 kW             | 4 h           | 12 - 18 kWh/mes     |
  | **TOTAL TIENDA DE ABARROTES / FRUTERÍA**  |                     |               | **322 - 438 kWh/mes**|
  +-------------------------------------------+---------------------+---------------+---------------------+
  | **B. PANADERÍA ARTESANAL CON OBRADOR:**                                                               |
  | Amasadora espiral industrial (1-2 quint.) | 3.0 kW (4 HP)       | 4 h           | 320 - 360 kWh/mes   |
  | Batidora planetaria (pasteles y masas)    | 1.5 kW (2 HP)       | 2.5 h         | 100 - 120 kWh/mes   |
  | Cámara de fermentación controlada / frío  | 1.2 kW              | 8 h           | 240 - 280 kWh/mes   |
  | Vitrina pastelera refrigerada (local)     | 0.35 kW             | 24 h (ciclos) | 180 - 220 kWh/mes   |
  | Rebanadora, iluminación, extracción aire  | 0.40 kW             | 10 h          | 90 - 120 kWh/mes    |
  | *Nota: Horno de cocción opera a GLP ind.* | (Combustible gas)   | -             | -                   |
  | **TOTAL PANADERÍA CON OBRADOR ACTIVO**    |                     |               | **930 - 1,100 kWh** |
  +-------------------------------------------+---------------------+---------------+---------------------+
  ```

- **Veredicto Técnico:**
  1. Para **tiendas de barrio, micromercados y fruterías**, el umbral de **500 kWh/mes es plenamente suficiente**, cubriendo entre el 110% y el 150% de sus requerimientos normales.
  2. Para **panaderías artesanales con obrador electromecánico**, el umbral original de 500 kWh/mes resultaba **insuficiente**, cubriendo únicamente el 45% al 55% de su gasto eléctrico indispensable. Dejar el 50% de su energía a tarifa comercial plena (~18 ¢USD/kWh) generaría un sobrecosto mensual de \$50 a \$80 dólares por panadería, forzando un aumento inmediato en el precio del "pan popular de batalla" (de 15 a 20 centavos por unidad).

- **Estructuración en Dos Niveles de Soberanía Alimentaria:**
  En virtud de esta evidencia técnica, la ley adopta una diferenciación categórica:
  - **Nivel 1 (hasta 500 kWh/mes):** Comercio minorista de alimentos (tiendas de víveres, micromercados barriales, fruterías).
  - **Nivel 2 (hasta 800 kWh/mes):** Panaderías artesanales con obrador, carnicerías con cuarto frío y centros comunitarios de acopio lechero rural. Con 800 kWh/mes, una panadería artesanal típica cubre entre el **80% y el 90%** de su requerimiento total a costo de energía barata, blindando el precio de los alimentos básicos de la mesa ecuatoriana contra la inflación.

---

### 3. ORDEN DE MÉRITO Y DIFERENCIACIÓN REGIONAL DE LA ENERGÍA MÁS BARATA

El despacho eléctrico y la asignación contable-regulatoria en el marco de la presente ley obedecen al principio de menor costo variable de generación (Order of Merit):

```
                        ORDEN DE MÉRITO CONTINENTAL (Costo Unitario LCOE/Marginal)
Menor Costo                                                                              Mayor Costo
   │                                                                                         │
   ├── [1. Hidroeléctrica Amortizada] (Paute, Mazar, Sopladora, Coca Codo) ── 1.5 - 3.5 ¢/kWh
   │
   ├── [2. Renovables No Convencionales Continentales] (Solar PV, Eólica, Biomasa) ── 4.5 - 6.5 ¢/kWh
   │
   ├── [3. Térmica a Gas Natural Local] (Termogas Machala, Amistad) ── 7.0 - 9.0 ¢/kWh
   │
   ├── [4. Térmica a Búnker / Fuel Oil No. 6] (Trinitaria, Esmeraldas) ── 11.0 - 15.0 ¢/kWh
   │
   └── [5. Térmica a Diésel e Importación Internacional] (Colombia/Perú en crisis) ── 18.0 - 35.0+ ¢/kWh
```

#### 3.1. Territorio Continental Ecuatoriano: Hidroelectricidad Amortizada
- Las grandes centrales hidroeléctricas públicas del Estado ecuatoriano presentan un costo marginal de operación y mantenimiento muy bajo, típicamente inferior a **3.5 centavos de dólar por kWh ($0.035 USD/kWh)**.
- Esta energía base limpia y de muy bajo costo es la que se asigna prioritariamente al Bloque Residencial (hasta 250 kWh) y al Bloque Alimentario (hasta 500 kWh).
- De agotarse la hidroelectricidad por factores estacionales, se recurre a la siguiente fuente más barata de la matriz (solar fotovoltaica, eólica y biomasa).

#### 3.2. Régimen Especial de la Provincia de Galápagos: Eólica y Solar Insular
- Galápagos no está interconectado a la red eléctrica continental.
- Históricamente, la generación térmica a diésel en las islas ha tenido un costo real superior a **35 a 50 ¢USD/kWh**, debido a los costos de transporte marítimo en barcazas de doble casco, riesgo de derrame ecológico y almacenamiento seguro.
- En contraste, los parques eólicos de San Cristóbal y Baltra, y los proyectos solares fotovoltaicos con baterías en Santa Cruz e Isabela generan energía a un costo normalizado local muy inferior al diésel importado (entre **8 y 14 ¢USD/kWh**).
- **Regla Territorial:** En Galápagos, la energía más barata asignada al Bloque Residencial de 250 kWh es obligatoriamente la generación eólica y solar local disponible, garantizando que el consumo de los habitantes insulares beneficie directamente a la transición ecológica y se reduzca la huella de carbono de las islas.

#### 3.3. Balance Energético Nacional: ¿Alcanza la energía hidroeléctrica barata para hogares y comida? ("¿Nos alcanza acaso la energía?")

Una interrogante técnica fundamental es si la matriz de generación de menor costo (principalmente hidroeléctrica en el continente) tiene la capacidad física y volumétrica para satisfacer íntegramente la demanda de los bloques protegidos.

Para verificarlo con total rigor, se confronta la **Demanda Protegida Total** contra la **Oferta Hidroeléctrica Disponible**, tanto en condiciones hidrológicas medias como durante el periodo de estiaje más crítico registrado en el Ecuador (fuentes: estadísticas oficiales CENACE y balances anuales ARCONEL):

```
+-------------------------------------------------------------------------------------------------------+
|                       BALANCE ENERGÉTICO ANUAL Y MENSUAL DE LA DEMANDA PROTEGIDA                      |
+---------------------------------------------+----------------------------+----------------------------+
| CONCEPTO / SECTOR                           | VOLUMEN ANUAL ESTIMADO     | PROMEDIO MENSUAL           |
+---------------------------------------------+----------------------------+----------------------------+
| 1. Clientes Residenciales (~5.4 millones)   |                            |                            |
|    - Consumo medio bloque subsistencia      | ~111 kWh/mes por abonado   | -                          |
|    - Demanda Residencial Protegida          | **7,200 GWh/año**          | **600 GWh/mes**            |
| 2. Soberanía Alimentaria (~120.000 locales) |                            |                            |
|    - Tiendas y micromercados (500 kWh)      | ~550 GWh/año               | ~46 GWh/mes                |
|    - Panaderías y obradores (800 kWh)       | ~314 GWh/año               | ~26 GWh/mes                |
|    - Demanda Alimentaria Protegida          | **864 GWh/año**            | **72 GWh/mes**             |
+---------------------------------------------+----------------------------+----------------------------+
| **DEMANDA PROTEGIDA TOTAL (A)**             | **8,064 GWh/año**          | **672 GWh/mes**            |
+---------------------------------------------+----------------------------+----------------------------+
| **OFERTA HIDROELÉCTRICA NACIONAL (B):**                                                               |
| • Año Hidrológico Normal (promedio histórico) | **22,000 a 25,500 GWh/año**| **~1,900 a 2,100 GWh/mes** |
|   - Cobertura de la Demanda Protegida       | **273% a 316%**            | **SOBRA > 1,200 GWh/mes**  |
| • Año de Sequía Severa / Estiaje Crítico    | **16,000 a 17,500 GWh/año**| **~1,350 a 1,450 GWh/mes** |
| • **Peor Mes de Estiaje Histórico** (Nov/Dic) | -                          | **1,150 a 1,300 GWh/mes**  |
|   - Cobertura en el peor mes de crisis      | -                          | **171% a 193%**            |
+---------------------------------------------+----------------------------+----------------------------+
| **MARGEN EXCEDENTE EN EL PEOR MES (B - A)** | -                          | **+478 a +628 GWh/mes**    |
+---------------------------------------------+----------------------------+----------------------------+
```

- **Conclusión Contundente: ¡SÍ ALCANZA Y CON AMPLIA HOLGURA!**
  1. Incluso en el mes más seco de la peor sequía de la historia del país (cuando el complejo Paute-Mazar y Coca Codo operan en niveles mínimos y la generación hidroeléctrica desciende a 1,150 GWh/mes), **la generación hidroeléctrica base supera en más del 70% los 672 GWh/mes necesarios para abastecer a todos los hogares y panaderías del Ecuador**.
  2. **¿Por qué ocurren los apagones entonces?**
     El déficit eléctrico no se produce por falta de energía para las casas y panaderías populares. El déficit se genera porque la **Demanda Total del País** (que incluye industrias pesadas, grandes centros comerciales, minería, bombeo petrolero, alumbrado y consumos residenciales altos) oscila entre **2,500 y 2,750 GWh/mes**.
  3. Al faltar 1,200 a 1,400 GWh/mes para abastecer el consumo no protegido, el país se ve obligado a encender termoeléctricas caras a diésel e importar desde Colombia.
  4. Al consagrar en la ley que la energía barata va **primero y de forma exclusiva** a hogares (hasta 250/320 kWh) y comida (hasta 500/800 kWh), **la canasta básica queda 100% blindada con hidroelectricidad limpia**. El costo del parque térmico de emergencia y las importaciones se traslada con estricta justicia a los sectores comerciales e industriales de alto consumo, incentivándolos de forma inmediata a autogenerar con energía solar en sus techos.

---

### 4. TARIFAS A COSTO REAL PARA EL RESTO DE SECTORES Y EXCEDENTES

#### 4.1. Estructura de Tarifa a Costo Real Pleno ($T_{\text{real}}$)

Para todos los consumidores no amparados por los bloques preferentes (comercio de media y gran escala, industrias, bancos, telecomunicaciones, minería, sector público, grandes consumidores) y para los consumos residenciales y alimentarios en la porción que exceda los 250 kWh (o 320 kWh bioclimático) y 500/800 kWh respectivamente, se aplicará la **Tarifa a Costo Real Pleno ($T_{\text{real}}$)**:

$$T_{\text{real}} = C_{\text{gen,real}} + C_{\text{trans}} + C_{\text{dist}} + C_{\text{com}} + C_{\text{pérdidas}} + C_{\text{SAPG}}$$

Donde:
- $C_{\text{gen,real}}$: Costo medio ponderado real o costo marginal de generación eficiente del sistema, sin subsidio estatal de combustibles ni subvenciones al capital.
- $C_{\text{trans}}$: Peaje de transmisión del Sistema Nacional de Transmisión (SNT), auditado por ARCONEL.
- $C_{\text{dist}}$: Valor agregado de distribución (VAD) eficiente según nivel de tensión.
- $C_{\text{com}}$: Costo de medición, lectura, facturación y recaudación.
- $C_{\text{pérdidas}}$: Reconocimiento exclusivo de pérdidas técnicas eficientes (máximo 8-9%, castigando la ineficiencia empresarial).
- $C_{\text{SAPG}}$: Servicio de Alumbrado Público General proporcional.

**Resultado Económico:** Se eliminan las transferencias ciegas del Estado que antes subvencionaban a empresas altamente rentables o a viviendas de alto consumo, liberando cientos de millones de dólares anuales en el Presupuesto General del Estado y recapitalizando el flujo de caja del sector eléctrico.

#### 4.2. El Piso Tarifario Mínimo Legal: Blindaje Financiero de las Empresas Distribuidoras

- **Riesgo Financiero Identificado:**
  Si la tarifa preferente se calculara exclusivamente deduciendo el costo marginal o nivelado de la hidroelectricidad amortizada (1.5 a 3.0 ¢USD/kWh) más peajes de transmisión y distribución eficiente, la tarifa resultante en baja tensión podría situarse matemáticamente en torno a los 7.0 – 8.0 ¢USD/kWh.
  Si bien esto parecería atractivo para el consumidor, una caída por debajo de las tarifas reguladas actuales (que promedian ~9.2 ¢USD/kWh residencial) provocaría un **descalce financiero y desfinanciamiento inmediato de las 20 empresas distribuidoras del país** (CNEL EP, EEQ, Centrosur, etc.), imposibilitando el pago de nóminas operativas, mantenimiento de cuadrillas, reposición de transformadores y luminarias.

- **Fórmula con Piso Tarifario Legal:**
  La ley establece con claridad meridiana que la tarifa preferente final ($T_{\text{preferente}}$) tendrá como **límite inferior irreductible** el pliego tarifario regulado actual a la fecha de promulgación:

  $$T_{\text{preferente}} = \max\left(T_{\text{actual, regulada}}, \; C_{\text{gen,barato}} + C_{\text{trans}} + C_{\text{dist}} + C_{\text{com}} + C_{\text{SAPG}}\right)$$

- **Beneficio Sistémico:**
  1. **Para la ciudadanía:** Las familias y panaderías mantienen su tarifa base habitual sin aumentos en condiciones hidrológicas ordinarias.
  2. **Para las distribuidoras:** Se preserva el 100% de su flujo de caja y recaudación histórica, garantizando su solvencia.
  3. **En sequías:** Si el costo de abastecimiento sube por sustitución térmica, la tarifa se ajusta temporalmente con el Factor de Contingencia Climática ($FCC$) hasta pagar el déficit.
  4. **En abundancia hídrica:** Al cobrarse costo real a la industria y grandes consumidores, los excedentes recaudados fluyen directamente a nutrir el Fondo Especial de Reinversión y Resiliencia Eléctrica (FERRE).

---

### 5. PARIDAD DE RED Y DETONANTE DE LA ENERGÍA SOLAR DISTRIBUIDA

Uno de los efectos económicos y transformadores más potentes de esta reforma es el alcance inmediato de la **Paridad de Red (Grid Parity)** para la autogeneración solar fotovoltaica en empresas y hogares de alto consumo.

#### 5.1. Comparativa del Retorno de Inversión (ROI) Solar: Con Subsidio vs. Tarifa Real Plena

```
+-----------------------------------------------------------------------------------------------------+
|                              MODELO ECONÓMICO DE PANELES SOLARES EN TECHO                           |
+-----------------------------------------+----------------------------+------------------------------+
| PARÁMETRO / INDICADOR                   | CON ESQUEMA SUBSIDIADO     | CON TARIFA A COSTO REAL      |
|                                         | (ANTERIOR)                 | (NUEVA LEY)                  |
+-----------------------------------------+----------------------------+------------------------------+
| Tarifa eléctrica de red pagada          | 8.5 a 10.0 ¢USD/kWh        | 16.0 a 22.0 ¢USD/kWh         |
| Costo nivelado solar (LCOE en cubierta) | 6.0 a 7.5 ¢USD/kWh         | 6.0 a 7.5 ¢USD/kWh           |
| Ahorro neto por kWh autogenerado        | 1.5 a 2.5 ¢USD/kWh         | 10.0 a 14.5 ¢USD/kWh         |
| Periodo de Recuperación (Payback)       | **9.5 a 12.0 años**        | **3.2 a 4.5 años**           |
| Tasa Interna de Retorno (TIR)           | 7.5% - 9.0%                | **24.0% - 31.5%**            |
| Viabilidad financiera para empresas     | Marginal / Desincentivada  | **Altamente Rentable**       |
+-----------------------------------------+----------------------------+------------------------------+
```

- **Por qué no despegaba la energía solar:** Cuando el Estado subsidiaba artificialmente la electricidad industrial y comercial a 9 ¢USD/kWh, un empresario que evaluaba invertir \$50.000 en paneles solares obtenía un retorno a más de 10 años, prefiriendo mantener el suministro convencional.
- **El detonante de la paridad:** Al eliminarse el subsidio y pagar la tarifa a costo real pleno (18 ¢USD/kWh en promedio), el ahorro mensual se cuadruplica. La inversión solar se amortiza en menos de 4 años, generando 20 años adicionales de electricidad prácticamente gratuita para la empresa.
- **Incentivo para el Consumidor Residencial de Alto Consumo:** Un hogar de clase media-alta que consume 600 kWh/mes pagará los primeros 250 kWh con la tarifa barata preferencial y los 350 kWh restantes a costo real pleno (~18 ¢USD/kWh). Esto incentiva inmediatamente la instalación de un microkit solar de 1.5 a 2.5 kWp (4 a 6 paneles), borrando el exceso y reduciendo la factura al mínimo.

#### 5.2. Régimen Fast-Track y Medición Neta 1:1
Para que la paridad de red se materialice en megavatios instalados, la ley derriba las barreras burocráticas históricas de las empresas distribuidoras:
1. **Silencio Administrativo Positivo en 15 días:** Evita que las distribuidoras retengan arbitrariamente los permisos de conexión.
2. **Net Metering 1 a 1:** Cada kWh solar inyectado a la red al mediodía se descuenta íntegramente de un kWh consumido de la red en la noche.

---

### 6. MITIGACIÓN DEL IMPACTO INFLACIONARIO Y TRANSICIÓN PRODUCTIVA

#### 6.1. Diagnóstico del Riesgo Inflacionario de Segunda Ronda
Si bien la ley blinda a las familias (hasta 250 kWh/mes) y a los comercios de alimentos básicos (hasta 500 kWh/mes), un encarecimiento intempestivo de la electricidad industrial podría trasladarse a los precios de bienes intermedios (envases, harinas procesadas, cadenas de frío logísticas).

#### 6.2. Estrategia Escalonada en 3 Trimestres (Curva de Adaptación)
Para evitar un shock inflacionario, el retiro del subsidio a industrias se dosifica en un año:
- **Trimestre 1:** Absorción de solo el 33% del diferencial real.
- **Trimestre 2:** Absorción del 66% del diferencial.
- **Trimestre 3:** 100% Costo Real Pleno.

**Ventana de Inversión:** Este plazo de 9 a 12 meses coincide exactamente con el tiempo necesario para que las empresas contraten e instalen plantas solares en techo o firmen contratos bilaterales PPA con autogeneradores limpios, neutralizando el impacto del costo antes de que llegue al 100%.

#### 6.3. Financiamiento Verde "Techo Solar Productivo"
El Banco Central del Ecuador, la CFN y BanEcuador dispondrán de líneas de crédito blando al 5% anual a 7 años plazo. Dado que la cuota mensual del crédito solar es inferior al ahorro generado en la factura eléctrica, la inversión genera flujo de caja positivo inmediato para la empresa desde el primer mes.

---

### 7. MODELADO BIOCLIMÁTICO: JUSTICIA TERRITORIAL ENTRE COSTA Y SIERRA

- En la región interandina (Quito, Cuenca, Riobamba, Loja), la temperatura media oscila entre 12°C y 18°C, sin necesidad de climatización mecánica en los hogares. El límite de **250 kWh/mes** cubre holgadamente al 82% de las familias serranas.
- En la región litoral (Guayaquil, Manta, Machala, Esmeraldas) y Amazonía, durante los meses de alta temperatura y humedad (diciembre a mayo), la temperatura ambiental supera con frecuencia los 32°C a 35°C con sensación térmica superior a 40°C.
- En estas condiciones, un hogar de ingresos medios o bajos requiere un equipo de aire acondicionado básico o ventiladores continuos durante las horas de descanso nocturno, elevando el consumo biológico indispensable a un rango de **270 a 310 kWh/mes**.
- **Solución Bioclimática:** La ley eleva de oficio el umbral preferente en Costa y Amazonía a **320 kWh/mes entre diciembre y mayo**, evitando un castigo económico injusto por razones climáticas y garantizando equidad regional.

---

### 8. COMPLEMENTARIEDAD HIDRO-SOLAR EN TEMPORADAS DE ESTIAJE

Existe una sinergia meteorológica crucial en el Ecuador:
- Durante la temporada seca o de estiaje en los Andes orientales (que alimenta a las cuencas de Paute, Mazar y Coca Codo), la nubosidad disminuye drásticamente, registrándose los niveles más altos del año de irradiancia solar global horizontal (GHI) en la Sierra y Costa ecuatoriana (5.2 a 6.0 kWh/m²/día).
- Al masificarse la autogeneración solar en empresas y techos residenciales:
  1. Durante las horas diurnas (08:00 a 16:30), la red se alimenta de energía solar descentralizada;
  2. Las compuertas de los embalses hidroeléctricos pueden cerrarse durante el día, **ahorrando agua para turbinarla en las horas de máxima demanda nocturna (18:00 a 22:00)**;
  3. Se minimiza el encendido de plantas térmicas a diésel y la importación de energía cara desde Colombia, reduciendo el monto del Factor de Contingencia Climática ($FCC$) que paga la sociedad.

---

### 9. RÉGIMEN DE ESTIAJE, SEQUÍAS Y CONTINGENCIA HIDROLÓGICA

#### 9.1. Mecánica del Despacho en Cascada ante Sequía
Cuando la cota de los embalses hidroeléctricos desciende por debajo de los niveles de seguridad operativa (Mazar a menos de 2.115 msnm, Paute a menos de 1.975 msnm):
1. La disponibilidad de energía hidroeléctrica barata disminuye.
2. El sistema despacha obligatoriamente la siguiente energía más económica disponible:
   - Solar fotovoltaica y eólica diurna;
   - Generación a biomasa de ingenios azucareros;
   - Centrales térmicas a gas natural local (Termogas Machala);
   - Centrales a búnker y fuel oil;
   - Como último recurso: turbinas térmicas a diésel e importaciones internacionales.
3. Para los bloques preferentes (250 kWh residencial y 500/800 kWh alimentario), se asigna contablemente la energía más barata que quede en el despacho en ese momento. Al agotarse la hidroelectricidad, la tarifa de dichos bloques absorberá únicamente el incremento real de la fuente sustituta más económica disponible.

#### 9.2. El Factor de Contingencia Climática por Estiaje ($FCC$)
El incremento del costo de despacho se refleja en un rubro temporal denominado **Factor de Contingencia Climática ($FCC$)**:

$$FCC_m = \frac{\sum_{i} (C_{\text{fuente }, i} - C_{\text{base}}) \times E_i + C_{\text{importaciones}}}{E_{\text{total facturada}}}$$

#### 9.3. Publicidad Previa Obligatoria y Transparencia
- El Ministerio de Energía y la ARCONEL tienen la obligación legal de anunciar el inicio de la temporada de ajuste con al menos **15 días de anticipación**.
- Se prohíben aumentos retroactivos o sorpresivos.
- En la planilla mensual del usuario se imprime un gráfico didáctico y el valor exacto del $FCC$, detallando cuántos centavos por kWh corresponden al estiaje y la fecha proyectada de cese.

#### 9.4. Regla de Mantenimiento Temporal y Cero Déficit
- La tarifa ajustada con el $FCC$ se mantendrá en vigencia **de manera continua hasta que se liquide y cancele el 100% de los pasivos generados durante la sequía** (pagos pendientes de combustibles a Petroecuador, liquidaciones comerciales con Colombia y Perú, contratos de generación de emergencia).
- Una vez que los embalses recuperen sus niveles normales y la cuenta de costos de contingencia llegue a saldo cero, el $FCC$ se desactiva de forma automática por resolución de ARCONEL, retornando las tarifas a sus valores base.

---

### 10. FONDO ESPECIAL DE REINVERSIÓN Y RESILIENCIA ELÉCTRICA (FERRE)

Uno de los aportes cardinales del proyecto es la gestión del excedente económico ("si sobra algo").

```
                                  FLUJO DE RECURSOS DEL SISTEMA
                                 ┌──────────────────────────────┐
                                 │ Recaudación Total Tarifaria  │
                                 └──────────────┬───────────────┘
                                                │
                                                ▼
                                 ┌──────────────────────────────┐
                                 │  Costos Operativos Reales,   │
                                 │  Combustibles e Importación  │
                                 └──────────────┬───────────────┘
                                                │
                                      ¿Existe Remanente?
                                                │
                                ┌───────────────┴───────────────┐
                                │                               │
                                ▼                               ▼
                         [SÍ: Superávit]                  [NO: Equilibrio]
                                │                               │
                                ▼                               ▼
               ┌──────────────────────────────────┐      [Cero Déficit]
               │ Fondo de Reinversión (FERRE)     │
               │ (Fideicomiso Intangible)         │
               └────────────────┬─────────────────┘
                                │
       ┌────────────────────────┼────────────────────────┬──────────────────────┐
       ▼                        ▼                        ▼                      ▼
 [Mantenimiento           [Baterías BESS           [Transmisión y         [Transición y
 Mayor de Centrales]      y Renovables]            Subestaciones SNT]     Resiliencia Galápagos]
```

#### 10.1. Blindaje Jurídico contra la Discrecionalidad Fiscal
- En el pasado, los excedentes de las empresas públicas del sector energético eran absorbidos por el Ministerio de Finanzas para financiar gasto corriente, salarios de la burocracia o subsidios políticos.
- La ley declara a los excedentes del sector eléctrico como **patrimonio autónomo, intangible e intransferible**.
- Queda prohibida su reversión a la Cuenta Única del Tesoro Nacional.

#### 10.2. Asignación Estratégica del FERRE:
1. **Mantenimiento Preventivo y Mayor:** Garantizar que turbinas, rodetes, transformadores y generadores térmicos tengan repuestos y mantenimiento a tiempo, evitando que salgan de servicio durante los estiajes.
2. **Almacenamiento Energético (BESS):** Financiar la instalación de bancos de baterías de ion-litio a gran escala que acumulen los excedentes de energía solar diurna e hidroeléctrica nocturna para inyectarla en horas pico (18:00 a 22:00).
3. **Reforzamiento del Sistema Nacional de Transmisión (SNT):** Eliminar cuellos de botella en líneas de 230 kV y 500 kV para evacuar energía renovable desde las zonas de generación hacia los grandes centros de consumo.
4. **Resiliencia en Galápagos:** Incrementar la penetración eólica y solar en el archipiélago para reducir al mínimo el consumo de combustibles fósiles.

---

### 11. CONCLUSIONES TÉCNICAS Y BENEFICIOS PARA EL ECUADOR

1. **Equidad Social Genuina:** Se garantiza a las familias ecuatorianas la energía más barata del país hasta 250 kWh/mes (320 kWh en Costa/Amazonía cálida), y se preserva el precio de los alimentos populares hasta 500 kWh/mes en tiendas y 800 kWh/mes en panaderías artesanales, con un piso tarifario legal que protege las finanzas de las distribuidoras.
2. **Responsabilidad Fiscal y Finanzas Sanas:** Al cobrar tarifa a costo real pleno al resto de actividades económicas y a los consumos excesivos, el Estado erradica el déficit tarifario crónico sin necesidad de endeudamiento público ni apagones programados.
3. **Resiliencia Adaptativa ante el Clima:** El sistema adquiere una regla matemática transparente para navegar temporadas de sequía, publicitando con antelación las variaciones y manteniendo las tarifas ajustadas solo el tiempo estrictamente necesario para no generar pérdidas.
4. **Sostenibilidad y Modernización Continua:** Cualquier ganancia o remanente se convierte automáticamente en nuevas inversiones eléctricas a través del FERRE, asegurando que el Ecuador cuente con una matriz robusta, moderna y soberana.
