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
| **Soberanía Alimentaria (500 kWh y 800 kWh)** | Asignación de energía más barata hasta **500 kWh/mes** para tiendas de barrio/micromercados y hasta **800 kWh/mes** para panaderías artesanales con obrador electromecánico y carnicerías. Excedente a **costo real**. | Protege el precio del pan de batalla y alimentos esenciales al cubrir el 85-100% de la carga de amasadoras, batidoras y frío continuo. Reconversión a equipos inverter. |
| **Red Pública Integral de Salud (Hospitales Públicos)** | Asignación prioritaria de energía de menor costo de generación a hospitales de especialidades, generales y centros 24h del MSP, IESS, ISSFA, ISSPOL. | Protege áreas críticas (UCI, quirófanos, neonatología y vacunas). **Cero subsidio interno:** las entidades de salud pagan obligatoriamente sus planillas sin deudas. |
| **Educación Pública Fiscal (Escuelas y Colegios)** | Asignación prioritaria de energía barata a ~12,400 planteles educativos fiscales. Curva de consumo diurno sin afectación al pico nocturno. | Garantiza iluminación, computación y bombeo de agua en escuelas. Pago obligatorio presupuestado por el Ministerio de Educación con débito MEF. |
| **Racionalización Subsidio 3ra Edad (Adultos Mayores)** | 50% de descuento restringido estrictamente hasta **50 kWh/mes** (~$2.35 USD/mes), 51-250 kWh/mes a tarifa familiar ordinaria y >250 kWh/mes a costo real pleno. **1 solo medidor a nivel nacional por cédula**. | Erradica el fraude de registrar mansiones, saunas y piscinas a nombre de abuelos. Ahorro fiscal de **$45 M USD/año** con bloqueo unificado en ARCONEL y depuración mensual del Registro Civil. |
| **Cinco Vías de Retiro de Subsidios Regresivos** | Exclusión de segundas residencias/playa (+35M), gran minería a LRMC (+120M), cargadores de autos de lujo >3.7 kW (+18M), macro-fraude agroindustrial/cripto (+150-220M) e infraestructura privada (+25M). | Recupera **$348 a $418 M USD/año adicionales** de sectores de alta capacidad de pago con **cero impacto en hogares vulnerables**. |
| **Erradicación de Subsidios Cruzados Intersectoriales** | Prohibición absoluta de sobretasas a la industria para subsidiar otros consumos. Regulación pura por Costo de Servicio (*Cost-of-Service*). | Devuelve competitividad a la manufactura ecuatoriana. El bloque residencial protegido **se autofinancia con hidroeléctricas amortizadas del Estado** (9.5¢ vs 3.5¢ de costo). |
| **Régimen Especial Galápagos (Arts. 258 y 396 CRE)** | Eólica/solar local hasta 250 kWh/mes a residentes. Tarifa a **costo real insular pleno (35-42 ¢USD/kWh)** a hoteles de lujo, cruceros y turismo. | Principio Contaminador-Pagador. El Payback solar+BESS privado para hoteles cae a **<2 años**, logrando Galápagos Cero Fósiles sin subsidios ni gasto público. |
| **Suficiencia y Balance Energético ("¿Nos alcanza?")** | Demanda protegida (hogares + comida + hospitales + escuelas): **729.5 GWh/mes** (8,754 GWh/año). Oferta hidro en peor mes histórico: **1,150 GWh/mes**. | **¡Sí alcanza en volumen (157.6%)!** La hidroeléctrica base cubre holgadamente la demanda prioritaria en sequía. El problema del país es la potencia en pico (18:00 a 22:00). |
| **Seis Optimizaciones de Ingeniería Estructural** | Ciclo Combinado Termogas Machala (+150 MW sin más gas), Interconexión 500 kV Perú (1,000 MW), Flare to Power privado (350-450 MW) y Compensación Reactiva CNEL (+150 MW útiles). | Recupera capacidad de red oculta, erradica apagones en horas pico y reduce el costo de contingencia sin sobreendeudamiento estatal. |
| **Paridad de Red, Techo Solar y Baterías BESS** | Tarifa real plena (~18 ¢USD/kWh) y tarifas horarias (Time of Use). Payback solar **3.5 años** y combo Solar+BESS **4.5 años**. **Fast-Track (15 días)** y **Net Metering 1 a 1**. | Desata inversión masiva en paneles solares y baterías BESS para industrias (arbitraje tarifario: cargar de día y descargar de 18:00 a 22:00 en pico). |
| **Premio al Ahorro en Sequía** | Exoneración del 100% del Factor de Contingencia ($FCC$) a hogares y comercios que reduzcan su consumo mensual en al menos un **10%** en estiaje. | Incentiva el consumo responsable y convierte a la ciudadanía en aliada activa contra los apagones. |
| **Transición Anti-Inflacionaria (12 meses)** | Retiro escalonado del subsidio industrial en 3 trimestres (33% -> 66% -> 100%) respaldado por líneas de **Crédito Verde (CFN/BanEcuador)** para autogeneración y BESS. | Permite que las industrias instalen paneles solares y baterías antes de recibir el impacto tarifario completo, mitigando la inflación en productos finales. |
| **Sinergia Hidro-Solar en Sequía** | La radiación solar máxima coincide con el estiaje andino. La energía solar diurna en techos **ahorra agua en las represas para turbinar de noche**. | Reduce drásticamente la quema de diésel térmico y las importaciones caras, bajando el costo de contingencia. |
| **Tarifas Horarias Dinámicas (TOU)** | Bloques horarios diferenciados: **Valle** (noche/sol diurno a bajo costo), **Llano** y **Pico** (18:00 a 22:00 a costo marginal térmico). | Incentiva el desplazamiento de carga (amasado nocturno en panaderías, recarga de baterías BESS e industrias), aplanando el pico nacional. |
| **Medidores Inteligentes (AMI) y Garantía (Costo + 10%)** | Principio de no gratuidad con derogatoria expresa: Depósito de garantía = **Costo del medidor + 10%**, financiado en la planilla hasta a 36 meses sin intereses (~$1.80 USD/mes). | Erradica tomas clandestinas, fondea stock permanente, absorbe costo de crédito y siniestros por rayos, y es 100% reembolsable. |
| **Pronto Pago (2%) y Margen del 10%** | Descuento del **2% en planilla** por pago en los primeros 5 días o débito automático. Prohibición de operar a pérdida (margen mínimo regulado del 10%). | Acelera la liquidez para pagar generación y combustibles, erradicando costos de mora y cortes. Asegura reinversión continua. |
| **Protocolo Coercitivo contra Deudas Públicas (4 Vías)** | Retención forzosa de tasas de basura/bomberos (>60 días), corte quirúrgico remoto a oficinas burocráticas (>30 días) y débito automático en MEF/BCE, con destitución de autoridades morosas. | La empresa eléctrica **no se queda con deudas incobrables de municipios ni ministerios**. Protege agua potable y quirófanos pero asfixia la morosidad burocrática. |
| **Fondo de Reinversión (FERRE) y Rubro de 1 Centavo** | Rubro de resiliencia de hasta **$0.01 USD/kWh** genera **$190 a $280 M USD/año** intangibles para baterías BESS y mantenimiento mayor. | Resuelve de raíz los problemas del sistema: acaba con los apagones en horas pico mediante acumulación energética a gran escala. |

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

