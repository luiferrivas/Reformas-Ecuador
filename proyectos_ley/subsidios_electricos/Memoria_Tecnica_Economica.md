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

#### 2.2. Bloque de Alimentación Básica y Comercio Barrial: Umbral de 500 kWh/mes
- **Fundamento Productivo y Social:**
  - Los pequeños comercios de abastecimiento de víveres (tiendas de barrio, micromercados, fruterías, carnicerías) y las panaderías artesanales operan con equipos indispensables de cadena de frío y fuerza motriz (refrigeradores exhibidores, congeladores de lácteos y carnes, amasadoras de pan, batidoras).
  - Un estudio técnico de carga eléctrica para una panadería o tienda barrial típica refleja un consumo mensual medio de **350 a 480 kWh/mes**.
  - Si a estos micronegocios se les aplicara la tarifa comercial plena desde el primer kilovatio, el incremento de costos operativos se trasladaría inevitablemente al precio final del pan, la leche, el queso y los alimentos diarios, provocando un impacto inflacionario regresivo en la canasta familiar básica.
  - El umbral de **500 kWh/mes** protege la producción y venta de alimentos populares, liquidando dicho bloque con la energía de generación más barata disponible.

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

---

### 4. TARIFAS A COSTO REAL PARA EL RESTO DE SECTORES Y EXCEDENTES

Para todos los consumidores no amparados por los bloques preferentes (comercio de media y gran escala, industrias, bancos, telecomunicaciones, minería, sector público, grandes consumidores) y para los consumos residenciales y alimentarios en la porción que exceda los 250 kWh o 500 kWh respectivamente, se aplicará la **Tarifa a Costo Real Pleno ($T_{\text{real}}$)**:

$$T_{\text{real}} = C_{\text{gen,real}} + C_{\text{trans}} + C_{\text{dist}} + C_{\text{com}} + C_{\text{pérdidas}} + C_{\text{SAPG}}$$

Donde:
- $C_{\text{gen,real}}$: Costo medio ponderado real o costo marginal de generación eficiente del sistema, sin subsidio estatal de combustibles ni subvenciones al capital.
- $C_{\text{trans}}$: Peaje de transmisión del Sistema Nacional de Transmisión (SNT), auditado por ARCONEL.
- $C_{\text{dist}}$: Valor agregado de distribución (VAD) eficiente según nivel de tensión.
- $C_{\text{com}}$: Costo de medición, lectura, facturación y recaudación.
- $C_{\text{pérdidas}}$: Reconocimiento exclusivo de pérdidas técnicas eficientes (máximo 8-9%, castigando la ineficiencia empresarial).
- $C_{\text{SAPG}}$: Servicio de Alumbrado Público General proporcional.

**Resultado Económico:** Se eliminan las transferencias ciegas del Estado que antes subvencionaban a empresas altamente rentables o a viviendas de alto consumo, liberando cientos de millones de dólares anuales en el Presupuesto General del Estado y recapitalizando el flujo de caja del sector eléctrico.

---

### 5. RÉGIMEN DE ESTIAJE, SEQUÍAS Y CONTINGENCIA HIDROLÓGICA

#### 5.1. Mecánica del Despacho en Cascada ante Sequía
Cuando la cota de los embalses hidroeléctricos desciende por debajo de los niveles de seguridad operativa (Mazar a menos de 2.115 msnm, Paute a menos de 1.975 msnm):
1. La disponibilidad de energía hidroeléctrica barata disminuye.
2. El sistema despacha obligatoriamente la siguiente energía más económica disponible:
   - Solar fotovoltaica y eólica diurna;
   - Generación a biomasa de ingenios azucareros;
   - Centrales térmicas a gas natural local (Termogas Machala);
   - Centrales a búnker y fuel oil;
   - Como último recurso: turbinas térmicas a diésel e importaciones internacionales.
3. Para los bloques preferentes (250 kWh y 500 kWh), se asigna contablemente la energía más barata que quede en el despacho en ese momento. Al agotarse la hidroelectricidad, la tarifa de dichos bloques absorberá únicamente el incremento real de la fuente sustituta más económica disponible.

#### 5.2. El Factor de Contingencia Climática por Estiaje ($FCC$)
El incremento del costo de despacho se refleja en un rubro temporal denominado **Factor de Contingencia Climática ($FCC$)**:

$$FCC_m = \frac{\sum_{i} (C_{\text{fuente }, i} - C_{\text{base}}) \times E_i + C_{\text{importaciones}}}{E_{\text{total facturada}}}$$

#### 5.3. Publicidad Previa Obligatoria y Transparencia
- El Ministerio de Energía y la ARCONEL tienen la obligación legal de anunciar el inicio de la temporada de ajuste con al menos **15 días de anticipación**.
- Se prohíben aumentos retroactivos o sorpresivos.
- En la planilla mensual del usuario se imprime un gráfico didáctico y el valor exacto del $FCC$, detallando cuántos centavos por kWh corresponden al estiaje y la fecha proyectada de cese.

#### 5.4. Regla de Mantenimiento Temporal y Cero Déficit
- La tarifa ajustada con el $FCC$ se mantendrá en vigencia **de manera continua hasta que se liquide y cancele el 100% de los pasivos generados durante la sequía** (pagos pendientes de combustibles a Petroecuador, liquidaciones comerciales con Colombia y Perú, contratos de generación de emergencia).
- Una vez que los embalses recuperen sus niveles normales y la cuenta de costos de contingencia llegue a saldo cero, el $FCC$ se desactiva de forma automática por resolución de ARCONEL, retornando las tarifas a sus valores base.

---

### 6. FONDO ESPECIAL DE REINVERSIÓN Y RESILIENCIA ELÉCTRICA (FERRE)

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

#### 6.1. Blindaje Jurídico contra la Discrecionalidad Fiscal
- En el pasado, los excedentes de las empresas públicas del sector energético eran absorbidos por el Ministerio de Finanzas para financiar gasto corriente, salarios de la burocracia o subsidios políticos.
- La ley declara a los excedentes del sector eléctrico como **patrimonio autónomo, intangible e intransferible**.
- Queda prohibida su reversión a la Cuenta Única del Tesoro Nacional.

#### 6.2. Asignación Estratégica del FERRE:
1. **Mantenimiento Preventivo y Mayor:** Garantizar que turbinas, rodetes, transformadores y generadores térmicos tengan repuestos y mantenimiento a tiempo, evitando que salgan de servicio durante los estiajes.
2. **Almacenamiento Energético (BESS):** Financiar la instalación de bancos de baterías de ion-litio a gran escala que acumulen los excedentes de energía solar diurna e hidroeléctrica nocturna para inyectarla en horas pico (18:00 a 22:00).
3. **Reforzamiento del Sistema Nacional de Transmisión (SNT):** Eliminar cuellos de botella en líneas de 230 kV y 500 kV para evacuar energía renovable desde las zonas de generación hacia los grandes centros de consumo.
4. **Resiliencia en Galápagos:** Incrementar la penetración eólica y solar en el archipiélago para reducir al mínimo el consumo de combustibles fósiles.

---

### 7. CONCLUSIONES TÉCNICAS Y BENEFICIOS PARA EL ECUADOR

1. **Equidad Social Genuina:** Se garantiza a las familias ecuatorianas la energía más barata del país hasta 250 kWh/mes, y se preserva el precio de los alimentos populares hasta 500 kWh/mes en panaderías y tiendas barriales.
2. **Responsabilidad Fiscal y Finanzas Sanas:** Al cobrar tarifa a costo real pleno al resto de actividades económicas y a los consumos excesivos, el Estado erradica el déficit tarifario crónico sin necesidad de endeudamiento público ni apagones programados.
3. **Resiliencia Adaptativa ante el Clima:** El sistema adquiere una regla matemática transparente para navegar temporadas de sequía, publicitando con antelación las variaciones y manteniendo las tarifas ajustadas solo el tiempo estrictamente necesario para no generar pérdidas.
4. **Sostenibilidad y Modernización Continua:** Cualquier ganancia o remanente se convierte automáticamente en nuevas inversiones eléctricas a través del FERRE, asegurando que el Ecuador cuente con una matriz robusta, moderna y soberana.
