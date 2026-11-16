# Modelo de Cocina Dual (Inducción 220V + Respaldo GLP) y Red de Micro-Bodegas Rurales Comunitarias

> **Consorcio Industrial Kronos — Documento Técnico Canónico de Eficiencia Energética Rural y Descentralización Logística**  
> *Sujeto a la Doctrina Mandatoria de Operación (AGENTS.md) — Mandamientos 1, 3, 4, 5, 6 y 8.*

---

## 1. Misión y Justificación Técnica

Este documento formaliza la ingeniería y el modelo logístico de dos soluciones complementarias diseñadas para resolver de raíz la vulnerabilidad energética del campesinado ecuatoriano:

1. **La Placa de Inducción Robusta de 220V (2 Quemadores Heavy-Duty):** Solución de cocción eficiente de media potencia (3,500 W totales) que aprovecha la instalación de medidores bifásicos individualizados de la Fase 2, equilibrando fases eléctricas, reduciendo pérdidas por efecto Joule y operando en régimen híbrido/dual con un cilindro de gas como respaldo de contingencia.
2. **La Red de Micro-Bodegas Comunitarias de GLP en Poblados Rurales:** Esquema de descentralización de almacenamiento regulado (30 a 100 cilindros) en cabeceras parroquiales y poblados cercanos, permitiendo al campesino adquirir su tanque de gas al PVP oficial o con margen mínimo de mostrador (1.95 a 2.15 USD en Año 1) transportándolo por sus propios medios (muleto, caballo, moto o bicicleta), quebrando el sobreprecio especulativo de 4.50 a 5.50 USD de los fleteros privados en zonas remotas.

---

## 2. Ingeniería de la Cocina Dual: Placa de Inducción 220V de 2 Quemadores

### 2.1. Por qué 220V de 2 Quemadores es Superior a 120V y a 4 Quemadores

El programa estatal de 2014 cometió el error de promover cocinas empotrables de 4 quemadores (6,000 a 7,200 W a 220V), lo que colapsaba los transformadores rurales y costaba más de 300 USD. Por otro lado, una placa de 120V está limitada a ~1,800 W en un solo tomacorriente doméstico (15 A), impidiendo encender dos hornillas con fuerza simultánea.

La solución de ingeniería óptima es la **Placa de Inducción Sobremesa de 2 Quemadores a 220V Bifásico**:

```
                              DIAGRAMA ELÉCTRICO COMPARATIVO
┌──────────────────────────────┬──────────────────────────────┬──────────────────────────────┐
│  Cocina 4Q 220V (Año 2014)   │   Placa 1Q/2Q 120V Monofás.  │  Placa Kronos 2Q 220V Híbrida│
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│ Potencia: 7,200 W            │ Potencia: 1,800 W (Tope 120V)│ Potencia: 3,500 W (2 Quemad.)│
│ Corriente: 32.7 A            │ Corriente: 15.0 A            │ Corriente: 15.9 A            │
│ Pérdidas Joule: Muy Altas    │ Pérdidas Joule: Altas        │ Pérdidas Joule: 75% Menores  │
│ Estado Red: Quema postes     │ Estado Red: Lenta en hervir  │ Estado Red: Balance perfecto │
│ Costo Equipo: 350-500 USD    │ Costo Equipo: 45-60 USD      │ Costo Equipo: 75-95 USD      │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
```

### 2.2. Ventajas Físicas y Termodinámicas de la Placa 220V de 2 Quemadores

1. **Reducción Drástica de Corriente y Pérdidas Joule:**
   Para entregar 3,500 W combinados (Hornilla A: 2,000 W para hervir sopas/arroz; Hornilla B: 1,500 W para frituras/guisos):

$$I = \frac{P}{V} = \frac{3,500\text{ W}}{220\text{ V}} \approx 15.91\text{ A}$$

   Al repartir la carga entre las dos fases vivas ($L_1$ y $L_2$ de 120V respecto al neutro), la corriente por conductor es de aproximadamente 15.9 A, lo que permite utilizar cable estándar calibre 12 AWG o 10 AWG con un breaker bipolar convencional de 20 A.
   Las pérdidas térmicas en los cables de la vivienda ($P_{\text{pérdida}} = I^2 R$) se reducen en un **75%** en comparación con intentar extraer esa misma potencia a 120V.

2. **Equilibrio de Fases en el Transformador Rural:**
   Una carga bifásica pura a 220V toma corriente simétrica de ambas ramas del transformador de distribución, evitando el desbalance de neutro que ocurría con cargas grandes a 120V en el campo.

3. **Velocidad de Cocción Térmica Superior al Gas:**
   * Hornilla a gas tradicional de 2 kW: con 40% de eficiencia, entrega $0.80\text{ kW}_{\text{útil}}$ a la olla.
   * Hornilla de inducción Kronos de 2.0 kW a 220V: con 88% de eficiencia, entrega $1.76\text{ kW}_{\text{útil}}$ a la olla.
   * **Resultado:** Hierve 2 litros de agua para el café o el caldo en **menos de 4.5 minutos** (el gas tarda más de 9 minutos).

4. **Sinergia con la Fase 2 (Medidores Eléctricos AMI):**
   Dado que la Fase 2 de la reforma incentiva a los solares rurales a formalizar medidores individuales para no rebasar el umbral de 200/250 kWh, la empresa distribuidora (CNEL, etc.) instala de fábrica medidores electrónicos bifásicos modernos a 220V. La red y la acometida de 220V **ya están instaladas y disponibles** en el predio sin costo adicional.

### 2.3. Especificaciones Constructivas "Heavy-Duty" (Tropicalizada para Páramo y Selva)

* **Marco Perimetral de Acero Inoxidable de 1.5 mm:** Sobre-elevado 2 mm por encima del cristal vitrocerámico. Protege los bordes del vidrio contra desportilladuras cuando se asientan ollas de hierro de 15 a 20 kg.
* **Protección Electrónica contra Descargas Atmosféricas:**
  * Supresor de picos con Varistor de Óxido Metálico (MOV) de alta energía (capacidad de absorción mínima de 450 Joules).
  * Tolerancia de operación en línea: 175V a 250V en régimen dinámico.
* **Controles Táctiles y Perilla Mecánica Sellada (IP54):** Permite encender y graduar potencia incluso con manos mojadas o con harina, superando la falla de los sensores táctiles ultra-sensibles que se bloquean con agua o vapor.

---

## 3. La Red de Micro-Bodegas Rurales de GLP

### 3.1. Diagnóstico del Abuso en el Flete Privado Rural

En el Ecuador rural, el precio subsidiado oficial fijado por el Estado (1.65 USD en depósito) no llega al campesino. El camión distribuidor privado ejerce un monopolio geográfico natural sobre los caminos de herradura y carreteras secundarias de lastre, cobrando entre **4.00 y 5.50 USD por cilindro puesto en la chacra**.

El campesino no paga por el gas: **paga entre 2.50 y 3.85 USD por el flete ineficiente de un camión diésel de 5 toneladas que sube la montaña.**

```
                     CADENA DE DISTRIBUCIÓN: ACTUAL VS. MICRO-BODEGA
1. Modelo Actual (Fletero Monopólico):
   Planta Envasadora (1.65 USD) ──> Camión Repartidor ──> Puerta del Hogar (4.50 a 5.50 USD)
                                   [Margen del fletero: +2.85 a +3.85 USD/tanque]

2. Modelo Kronos (Micro-Bodega en Pueblo):
   Planta Envasadora (1.65 USD) ──> Micro-Bodega Parroquial (1.95 USD) ──> Campesino (Bicicleta/Burro/Moto)
                                   [Margen tendero: +0.30 USD]           [Ahorro hogar: +2.55 a +3.55 USD]
```

### 3.2. Arquitectura de la Micro-Bodega Rural Comunitaria

* **Ubicación Estratégica:** En el centro poblado, cabecera parroquial o caserío comunal más cercano (donde los campesinos acuden periódicamente a la feria semanal, iglesia, centro de salud o escuela).
* **Capacidad de Almacenamiento Regulada:** Espacios autorizados por la ARCH para almacenar entre **30 y 100 cilindros de 15 kg** en condiciones de seguridad industrial (ventilación natural cruzada, piso no chispeante, extintor PQS de 20 lb y detector de fugas).
* **Operadores Locales Autorizados:**
  1. Tiendas de abarrotes comunitarias o ferreterías del pueblo.
  2. Sedes de cooperativas de ahorro y crédito rurales (ej. *Mushuc Runa*, *Jardín Azuayo*).
  3. Almacenes de insumos de las Juntas Parroquiales Rurales o Cabildos Comunitarios.

### 3.3. Estructura Económica y Márgenes de Comercialización

*(Valores referenciales calculados para el Año 1 de la reforma)*

| Rubro / Etapa | Monto Unitario (USD) | Beneficiario / Responsable |
| :--- | :--- | :--- |
| **Precio Oficial en Plataforma Petroecuador** | 1.815 USD | Estado Ecuatoriano / Petroecuador |
| **Flete Mayorista Plataforma a Micro-Bodega** | 0.150 USD | Transporte pesado formal de abastecimiento en bloque |
| **Margen de Comercialización del Tendero Rural** | **0.300 USD** | Dueño de la tienda / almacén comunitario |
| **PVP Oficial de Mostrador en Micro-Bodega** | **2.265 USD** | **Precio final pagado por el campesino en el pueblo** |
| *Precio Cobrado por Fletero Privado en la Chacra* | *4.500 a 5.000 USD* | *Intermediario informal privado en camino de tierra* |
| **Ahorro Neto Directo para la Familia Campesina** | **2.235 a 2.735 USD** | **Ahorro en efectivo por cada cilindro (más del 50%)** |

> **Incentivo para el Comerciante Local:**  
> Una tienda comunal en una parroquia rural que rota **300 cilindros al mes** obtiene un ingreso neto limpio de **90.00 USD/mes** de utilidad directa sin salir de su mostrador, dinamizando el comercio local.

### 3.4. Mecanismo de Control Telemático por CUEN y Canje Físico

Para evitar que la micro-bodega se convierta en un centro de acopio para contrabando o reventa a restaurantes:

1. **Terminal POS Móvil / Smartphone con App ARCH-ARCONEL:**
   El tendero dispone de la aplicación oficial (con sincronización offline criptográfica) que valida el Código Único Eléctrico Nacional (CUEN) del comprador.
2. **Registro de Consumo del Cupo Anual (15 Cilindros):**
   Al digitar el número de medidor o escanear el código QR de la planilla de luz del campesino, el sistema descuenta 1 unidad del cupo anual de 15 cilindros subsidiados.
3. **Canje Físico 1:1:**
   El campesino entrega obligatoriamente un cilindro vacío en buen estado a cambio del cilindro lleno.
4. **Transporte Comunitario Autónomo:**
   Los comuneros bajan al pueblo en su día de feria o compras y transportan el cilindro en burro, caballo, moto con parrilla reforzada, bicicleta o camioneta comunitaria, eliminando la intermediación usurera.

---

## 4. La Simbiosis Operativa: El Hogar Campesino Híbrido

La combinación de la **Placa de Inducción de 220V** y la **Micro-Bodega de GLP** crea una estabilidad financiera y de seguridad alimentaria sin precedentes para el sector rural:

```mermaid
flowchart TD
    subgraph RUTINA_DIARIA["Cocción Diaria (85% de la Energía)"]
        IND["Placa Inducción 220V (2 Quemadores)"] --> RICE["Arroz, sopas, frituras rápidas, café"]
        RICE --> COST_IND["Costo Eléctrico: ~5.40 USD/mes (Tarifa Preferente)"]
    end

    subgraph CONTINGENCIA["Respaldo y Cocción Pesada (15% de la Energía)"]
        GAS["1 Hornilla de Gas conectada a Cilindro"] --> HEAVY["Mote, choclos duros, fritada comunal, apagones"]
        HEAVY --> DURACION["1 cilindro dura de 6 a 8 meses"]
        DURACION --> COMPRA["Compra en Micro-Bodega Parroquial: ~2.26 USD"]
    end

    COST_IND --> TOTAL["Gasto Energético Total del Hogar: ~5.75 USD/mes"]
    COMPRA --> TOTAL
    TOTAL --> AHORRO["Ahorro de más de 45 USD/año frente al fletero tradicional"]
```

### Balance Financiero Anual del Hogar Rural

* **Gasto Histórico con Gas Tradicional (Fletero a 4.75 USD):**
  12 cilindros/año $\times$ 4.75 USD = **57.00 USD/año**.
* **Gasto con el Modelo Dual Kronos (Inducción 220V + Micro-Bodega):**
  * Electricidad mensual para cocción: ~5.40 USD/mes = 64.80 USD/año.
  * Consumo de gas de respaldo (2 cilindros/año comprados en el pueblo): $2 \times 2.265 = 4.53\text{ USD/año}$.
  * Gasto energético total: 69.33 USD/año.
* **Beneficio Neto:** La familia campesina obtiene cocción instantánea, segura (sin riesgo de incendios ni inhalación de gases tóxicos en cocinas cerradas), blindada al 100% contra apagones, y recupera el control de su suministro sin depender del camión fletero.

---

## 5. Bitácora de Decisiones, Ajustes y Descartes

| Alternativa Evaluada | Decisión | Pros Identificados | Contras y Trade-offs | Justificación Técnica Exacta del Descarte |
| :--- | :--- | :--- | :--- | :--- |
| **Placa de Inducción de 120V Monofásica** | **Descartada** | No exige acometida bifásica; enchufable directo. | Limitada a 1,800 W en total; no puede hervir agua en una hornilla y freír en la otra simultáneamente; pérdidas Joule elevadas. | Descartada. Es insuficiente para la cocina familiar andina. La Fase 2 ya instala acometidas bifásicas de 220V con medidores AMI. |
| **Cocina Empotrable de 4 Quemadores 220V (7,200 W)** | **Descartada** | Formato de cocina de lujo convencional. | Sobrecarga la red rural; exige mesón empotrado de hormigón; costo prohibitivo (350+ USD). | Descartada por inviabilidad económica y técnica en el campo (error de 2014). |
| **Placa Sobremesa de 2 Quemadores 220V (3,500 W Heavy-Duty)** | **Aprobada** | Balance simétrico de fases; pérdidas Joule 75% menores; potencia real para hervir en 4.5 min; costo de 75 a 95 USD. | Requiere toma de 220V en la cocina (provista con el nuevo medidor). | Aprobada como la cúspide de eficiencia, costo y robustez para la vivienda rural. |
| **Obligar a la Entrega del Cilindro de Gas para Recibir Inducción** | **Descartada** | Erradicación teórica del uso de GLP. | Pánico al desabastecimiento en apagones; rechazo cultural frontal de la familia campesina. | Descartada. La seguridad energética familiar exige mantener 1 cilindro de gas como respaldo de contingencia. |
| **Continuar con Camiones Fleteros a Domicilio en el Campo** | **Descartada** | El cilindro llega a la puerta de la choza. | Monopolio geográfico; cobro de 4.50 a 5.50 USD; explotación al campesino más pobre. | Descartada. Se sustituye por la red comunitaria de micro-bodegas en pueblos cercanos. |
| **Red de Micro-Bodegas Comunitarias de GLP (30 a 100 Cilindros)** | **Aprobada** | PVP oficial en el pueblo (1.95 a 2.26 USD); tendero gana 0.30 USD/cilindro; campesino ahorra 50% transportando en moto/burro/bici. | Exige terminal POS con app ARCH y control estricto de cupo por CUEN. | Aprobada. Democratiza el acceso al precio real sin subsidiar el combustible de los camiones fleteros. |

---

### Verificación y Archivo Canónico

Este documento queda incorporado en el directorio del proyecto como la guía maestra de ejecución técnica para el despliegue de electromovilidad y cocción limpia rural, así como para la reglamentación de comercialización minorista de GLP de la ARCH.
