# ⚙️ Configuraciones del Proyecto Reformas Ecuador

Este directorio centraliza todos los parámetros técnicos, macroeconómicos, regulatorios y tarifarios que sustentan los proyectos de ley, memorias técnicas y modelos de simulación del repositorio.

---

## 📂 Estructura del Directorio

```text
config/
├── README.md                                # Esta guía de documentación y uso
├── general.yaml                             # Metadatos del proyecto, entidades e instituciones reguladoras
├── agentes/                                 # Doctrina mandatoria, prompts y plantillas operativas de agentes
│   ├── README.md                            # Guía y resumen de los 12 mandamientos inviolables
│   ├── doctrina.yaml                        # Especificaciones estructuradas y reglas de validación
│   ├── system_prompt_base.md                # Prompt de sistema maestro para inyección en agentes
│   ├── SUMMARY_TEMPLATE.md                  # Plantilla mandatoria de SUMMARY.md (L1 Cache)
│   └── HISTORICO_HEADER_TEMPLATE.md         # Plantilla de cabecera forense para carpeta historico/
├── schemas/                                 # Esquemas de validación (JSON Schema)
│   └── reforma_electrica.schema.json        # Esquema de validación para parámetros de la reforma eléctrica
└── reformas/                                # Configuraciones específicas por cada iniciativa de ley
    └── subsidios_electricos.yaml            # Parámetros, umbrales, tarifas y constantes de la reforma eléctrica
```

---

## 📋 Archivos Principales

### 1. `general.yaml`
Contiene la configuración global del repositorio:
- **Metadatos del Proyecto:** Nombre, versión, país objetivo (`EC`), moneda oficial (`USD`), y marco legislativo (`Constitución del Ecuador`, `LOFL`).
- **Instituciones Clave:** Mapeo de entidades gubernamentales, técnicas y financieras vinculadas (Asamblea Nacional, ARCONEL, CENACE, CELEC EP, Distribuidoras, CFN, BanEcuador).
- **Iniciativas Activas:** Registro de proyectos de ley en desarrollo y su estado legislativo.

### 2. `reformas/subsidios_electricos.yaml`
Define los valores cuantitativos y reglas del Proyecto de Ley Reformatoria a la LOSPEE:
- **Umbrales de Consumo Preferente:**
  - Residencial Sierra / Costa / Amazonía (250 kWh/mes base, hasta 300–320 kWh/mes en temporada cálida).
  - Soberanía Alimentaria Nivel 1 (Tiendas y micromercados: 500 kWh/mes).
  - Soberanía Alimentaria Nivel 2 (Panaderías artesanales con obrador y carnicerías: 800 kWh/mes).
- **Estructura Tarifaria y Piso Mínimo:** Pliegos base, componentes de tarifa a costo real pleno ($T_{\text{real}}$), y fórmula de salvaguarda financiera para distribuidoras.
- **Bloques Horarios (Time-of-Use - TOU):** Franjas valle, llana y pico (18:00 a 22:00).
- **Mecanismos de Contingencia y Mitigación:** Factor de Contingencia Climática ($FCC$), bonificación de ahorro (descuento del 100% del $FCC$ al reducir $\ge 10\%$).
- **Transición Productiva Escalonada:** Retiro gradual de subsidio a industrias en 3 trimestres (33% $\rightarrow$ 66% $\rightarrow$ 100%).
- **Infraestructura AMI y Medidores Inteligentes:** Depósito de garantía (Costo $+ 5\%$) y plazos de amortización social (hasta 36 meses).
- **Fondos Especiales:** Fondo de Reinversión y Resiliencia Eléctrica (FERRE).

### 3. `schemas/reforma_electrica.schema.json`
Esquema formal JSON Schema (Draft 7/2020-12 compatible) para asegurar que cualquier modificación a los parámetros mantenga integridad referencial, tipos numéricos correctos, rangos válidos y campos obligatorios.

### 4. `agentes/`
Módulo operativo que implementa la **Doctrina Mandatoria de Operación de Agentes** (12 Mandamientos Inviolables del Consorcio Industrial Kronos):
- **[`doctrina.yaml`](./agentes/doctrina.yaml):** Reglas estructuradas para validación programática.
- **[`system_prompt_base.md`](./agentes/system_prompt_base.md):** Directiva base inyectable en subagentes y modelos.
- **[`SUMMARY_TEMPLATE.md`](./agentes/SUMMARY_TEMPLATE.md):** Plantilla de interfaz L1 Cache por subproyecto (Mandamiento 9).
- **[`HISTORICO_HEADER_TEMPLATE.md`](./agentes/HISTORICO_HEADER_TEMPLATE.md):** Cabecera forense obligatoria para archivos en `historico/` (Mandamiento 12).
- Ver también el documento maestro en la raíz: [`AGENTS.md`](../AGENTS.md).

---

## 🛠️ Cómo Agregar una Nueva Reforma

1. Crear un nuevo archivo de configuración en `config/reformas/<nombre_reforma>.yaml`.
2. Registrar la iniciativa en la sección `iniciativas_activas` de `config/general.yaml`.
3. (Opcional pero recomendado) Diseñar su respectivo esquema de validación en `config/schemas/<nombre_reforma>.schema.json`.
