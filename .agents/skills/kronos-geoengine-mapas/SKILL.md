---
name: kronos-geoengine-mapas
description: >-
  Generador cartográfico forense e interactivo para proyectos hidroeléctricos,
  presas, túneles, viaductos ferroviarios y cuencas territoriales de Kronos.
  Especializado en topografía montañosa andina: snapping obligatorio a cauce real OSM (0.00m),
  verificación de monotonicidad hidráulica descendente, confinamiento de embalses a cañones en 'V',
  cálculo de estaciones batimétricas cada 500m, visores web Leaflet con OpenTopoMap (curvas de nivel)
  y modelos georreferenciados 3D KML con auditoría Red Team integrada.
---

# Kronos GeoEngine: Generador Cartográfico Forense e Interactivo (`kronos-geoengine-mapas`)

## 1. Filosofía de Ingeniería y Mandato Base para Topografía Montañosa

Queda terminantemente prohibido en el ecosistema Kronos presentar mapas con trazas fluviales simplificadas o sintéticas que corten cordilleras, coordenadas nominales aproximadas que coloquen presas sobre laderas montañosas, o basar la visualización exclusivamente en imágenes satelitales planas donde la vegetación selvática oculta cañones, pendientes y fallas estructurales.

En el relieve montañoso de los Andes (valles intramontañosos, cañones en "V" de la Formación Macuchi, batolitos graníticos y gargantas fluviales meándricas), una discrepancia de apenas $100\text{ a }300\text{ metros}$ en coordenadas proyecta una presa sobre una cresta rocosa a $150\text{ m}$ de altura sobre el río, o transfiere la infraestructura a una subcuenca vecina con vector de flujo opuesto.

Este skill automatiza y audita la creación de dos productos cartográficos complementarios de grado de ingeniería:
1. **Visor Web Interactivo HTML (Leaflet.js):** Con relieve topográfico real por curvas de nivel (**OpenTopoMap** como capa base obligatoria), trazado vectorial de la red fluvial real de OpenStreetMap (cientos a miles de puntos GPS), estaciones batimétricas cada 500 metros con calado de agua, polígonos de vasos laterales confinados a cañones, túneles subterráneos y panel HUD con métricas clave.
2. **Archivo Georreferenciado 3D KML (KML 2.2 Estándar):** Compatible con Google Earth Desktop y software GIS profesional para sobrevuelos tridimensionales y verificación altimétrica y de laderas.

---

## 2. Las 5 Reglas Inviolables de Topografía Montañosa

### Regla 1: Snapping Fluvial Obligatorio (Tolerancia 0.00 m al Cauce)
Toda infraestructura civil en contacto con el río (eje de presa, azud sumergible, toma tirolesa/Coanda, desarenador, descarga de casa de máquinas y cola de embalse) **DEBE estar matemáticamente bloqueada (`snapped`) al nodo vectorial exacto del río en OpenStreetMap**.
- Queda prohibido utilizar coordenadas estimadas o nominales de gabinete.
- Si un punto de diseño presenta una desviación $> 20\text{ m}$ respecto a la polilínea del río, el script de batimetría emite una alerta roja y reasigna automáticamente las coordenadas al nodo fluvial más próximo, reportando la distancia corregida.

### Regla 2: Monotonicidad Hidráulica y Anti-Inversión de Flujo
En orografía montañosa, ríos afluentes corren frecuentemente en direcciones cardinales opuestas a la troncal principal (ej. afluentes que corren al Norte para verter en un cañón que discurre al Oeste).
El compilador cartográfico debe verificar de forma estricta que la secuencia hidrológica sea monotónicamente descendente:

$$Z_{\text{cola}} \ge Z_{\text{NAMO}} > Z_{\text{lecho, presa}} > Z_{\text{casa\_maquinas}} \ge Z_{\text{descarga}}$$

A nivel topológico a lo largo de la polilínea del río:

$$\text{idx}_{\text{cola}} < \text{idx}_{\text{presa}} < \text{idx}_{\text{descarga}} \le \text{idx}_{\text{cola\_subsiguiente}}$$

> [!CAUTION]
> Queda terminantemente prohibido colocar una casa de máquinas aguas arriba de su presa o trazar túneles de aducción cruzando divisorias hacia valles con cotas incompatibles (salto negativo).

### Regla 3: Extracción Topográfica Real del Espejo de Agua (DEM 30m a Cota NAMO) y Límite Downstream en Eje de Presa
Queda terminantemente prohibido utilizar buffers artificiales rectilíneos o cintas uniformes que sólo hagan al río "parecer más ancho". En topografía montañosa, el espejo de agua de un embalse es una superficie equipotencial horizontal a cota NAMO que inunda todas las quebradas tributarias, terrazas y depresiones conectadas.
- El polígono del espejo de agua debe generarse extrayendo pixel a pixel la máscara de inundación del Modelo Digital de Elevaciones (DEM SRTM 30m o Terrarium) donde $Z \le \text{NAMO}$ conectado hidrológicamente al cauce fluvial.
- **Límite Downstream Estricto en el Eje de Presa (Corte 0.00 m Aguas Abajo):** Un embalse o espejo de agua retiene líquido EXCLUSIVAMENTE aguas arriba del cuerpo de presa. El eje de la presa (plano normal al vector de flujo fluvial en las coordenadas del dique) constituye la frontera física infranqueable del espejo. Queda estrictamente prohibido que el polígono de inundación se fugue o extienda aguas abajo de la represa; todo píxel del DEM o vértice vectorial con proyección downstream del dique debe ser recortado o proyectado rígidamente sobre la corona de la presa (tolerancia downstream = 0.00 m).
- La frontera del polígono debe corresponder con exactitud a la curva de nivel NAMO impresa en OpenTopoMap, permitiendo cuantificar con precisión métrica la superficie anegada en kilómetros cuadrados ($\text{km}^2$), la cota de inundación en cada quebrada afluente y los predios o infraestructuras afectadas.

### Regla 4: Extracción Hidrográfica Multi-Servidor y Consulta por Relación OSM
Para ríos principales de cuencas andinas (ej. Río Guayllabamba, Río Mira, Río Paute, Río Zamora, Río Santiago, Río San Juan), el extractor debe consultar prioritariamente la Relación OSM (`relation["waterway"="river"]["name"="..."]`), incorporando rotación automática de endpoints Overpass (`overpass-api.de`, `overpass.kumi.systems`, `overpass.private.coffee`) para garantizar alta disponibilidad sin bloqueos.

### Regla 5: Capa Base OpenTopoMap Obligatoria para Auditoría de Relieve
Todo visor debe incluir OpenTopoMap como capa base predeterminada con curvas de nivel sombreadas cada $10 - 20\text{ m}$. Esto permite al usuario y al auditor Red Team comprobar visualmente que las presas cierran gargantas orográficas reales y que los embalses se mantienen dentro de las cotas del cañón.

---

## 3. Herramientas Automatizadas del Skill

Ubicadas en `.agents/skills/kronos-geoengine-mapas/scripts/`:

```
.agents/skills/kronos-geoengine-mapas/
├── SKILL.md
└── scripts/
    ├── extract_osm_hydrography.py         # Extractor multi-servidor OSM por Nombre o BBox
    ├── compute_stations_and_bathymetry.py # Batimetría cada 500m + Snapping fluvial obligatorio
    └── build_interactive_map.py            # Compilador paralelo HTML (Leaflet) + KML 3D
```

---

## 4. Flujo de Trabajo Operativo en 5 Fases

```
   FASE 1: EXTRACCIÓN OSM (Overpass Multi-Servidor)
   [Nombre de Río o Bounding Box] ──► extract_osm_hydrography.py ──► rivers.json
                                                                           │
   FASE 2: BATIMETRÍA Y SNAPPING OBLIGATORIO A CAUCE                       │
   [Infraestructura preliminar + cotas] ──► compute_stations... ──► stations_500m.json
                                                    │               infra_snapped.json (0.00m)
   FASE 3: CONFINAMIENTO DE EMBALSE EN CAÑÓN        │                      │
   [Extrusión W(s) sobre nodos reales] ─────────────┴──► project_config.json ◄──┘
                                                               │
   FASE 4: COMPILACIÓN PARALELA HTML + KML                     ▼
   build_interactive_map.py ──┬──► mapa_opentopomap_cascada.html (Leaflet + Curvas de Nivel)
                              └──► cascada_opentopomap_3d.kml (Google Earth 3D)
                                                               │
   FASE 5: AUDITORÍA RED TEAM Y BITÁCORA                       ▼
   [Verificación monotonicidad + Autonomía estiaje] ──► BIT-AUD-XXX en Bitácora Regla 7
```

### Fase 1: Extracción de Hidrografía Real
Por nombre oficial de río (recomendado en cuencas andinas):
```bash
python .agents/skills/kronos-geoengine-mapas/scripts/extract_osm_hydrography.py \
  --main-river "Guayllabamba" \
  --output scratch/guayllabamba_rivers.json
```
O por caja geográfica:
```bash
python .agents/skills/kronos-geoengine-mapas/scripts/extract_osm_hydrography.py \
  --bbox -0.12,-79.05,0.35,-78.30 \
  --main-river "Guayllabamba" \
  --output scratch/guayllabamba_rivers.json
```

### Fase 2: Batimetría y Snapping de Infraestructura
Calcula estaciones cada 500 metros y bloquea matemáticamente las presas al río:
```bash
python .agents/skills/kronos-geoengine-mapas/scripts/compute_stations_and_bathymetry.py \
  --input scratch/guayllabamba_rivers.json \
  --interval 500.0 \
  --cota-start 1648.0 \
  --cota-dam 450.0 \
  --cota-namo 1648.0 \
  --snap-points scratch/infraestructura_propuesta.json \
  --output scratch/stations_500m.json
```

### Fase 3 y 4: Compilación Cartográfica (HTML + KML)
Estructurar `project_config.json` con los nodos bloqueados al cauce y ejecutar el compilador:
```bash
python .agents/skills/kronos-geoengine-mapas/scripts/build_interactive_map.py --config project_config.json
```

---

## 5. Auditoría Red Team y Cumplimiento Normativo Kronos

1. **KaTeX Puro y Aislamiento de Fórmulas (Regla 6):**  
   Queda prohibido usar delimitadores `$` dentro de tablas Markdown. Fórmulas siempre en bloques independientes `$$ ... $$` con unidades en `\text{...}`.
2. **Bitácora Obligatoria de Decisiones y Descartes (Regla 7):**  
   Todo mapa debe documentar explícitamente en su informe la justificación de ubicación de presas, el porqué se descartaron alternativas previas desalineadas con el relieve montañoso (`BIT-AUD-OTM-XX` / `BIT-AUD-OSM-XX`).
3. **Cero Dependencia de Subsidios (Regla 8):**  
   Los proyectos cartografiados deben ser económicamente autosuficientes por generación energética y aprovechamiento de sedimentos.
4. **Formato Financiero (Regla 9):**  
   Valores monetarios siempre en **USD**, indicando moneda local entre paréntesis si aplica.
