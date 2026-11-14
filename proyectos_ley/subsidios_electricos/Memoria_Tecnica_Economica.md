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

#### 2.3. Racionalización del Subsidio a la Tercera Edad (Adultos Mayores): Capping Vital de 50 kWh/mes y Blindaje Antifraude

- **Diagnóstico del Fraude Histórico y Fuga Fiscal:**
  La Ley Orgánica de las Personas Adultas Mayores (LOPAM), en su artículo 14, estableció históricamente una exoneración del 50% en las planillas de energía eléctrica para ciudadanos mayores de 65 años. Si bien la intención social original era proteger a los ancianos en condición de vulnerabilidad, la ausencia de un tope de consumo por kilovatio-hora convirtió este beneficio en una de las fuentes de distorsión y fraude más regresivas del sector eléctrico ecuatoriano:
  1. **Mansiones y Fincas a Nombre de Adultos Mayores:** Familias de altos ingresos en sectores residenciales exclusivos (Samborondón, Cumbayá, Puembo) registraban medidores de residencias de 800 a 2,500 kWh/mes (con 6 aires acondicionados splits, saunas y piscinas temperadas) a nombre de abuelos o familiares ancianos, obteniendo un subsidio del 50% financiado por el Estado sobre consumos desmedidos y suntuarios.
  2. **Medidores Múltiples y Fallecidos:** Se detectaron catastros con hasta 4 medidores registrados bajo una misma cédula de adulto mayor en diferentes cantones, así como suministros que mantuvieron activo el subsidio durante años tras el fallecimiento del titular por falta de cruce con el Registro Civil.
  3. **Costo de la Fuga:** Esta fuga fiscal y distorsión comercial drenaba entre **$45.00 y $65.00 millones de USD anuales** a las empresas distribuidoras.

- **Estructura Técnica y Socialmente Justa por Tramos:**
  La reforma introduce una fórmula en tres tramos que protege el consumo vital auténtico del adulto mayor y extingue el subsidio a la opulencia:

  ```
  +-------------------------------------------------------------------------------------------------------+
  |              ESTRUCTURA TARIFARIA RACIONALIZADA PARA ADULTOS MAYORES (3RA EDAD)                       |
  +--------------------------------+----------------------------+-----------------------------------------+
  | TRAMO DE CONSUMO MENSUAL       | TRATAMIENTO TARIFARIO      | VALOR ESTIMADO Y JUSTIFICACIÓN          |
  +--------------------------------+----------------------------+-----------------------------------------+
  | **Tramo 1: 0 a 50 kWh/mes**    | 50% de Descuento sobre     | **~$2.35 USD / mes**                    |
  | (Consumo Vital de Subsistencia)| Tarifa Base de Subsistencia| Cubre iluminación LED, radio/TV y       |
  |                                |                            | refrigerador pequeño eficiente.         |
  +--------------------------------+----------------------------+-----------------------------------------+
  | **Tramo 2: 51 a 250 kWh/mes**  | Tarifa Preferencial        | **~9.5 ¢USD / kWh**                     |
  | (Confort Familiar Ordinario)   | Residencial Ordinaria      | Tarifa familiar protegida sin descuento |
  |                                | (Piso Regulado)            | extra del 50%, sin costo real suntuario.|
  +--------------------------------+----------------------------+-----------------------------------------+
  | **Tramo 3: Más de 250 kWh/mes**| 100% Tarifa a Costo Real   | **18.0 a 22.0 ¢USD / kWh (+ FCC)**      |
  | (Consumo Suntuario / Exceso)   | Pleno del Servicio         | Se liquida a costo real pleno sin       |
  |                                |                            | ningún subsidio estatal.                |
  +--------------------------------+----------------------------+-----------------------------------------+
  ```

- **Mecánica Matemática de Liquidación:**
  Para un adulto mayor con un consumo real, la facturación mensual responde a:

  $$\text{Factura}_{\text{3ra Edad}} = (0.50 \times T_{\text{preferente}} \times \min(C, 50)) + (T_{\text{preferente}} \times \max(0, \min(C, 250) - 50)) + (T_{\text{real}} \times \max(0, C - 250))$$

- **Candados Antifraude Estrictos:**
  1. **Un solo medidor residencial por cédula:** El beneficio aplica de forma exclusiva al predio donde efectivamente resida el adulto mayor.
  2. **Interconexión en tiempo real con Registro Civil:** Depuración mensual automática del padrón para dar de baja de oficio el subsidio ante defunciones.
  3. **Ahorro Fiscal Neto:** Esta medida recupera aproximadamente **$45.00 millones de USD anuales**, preservando íntegra la protección al adulto mayor humilde.

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

#### 3.2. Régimen Especial de la Provincia de Galápagos: Constitucionalidad, Principio Contaminador-Pagador y Descarbonización por Fuerzas de Mercado

- **¿Es legal y constitucional cobrar la tarifa real en Galápagos? (Análisis Jurídico Forense):**
  Frente a la inquietud sobre si la figura legal es constitucionalmente válida en Galápagos, la auditoría jurídica concluye que **no solo es 100% legal y constitucional, sino que la práctica actual de subsidiar el diésel fósil en el archipiélago vulnera abiertamente la Constitución**:
  1. **Artículo 258 de la Constitución (CRE) — Régimen Especial de Galápagos:** Consagra que el desarrollo y planificación de la provincia de Galápagos se regirá de forma prioritaria por el principio de conservación estricta de sus ecosistemas frágiles y su patrimonio natural de la humanidad.
  2. **Artículos 395 y 396 de la CRE — Principio Contaminador-Pagador (*Polluter-Pays Principle*) y de Precaución:**
     - El Art. 396 CRE ordena taxativamente que: *"Cada uno de los actores de los procesos de producción, distribución, comercialización y uso de bienes o servicios asumirá la responsabilidad directa de prevenir cualquier impacto ambiental, de mitigar y reparar los daños que cause, y de mantener un sistema de control ambiental permanente"*.
     - Subsidiar con fondos públicos el diésel importado en barcazas de alto riesgo de naufragio o derrame en la Reserva Marina de Galápagos (como la catástrofe del petrolero *Jessica* en 2001) para que hoteles de lujo, cruceros internacionales y discotecas consuman energía barata artificialmente subvencionada constituye una aberración ecológica y una violación constitucional flagrante.
  3. **Ley Orgánica de Régimen Especial de Galápagos (LOREG):** Exige la transición acelerada hacia el objetivo de "Cero Combustibles Fósiles en Galápagos" y promueve la autosuficiencia energética con fuentes renovables locales.

- **La Realidad Económica y Termodinámica Insular:**
  Galápagos es un sistema aislado no interconectado al continente:
  - **Costo Real de la Generación Térmica a Diésel:** El costo nivelado de generar electricidad con diésel importado asciende a **35.0 a 42.0 centavos de dólar por kilovatio-hora ($0.35 a $0.42 USD/kWh)**. Este costo incluye: precio del combustible a paridad de importación internacional (marcador WTI), flete marítimo especializado en barcazas de doble casco desde Guayaquil, trasvase seguro en puerto, almacenamiento insular y mantenimiento electromecánico de grupos electrógenos.
  - **Costo de las Renovables Locales (Eólica y Solar + BESS):** Los parques eólicos de San Cristóbal y Baltra, junto con las centrales solares fotovoltaicas y sistemas de baterías BESS en Santa Cruz e Isabela, generan energía limpia a un costo de **8.0 a 14.0 ¢USD/kWh**.

- **Estructura Tarifaria Insular Sincera y Justa:**
  1. **Bloque Residencial Insular de Subsistencia (hasta 250 kWh/mes):** Se asigna contable y prioritariamente la energía renovable local más barata (solar y eólica), facturándose a la tarifa base insular eficiente (~12.0 a 14.0 ¢USD/kWh). Esto protege íntegramente a las familias residentes permanentes de Galápagos.
  2. **Consumo Excedente (>250 kWh/mes) y Sector Turístico Comercial:** Hoteles de lujo, cruceros, ecolodges, restaurantes turísticos y centros de buceo pagarán el **100% de la tarifa a costo real insular pleno (35.0 a 42.0 ¢USD/kWh)**.

- **La Revolución de la Paridad de Red: Descarbonización Privada en Menos de 2 Años:**
  El cobro a costo real genera un efecto económico extraordinario:
  ```
  +-------------------------------------------------------------------------------------------------------+
  |              PARIDAD DE RED SOLAR + BESS EN GALÁPAGOS: SECTOR HOTELERO Y TURÍSTICO                    |
  +---------------------------------------+-----------------------------+---------------------------------+
  | INDICADOR / PARÁMETRO                 | CON DIÉSEL SUBSIDIADO (HOY) | CON TARIFA REAL INSULAR (LEY)   |
  +---------------------------------------+-----------------------------+---------------------------------+
  | Tarifa de Red Pagada por Hoteles      | 10.5 a 12.0 ¢USD / kWh      | **35.0 a 42.0 ¢USD / kWh**      |
  | Costo Nivelado Solar + BESS en Sitio  | 11.0 a 13.5 ¢USD / kWh      | 11.0 a 13.5 ¢USD / kWh          |
  | Ahorro Neto por kWh Autogenerado      | (-1.5) a +0.5 ¢USD / kWh    | **+24.0 a +28.5 ¢USD / kWh**    |
  | Periodo de Recuperación (Payback)     | **> 12 años (Inviable)**    | **1.8 a 2.3 años (Ultra-rápido)**|
  | Transición Ecológica Financiada Por   | Subsidio Estatal Deficitario| **100% Inversión Privada**      |
  +---------------------------------------+-----------------------------+---------------------------------+
  ```
  Al sincerar la tarifa a 38 ¢USD/kWh, un hotel de 30 habitaciones en Santa Cruz amortiza sus paneles solares y baterías BESS en **menos de dos años**. Los empresarios hoteleros se apresurarán a instalar cubiertas solares privadas para autoabastecerse, reduciendo la importación de diésel al archipiélago a mínimos históricos, **sin que el Estado ecuatoriano gaste un solo centavo de presupuesto público ni subsidios**.

#### 3.3. Balance Energético Nacional: ¿Alcanza la energía hidroeléctrica barata para hogares, comida, hospitales y escuelas públicas? ("¿Nos alcanza acaso la energía?")

Una interrogante técnica fundamental es si la matriz de generación de menor costo (principalmente hidroeléctrica en el continente) tiene la capacidad física y volumétrica para satisfacer íntegramente la demanda de los bloques protegidos: hogares, cadena popular de alimentos, hospitales de la Red Pública Integral de Salud (RPIS) y planteles educativos fiscales.

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
| 3. Red Pública Integral de Salud (RPIS)     |                            |                            |
|    - Hospitales de especialidades, generales|                            |                            |
|      y centros de salud 24h (~840 unidades) | **450 GWh/año**            | **37.5 GWh/mes**           |
| 4. Educación Pública Fiscal                 |                            |                            |
|    - Escuelas básicas, colegios fiscales y  |                            |                            |
|      Unidades del Milenio (~12,400 centros) | **240 GWh/año**            | **20.0 GWh/mes**           |
+---------------------------------------------+----------------------------+----------------------------+
| **DEMANDA PROTEGIDA TOTAL (A)**             | **8,754 GWh/año**          | **729.5 GWh/mes**          |
+---------------------------------------------+----------------------------+----------------------------+
| **OFERTA HIDROELÉCTRICA NACIONAL (B):**                                                               |
| • Año Hidrológico Normal (promedio histórico) | **22,000 a 25,500 GWh/año**| **~1,900 a 2,100 GWh/mes** |
|   - Cobertura de la Demanda Protegida       | **251% a 291%**            | **SOBRA > 1,170 GWh/mes**  |
| • Año de Sequía Severa / Estiaje Crítico    | **16,000 a 17,500 GWh/año**| **~1,350 a 1,450 GWh/mes** |
| • **Peor Mes de Estiaje Histórico** (Nov/Dic) | -                          | **1,150 a 1,300 GWh/mes**  |
|   - Cobertura en el peor mes de crisis      | -                          | **157.6% a 178.2%**        |
+---------------------------------------------+----------------------------+----------------------------+
| **MARGEN EXCEDENTE EN EL PEOR MES (B - A)** | -                          | **+420.5 a +570.5 GWh/mes**|
+---------------------------------------------+----------------------------+----------------------------+
```

- **Conclusión Contundente: ¡SÍ ALCANZA Y CON AMPLIA HOLGURA EN ENERGÍA!**
  1. Incluso en el mes más seco de la peor sequía registrada en el país (con Mazar en cota crítica y Coca Codo en estiaje amazónico con 1,150 GWh/mes), **la oferta hidroeléctrica base cubre al 157.6% toda la demanda protegida combinada de familias, panaderías, tiendas, hospitales y escuelas públicas**.
  2. Queda un excedente mensual mínimo de **+420.5 GWh/mes** de energía hidroeléctrica barata para inyectar al resto de la economía.

#### 3.4. La Distinción Física y Operativa Crucial: Energía (MWh Acumulados) vs. Potencia Pico (MW Instantáneos a las 19:00 horas)

Uno de los errores más comunes en la política energética ecuatoriana es confundir el volumen de agua/energía mensual con la potencia instantánea de la red:
* **El problema no es de Energía mensual:** Como demuestra la tabla anterior, el agua que entra a los embalses en el mes entero alcanza para generar 1,150 GWh, superando los 729.5 GWh requeridos por los sectores protegidos.
* **El problema real es de Potencia Pico (MW):** Entre las 18:00 y las 22:00 horas, la demanda nacional trepa a **4,800 - 5,000 MW**.
  - Durante el estiaje, al bajar la cota de agua, las hidroeléctricas no pueden operar todas sus turbinas al mismo tiempo sin vaciar el embalse en pocas horas. La potencia hidroeléctrica disponible en punta se reduce a **~2,200 MW**.
  - El sistema requiere **~2,700 MW de potencia térmica e importaciones** para no colapsar.
  - Si las plantas térmicas están averiadas por falta de mantenimiento histórico o si Colombia corta las exportaciones, el sistema sufre un **déficit de potencia instantánea**, obligando a desconectar circuitos (apagones).
* **Por qué las Escuelas y Colegios encajan a la perfección:**  
  La red escolar consume energía entre las 07:00 y 17:30 horas (horario diurno), cuando la irradiancia solar es máxima y la demanda nacional es moderada. A las 18:00 horas las escuelas apagan sus luces y computadoras, **demandando cero potencia en la hora pico nocturna**.
* **La Solución Estructural al Pico:** Para solucionar el cuello de botella de potencia sin subsidios, el proyecto introduce tres herramientas sinérgicas:
  1. Tarifas horarias dinámicas (TOU) que castigan el consumo prescindible de 18:00 a 22:00;
  2. Baterías BESS industriales cargadas con sol diurno; y,
  3. El Fondo FERRE financiado con tarifas a costo real y el rubro de resiliencia de hasta $0.01 USD/kWh para instalar baterías BESS a gran escala en subestaciones del Estado.

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

#### 4.3. Auditoría Forense del Subsidio Real Total: Combustibles de Petroecuador y Ahorro Fiscal Consolidado

Una auditoría macroeconómica rigurosa exige transparentar los subsidios indirectos que históricamente se han ocultado en los balances de EP Petroecuador y en el Presupuesto General del Estado (PGE).

```
+-------------------------------------------------------------------------------------------------------+
|                 AUDITORÍA FORENSE DEL SUBSIDIO REAL TOTAL DEL SECTOR ELÉCTRICO ECUATORIANO            |
+---------------------------------------------+-----------------------------+---------------------------+
| COMPONENTE DEL SUBSIDIO                     | CONDICIÓN HIDROLÓGICA NORMAL| CRISIS DE ESTIAJE SEVERO  |
+---------------------------------------------+-----------------------------+---------------------------+
| 1. Déficit Tarifario Directo Reconocido     | $550.00 M USD / año         | $700.00 M USD / año       |
|    (Brecha tarifa media 9.5¢ vs costo 14.5¢)|                             |                           |
| 2. Subsidio Oculto en Combustibles Térmicos | $450.00 M USD / año         | $1,150.00 M USD / año     |
|    (Absorbido en pérdidas de Petroecuador)  |                             |                           |
| 3. Subsidio en Importaciones de Emergencia  | $50.00 M USD / año          | $350.00 M USD / año       |
|    (Comprada a Colombia a 28¢, vendida a 9¢)|                             |                           |
| 4. Pérdidas No Técnicas (Hurto de Energía)  | $200.00 M USD / año         | $350.00 M USD / año       |
|    (Energía inyectada no facturada en CNEL) |                             |                           |
+---------------------------------------------+-----------------------------+---------------------------+
| **GRAN TOTAL SUBSIDIO REAL INTEGRAL**       | **$1,250.00 M USD / año**   | **$2,550.00 M USD / año** |
+---------------------------------------------+-----------------------------+---------------------------+
```

##### A. Subsidio en Combustibles Térmicos a Precios Internacionales (WTI Base)
Las generadoras térmicas han operado con precios artificialmente deprimidos fijados por decretos ejecutivos:
1. **Diésel Eléctrico No. 2:** Transferido a CELEC a 0.92 - 1.10 USD/galón, cuando el precio de paridad de importación internacional (marcador WTI + flete CIF) es de **2.90 a 3.20 USD/galón**. En estiaje severo (quema de 180 a 250 millones de galones), Petroecuador pierde entre **$360 y $525 millones de USD anuales** solo en este rubro.
2. **Fuel Oil No. 4 y No. 6 (Búnker):** Transferido a 0.45 - 0.60 USD/galón (19 a 25 USD/barril), frente a una paridad internacional WTI de **1.35 a 1.55 USD/galón** (57 a 65 USD/barril). En 150 a 190 millones de galones quemados, el subsidio absorbido es de **$135 a $180 millones de USD anuales**.
3. **Gas Natural Local (Campo Amistad):** Transferido a 1.50 - 2.00 USD/MMBTU frente a un costo de oportunidad de **8.00 a 11.00 USD/MMBTU**, representando un subsidio implícito de **$80 a $120 millones de USD anuales**.

##### B. Ahorro Fiscal y Liberación de Recursos al Eliminar el 100% de Subsidios Directos e Indirectos
Al obligar a que las generadoras térmicas paguen el 100% del combustible a precio real de mercado y facturar a costo real los 19,246 GWh/año de demanda no protegida:

```
+-------------------------------------------------------------------------------------------------------+
|                    BALANCE FISCAL Y FINANCIERO CON ELIMINACIÓN TOTAL DE SUBSIDIOS                     |
+-----------------------------------------------------------------------+-------------------------------+
| CONCEPTO / FLUJO FINANCIERO                                           | IMPACTO FISCAL ANUAL (USD)    |
+-----------------------------------------------------------------------+-------------------------------+
| Ahorro por venta de combustibles a precio real (Petroecuador)         | +$700.00 a +$1,150.00 M USD   |
| Ahorro por traslado de importaciones internacionales al FCC           | +$150.00 a +$350.00 M USD     |
| Recaudación adicional neta por tarifa a costo real pleno              | +$1,500.00 a +$1,750.00 M USD |
| Erradicación del déficit tarifario histórico en CELEC y Distribuidoras| Liquidez operativa positiva   |
+-----------------------------------------------------------------------+-------------------------------+
| **LIBERACIÓN TOTAL DE RECURSOS PARA EL ESTADO (AHORRO + RECAUDACIÓN)**| **+$2,350.00 a +$3,250.00 M** |
+-----------------------------------------------------------------------+-------------------------------+
```

El Estado ecuatoriano se ahorra y recupera anualmente entre **$2,350 y $3,250 millones de USD**, equivalentes al 2.5% - 3.2% del Producto Interno Bruto (PIB), saneando de forma estructural el déficit fiscal de la República sin endeudamiento.

#### 4.4. Erradicación de Subsidios Cruzados Intersectoriales y Regulación por Costo de Servicio (Cost-of-Service)

- **La Distorsión Histórica de los Subsidios Cruzados:**
  En la regulación eléctrica tradicional, se recurrió a la práctica distorsiva de cargar sobrecostos a las industrias y comercios formales para financiar tarifas residenciales artificialmente bajas o compensar la incapacidad de las distribuidoras (particularmente CNEL EP) para cobrar y reducir sus pérdidas no técnicas (robo de energía de hasta 26%).
  Esta arquitectura viciada generaba tres efectos letales:
  1. **Pérdida de Competitividad Industrial:** Los costos de producción de las empresas nacionales se encarecían artificialmente frente a competidores de Colombia, Perú o Chile, destruyendo empleo industrial formal.
  2. **Opacidad Contable y Cero Incentivo de Eficiencia:** Al licuar las pérdidas comerciales dentro de tarifas cruzadas, las distribuidoras no tenían presión gerencial para erradicar las conexiones clandestinas.
  3. **Incapacidad de Sinceramiento:** Resultaba imposible saber con exactitud matemática cuánto costaba servir a cada clase de usuario.

- **La Separación Estricta Basada en Costo de Servicio (*Cost-of-Service Regulation*):**
  La ley consagra la prohibición absoluta de subsidios cruzados intersectoriales. Cada categoría tarifaria se liquida estrictamente con base en los costos eficientes requeridos para su abastecimiento:
  - **Industria y Alta Tensión:** Pagan costos de generación real eficiente, peaje de transmisión troncal y una fracción mínima de distribución (ya que no utilizan la red de baja tensión de los barrios residenciales). No pagan ni un solo centavo de sobretasa para cubrir a los hogares ni a los comercios.
  - **Comercio y Media Tensión:** Pagan sus costos nivelados auditados correspondientes.
  - **Bloque Residencial y Alimentario Protegido:** Se abastecen de la hidroelectricidad amortizada más barata del Estado (LCOE de 1.5 a 3.5 ¢USD/kWh).

- **Demostración Matemática: ¿Por qué la Tarifa Protegida NO es un Subsidio Cruzado de la Industria?**
  A menudo se confunde una tarifa preferente con un subsidio cruzado financiado por las empresas. La realidad física y contable desmiente esta falacia:
  1. El costo marginal de generación hidroeléctrica amortizada (Paute, Mazar, Coca Codo) es de **$0.025 USD/kWh** en promedio.
  2. El peaje de transmisión eficiente del SNT es de **$0.008 USD/kWh**.
  3. El Valor Agregado de Distribución (VAD) eficiente en baja tensión residencial es de **$0.045 USD/kWh**.
  4. Costos de comercialización y alumbrado: **$0.010 USD/kWh**.
  - **Costo Integral de Servir al Hogar Protegido:** **$0.088 USD/kWh**.
  - Al fijarse un **Piso Tarifario Regulado de ~0.095 USD/kWh**, el usuario residencial protegido paga **$0.007 USD/kWh por encima de su costo integral de abastecimiento**.
  - **Conclusión:** El Bloque Residencial Protegido es **100% autosuficiente y genera un margen operativo positivo de 8% a 10%** para la empresa distribuidora sin necesidad de subsidios estatales ni de recargos sobre la industria. La eliminación de los subsidios cruzados transparenta los costos y permite una reducción técnica de sobrecostos a la industria formal.

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

#### 5.3. Baterías de Almacenamiento (BESS) y Arbitraje Tarifario (Peak Shaving)

El sinceramiento tarifario y la variabilidad en estiaje detonan la rentabilidad no solo de los paneles solares, sino de la combinación **Solar + Sistemas de Almacenamiento con Baterías (BESS)** para empresas y comercios:
1. **La Problemática Tradicional:** La energía solar fotovoltaica genera exclusivamente durante el día (08:00 a 16:30). Sin embargo, el pico de máxima demanda y mayor estrés del sistema eléctrico ecuatoriano ocurre entre las 18:00 y las 22:00.
2. **El Arbitraje Tarifario (Time of Use):** Al cobrarse tarifa a costo real pleno (o tarifas horarias donde la energía en hora punta es sustancialmente más cara), una empresa industrial o comercial puede cargar sus baterías con excedentes solares al mediodía (costo marginal ~6.5 ¢/kWh) y descargar la energía almacenada durante el horario nocturno pico de 18:00 a 22:00 (evitando pagar de 20 a 25 ¢/kWh de la red).
3. **Respaldo Limpio vs. Generador a Diésel:** Sustituye a los generadores térmicos a diésel (que cuestan >30 ¢USD/kWh entre combustible y mantenimiento), garantizando continuidad operativa con cero emisiones y cero ruido.
4. **Viabilidad Financiera:** Con la superdeducción del 100% de Impuesto a la Renta y arancel 0%, el retorno de inversión del combo **Solar + BESS industrial** se reduce a **4.0 a 5.2 años**, transformando a las empresas en agentes de estabilidad para la red pública.

---

### 6. MITIGACIÓN DEL IMPACTO INFLACIONARIO Y TRANSICIÓN PRODUCTIVA

#### 6.1. Diagnóstico del Riesgo Inflacionario de Segunda Ronda
Si bien la ley blinda a las familias (hasta 250/300 kWh/mes) y a los comercios de alimentos básicos (hasta 500 kWh en tiendas y 800 kWh en panaderías), un encarecimiento intempestivo de la electricidad industrial podría trasladarse a los precios de bienes intermedios (envases, harinas procesadas, cadenas de frío logísticas).

#### 6.2. Estrategia Escalonada en 3 Trimestres (Curva de Adaptación)
Para evitar un shock inflacionario, el retiro del subsidio a industrias se dosifica en un año:
- **Trimestre 1:** Absorción de solo el 33% del diferencial real.
- **Trimestre 2:** Absorción del 66% del diferencial.
- **Trimestre 3:** 100% Costo Real Pleno.

**Ventana de Inversión:** Este plazo de 9 a 12 meses coincide exactamente con el tiempo necesario para que las empresas contraten e instalen plantas solares en techo y baterías BESS o firmen contratos bilaterales PPA con autogeneradores limpios, neutralizando el impacto del costo antes de que llegue al 100%.

#### 6.3. Financiamiento Verde "Techo Solar y Baterías Productivas"
El Banco Central del Ecuador, la CFN y BanEcuador dispondrán de líneas de crédito blando al 5% anual a 7 años plazo. Dado que la cuota mensual del crédito solar/BESS es inferior al ahorro generado en la factura eléctrica, la inversión genera flujo de caja positivo inmediato para la empresa desde el primer mes.

---

### 7. MODELADO BIOCLIMÁTICO, ELASTICIDAD PRECIO Y EFECTO SUSTITUCIÓN (VENTILADOR vs. AIRE ACONDICIONADO)

#### 7.1. Elasticidad Precio de la Demanda Residencial por Estratos de Ingreso
La respuesta del consumo residencial ante un sinceramiento tarifario o ante el incremento por estiaje ($FCC$) no es homogénea, sino que se comporta de forma **parcialmente elástica según el nivel de ingresos**:

```
+-------------------------------------------------------------------------------------------------------+
|                    COMPORTAMIENTO DE ELASTICIDAD Y EFECTO SUSTITUCIÓN EN LA COSTA                     |
+------------------------+-------------------+----------------------------+-----------------------------+
| ESTRATO SOCIOECONÓMICO | ELASTICIDAD PRECIO| REACCIÓN ANTE TARIFA CARA  | IMPACTO EN EL SISTEMA       |
|                        | DE LA DEMANDA     | (SEÑAL DE PRECIO EN SEQUÍA)|                             |
+------------------------+-------------------+----------------------------+-----------------------------+
| **Quintiles 1, 2 y 3** | **Alta Elasticidad**| **Sustitución Inmediata:**  | **Descongestionamiento:**   |
| (Ingresos Bajos-Medios)| (ε_p ≈ -0.55)     | Apagan aire acondicionado; | Desploma la demanda pico de |
| ~75% de la población   | Sensibles a la    | Encienden ventilador de    | noche en 15% a 22%. Ahorro  |
|                        | planilla mensual  | pedestal/techo eficiente.  | de agua en embalses.        |
+------------------------+-------------------+----------------------------+-----------------------------+
| **Quintiles 4 y 5**    | **Inelástica**    | **Mantienen Confort:**     | **Aporte Financiero Pleno:**|
| (Altos Ingresos)       | (ε_p ≈ -0.12)     | No apagan aire ni splits;  | Pagan 100% costo real sin   |
| ~25% de la población   | Priorizan confort | pagan la tarifa real sobre | subsidio. Financian el parque|
|                        | sobre el costo    | los 400 a 1.200 kWh extras.| térmico de respaldo.        |
+------------------------+-------------------+----------------------------+-----------------------------+
```

#### 7.2. Comparativa Energética y Económica: Ventilador vs. Aire Acondicionado
El efecto de sustitución inducido por la tarifa real genera una reducción drástica del consumo eléctrico en los hogares de la Costa:

```
+-------------------------------------------------------------------------------------------------------+
|                 ANÁLISIS COMPARATIVO DE CONSUMO: AIRE ACONDICIONADO vs. VENTILADOR                    |
+------------------------------------+-----------------------------+------------------------------------+
| PARÁMETRO / INDICADOR              | AIRE ACONDICIONADO SPLIT    | VENTILADOR DE TECHO / PEDESTAL     |
|                                    | (12,000 BTU convencional)   | (Eficiencia energética motor DC)   |
+------------------------------------+-----------------------------+------------------------------------+
| Potencia eléctrica de operación    | **1,200 Watts (1.20 kW)**   | **60 Watts (0.06 kW)**             |
| Uso nocturno estimado (8 horas)    | 9.60 kWh / noche            | 0.48 kWh / noche                   |
| Consumo mensual acumulado          | **288 kWh / mes**           | **14.4 kWh / mes**                 |
| Costo mensual a Tarifa Real Plena  |                             |                                    |
| (estimada en 20 ¢USD/kWh)          | **$57.60 USD / mes**       | **$2.88 USD / mes**               |
| Costo dentro del Bloque Preferente |                             |                                    |
| (piso tarifario base ~9.5 ¢/kWh)   | N/A (Excede el umbral base) | **$1.37 USD / mes**               |
+------------------------------------+-----------------------------+------------------------------------+
| **AHORRO ENERGÉTICO Y MONETARIO**  | **Reducción del 95% en consumo y $54.72 USD de ahorro mensual**   |
+------------------------------------+------------------------------------------------------------------+
```

- **Por qué ayuda a mitigar la sequía:**
  Durante los meses críticos de estiaje, miles de familias en la Costa ecuatoriana, al enfrentarse al cobro real de los excedentes, prefieren encender el ventilador en lugar del aire acondicionado. Esto retira de la red aproximadamente **1.14 kW de potencia por cada hogar que modera su consumo**.
  Multiplicado por 400,000 familias en la cuenca del Guayas, Manabí, El Oro y Esmeraldas, esto representa un **alivio instantáneo de hasta 450 MW de potencia en el pico nocturno**, equivalente a apagar tres barcazas térmicas de generación diésel importada.

#### 7.3. Bonificación por Ahorro Voluntario en Estiaje
Para potenciar la elasticidad de la demanda de forma proactiva, la ley premia el ahorro:
- Los hogares y micronegocios que reduzcan su consumo mensual en al menos un **10%** respecto a su historial previo en época seca quedan **100% exonerados del Factor de Contingencia ($FCC$)**.
- La combinación de tarifa real para el exceso y bonificación por ahorro convierte al ciudadano en un agente activo de la seguridad energética del país.

---

### 8. COMPLEMENTARIEDAD HIDRO-SOLAR EN TEMPORADAS DE ESTIAJE

Existe una sinergia meteorológica crucial en el Ecuador:
- Durante la temporada seca o de estiaje en los Andes orientales (que alimenta a las cuencas de Paute, Mazar y Coca Codo), la nubosidad disminuye drásticamente, registrándose los niveles más altos del año de irradiancia solar global horizontal (GHI) en la Sierra y Costa ecuatoriana (5.2 a 6.0 kWh/m²/día).
- Al masificarse la autogeneración solar en empresas y techos residenciales:
  1. Durante las horas diurnas (08:00 a 16:30), la red se alimenta de energía solar descentralizada;
  2. Las compuertas de los embalses hidroeléctricos pueden cerrarse durante el día, **ahorrando agua para turbinarla en las horas de máxima demanda nocturna (18:00 a 22:00)**;
  3. Se minimiza el encendido de plantas térmicas a diésel y la importación de energía cara desde Colombia, reduciendo el monto del Factor de Contingencia Climática ($FCC$) que paga la sociedad.

---

### 9. TARIFAS HORARIAS DINÁMICAS (TIME-OF-USE), MEDICIÓN INTELIGENTE (AMI) Y RÉGIMEN DE GARANTÍA AUTOFINANCIADA (COSTO + 5%)

#### 9.1. La Curva de Carga Horaria y el Aplanamiento del Pico Nacional
La demanda eléctrica en el Ecuador experimenta tres fases horarias claramente diferenciadas durante el ciclo diario de 24 horas:
1. **Horas Valle y Supervalle (23:00 a 06:00 y horas de sol pico 10:00 a 14:00):** La demanda cae a mínimos de 1,700 a 2,000 MW. Sobra agua en las hidroeléctricas de pasada o radiación solar en los techos. El costo marginal es mínimo (~2.5 a 4.5 ¢USD/kWh).
2. **Horas Llanas (06:00 a 18:00 y 22:00 a 23:00):** Demanda moderada comercial e industrial continua (~2,200 a 2,400 MW).
3. **Horas Pico o de Máxima Demanda (18:00 a 22:00):** Coincide el retorno de las familias a los hogares con el comercio activo. La demanda trepa bruscamente hasta **4,800 a 5,000 MW**. Al no haber sol y descender los embalses, el sistema debe encender termoeléctricas caras a diésel e importar desde Colombia a costos de 25 a 35 ¢USD/kWh.

**Impacto del Esquema Horario (Time-of-Use - TOU):**
- Al declarar una tarifa diferenciada por horas, se genera un fuerte incentivo para el **desplazamiento de carga (Load Shifting)**:
  - Panaderías artesanales desplazan parte de su proceso de amasado hacia las horas valle de la madrugada (02:00 a 06:00) o de mediodía, reduciendo sensiblemente su planilla mensual.
  - Industrias y comercios cargan sus baterías BESS en horas valle diurnas o nocturnas y las descargan de 18:00 a 22:00, ahorrando dinero y evitando apagones.
  - Hogares programan lavadoras, bombas de agua o recarga de autos eléctricos fuera del pico nocturno.

#### 9.2. Infraestructura de Medición Avanzada (AMI - Medidores Inteligentes)
Para que el usuario pueda facturar con tarifas horarias y aprovechar el net metering solar 1:1, es indispensable la transición tecnológica de los antiguos medidores electromecánicos a **medidores inteligentes bidireccionales con telemetría**:
- Registro por intervalos de 15 minutos de energía activa y reactiva.
- Corte y reconexión remota inmediata (reduciendo cuadrillas y costos operativos de campo).
- Comunicación bidireccional mediante radiofrecuencia o celular (GPRS/LTE/PLC).
- Detección instantánea de fraudes, manipulaciones y pérdidas no técnicas.

#### 9.3. Modelo Económico del Depósito de Garantía: Costo + 10%
Históricamente, en el Ecuador la provisión de medidores por parte de las distribuidoras ha sido ineficiente, con escasez recurrente de inventarios, trámites que demoraban más de un año y pérdidas patrimoniales al considerarse el medidor como un gasto absorbido por la empresa pública.

Frente a la alternativa de un recargo del 5%, la modelación económica demuestra que **un recargo del diez por ciento (10%) sobre los costos eficientes es técnicamente superior y financiero-sostenible**:

```
+-------------------------------------------------------------------------------------------------------+
|                    ESTRUCTURA ECONÓMICA DEL MEDIDOR INTELIGENTE AUTOFINANCIADO                        |
+--------------------------------------------+-----------------------------+----------------------------+
| COMPONENTE / CONCEPTO                      | VALOR MONETARIO ESTIMADO    | PROPÓSITO TÉCNICO          |
+--------------------------------------------+-----------------------------+----------------------------+
| Costo de compra consolidada a escala       | $55.00 a $65.00 USD         | Medidor inteligente AMI    |
| (Importación masiva CELEC/Distribuidoras)  |                             | bidireccional homologado   |
| Recargo operativo de garantía (+10%)       | $5.50 a $6.50 USD           | Cobertura y fondo de stock |
+--------------------------------------------+-----------------------------+----------------------------+
| **DEPÓSITO DE GARANTÍA TOTAL AL USUARIO**  | **$60.50 a $71.50 USD**     | Saldo patrimonial abonado  |
+--------------------------------------------+-----------------------------+----------------------------+
| **Financiamiento social diferido**         | **$1.68 a $1.98 USD / mes** | Diferido a 36 meses        |
| (Cuota fija en planilla mensual de luz)    |                             | sin intereses              |
+--------------------------------------------+-----------------------------+----------------------------+
```

- **Por qué el 10% es la cifra óptima frente al 5%:**
  1. **Absorción del Costo Financiero del Diferimiento (36 meses):** En el Ecuador, la tasa de interés activa referencial bordea el 9% a 11% anual. Al conceder financiamiento a 3 años sin intereses para los abonados humildes, la distribuidora inmoviliza capital de trabajo. Un 5% quedaba corto; el 10% compensa el costo de oportunidad del dinero.
  2. **Cobertura por Siniestralidad y Mortalidad Técnica (Rayos y Sobretensión):** En el clima tropical y húmedo del Ecuador (Costa y Amazonía), las descargas atmosféricas y fallas de red provocan una tasa de mortalidad técnica del 2% al 3% anual en componentes electrónicos de telemetría. El 10% cubre este seguro de reposición sin pedir dinero al Presupuesto General del Estado.
  3. **Stock Permanente y Cero Burocracia:** El remanente nutre un fondo rotativo que financia bodegaje, calibración del laboratorio técnico y custodia para que nunca más falte un medidor en ninguna agencia cantonal.
  4. **Universalidad (Inclusión sin Exclusión):** Con una cuota mensual de apenas **$1.68 a $1.98 USD al mes**, ninguna familia queda excluida del servicio formal.

#### 9.4. Viabilidad Jurídica: Cómo Sortear la Prohibición Histórica de Cobro de Medidores
- **El Obstáculo Jurídico Previo:** En el Ecuador existía la noción jurídica y reglamentaria (en resoluciones previas de ARCONEL y en interpretaciones de la Ley Orgánica de Defensa del Consumidor, Art. 40) de que las empresas de servicios públicos domiciliarios no pueden cobrar al usuario por la instalación de equipos indispensables para la medición del servicio.
- **La Solución en la Ley Orgánica Reformatoria:**
  1. **Principio de Jerarquía Normativa (Lex Posterior y Lex Specialis):** Este proyecto tiene rango de **Ley Orgánica**, jerárquicamente superior a la Ley del Consumidor (que es ordinaria en materia de servicios públicos regulados por ley especial) y a las resoluciones de ARCONEL. La ley incorpora una **derogatoria expresa** de cualquier prohibición previa.
  2. **Naturaleza Jurídica de "Depósito de Garantía Patrimonial" (No Venta Forzosa):** La ley no estructura el mecanismo como una venta mercantil forzosa, sino como un **depósito de garantía por custodia del bien público**. Si el usuario cancela su contrato y entrega el medidor operativo, **recibe el 100% de su dinero de vuelta**, o puede traspasarlo al nuevo propietario del predio. Esto blinda la norma contra cualquier demanda de inconstitucionalidad.

#### 9.5. Sostenibilidad Financiera: Prohibición de Servicio a Pérdida y Descuento del 2% por Pronto Pago
- **Finanzas Sanas para Invertir:** El sector eléctrico no puede operar a pérdida ni a ganancia mínima. La ley fija un **margen operativo de rentabilidad y reinversión del sector no inferior al diez por ciento (10%)** en los pliegos tarifarios, garantizando que CELEC y las distribuidoras tengan fondos para repuestos y expansión.
- **Estrategia de Liquidez Acelerada (Descuento del 2% por Pronto Pago):**
  - Se concede un **descuento del 2% en la planilla** si el abonado paga dentro de los primeros 5 días hábiles o mediante débito automático bancario.
  - **Rentabilidad Financiera de la Medida:** A la empresa distribuidora le cuesta mucho más la cartera vencida, el costo del capital de trabajo y el costo operativo de enviar cuadrillas de corte y reconexión que otorgar un 2% de descuento comercial. La recaudación masiva en los primeros 5 días del mes inyecta liquidez líquida inmediata para pagar a generadores y evitar paradas por falta de combustible.

#### 9.6. Régimen Coercitivo contra la Morosidad Pública y Extinción Forzosa de Deudas: ¿Por qué no solo cortar o embargar cuentas?
Uno de los mayores drenajes de liquidez histórica en el sector eléctrico ecuatoriano ha sido la cartera incobrable del sector público (municipios, empresas públicas y ministerios). Históricamente, las herramientas ordinarias fracasaban por dos trampas estructurales:
1. **La Trampa Constitucional del Corte Total:** Si la eléctrica corta el suministro general a un municipio, apaga las estaciones de bombeo de agua potable o plantas de tratamiento de aguas servidas. En menos de 4 horas, un juez constitucional otorga una Acción de Protección con Medida Cautelar por vulneración al derecho humano al agua (Art. 12 CRE) y ordena la reconexión bajo amenaza de destitución del gerente eléctrico.
2. **La Trampa del Juicio Coactivo y Embargo de Cuentas Públicas:** Conforme al Art. 165 del COPLAFIP, los recursos del Presupuesto General del Estado y del Modelo de Equidad Territorial en el Banco Central del Ecuador (BCE) son legalmente inembargables para coactivas ordinarias entre entidades públicas, entrampando el cobro en el Tribunal Contencioso Administrativo durante 5 a 10 años.

**La Solución Estructural de 4 Vías Implementada en la Ley:**
```
                           ESQUEMA COERCITIVO DE COBRO AL SECTOR PÚBLICO
                                          ┌──────────────┐
                                          │ Mora Pública │
                                          └──────┬───────┘
                                                 │
                      ┌──────────────────────────┴──────────────────────────┐
                      ▼                                                     ▼
           [30 Días de Incumplimiento]                           [60 Días de Incumplimiento]
                      │                                                     │
                      ▼                                                     ▼
         ┌─────────────────────────┐                           ┌─────────────────────────┐
         │ Corte Remoto Quirúrgico │                           │ Retención y Compensación│
         │ (Medición AMI)          │                           │ de Tasas Municipales    │
         │ - Palacios Municipales  │                           │ (Aseo y Bomberos)       │
         │ - Sedes Administrativas │                           └────────────┬────────────┘
         │ - Estadios y Piletas    │                                        │
         │ (Cero medidas cautelares│                               ¿Deuda no cubierta?
         │  para burocracia)       │                                        │
         └─────────────────────────┘                           ┌────────────┴────────────┐
                                                               ▼                         ▼
                                                    ┌────────────────────┐    ┌────────────────────┐
                                                    │ Débito Automático  │    │ Responsabilidad    │
                                                    │ MEF / Banco Central│    │ Solidaria y        │
                                                    │ (Descuento de la   │    │ Destitución por la │
                                                    │  alícuota fiscal)  │    │ Contraloría        │
                                                    └────────────────────┘    └────────────────────┘
```

1. **Retención Líquida Directa de Tasas (Compensación de Obligaciones):** La distribuidora ya recauda en efectivo las tasas de aseo y bomberos de la ciudadanía. La ley establece la compensación forzosa automática: la eléctrica no transfiere ese dinero al GAD moroso hasta saldar al 100% las facturas eléctricas vencidas (>60 días).
2. **Corte Remoto Quirúrgico a Cargas No Esenciales:** Se prohíbe cortar salas de cuidados intensivos o bombeo de agua, pero se ejecuta el corte remoto inmediato mediante tecnología AMI al Palacio Municipal, oficinas de tránsito, complejos deportivos y luminarias ornamentales. La ley prohíbe taxativamente a jueces constitucionales otorgar medidas cautelares a dependencias burocráticas morosas.
3. **Débito Automático en Fuente del MEF y Banco Central:** Si las tasas retenidas no cubren la deuda, el MEF y el BCE debitan de oficio los valores de las alícuotas del Modelo de Equidad Territorial o del presupuesto institucional del ministerio deudor, transfiriéndolos a la distribuidora en 5 días hábiles.
4. **Sanción de Destitución Inmediata y Juicio de Cuentas:** La autoridad y el director financiero que no presupuesten o no paguen la luz incurren en responsabilidad civil solidaria y causal de destitución automática por la Contraloría General del Estado.

---

### 10. RÉGIMEN DE ESTIAJE, SEQUÍAS Y CONTINGENCIA HIDROLÓGICA

#### 10.1. Mecánica del Despacho en Cascada ante Sequía
Cuando la cota de los embalses hidroeléctricos desciende por debajo de los niveles de seguridad operativa (Mazar a menos de 2.115 msnm, Paute a menos de 1.975 msnm):
1. La disponibilidad de energía hidroeléctrica barata disminuye.
2. El sistema despacha obligatoriamente la siguiente energía más económica disponible:
   - Solar fotovoltaica y eólica diurna;
   - Generación a biomasa de ingenios azucareros;
   - Centrales térmicas a gas natural local (Termogas Machala);
   - Centrales a búnker y fuel oil;
   - Como último recurso: turbinas térmicas a diésel e importaciones internacionales.
3. Para los bloques preferentes (250 kWh residencial y 500/800 kWh alimentario), se asigna contablemente la energía más barata que quede en el despacho en ese momento. Al agotarse la hidroelectricidad, la tarifa de dichos bloques absorberá únicamente el incremento real de la fuente sustituta más económica disponible.

#### 10.2. El Factor de Contingencia Climática por Estiaje ($FCC$)
El incremento del costo de despacho se refleja en un rubro temporal denominado **Factor de Contingencia Climática ($FCC$)**:

$$FCC_m = \frac{\sum_{i} (C_{\text{fuente }, i} - C_{\text{base}}) \times E_i + C_{\text{importaciones}}}{E_{\text{total facturada}}}$$

#### 10.3. Publicidad Previa Obligatoria y Transparencia
- El Ministerio de Energía y la ARCONEL tienen la obligación legal de anunciar el inicio de la temporada de ajuste con al menos **15 días de anticipación**.
- Se prohíben aumentos retroactivos o sorpresivos.
- En la planilla mensual del usuario se imprime un gráfico didáctico y el valor exacto del $FCC$, detallando cuántos centavos por kWh corresponden al estiaje y la fecha proyectada de cese.

#### 10.4. Regla de Mantenimiento Temporal y Cero Déficit
- La tarifa ajustada con el $FCC$ se mantendrá en vigencia **de manera continua hasta que se liquide y cancele el 100% de los pasivos generados durante la sequía** (pagos pendientes de combustibles a Petroecuador, liquidaciones comerciales con Colombia y Perú, contratos de generación de emergencia).
- Una vez que los embalses recuperen sus niveles normales y la cuenta de costos de contingencia llegue a saldo cero, el $FCC$ se desactiva de forma automática por resolución de ARCONEL, retornando las tarifas a sus valores base.

---

### 11. FONDO ESPECIAL DE REINVERSIÓN Y RESILIENCIA ELÉCTRICA (FERRE)

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

#### 11.1. Blindaje Jurídico contra la Discrecionalidad Fiscal
- En el pasado, los excedentes de las empresas públicas del sector energético eran absorbidos por el Ministerio de Finanzas para financiar gasto corriente, salarios de la burocracia o subsidios políticos.
- La ley declara a los excedentes del sector eléctrico como **patrimonio autónomo, intangible e intransferible**.
- Queda prohibida su reversión a la Cuenta Única del Tesoro Nacional.

#### 11.2. Asignación Estratégica del FERRE:
1. **Mantenimiento Preventivo y Mayor:** Garantizar que turbinas, rodetes, transformadores y generadores térmicos tengan repuestos y mantenimiento a tiempo, evitando que salgan de servicio durante los estiajes.
2. **Almacenamiento Energético (BESS):** Financiar la instalación de bancos de baterías de ion-litio a gran escala que acumulen los excedentes de energía solar diurna e hidroeléctrica nocturna para inyectarla en horas pico (18:00 a 22:00).
3. **Reforzamiento del Sistema Nacional de Transmisión (SNT):** Eliminar cuellos de botella en líneas de 230 kV y 500 kV para evacuar energía renovable desde las zonas de generación hacia los grandes centros de consumo.
4. **Resiliencia en Galápagos:** Incrementar la penetración eólica y solar en el archipiélago para reducir al mínimo el consumo de combustibles fósiles.

#### 11.3. Modelación Cuantitativa del Rubro de Resiliencia de 1 Centavo ($0.01 USD/kWh): Solución de Fondo y Ganancias de Reinversión

Para transformar el sector eléctrico de un sistema crónicamente quebrado a uno solvente con capacidad de inversión continua, la incorporación de un rubro de resiliencia de **un centavo de dólar por kilovatio-hora ($0.01 USD/kWh)** representa una palanca financiera de enorme potencia:

```
+-------------------------------------------------------------------------------------------------------+
|                    RECAUDACIÓN Y CAPACIDAD DE INVERSIÓN DEL RUBRO DE 1 CENTAVO (FERRE)                |
+---------------------------------------------+-----------------------------+---------------------------+
| ESCENARIO DE APLICACIÓN                     | ENERGÍA FACTURABLE ANUAL    | RECAUDACIÓN NETA ANUAL    |
+---------------------------------------------+-----------------------------+---------------------------+
| **Escenario A: Tarifa General Universal**   | 28,000 GWh / año            | **$280.00 M USD / año**   |
| (Aplica a toda la energía facturada)        | (28,000,000,000 kWh)        |                           |
| **Escenario B: Modulado y Progresivo**      | 19,250 GWh / año            | **$192.50 M USD / año**   |
| (Exonera los 250 kWh base y aplica a resto) | (19,250,000,000 kWh)        |                           |
+---------------------------------------------+-----------------------------+---------------------------+
```

* **Poder Adquisitivo del Fondo en el Mundo Real:**
  1. **Año 1:** Financiamiento e instalación de **250 MW / 1,000 MWh en sistemas de baterías BESS** en subestaciones críticas (Trinitaria, Pascuales, Dos Cerritos, Tisaleo). Esto inyecta 250 MW en la hora pico nocturna (18:00 a 22:00), eliminando de golpe los racionamientos por déficit de potencia.
  2. **Año 2:** Recuperación y modernización mayor de la central termoeléctrica a gas natural local Termogas Machala (incorporando ciclo combinado) y dragado/desarenado de sedimentos en Coca Codo Sinclair y Paute.
  3. **Año 3:** Blindaje de redes de distribución, subestaciones y telemetría de CNEL EP, reduciendo pérdidas del 20% al 12% (ahorrando otros $150 M USD/año recurrentes).
* **Impacto en el usuario:**
  - Para un usuario que consume 200 kWh (dentro del bloque protegido), el impacto es de \$0.00 en el Escenario B o de apenas **\$2.00 USD al mes** en el Escenario A.
  - El usuario prefiere pagar \$2.00 USD más al mes antes que sufrir apagones que le queman los electrodomésticos, le pudren la comida en la refrigeradora o lo obligan a gastar \$150 USD en gasolina para un generador ruidoso.

---

### 12. PROPUESTAS DE INGENIERÍA ESTRUCTURAL Y OPTIMIZACIÓN DEL SISTEMA ELÉCTRICO NACIONAL

A fin de erradicar de forma definitiva los problemas de racionamiento, déficit de potencia en horas pico y obsolescencia operativa, el sinceramiento tarifario y la gobernanza del FERRE se articulan con seis optimizaciones de ingeniería de alto impacto:

#### 12.1. Cierre de Ciclo Combinado en Termogas Machala (+150 MW sin Consumo de Gas Adicional)
- **Diagnóstico Termodinámico:** La central termoeléctrica Termogas Machala (provincia de El Oro) opera actualmente con turbinas de gas en ciclo abierto simple (eficiencia térmica de solo 32% a 34%), arrojando gases de combustión a más de 500 °C por las chimeneas a la atmósfera.
- **La Solución de Ingeniería:** Instalación de calderas de recuperación de calor por vapor (HRSG - *Heat Recovery Steam Generators*) acopladas a una turbina de vapor de condensación, cerrando el ciclo termodinámico (Ciclo Combinado).
- **Impacto Energético y Económico:**
  - Añade entre **130 y 150 MW de potencia eléctrica firme y continua** al Sistema Nacional Interconectado sin requerir ni un solo pie cúbico adicional de gas natural del Golfo de Guayaquil (Campo Amistad).
  - Eleva la eficiencia térmica de la central al **54% - 56%**.
  - Reduce el costo medio de generación de la planta de 8.5 a **5.0 ¢USD/kWh**, aportando potencia de base firme a la Costa ecuatoriana para blindar el bombeo y la industria camaronera.

#### 12.2. Aceleración de la Interconexión Internacional a 500 kV Ecuador-Perú
- **Diagnóstico de Complementariedad Hidrológica:** Las cuencas hidrográficas de la vertiente amazónica del Ecuador y del Perú presentan regímenes pluviométricos desfasados y complementarios:
  - Cuando los ríos andinos orientales de Ecuador entran en estiaje severo (octubre a marzo), Perú dispone de caudales estables y un superávit estructural de generación térmica a gas natural de bajo costo proveniente de los yacimientos de Camisea.
  - Cuando Ecuador goza de abundancia hídrica (abril a septiembre), las hidroeléctricas ecuatorianas pueden exportar excedentes limpios a Perú.
- **La Obra Estratégica:** Línea de transmisión a 500 kV Chorrillos - Pasaje - Frontera (aproximadamente 550 km de circuito troncal binacional con capacidad de transporte de **1,000 MW**).
- **Beneficio Financiero:** Permite importar potencia firme peruana durante el estiaje a costos regulados de **7.0 a 9.0 ¢USD/kWh**, desplazando por completo la importación colombiana de emergencia a diésel que ha llegado a costar entre 28.0 y 45.0 ¢USD/kWh.

#### 12.3. Conversión de Gas de Mecheros Petroleros a Electricidad en Boca de Pozo ("Flare-to-Power" Modular Privado)
- **Diagnóstico Ambiental y Energético:** En los campos petroleros de la Amazonía (Orellana y Sucumbíos) se queman en mecheros aproximadamente **60 a 80 millones de pies cúbicos diarios (MMSCFD) de gas natural asociado**, liberando CO2 y calor mientras las operaciones de bombeo del SOTE y pozos queman diésel importado subsidiado.
- **La Solución Modular Kronos:** Autorizar de inmediato contratos privados de autogeneración en sitio donde empresas especializadas instalan **motogeneradores y microturbinas modulares en contenedores (skids sobre ruedas)** directamente al pie de los pozos petroleros.
- **Impacto:**
  - Generación de **350 a 450 MW de potencia firme** en el Oriente ecuatoriano.
  - Autoabastecimiento del 100% de la carga electromecánica petrolera (bombeo electrosumergible y estaciones de bombeo de crudo), retirando más de 200 MW de demanda de la red nacional y apagando generadores diésel contaminantes.
  - Cero gasto del Fisco: inversión 100% privada con cobro eficiente por kWh entregado en borne de pozo.

#### 12.4. Compensación Reactiva Dinámica y Recuperación de Capacidad en Subestaciones de CNEL EP (+150 MW Útiles)
- **Diagnóstico de Red en la Costa:** En las áreas de concesión de CNEL EP (Guayas, Manabí, Los Ríos, El Oro), la proliferación de motores industriales sin corregir y equipos de climatización genera una demanda masiva de potencia reactiva inductiva, degradando el factor de potencia a niveles críticos de **0.80 a 0.84**.
- **Consecuencia Técnica:** La potencia reactiva satura las líneas de transmisión y sobrecalienta los transformadores, provocando caídas de voltaje severas y bloqueando el transporte de potencia activa real.
- **La Optimización:** Instalación de bancos automáticos de capacitores y compensadores estáticos de reactivos dinámicos (STATCOMs) en 24 subestaciones troncales de distribución.
- **Resultado:** Al corregir el factor de potencia a **0.98**, se liberan de golpe entre **120 y 180 MW de capacidad de transporte útil** en las mismas líneas existentes, estabilizando el voltaje en Guayaquil, Manta y Machala sin tender un solo kilómetro de cable nuevo.

#### 12.5. Electrificación Eficiente del Sector Camaronero (Sustitución de Bombeo Diésel por Motores Trifásicos a Costo Real)
- **Diagnóstico Productivo:** El sector camaronero ecuatoriano (más de 220,000 hectáreas de piscinas) consumía históricamente millones de galones de diésel subsidiado en motores de combustión interna estacionarios para aireación y bombeo de recambio de agua.
- **La Optimización:** Tendido de redes trifásicas dedicadas de media tensión (13.8 / 34.5 kV) para alimentar motores eléctricos y aireadores tipo *paddlewheel* con variadores de frecuencia.
- **Rentabilidad Mutua sin Subsidios:** A una tarifa industrial a costo real eficiente de **10.0 a 11.5 ¢USD/kWh**, el costo de operación del productor camaronero se reduce en un **38% a 45%** frente al costo de operar con diésel no subsidiado, amortizando la infraestructura eléctrica en menos de 3 años, reduciendo la huella de carbono de la exportación acuícola y erradicando el contrabando de combustible marino.

#### 12.6. Despacho Hidrotérmico Predictivo con Modelado Satelital y Redes Neuronales en CENACE
- **Diagnóstico Operativo:** El CENACE ha dependido históricamente de reglas hidrológicas deterministas con escasa anticipación sobre las crecidas y secas de la cuenca amazónica (Paute, Mazar y Coca Codo).
- **La Modernización:** Implementación de un gemelo digital con modelos hidrológicos predictivos basados en redes neuronales e inteligencia artificial, alimentados por telemetría satelital de radar y precipitación en tiempo real (misiones GPM de la NASA y Copernicus de la ESA).
- **Impacto en Confiabilidad:** Permite anticipar caudales con **72 a 96 horas de anticipación**, optimizando el llenado y vaciado estratégico de los embalses de Mazar y Amaluza, eliminando vertimientos no controlados de agua y reteniendo el recurso hídrico para cubrir con precisión matemática el pico nocturno de las 18:00 a las 22:00 horas.

---

### 13. CONCLUSIONES TÉCNICAS Y BENEFICIOS PARA EL ECUADOR

1. **Equidad Social Genuina y Ampliada:** Se garantiza a las familias ecuatorianas la energía más barata del país hasta 250 kWh/mes (300 kWh en Costa/Amazonía cálida), a los alimentos populares (hasta 500 kWh en tiendas y 800 kWh en panaderías artesanales), a los adultos mayores (50% de descuento vital hasta 50 kWh/mes), a los hospitales públicos de la RPIS y a las escuelas y colegios fiscales, con un piso tarifario legal que protege las finanzas de las distribuidoras.
2. **Responsabilidad Fiscal y Finanzas Sanas:** Al cobrar tarifa a costo real pleno al resto de actividades económicas, a los consumos excesivos y erradicar los subsidios al combustible térmico en Petroecuador, el Estado recupera entre **$2,350 y $3,250 millones de USD anuales** (2.5% a 3.2% del PIB), saneando de raíz el déficit fiscal nacional.
3. **Erradicación de Subsidios Cruzados y Justicia Productiva:** Se prohíben las sobretasas artificiales a la industria; cada segmento responde a su costo real de servicio (*Cost-of-Service*), demostrándose que los bloques protegidos se autofinancian con la hidroelectricidad amortizada del Estado sin gravar al sector productivo.
4. **Descarbonización Insular Acelerada en Galápagos:** Bajo el amparo de los Arts. 258 y 396 de la CRE y la LOREG, cobrar el costo real de 35 a 42 ¢USD/kWh al turismo y consumo suntuario desploma el Payback de techos solares con baterías BESS a menos de 2 años, logrando la transición limpia financiada íntegramente por el capital privado sin gasto público.
5. **Modernización Tecnológica Universal y No Gratuita:** El esquema de medidores inteligentes con depósito de garantía (Costo + 10%) financiado a 36 meses (~$1.80/mes) asegura la universalización de la medición formal, erradica tomas clandestinas y permite tarifas horarias sin desfinanciar a las empresas distribuidoras.
6. **Ganancias Mínimas y Solución Estructural Continua:** La inclusión del margen regulado del 10% y el rubro de resiliencia de hasta 1 centavo/kWh ($0.01 USD/kWh) canalizado al FERRE genera entre $190 y $280 millones anuales en liquidez para mantenimiento de plantas y baterías BESS, acabando definitivamente con los apagones.
