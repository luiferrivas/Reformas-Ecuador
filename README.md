# Reformas Ecuador 🇪🇨

Repositorio de iniciativas legislativas, proyectos de ley orgánicos y propuestas de política pública orientadas a la modernización institucional, la sostenibilidad económica y la equidad social en la República del Ecuador.

---

## ⚡ Iniciativa Legislativa Destacada: Reforma al Régimen Tarifario y Subsidios Eléctricos

### Denominación del Proyecto de Ley
**"Ley Orgánica Reformatoria a la Ley Orgánica del Servicio Público de Energía Eléctrica (LOSPEE) para la Asignación Prioritaria de Energía de Menor Costo, Focalización Tarifaria Equitativa y Sostenibilidad Financiera ante Contingencias Climáticas"**

### Documentos del Proyecto
1. **[L1 Cache Contractual y Resumen Ejecutivo (SUMMARY.md)](./proyectos_ley/subsidios_electricos/SUMMARY.md)**: Interfaz primaria y parámetros críticos del proyecto bajo la doctrina Olimpo.
2. **[Proyecto de Ley Completo (Formato Legislativo Oficial)](./proyectos_ley/subsidios_electricos/Proyecto_Ley_Subsidios_Electricos_Ecuador.md)**: Texto legal estructurado con Exposición de Motivos, Considerandos, Articulado Reformatorio, Disposiciones Generales, Transitorias, Derogatorias y Final.
3. **[Memoria Técnica y Económica de Soporte](./proyectos_ley/subsidios_electricos/Memoria_Tecnica_Economica.md)**: Análisis cuantitativo de demanda, modelado de los umbrales de 250 kWh, 500 kWh y 800 kWh, regla de despacho por orden de mérito regional, tarifas horarias TOU, formulación del $FCC$, gobernanza del FERRE y régimen de medidores con garantía (Costo + 10%).
4. **[Auditoría de Viabilidad Política y Optimización del Sistema Eléctrico](./proyectos_ley/subsidios_electricos/Auditoria_Politica_y_Optimizacion_Electrica.md)**: Análisis de realismo político y límites constitucionales sobre mecheros petroleros, autonomía municipal en cobranzas, sindicatos de CNEL, hidroeléctricas de bombeo, solares flotantes y el modelo de luz prepago digital.
5. **[Especificación Técnica Placa Inducción Heavy-Duty 220V](./proyectos_ley/subsidios_electricos/Especificacion_Tecnica_Placa_Induccion_HeavyDuty_220V.md)**: Diseño industrial e ingeniería de la placa sobremesa de 2 quemadores (3,500 W con limitador dinámico a 2,800 W), chasis de acero inoxidable austenítico AISI 304 no magnético (carga de 35 kg por hornilla), perillas encoder IP54 y protección MOV 450 J contra rayos andinos.
6. **[Parámetros y Configuraciones Técnicas](./config/reformas/subsidios_electricos.yaml)**: Parámetros estructurados en YAML para simulación y regulación (umbrales, costos, tarifas horarias TOU, balance nacional y fondo FERRE; ver guía en [`config/README.md`](./config/README.md)).

---

### Ejes Cardinales de la Propuesta

| Eje | Descripción | Impacto |
| :--- | :--- | :--- |
| **Hogares: 200 kWh Base y 250 kWh con Inducción** | Asignación de energía barata hasta **200 kWh/mes base** a nivel nacional y hasta **250 kWh/mes con cocina de inducción** (+50 kWh de cupo de cocción limpia). Excedente suntuario (splits en Costa; calefactores y duchas de 5 kW en Sierra) paga **costo real + recargo de 2 centavos en estiaje**. | Fomenta el abandono del GLP importado subsidiado, recauda 64.8 M USD/año adicionales en el sector eléctrico y activa la sustitución técnica (ventiladores DC de 60 W y calentamiento solar/gas). |
| **Piso Tarifario Mínimo Legal** | La tarifa preferente resultante tiene como límite inferior irreductible el **pliego tarifario regulado actual**. | Protege la estabilidad financiera de las 20 empresas eléctricas distribuidoras (CNEL, EEQ, etc.), impidiendo descalces de ingresos. |
| **Soberanía Alimentaria y Agroindustria Interna** | Asignación de energía más barata hasta **500 kWh/mes** (tiendas), **800 kWh/mes** (panaderías artesanales) y tarifa base eficiente (~7.5 ¢/kWh) a **agroindustria de consumo nacional** (molinos de harina/trigo, arroz, balanceado y lácteos básicos). Agroexportación y minería pagan **100% costo real**. | Protege el precio del pan de batalla, arroz, pollo, huevos y leche contra la inflación en sequías. Filtro forense con DAEs del SENAE: cero energía barata a la exportación. |
| **Agua Potable, Riego Campesino y Fármacos Esenciales** | Asignación de energía base hidroeléctrica eficiente a plantas cantonales de agua potable y saneamiento (~38 GWh/mes con débito BCE), juntas de riego comunitarias (~16 GWh/mes) y farmacéuticas de genéricos del CNMB (~11 GWh/mes). | Garantiza el derecho humano al agua (Art. 12 CRE), desactiva la conflictividad agraria campesina y abarata costos de medicamentos genéricos y sueros hospitalarios sin moras. |
| **Red Pública Integral de Salud (Hospitales Públicos)** | Asignación prioritaria de energía de menor costo de generación a hospitales de especialidades, generales y centros 24h del MSP, IESS, ISSFA, ISSPOL. | Protege áreas críticas (UCI, quirófanos, neonatología y vacunas). **Cero subsidio interno:** las entidades de salud pagan obligatoriamente sus planillas sin deudas. |
| **Educación Pública Fiscal (Escuelas y Colegios)** | Asignación prioritaria de energía barata a ~12,400 planteles educativos fiscales. Curva de consumo diurno sin afectación al pico nocturno. | Garantiza iluminación, computación y bombeo de agua en escuelas. Pago obligatorio presupuestado por el Ministerio de Educación con débito MEF. |
| **Racionalización Subsidio 3ra Edad (Adultos Mayores)** | 50% de descuento restringido estrictamente hasta **50 kWh/mes** (~2.35 USD/mes), 51-250 kWh/mes a tarifa familiar ordinaria y >250 kWh/mes a costo real pleno. **1 solo medidor a nivel nacional por cédula**. | Erradica el fraude de registrar mansiones, saunas y piscinas a nombre de abuelos. Ahorro fiscal de **45 M USD/año** con bloqueo unificado en ARCONEL y depuración mensual del Registro Civil. |
| **Mecanismos Quirúrgicos Anti-Regresivos** | Exclusión de segundas residencias/playa (+35M), macro-fraude agroindustrial/cripto (+150-220M) e infraestructura privada (+25M). La minería tributa tarifa real universal y los autos eléctricos se absorben en el tope de 250 kWh. | Recupera **+210 a +280 M USD/año adicionales** de evasores y nichos de recreación con **cero impacto en hogares vulnerables**. |
| **Erradicación de Subsidios Cruzados Intersectoriales** | Prohibición absoluta de sobretasas a la industria para subsidiar otros consumos. Regulación pura por Costo de Servicio (*Cost-of-Service*). | Devuelve competitividad a la manufactura ecuatoriana. El bloque residencial protegido **se autofinancia con hidroeléctricas amortizadas del Estado** (9.5¢ vs 3.5¢ de costo). |
| **Régimen Especial Galápagos (Arts. 258 y 396 CRE)** | Eólica/solar local hasta 250 kWh/mes a residentes. Tarifa a **costo real insular pleno (35-42 ¢USD/kWh)** a hoteles de lujo, cruceros y turismo. | Principio Contaminador-Pagador. El Payback solar+BESS privado para hoteles cae a **<2 años**, logrando Galápagos Cero Fósiles sin subsidios ni gasto público. |
| **Suficiencia y Balance Energético ("¿Nos alcanza?")** | Demanda protegida (hogares + comida + agua + riego + salud + educación): **879.5 GWh/mes** (10,554 GWh/año). Oferta hidro en peor mes: **1,150 GWh/mes**. | **¡Sí alcanza en volumen (130.8%)!** La hidroeléctrica base cubre holgadamente toda la demanda prioritaria en sequía con un superávit de +270.5 GWh/mes. El problema del país es la potencia en pico (18:00 a 22:00). |
| **Ahorro Fiscal Trienal (Series 2023-2025)** | Eliminación de subsidios térmicos WTI, déficit tarifario, contratos de barcazas y fraude: Ahorro de **1,982 M USD (2023)**, **3,535 M USD (2024)** y **2,925 M USD (2025)**. | Libera entre **2,605 y 3,575 M USD/año** (Promedio: **3,090 M USD/año** = 2.7% - 3.4% del PIB), eliminando hasta el 78% del déficit presupuestario general del Estado. |
| **Siete Optimizaciones de Ingeniería Estructural** | Ciclo Combinado Termogas Machala (+150 MW), Interconexión 500 kV Perú (1,000 MW), Flare to Power (350-450 MW), Compensación Reactiva CNEL (+150 MW), y Hoja de Ruta Hidroeléctrica: Proyecto Cardenillo (596 MW en cascada Paute) y Centrales de Bombeo Reversible (Pumped-Storage 300-500 MW). Descarte de macro filo de agua sin embalse. | Recupera capacidad de red oculta, erradica apagones en horas pico y aporta potencia firme limpia sin sobreendeudamiento estatal. |
| **Paridad de Red, Net Billing 70/30 y Baterías BESS** | Tarifa real plena (~18 ¢USD/kWh), **Net Billing Asimétrico 70/30** (retención del 30% para pérdidas, peajes y FERRE) y 100% de reconocimiento en pico para BESS. Payback solar **3.5 años** y BESS **4.5 años**. **Fast-Track (15 días)** hasta 2,000 kWp. | Desata la inyección solar de todo el sistema industrial al SNI para ahorrar agua diurna en embalses, y descarga de baterías BESS en horas pico. |
| **Premio al Ahorro en Sequía** | Exoneración del 100% del Factor de Contingencia (FCC) a hogares y comercios que reduzcan su consumo mensual en al menos un **10%** en estiaje. | Incentiva el consumo responsable y convierte a la ciudadanía en aliada activa contra los apagones. |
| **Transición Anti-Inflacionaria (12 meses)** | Retiro escalonado del subsidio industrial en 3 trimestres (33% -> 66% -> 100%) respaldado por líneas de **Crédito Verde (CFN/BanEcuador)** para autogeneración y BESS. | Permite que las industrias instalen paneles solares y baterías antes de recibir el impacto tarifario completo, mitigando la inflación en productos finales. |
| **Sinergia Hidro-Solar en Sequía** | La radiación solar máxima coincide con el estiaje andino. La energía solar diurna en techos **ahorra agua en las represas para turbinar de noche**. | Reduce drásticamente la quema de diésel térmico y las importaciones caras, bajando el costo de contingencia. |
| **Tarifas Horarias TOU y Movilidad Eléctrica Condicionada** | Bloques: **Valle** (23:00-06:00 y solar 10:00-14:00), **Llano** y **Pico** (18:00-22:00). **Regla de Autos Eléctricos:** Tarifa reducida únicamente en horas valle con superávit de red; fuera de valle pagan tarifa ordinaria o costo real pleno TOU + FCC. | Desplaza la recarga de baterías y vehículos eléctricos a la madrugada/mediodía con energía limpia sobrante, prohibiendo subsidiar recargas en horas de pico térmico. |
| **Medidores Inteligentes (AMI) y Garantía (Costo + 10%)** | Principio de no gratuidad con derogatoria expresa: Depósito de garantía = **Costo del medidor + 10%**, financiado en la planilla hasta a 36 meses sin intereses (~1.80 USD/mes). | Erradica tomas clandestinas, fondea stock permanente, absorbe costo de crédito y siniestros por rayos, y es 100% reembolsable. |
| **Pronto Pago (2%) y Margen del 10%** | Descuento del **2% en planilla** por pago en los primeros 5 días o débito automático. Prohibición de operar a pérdida (margen mínimo regulado del 10%). | Acelera la liquidez para pagar generación y combustibles, erradicando costos de mora y cortes. Asegura reinversión continua. |
| **Protocolo Coercitivo contra Deudas Públicas (4 Vías)** | Retención forzosa de tasas de basura/bomberos (>60 días), corte quirúrgico remoto a oficinas burocráticas (>30 días) y débito automático en MEF/BCE, con destitución de autoridades morosas. | La empresa eléctrica **no se queda con deudas incobrables de municipios ni ministerios**. Protege agua potable y quirófanos pero asfixia la morosidad burocrática. |
| **Fondo FERRE, Fideicomiso BCE y Capping VAD (8.5%)** | Titularización de bonos verdes (1,200 a 1,500 M USD para Cardenillo/BESS). Cuenta Fiduciaria Maestra Única en el BCE con orden de pago forzoso (CELEC -> Transelectric -> FERRE -> Distribución). Capping de pérdidas en distribución al 8.5% en el VAD. | Blinda la cadena de pagos, erradica el desvío de fondos para burocracia local y obliga a las distribuidoras a absorber pérdidas por fraude en su balance. |
| **Transporte Público Masivo Eléctrico (Metro y Tranvía)** | Tarifa preferente por Costo de Servicio (~8.2 ¢/kWh) para Metro de Quito, Tranvía de Cuenca y electro-corredores urbanos. Mayor que hospital (~5 ¢) pero menor que minería/exportación (~16 ¢). | Fomenta la sustitución masiva del diésel importado por tracción eléctrica limpia, protegiendo la tarifa del pasaje popular con recarga en horas valle. |

---

## 🛢️ Iniciativa Legislativa Destacada: Reforma Modular por Etapas a los Subsidios en Combustibles

### Denominación del Proyecto de Ley
**"Ley Orgánica para la Eficiencia Energética en el Sector Acuícola, Sinceramiento Gradual del Gas Licuado de Petróleo, Prohibición de Crédito Fiscal de IVA en Combustibles, Capping a 5 Años de Compensaciones Vehiculares, Subsidio Directo a la Pesca Artesanal contra GDOs y Sendero Industrial"**

### Documentos del Proyecto
1. **[L1 Cache Contractual y Resumen Ejecutivo (SUMMARY.md)](./proyectos_ley/subsidios_combustibles/SUMMARY.md)**: Interfaz primaria, parámetros congelados, balance de ahorro fiscal y doble payback.
2. **[Proyecto de Ley Completo (Formato Legislativo Oficial)](./proyectos_ley/subsidios_combustibles/Proyecto_Ley_Subsidios_Combustibles.md)**: Texto legal estructurado con Exposición de Motivos, Considerandos, Articulado Reformatorio, Disposiciones Generales, Transitorias, Derogatorias y Final.
3. **[Memoria Técnica y Económica de Soporte](./proyectos_ley/subsidios_combustibles/Memoria_Tecnica_Economica_Combustibles.md)**: Análisis macroeconómico del déficit estatal 2023-2026, modelado de termodinámica de bombeo camaronero, proyección a 22 años del GLP al 10% anual, reforma tributaria al IVA en combustibles, capping a 5 años del Decreto 308, modelo de pesca artesanal con escudo satelital AIS contra GDOs y sendero industrial.
4. **[Balance de Subsidios y Precios Dinámicos HOY](./proyectos_ley/subsidios_combustibles/Balance_Subsidios_Dinamicos_Hoy.md)**: Radiografía en tiempo real de qué subsidios le restan al Estado, tabla de precios dinámicos y balance comparativo.
5. **[Auditoría Forense de Resistencia CONAIE y Hoja de Ruta Secuencial](./proyectos_ley/subsidios_combustibles/Critica_Forense_Resistencia_CONAIE_y_Hoja_Ruta_Secuencial.md)**: Análisis sin complacencia de detonantes de paros históricos, superación de la trampa del solar rural mediante la reforma eléctrica previa, exclusión de camiones C2 campesinos y hoja de ruta en 3 fases.
6. **[Modelo de Cocina Dual (Inducción 220V) y Red de Micro-Bodegas Rurales](./proyectos_ley/subsidios_combustibles/Modelo_Cocina_Dual_Induccion_y_Red_Depositos_Rurales.md)**: Ingeniería de la placa robusta 220V de 2 quemadores (3,500 W Heavy-Duty), convivencia dual con 1 tanque de gas de respaldo y red de micro-bodegas comunales en poblados para venta a PVP oficial (2.26 USD en Año 1).
7. **[Auditoría Forense de Viabilidad Práctica (Inducción 220V y Micro-Bodegas)](./proyectos_ley/subsidios_combustibles/Auditoria_Viabilidad_Induccion_220V_y_Microbodegas.md)**: Confrontación de la oferta comercial de placas 220V, solución al cableado interno campesino mediante kits preensamblados de CNEL, blindaje legal ARCH-Bomberos y las 6 anclas de viabilidad práctica.
8. **[Matriz de Riesgos Integrales y Estrategias de Mitigación](./proyectos_ley/subsidios_combustibles/Matriz_Riesgos_Integrales_y_Estrategias_Mitigacion.md)**: Mapeo exhaustivo de 14 riesgos sociopolíticos, técnicos, regulatorios y de mercado, con sus protocolos de ingeniería y contingencia.
9. **[Estrategia de Micro-Bodegas Rurales y Protocolo 2FA CUEN](./proyectos_ley/subsidios_combustibles/Estrategia_Red_Microbodegas_GLP_y_Protocolo_2FA_CUEN.md)**: Despliegue territorial de micro-depósitos de 30-100 tanques en cada pueblo a PVP oficial (2.26 USD en Año 1), validación en 2 pasos con medidor eléctrico (consumo $\ge 15\text{ kWh}$, cadencia 20 días, SMS OTP / biométrica dactilar) y modo offline criptográfico Ed25519.
10. **[Parámetros y Configuraciones Técnicas](./config/reformas/subsidios_combustibles.yaml)**: Parámetros estructurados en YAML para simulación y regulación.

---

### Ejes Cardinales de la Propuesta Modular ("Divide y Conquista")

| Eje | Descripción | Impacto |
| :--- | :--- | :--- |
| **Etapa 1: Remoción 100% Diésel Camaronero** | Derogatoria expresa de la excepción de 30 hectáreas (Decreto 675) y cruce con DAEs del SENAE. Diésel a 100% paridad internacional WTI para toda la acuacultura. | Ahorro fiscal inmediato de **75.00 M USD/año**. Cero riesgo de paro social popular y blindaje contra sanciones por dumping/subsidios prohibidos en EE.UU. y la UE. |
| **Etapa 1: Electrificación Camaronera sin Subsidios** | Conexión simplificada (15 días) a media tensión (13.8/34.5 kV) y tarifa industrial por Costo de Servicio (~8.5 ¢/kWh). | La electricidad es un **50.2% más barata que el diésel real** para bombeo y aireación. Fomenta inversión privada en electrificación con Payback de 2.8 a 4 años. |
| **Etapa 2: Sendero Suave del 10% Anual en GLP** | Incremento automático legal del 10% compuesto cada 1 de enero en el cilindro de 15 kg residencial (1.65 a 1.815 USD en Año 1, 1.996 USD en Año 2). | Ajuste imperceptible para los hogares (+16 centavos/cilindro en Año 1 = 1.3 ¢/mes), desactivando el conflicto social. Convergencia a paridad en 22 años (+11.5M en Año 1 garantizados, +70.2M en Año 5). |
| **Etapa 2: Desmonte Inmediato en GLP Comercial** | Prohibición absoluta de cilindros subsidiados en restaurantes, hoteles, saunas, polleras y calderas (pagan 100% paridad: 13.50 USD/cilindro). | Genera liquidez fiscal inmediata de **180.00 M USD/año** netos desde el Día 1, sin tocar la economía del ama de casa humilde. |
| **Reforma Tributaria IVA en Combustibles (LORTI Art. 66)** | Prohibición taxativa de usar el IVA de combustibles fósiles como crédito fiscal de IVA para ventas. Solo deducible en Impuesto a la Renta. | Captura **135.00 M USD/año** netos para el fisco y erradica el mercado negro de facturas fantasmas, con **cero incremento del precio en surtidor**. |
| **Capping a 5 Años (Decreto 308) y GNV** | Desescalamiento del 20% anual en la compensación de gasolinas Extra/Ecopaís a 84,000 taxis, camionetas rurales y tricimotos, con financiamiento CFN para GNV. | Extingue de forma permanente los **80.00 M USD/año** de subsidio a 5 años sin días de shock traumáticos, protegiendo al sector campesino de discriminaciones. |
| **Pesca Artesanal y Escudo contra GDOs** | 100% de paridad en surtidor marino; compensación en Tarjeta Prepago BanEcuador por zarpe DIRNEA con 1 año de gracia y desescalamiento del 10% anual; crédito CFN para motores 4T EFI; AIS y geocercas satelitales. | Quiebra el arbitraje narco a lanchas *go-fast*; reduce consumo físico 45% con motores 4T; neutraliza extorsiones de GDOs (+50.00 M USD/año ahorrados a término). |
| **Sendero Industrial Gradual (36 Meses)** | Ajuste reglado del 1.5% mensual a diésel y gasolinas de manufactura nacional hasta paridad de importación WTI. | Permite la reconversión a biomasa, vapor eléctrico y GNL/GNC sin quebrar a las industrias (+40.00 M USD/año ahorrados). |
| **Cupo GLP por Medidor (CUEN) y 4 Candados** | Límite protegido de **15 cilindros/año por medidor residencial (CUEN)** (~5.3M de hogares). Excedentes a paridad (13.50 USD). 4 candados: cadencia 20 días, canje 1:1 con SMS de alerta, consumo mínimo de 15 kWh/mes y geocercas GPS. | Cubre el 148% de la cocción familiar; erradica el tráfico de cédulas alquiladas; bloquea el contrabando fronterizo y el desvío comercial (elusión < 2%). |
| **Sendero Suave Diésel Pesado (10% Anual)** | Ajuste del 10% anual compuesto cada 1 de enero en transporte pesado de carga (C2 a C3S3), desacoplado de buses. Cláusula obligatoria de flete al cargador y arancel 0% en neumáticos y repuestos. | Libera **+220.50 M USD en Año 1** (+1,701 M USD a paridad en 6.5 años); nulo impacto en alimentos (1.6 ¢/quintal); neutraliza el veto de FENATRAPE. |
| **Alivio Fiscal Consolidado (Años 1 al 6+)** | Base Modular (+401.51 M Año 1 a +623.00 M Año 6) y Paquete Ampliado con Transporte Pesado (+622.01 M Año 1 a +2,324.00 M Año 6). | Libera de inmediato el **19.75% del déficit PGE en el Año 1**, escalando a **+1,929.90 M en Año 5 (61.27%)** y extinguiendo el **73.78% del déficit total en el Año 6**. |

---

## 💼 Iniciativa Legislativa: Reforma Fiscal, Sustitución de Impuestos al Patrimonio y Racionalización del IVA/GLP

### Denominación del Proyecto de Ley
**"Ley Orgánica de Competitividad Tributaria, Sustitución de Impuestos al Patrimonio y Racionalización de Subsidios"**

### Documentos del Proyecto
1. **[L1 Cache Contractual y Resumen Ejecutivo (SUMMARY.md)](./proyectos_ley/reforma_fiscal_tributaria/SUMMARY.md)**: Interfaz primaria y parámetros críticos del proyecto fiscal bajo la doctrina Kronos.
2. **[Proyecto de Ley Completo (Formato Legislativo Oficial)](./proyectos_ley/reforma_fiscal_tributaria/Proyecto_Ley_Reforma_Fiscal_Tributaria.md)**: Texto legal estructurado con Exposición de Motivos, Considerandos, Articulado Reformatorio (LRTI, COOTAD, GLP, CNT S.A.), Disposiciones Generales, Transitorias, Derogatorias y Final.
3. **[Memoria Técnica y Económica de Soporte](./proyectos_ley/reforma_fiscal_tributaria/Memoria_Tecnica_Economica.md)**: Análisis cuantitativo de contracción comercial por IVA 15% vs 12%, sustitución de Patente/1.5 por mil por Sobretasa al IR, curva de escalamiento del GLP al 10% anual, cupos biométricos de frontera y matriz de equilibrio macrofiscal.
4. **[Parámetros y Configuraciones Técnicas](./config/reformas/reforma_fiscal_tributaria.yaml)**: Parámetros estructurados en YAML para simulación y balance fiscal.

### Ejes Cardinales de la Propuesta Fiscal

| Eje | Descripción | Impacto |
| :--- | :--- | :--- |
| **Retorno del IVA del 15% al 12%** | Disminución de 3 puntos porcentuales de la tarifa general de IVA para inyectar liquidez directa al comercio y hogares. | Revierte la recesión comercial (-3.5% en Quito, -4.4% en Guayaquil, -18.7% autos), reactiva la demanda y expande la base de Impuesto a la Renta. |
| **Derogatoria de Patente y 1.5 por Mil** | Eliminación de los impuestos patrimoniales a los activos y capital de trabajo en el COOTAD. Cero utilidad = Cero impuesto municipal. | Elimina la asfixia fiscal a empresas en años de pérdidas y startups en fase de inversión. |
| **Sobretasa Municipal sobre Renta Neta (SM-IR)** | Creación de una sobretasa de hasta el 1.5% calculada exclusivamente sobre la Renta Neta Imponible del SRI, prorrateada por ventas y nómina local. | Garantiza neutralidad fiscal a los 221 municipios (~490 M USD/año) sin requerir transferencias del Presupuesto Central (Art. 271 CRE). |
| **Fiscalización Concurrente Antievasión GAD-SRI** | Los municipios auditan informalidad y facturación territorial, recibiendo el 30% de la recaudación recuperada por evasión local. | Convierte a los 221 municipios en aliados activos del SRI para combatir la evasión del Impuesto a la Renta. |
| **Escalamiento GLP 10% Anual y Cupos Biométricos** | Incremento del 10% anual compuesto al precio del cilindro + cupos estrictos en frontera (1 cilindro/mes por persona o 1 cada 35-40 días por hogar). | Corta 120 M USD de contrabando hacia Perú/Colombia y 280 M USD de desvío comercial de inmediato, protegiendo a las familias vulnerables. |
| **Fondo de Infraestructura de Gas (Margen 10%)** | Recargo del 10% post-paridad de importación destinado a un Fideicomiso Mercantil para renovación de cilindros y redes de gas natural. | Asegura la autosuficiencia operativa permanente del sector de hidrocarburos sin subsidios del PGE. |
| **Focalización Quirúrgica Devolución IVA** | 100% de devolución preservada a personas con discapacidad; tercera edad restringida a ingresos <2 SBU y canasta exclusiva de comida y medicinas. | Erradica el mercado negro de facturas ajenas y ahorra 240 M USD/año al SRI cumpliendo la jurisprudencia de la Corte Constitucional. |
| **Transformación de CNT EP a CNT S.A.** | Transformación a Sociedad Anónima privada regida por Ley de Compañías y Código del Trabajo ordinario (Modelo Banco del Pacífico). | Despolitiza la empresa, la excluye de compras SERCOP, anula contratos colectivos abusivos y genera 250 M USD/año en dividendos limpios. |

---

## 🏛️ Trámite Constitucional y Parlamentario

Este proyecto ha sido redactado observando las normas de la técnica legislativa de la **Asamblea Nacional de la República del Ecuador** y los preceptos de la **Constitución de la República (Arts. 133, 285, 286, 313, 314 y 315)** y de la **Ley Orgánica de la Función Legislativa (LOFL)**:
- Requiere trámite de **Ley Orgánica**.
- Calificación por el Consejo de Administración Legislativa (CAL).
- Tratamiento en la Comisión Especializada Permanente de Desarrollo Económico, Productivo y la Microempresa.
- Dos debates en el Pleno de la Asamblea Nacional.

---

## 🤖 Doctrina y Gobernanza de Agentes IA

El desarrollo, modelado cuantitativo y redacción técnica en este repositorio se rigen obligatoriamente bajo los **12 Mandamientos Inviolables de Ejecución del Sistema de Mesa de Mejoras a Largo Plazo (Olimpo)**:
- **Documento Maestro:** [`AGENTS.md`](./AGENTS.md)
- **Módulo de Configuración y Prompts:** Directorio [`config/agentes/`](./config/agentes/)
  - [`doctrina.yaml`](./config/agentes/doctrina.yaml): Especificación estructurada y reglas de validación.
  - [`system_prompt_base.md`](./config/agentes/system_prompt_base.md): System prompt maestro para subagentes.
  - [`SUMMARY_TEMPLATE.md`](./config/agentes/SUMMARY_TEMPLATE.md): Plantilla estándar obligatoria L1 Cache (`SUMMARY.md`).
  - [`HISTORICO_HEADER_TEMPLATE.md`](./config/agentes/HISTORICO_HEADER_TEMPLATE.md): Plantilla forense para carpetas `historico/`.

