# Reformas Ecuador 🇪🇨

Repositorio de iniciativas legislativas, proyectos de ley orgánicos y propuestas de política pública orientadas a la modernización institucional, la sostenibilidad económica y la equidad social en la República del Ecuador.

---

## ⚡ Iniciativa Legislativa Destacada: Reforma al Régimen Tarifario y Subsidios Eléctricos

### Denominación del Proyecto de Ley
**"Ley Orgánica Reformatoria a la Ley Orgánica del Servicio Público de Energía Eléctrica (LOSPEE) para la Asignación Prioritaria de Energía de Menor Costo, Focalización Tarifaria Equitativa y Sostenibilidad Financiera ante Contingencias Climáticas"**

### Documentos del Proyecto
1. **[L1 Cache Contractual y Resumen Ejecutivo (SUMMARY.md)](./proyectos_ley/subsidios_electricos/SUMMARY.md)**: Interfaz primaria y parámetros críticos del proyecto bajo la doctrina Kronos.
2. **[Proyecto de Ley Completo (Formato Legislativo Oficial)](./proyectos_ley/subsidios_electricos/Proyecto_Ley_Subsidios_Electricos_Ecuador.md)**: Texto legal estructurado con Exposición de Motivos, Considerandos, Articulado Reformatorio, Disposiciones Generales, Transitorias, Derogatorias y Final.
3. **[Memoria Técnica y Económica de Soporte](./proyectos_ley/subsidios_electricos/Memoria_Tecnica_Economica.md)**: Análisis cuantitativo de demanda, modelado de los umbrales de 250 kWh, 500 kWh y 800 kWh, regla de despacho por orden de mérito regional, tarifas horarias TOU, formulación del $FCC$, gobernanza del FERRE y régimen de medidores con garantía (Costo + 5%).
4. **[Auditoría de Viabilidad Política y Optimización del Sistema Eléctrico](./proyectos_ley/subsidios_electricos/Auditoria_Politica_y_Optimizacion_Electrica.md)**: Análisis de realismo político y límites constitucionales sobre mecheros petroleros, autonomía municipal en cobranzas, sindicatos de CNEL, hidroeléctricas de bombeo, solares flotantes y el modelo de luz prepago digital.
5. **[Parámetros y Configuraciones Técnicas](./config/reformas/subsidios_electricos.yaml)**: Parámetros estructurados en YAML para simulación y regulación (umbrales, costos, tarifas horarias TOU, balance nacional y fondo FERRE; ver guía en [`config/README.md`](./config/README.md)).

---

### Ejes Cardinales de la Propuesta

| Eje | Descripción | Impacto |
| :--- | :--- | :--- |
| **Hogares, Criterio Bioclimático y Elasticidad** | Asignación de energía barata hasta **250 kWh/mes** en Sierra y hasta **300 kWh/mes** en meses cálidos en Costa/Amazonía. Excedente a **costo real + FCC**. | Activa la elasticidad de la demanda: las familias sustituyen aire acondicionado (1.200 W) por ventilador (60 W), ahorrando un 95% de energía y descongestionando la red en sequía. |
| **Piso Tarifario Mínimo Legal** | La tarifa preferente resultante tiene como límite inferior irreductible el **pliego tarifario regulado actual**. | Protege la estabilidad financiera de las 20 empresas eléctricas distribuidoras (CNEL, EEQ, etc.), impidiendo descalces de ingresos. |
| **Soberanía Alimentaria y Agroindustria Interna** | Asignación de energía más barata hasta **500 kWh/mes** (tiendas), **800 kWh/mes** (panaderías artesanales) y tarifa base eficiente (~7.5 ¢/kWh) a **agroindustria de consumo nacional** (molinos de harina/trigo, arroz, balanceado y lácteos básicos). Agroexportación y minería pagan **100% costo real**. | Protege el precio del pan de batalla, arroz, pollo, huevos y leche contra la inflación en sequías. Filtro forense con DAEs del SENAE: cero energía barata a la exportación. |
| **Agua Potable, Riego Campesino y Fármacos Esenciales** | Asignación de energía base hidroeléctrica eficiente a plantas cantonales de agua potable y saneamiento (~38 GWh/mes con débito BCE), juntas de riego comunitarias (~16 GWh/mes) y farmacéuticas de genéricos del CNMB (~11 GWh/mes). | Garantiza el derecho humano al agua (Art. 12 CRE), desactiva la conflictividad agraria campesina y abarata costos de medicamentos genéricos y sueros hospitalarios sin moras. |
| **Red Pública Integral de Salud (Hospitales Públicos)** | Asignación prioritaria de energía de menor costo de generación a hospitales de especialidades, generales y centros 24h del MSP, IESS, ISSFA, ISSPOL. | Protege áreas críticas (UCI, quirófanos, neonatología y vacunas). **Cero subsidio interno:** las entidades de salud pagan obligatoriamente sus planillas sin deudas. |
| **Educación Pública Fiscal (Escuelas y Colegios)** | Asignación prioritaria de energía barata a ~12,400 planteles educativos fiscales. Curva de consumo diurno sin afectación al pico nocturno. | Garantiza iluminación, computación y bombeo de agua en escuelas. Pago obligatorio presupuestado por el Ministerio de Educación con débito MEF. |
| **Racionalización Subsidio 3ra Edad (Adultos Mayores)** | 50% de descuento restringido estrictamente hasta **50 kWh/mes** (~2.35 USD/mes), 51-250 kWh/mes a tarifa familiar ordinaria y >250 kWh/mes a costo real pleno. **1 solo medidor a nivel nacional por cédula**. | Erradica el fraude de registrar mansiones, saunas y piscinas a nombre de abuelos. Ahorro fiscal de **45 M USD/año** con bloqueo unificado en ARCONEL y depuración mensual del Registro Civil. |
| **Mecanismos Quirúrgicos Anti-Regresivos** | Exclusión de segundas residencias/playa (+35M), macro-fraude agroindustrial/cripto (+150-220M) e infraestructura privada (+25M). La minería tributa tarifa real universal y los autos eléctricos se absorben en el tope de 250 kWh. | Recupera **210 a 280 M USD/año adicionales** de evasores y nichos de recreación con **cero impacto en hogares vulnerables**. |
| **Erradicación de Subsidios Cruzados Intersectoriales** | Prohibición absoluta de sobretasas a la industria para subsidiar otros consumos. Regulación pura por Costo de Servicio (*Cost-of-Service*). | Devuelve competitividad a la manufactura ecuatoriana. El bloque residencial protegido **se autofinancia con hidroeléctricas amortizadas del Estado** (9.5¢ vs 3.5¢ de costo). |
| **Régimen Especial Galápagos (Arts. 258 y 396 CRE)** | Eólica/solar local hasta 250 kWh/mes a residentes. Tarifa a **costo real insular pleno (35-42 ¢USD/kWh)** a hoteles de lujo, cruceros y turismo. | Principio Contaminador-Pagador. El Payback solar+BESS privado para hoteles cae a **<2 años**, logrando Galápagos Cero Fósiles sin subsidios ni gasto público. |
| **Suficiencia y Balance Energético ("¿Nos alcanza?")** | Demanda protegida (hogares + comida + agua + riego + salud + educación): **879.5 GWh/mes** (10,554 GWh/año). Oferta hidro en peor mes: **1,150 GWh/mes**. | **¡Sí alcanza en volumen (130.8%)!** La hidroeléctrica base cubre holgadamente toda la demanda prioritaria en sequía con un superávit de +270.5 GWh/mes. El problema del país es la potencia en pico (18:00 a 22:00). |
| **Ahorro Fiscal Trienal (Series 2023-2025)** | Eliminación de subsidios térmicos WTI, déficit tarifario, contratos de barcazas y fraude: Ahorro de **1,982 M USD (2023)**, **3,535 M USD (2024)** y **2,925 M USD (2025)**. | Libera entre **2,605 y 3,575 M USD/año** (Promedio: **3,090 M USD/año** = 2.7% - 3.4% del PIB), eliminando hasta el 78% del déficit presupuestario general del Estado. |
| **Seis Optimizaciones de Ingeniería Estructural** | Ciclo Combinado Termogas Machala (+150 MW sin más gas), Interconexión 500 kV Perú (1,000 MW), Flare to Power privado (350-450 MW) y Compensación Reactiva CNEL (+150 MW útiles). | Recupera capacidad de red oculta, erradica apagones en horas pico y reduce el costo de contingencia sin sobreendeudamiento estatal. |
| **Paridad de Red, Net Billing 70/30 y Baterías BESS** | Tarifa real plena (~18 ¢USD/kWh), **Net Billing Asimétrico 70/30** (retención del 30% para pérdidas, peajes y FERRE) y 100% de reconocimiento en pico para BESS. Payback solar **3.5 años** y BESS **4.5 años**. **Fast-Track (15 días)** hasta 2,000 kWp. | Desata la inyección solar de todo el sistema industrial al SNI para ahorrar agua diurna en embalses, y descarga de baterías BESS en horas pico. |
| **Premio al Ahorro en Sequía** | Exoneración del 100% del Factor de Contingencia (FCC) a hogares y comercios que reduzcan su consumo mensual en al menos un **10%** en estiaje. | Incentiva el consumo responsable y convierte a la ciudadanía en aliada activa contra los apagones. |
| **Transición Anti-Inflacionaria (12 meses)** | Retiro escalonado del subsidio industrial en 3 trimestres (33% -> 66% -> 100%) respaldado por líneas de **Crédito Verde (CFN/BanEcuador)** para autogeneración y BESS. | Permite que las industrias instalen paneles solares y baterías antes de recibir el impacto tarifario completo, mitigando la inflación en productos finales. |
| **Sinergia Hidro-Solar en Sequía** | La radiación solar máxima coincide con el estiaje andino. La energía solar diurna en techos **ahorra agua en las represas para turbinar de noche**. | Reduce drásticamente la quema de diésel térmico y las importaciones caras, bajando el costo de contingencia. |
| **Tarifas Horarias Dinámicas (TOU)** | Bloques horarios diferenciados: **Valle** (noche/sol diurno a bajo costo), **Llano** y **Pico** (18:00 a 22:00 a costo marginal térmico). | Incentiva el desplazamiento de carga (amasado nocturno en panaderías, recarga de baterías BESS e industrias), aplanando el pico nacional. |
| **Medidores Inteligentes (AMI) y Garantía (Costo + 10%)** | Principio de no gratuidad con derogatoria expresa: Depósito de garantía = **Costo del medidor + 10%**, financiado en la planilla hasta a 36 meses sin intereses (~1.80 USD/mes). | Erradica tomas clandestinas, fondea stock permanente, absorbe costo de crédito y siniestros por rayos, y es 100% reembolsable. |
| **Pronto Pago (2%) y Margen del 10%** | Descuento del **2% en planilla** por pago en los primeros 5 días o débito automático. Prohibición de operar a pérdida (margen mínimo regulado del 10%). | Acelera la liquidez para pagar generación y combustibles, erradicando costos de mora y cortes. Asegura reinversión continua. |
| **Protocolo Coercitivo contra Deudas Públicas (4 Vías)** | Retención forzosa de tasas de basura/bomberos (>60 días), corte quirúrgico remoto a oficinas burocráticas (>30 días) y débito automático en MEF/BCE, con destitución de autoridades morosas. | La empresa eléctrica **no se queda con deudas incobrables de municipios ni ministerios**. Protege agua potable y quirófanos pero asfixia la morosidad burocrática. |
| **Fondo de Reinversión (FERRE) y Rubro de 1 Centavo** | Rubro de resiliencia de hasta **0.01 USD/kWh** genera **190 a 280 M USD/año** intangibles para baterías BESS y mantenimiento mayor. | Resuelve de raíz los problemas del sistema: acaba con los apagones en horas pico mediante acumulación energética a gran escala. |
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
5. **[Parámetros y Configuraciones Técnicas](./config/reformas/subsidios_combustibles.yaml)**: Parámetros estructurados en YAML para simulación y regulación.

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
| **Colchón Contracíclico (5% al 10%) y CFEC** | Margen técnico sobre fórmula de paridad depositado en la Cuenta CFEC del BCE para gasolinas y diésel automotriz. | Absorbe picos y volatilidades externas sin desembolsos del Estado. Garantiza permanentemente un **subsidio estatal neto de 0.00 USD**. |
| **Cupo Telemático de GLP por Medidor (CUEN)** | Límite protegido de **15 cilindros/año por medidor residencial (CUEN)** (~5.3M de hogares). Excedentes a paridad internacional (13.50 USD). Trazabilidad telemática ARCH-SRI en bodegas y camiones repartidores, con CUEN Virtual rural. | Cubre el 148% de la cocción familiar; erradica el tráfico clandestino de cédulas alquiladas; bloquea el contrabando fronterizo y el desvío a comercios. |
| **Alivio Fiscal Consolidado (Años 1 al 5)** | Suma de diésel camaronero, GLP comercial, GLP residencial 10%, reforma tributaria de IVA, capping vehicular, sendero industrial y desescalamiento pesquero. | Libera **+401.51 M USD en el Año 1** (12.75% del déficit PGE), escalando a **+584.22 M USD en el Año 5 (18.55%)**, y superando los **+623.00 M USD en el Año 6+ (19.78%)**. |

---

## 🏛️ Trámite Constitucional y Parlamentario

Este proyecto ha sido redactado observando las normas de la técnica legislativa de la **Asamblea Nacional de la República del Ecuador** y los preceptos de la **Constitución de la República (Arts. 133, 285, 286, 313, 314 y 315)** y de la **Ley Orgánica de la Función Legislativa (LOFL)**:
- Requiere trámite de **Ley Orgánica**.
- Calificación por el Consejo de Administración Legislativa (CAL).
- Tratamiento en la Comisión Especializada Permanente de Desarrollo Económico, Productivo y la Microempresa.
- Dos debates en el Pleno de la Asamblea Nacional.

---

## 🤖 Doctrina y Gobernanza de Agentes IA

El desarrollo, modelado cuantitativo y redacción técnica en este repositorio se rigen obligatoriamente bajo los **12 Mandamientos Inviolables de Ejecución del Consorcio Industrial Kronos**:
- **Documento Maestro:** [`AGENTS.md`](./AGENTS.md)
- **Módulo de Configuración y Prompts:** Directorio [`config/agentes/`](./config/agentes/)
  - [`doctrina.yaml`](./config/agentes/doctrina.yaml): Especificación estructurada y reglas de validación.
  - [`system_prompt_base.md`](./config/agentes/system_prompt_base.md): System prompt maestro para subagentes.
  - [`SUMMARY_TEMPLATE.md`](./config/agentes/SUMMARY_TEMPLATE.md): Plantilla estándar obligatoria L1 Cache (`SUMMARY.md`).
  - [`HISTORICO_HEADER_TEMPLATE.md`](./config/agentes/HISTORICO_HEADER_TEMPLATE.md): Plantilla forense para carpetas `historico/`.

