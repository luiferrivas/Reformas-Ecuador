"""
Kronos GeoEngine - Script 3: Generador de Mapa Interactivo HTML (Leaflet.js) y Archivo 3D KML
Compila un visor web con OpenTopoMap por defecto, control de capas, HUD Glassmorphism y archivo KML 2.2 georreferenciado.
Soporta:
- Eje Fluvial Principal (OSM) y Estaciones Batimétricas cada 500m
- Embalses Multibrazo / Vasos Laterales con Polígonos Limpios
- Red Vial y Alternativas (Variantes Altas, Bypasses, Tramos Sumergidos, Corredores Fluviales)
- Zonas y Poblados Sumergidos con tirante de inundación
- Mesetas y Nuevas Ciudades de Reasentamiento Definitivo
- Obras Hidráulicas, Presas, Puertos, Malecones y Túneles
"""

import sys
import os
import json
import argparse

def normalize_points(pts):
    if not pts:
        return []
    res = []
    for p in pts:
        if isinstance(p, dict):
            res.append({'lat': float(p.get('lat', p.get('latitude', 0))), 'lon': float(p.get('lon', p.get('lng', p.get('longitude', 0))))})
        elif isinstance(p, (list, tuple)) and len(p) >= 2:
            res.append({'lat': float(p[0]), 'lon': float(p[1])})
    return res

def normalize_ring(pts):
    res = []
    for p in pts:
        if isinstance(p, dict):
            res.append([float(p.get('lat', p.get('latitude', 0))), float(p.get('lon', p.get('lng', p.get('longitude', 0))))])
        elif isinstance(p, (list, tuple)) and len(p) >= 2:
            res.append([float(p[0]), float(p[1])])
    return res

def normalize_polygon(pts):
    if not pts:
        return []
    # If pts is a list of rings: [[p1, p2, ...], [h1, h2, ...]]
    if isinstance(pts[0], (list, tuple)) and len(pts[0]) > 0 and isinstance(pts[0][0], (list, tuple, dict)):
        return [normalize_ring(ring) for ring in pts]
    return normalize_ring(pts)

def generate_html_map(config, main_river, stations, lateral_reservoirs, tunnels, infrastructure, roads, submerged_zones, resettlement_cities, output_html):
    norm_main = normalize_points(main_river)
    
    # Center coordinates
    if stations:
        center_lat = stations[len(stations)//2]['lat']
        center_lon = stations[len(stations)//2]['lon']
    elif norm_main:
        center_lat = norm_main[len(norm_main)//2]['lat']
        center_lon = norm_main[len(norm_main)//2]['lon']
    elif infrastructure:
        center_lat = infrastructure[0]['lat']
        center_lon = infrastructure[0]['lon']
    else:
        center_lat = -3.48
        center_lon = -78.53

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{config.get('title', 'Proyecto Territorial Kronos - Mapa Interactivo')}</title>
  <!-- Leaflet CSS -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      display: flex;
      height: 100vh;
      overflow: hidden;
      background: #0b1120;
      color: #f8fafc;
    }}
    #sidebar {{
      width: 460px;
      background: #1e293b;
      border-right: 1px solid #334155;
      display: flex;
      flex-direction: column;
      z-index: 1000;
      box-shadow: 4px 0 24px rgba(0,0,0,0.6);
      transition: transform 0.3s ease;
    }}
    #sidebar.collapsed {{
      transform: translateX(-460px);
    }}
    #header {{
      padding: 18px 20px;
      background: #0f172a;
      border-bottom: 1px solid #334155;
    }}
    #header h1 {{
      font-size: 1.15rem;
      color: #38bdf8;
      font-weight: 700;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    #header p {{
      font-size: 0.78rem;
      color: #94a3b8;
      line-height: 1.35;
      margin-top: 4px;
    }}
    #content {{
      padding: 16px 20px;
      overflow-y: auto;
      flex: 1;
      font-size: 0.82rem;
      line-height: 1.5;
    }}
    .badge {{
      display: inline-block;
      padding: 2px 8px;
      border-radius: 9999px;
      font-size: 0.68rem;
      font-weight: 600;
      text-transform: uppercase;
      margin-bottom: 6px;
    }}
    .badge-danger {{ background: #ef444422; color: #f87171; border: 1px solid #ef444455; }}
    .badge-success {{ background: #10b98122; color: #34d399; border: 1px solid #10b98155; }}
    .badge-info {{ background: #0284c722; color: #38bdf8; border: 1px solid #0284c755; }}
    .card {{
      background: #0f172a88;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 12px 14px;
      margin-bottom: 14px;
    }}
    .card h3 {{
      font-size: 0.88rem;
      color: #f1f5f9;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .card p {{
      color: #cbd5e1;
      margin-bottom: 6px;
      font-size: 0.78rem;
    }}
    .card ul {{
      padding-left: 18px;
      color: #94a3b8;
      font-size: 0.76rem;
    }}
    .card ul li {{
      margin-bottom: 4px;
    }}
    .stat-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin: 10px 0 14px 0;
    }}
    .stat-box {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 6px;
      padding: 8px 10px;
      text-align: center;
    }}
    .stat-val {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #38bdf8;
    }}
    .stat-lbl {{
      font-size: 0.68rem;
      color: #64748b;
      text-transform: uppercase;
    }}
    #map {{
      flex: 1;
      height: 100%;
      background: #090d16;
    }}
    .legend-item {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 5px;
      font-size: 0.75rem;
      color: #cbd5e1;
    }}
    .legend-color {{
      width: 14px;
      height: 14px;
      border-radius: 3px;
      flex-shrink: 0;
    }}
    #toggle-sidebar {{
      position: absolute;
      top: 16px;
      left: 476px;
      z-index: 1001;
      background: #0f172aee;
      color: #38bdf8;
      border: 1px solid #38bdf855;
      padding: 8px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.8rem;
      font-weight: 600;
      box-shadow: 0 4px 12px rgba(0,0,0,0.5);
      transition: left 0.3s ease;
    }}
    #toggle-sidebar.collapsed {{
      left: 16px;
    }}
    .leaflet-popup-content-wrapper {{
      background: #1e293b;
      color: #f8fafc;
      border-radius: 8px;
      border: 1px solid rgba(56, 189, 248, 0.35);
      box-shadow: 0 8px 25px rgba(0,0,0,0.6);
    }}
    .leaflet-popup-content h4 {{
      margin: 0 0 5px 0;
      color: #38bdf8;
      font-size: 13.5px;
    }}
    .leaflet-popup-content p {{
      margin: 0;
      font-size: 11.5px;
      color: #cbd5e1;
      line-height: 1.45;
    }}
  </style>
</head>
<body>

  <div id="sidebar">
    <div id="header">
      <div class="badge badge-info">{config.get('badge_text', 'KRONOS GEOENGINE')}</div>
      <h1>{config.get('heading', '🏔️ ' + config.get('title', 'Proyecto Territorial'))}</h1>
      <p>{config.get('description', '')}</p>
    </div>

    <div id="content">
      <div class="stat-grid">
"""
    for stat in config.get('stats', []):
        html += f"""        <div class="stat-box">
          <div class="stat-val">{stat.get('val', '')}</div>
          <div class="stat-lbl">{stat.get('label', '')}</div>
        </div>
"""
    html += f"""      </div>

      <div class="card">
        <h3>💧 Espejo de Agua y Red Fluvial</h3>
        <div class="legend-item"><div class="legend-color" style="background:#0284c7;"></div> <span>{config.get('main_river_desc', 'Río Principal (Traza Vectorial OSM)')}</span></div>
"""
    for res in lateral_reservoirs:
        c = res.get('color', '#a855f7')
        v_txt = f" ({res.get('vol_hm3', 0)} hm³)" if res.get('vol_hm3') else ""
        html += f"""        <div class="legend-item"><div class="legend-color" style="background:{c};"></div> <span><strong>{res.get('name', 'Vaso')}</strong>{v_txt}</span></div>\n"""

    if roads:
        html += """        <div class="legend-item"><div class="legend-color" style="background:#10b981; height:4px;"></div> <span>Variantes Viales Altas</span></div>
        <div class="legend-item"><div class="legend-color" style="background:#ef4444; height:3px; border-top:2px dashed #fff;"></div> <span>Vías Antiguas Sumergidas</span></div>
"""
    if tunnels:
        html += """        <div class="legend-item"><div class="legend-color" style="background:#facc15; height:3px; border-top:2px dashed #fff;"></div> <span>Túneles y Conducciones</span></div>\n"""
    
    html += "      </div>\n"

    if submerged_zones:
        html += """      <div class="card">
        <span class="badge badge-danger">Sumergidos Bajo Cota NAMO</span>
        <h3>🚨 Poblados y Zonas Sumergidas</h3>
        <ul>\n"""
        for sz in submerged_zones:
            html += f"""          <li><strong>{sz.get('name', 'Zona')} ({sz.get('alt', 'N/D')} msnm):</strong> Tirante: -{sz.get('depth', 0)} m.</li>\n"""
        html += "        </ul>\n      </div>\n"

    if resettlement_cities:
        html += """      <div class="card">
        <span class="badge badge-success">Reasentamiento Permanente</span>
        <h3>🏙️ Nuevas Ciudades y Mesetas Altas</h3>
        <ul>\n"""
        for rc in resettlement_cities:
            html += f"""          <li><strong>{rc.get('name', 'Ciudad')} ({rc.get('alt', 'N/D')} msnm):</strong> {rc.get('desc', '')}</li>\n"""
        html += "        </ul>\n      </div>\n"

    if infrastructure:
        html += """      <div class="card">
        <span class="badge badge-info">Obras Civiles</span>
        <h3>🏗️ Presas y Puertos</h3>
        <ul>\n"""
        for item in infrastructure:
            html += f"""          <li><strong>{item.get('name', 'Obra')} ({item.get('cota', 'N/D')} msnm):</strong> {item.get('desc', '')}</li>\n"""
        html += "        </ul>\n      </div>\n"

    html += """    </div>
  </div>

  <button id="toggle-sidebar">◀ Ocultar Panel</button>
  <div id="map"></div>

  <!-- Leaflet JS -->
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
  <script>
    const map = L.map('map', {
      center: [""" + f"{center_lat}, {center_lon}" + """],
      zoom: 12,
      minZoom: 8,
      maxZoom: 18
    });

    // 1. OpenTopoMap (Curvas de nivel reales - DEFAULT OBLIGATORIO)
    const openTopo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
      maxZoom: 17,
      attribution: 'Map data: &copy; OpenStreetMap contributors, SRTM | Style: OpenTopoMap'
    }).addTo(map);

    // 2. Google Maps Suite (Relieve, Satélite Híbrido, Satélite y Calles)
    const googleHybrid = L.tileLayer('https://mt{s}.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', {
      subdomains: ['0', '1', '2', '3'],
      maxZoom: 20,
      attribution: '&copy; Google Maps'
    });

    const googleTerrain = L.tileLayer('https://mt{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}', {
      subdomains: ['0', '1', '2', '3'],
      maxZoom: 20,
      attribution: '&copy; Google Maps'
    });

    const googleSat = L.tileLayer('https://mt{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
      subdomains: ['0', '1', '2', '3'],
      maxZoom: 20,
      attribution: '&copy; Google Maps'
    });

    const googleRoad = L.tileLayer('https://mt{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
      subdomains: ['0', '1', '2', '3'],
      maxZoom: 20,
      attribution: '&copy; Google Maps'
    });

    // 3. Esri Suite
    const esriSat = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 19,
      attribution: 'Tiles &copy; Esri'
    });

    const esriTopo = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 19,
      attribution: 'Tiles &copy; Esri'
    });

    // 4. OpenStreetMap y CartoDB Modo Oscuro
    const osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; OpenStreetMap contributors'
    });

    const cartoDark = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
      maxZoom: 19,
      attribution: '&copy; CartoDB &copy; OpenStreetMap'
    });

    // Layer Groups
    const layerMain = L.layerGroup().addTo(map);
    const layerStations = L.layerGroup().addTo(map);
    const layerTunnels = L.layerGroup().addTo(map);
    const layerInfra = L.layerGroup().addTo(map);
    const layerRoads = L.layerGroup().addTo(map);
    const layerSubmerged = L.layerGroup().addTo(map);
    const layerCities = L.layerGroup().addTo(map);

    const overlays = {
      "⚡ Eje Río Principal": layerMain,
      "📍 Estaciones cada 500m": layerStations,
      "🟡 Túneles y Conducciones": layerTunnels,
      "🏗️ Infraestructura y Presas": layerInfra,
      "🛣️ Red Vial y Alternativas": layerRoads,
      "🚨 Poblados Sumergidos": layerSubmerged,
      "🏙️ Ciudades de Reubicación": layerCities
    };
"""
    # Main river
    if norm_main:
        pts_json = json.dumps([[p['lat'], p['lon']] for p in norm_main])
        html += f"""
    const mainRiverPts = {pts_json};
    if (mainRiverPts.length > 0) {{
      L.polyline(mainRiverPts, {{
        color: '#0284c7',
        weight: 6,
        opacity: 0.95
      }}).bindPopup("<h4>🌊 Eje Fluvial Principal</h4><p>{config.get('main_river_desc', 'Cauce principal georreferenciado.')}</p>").addTo(layerMain);
    }}
"""
    # Lateral reservoirs / multi-branch arms
    for idx, res in enumerate(lateral_reservoirs):
        layer_var = f"layerLat_{idx}"
        color = res.get('color', '#a855f7')
        norm_poly = normalize_polygon(res.get('polygon', []))
        norm_stream = normalize_points(res.get('stream_geom', []))
        
        html += f"""
    const {layer_var} = L.layerGroup().addTo(map);
    overlays["🌊 {res.get('name', 'Vaso Lateral')}"] = {layer_var};
"""
        if norm_stream:
            st_json = json.dumps([[p['lat'], p['lon']] for p in norm_stream])
            html += f"""
    L.polyline({st_json}, {{
      color: '{color}',
      weight: 3.5,
      opacity: 0.85
    }}).bindPopup("<h4>{res.get('name', 'Quebrada')} (Eje Fluvial)</h4><p>{res.get('desc', '')}</p>").addTo({layer_var});
"""
        if norm_poly:
            poly_json = json.dumps(norm_poly)
            vol_str = f"<strong>Volumen Útil:</strong> {res.get('vol_hm3', 0)} hm³<br>" if res.get('vol_hm3') else ""
            html += f"""
    L.polygon({poly_json}, {{
      color: '#00e5ff',
      fillColor: '{color}',
      fillOpacity: 0.50,
      weight: 2
    }}).bindPopup("<h4>{res.get('name', 'Vaso')}</h4><p>{vol_str}{res.get('desc', '')}</p>").addTo({layer_var});
"""
        if res.get('dam_coord'):
            dam_c = res.get('dam_coord')
            dam_pt = [dam_c['lat'], dam_c['lon']] if isinstance(dam_c, dict) else [dam_c[0], dam_c[1]]
            html += f"""
    L.marker({json.dumps(dam_pt)}).bindPopup("<h4>{res.get('dam_title', 'Presa Lateral')}</h4><p>{res.get('dam_desc', '')}</p>").addTo(layerInfra);
"""

    # Stations
    if stations:
        html += f"""
    const stationsData = {json.dumps(stations)};
    stationsData.forEach(st => {{
      L.circleMarker([st['lat'], st['lon']], {{
        radius: 4.5,
        fillColor: '#f59e0b',
        color: '#000',
        weight: 1.5,
        fillOpacity: 0.95
      }}).bindPopup(`
        <h4>${{st['pk']}}</h4>
        <p><strong>Distancia acumulada:</strong> ${{st['dist_m']}} m<br>
        <strong>Cota Fondo Lecho:</strong> ${{st['lecho_cota']}} msnm<br>
        <strong>Cota NAMO:</strong> ${{st['namo_cota']}} msnm<br>
        <strong>Calado de Agua:</strong> ${{st['calado_m']}} m</p>
      `).addTo(layerStations);
    }});
"""

    # Tunnels
    for t in tunnels:
        norm_t = normalize_polygon(t.get('coords', []))
        html += f"""
    L.polyline({json.dumps(norm_t)}, {{
      color: '{t.get('color', '#eab308')}',
      weight: 4,
      dashArray: '6, 6',
      opacity: 0.95
    }}).bindPopup("<h4>{t.get('name', 'Túnel')}</h4><p>{t.get('desc', '')}</p>").addTo(layerTunnels);
"""

    # Roads
    for r in roads:
        norm_r = normalize_polygon(r.get('coords', []))
        color = r.get('color', '#10b981')
        dash = ", dashArray: '6, 6'" if 'Sumerg' in r.get('name', '') or 'Fluvial' in r.get('name', '') or 'Túnel' in r.get('name', '') else ""
        weight = 4 if 'Alternativa' in r.get('name', '') or 'Variante' in r.get('name', '') else 3
        html += f"""
    L.polyline({json.dumps(norm_r)}, {{
      color: '{color}',
      weight: {weight}{dash},
      opacity: 0.95
    }}).bindPopup("<h4>{r.get('name', 'Vía')}</h4><p>{r.get('desc', '')}</p>").addTo(layerRoads);
"""

    # Submerged Zones
    for sz in submerged_zones:
        html += f"""
    L.circleMarker([{sz['lat']}, {sz['lon']}], {{
      radius: 7,
      fillColor: '#ef4444',
      color: '#ffffff',
      weight: 1.5,
      fillOpacity: 0.90
    }}).bindPopup("<h4>🚨 {sz.get('name', 'Zona Sumergida')}</h4><p>{sz.get('desc', '')}<br><strong>Cota Terreno:</strong> {sz.get('alt', 'N/D')} msnm<br><strong>Tirante de Inundación:</strong> {sz.get('depth', 'N/D')} m</p>").addTo(layerSubmerged);
"""

    # Resettlement Cities
    for rc in resettlement_cities:
        html += f"""
    L.circleMarker([{rc['lat']}, {rc['lon']}], {{
      radius: 9,
      fillColor: '#10b981',
      color: '#ffffff',
      weight: 2,
      fillOpacity: 0.95
    }}).bindPopup("<h4>🏙️ {rc.get('name', 'Nueva Ciudad')}</h4><p>{rc.get('desc', '')}<br><strong>Altitud:</strong> {rc.get('alt', 'N/D')} msnm</p>").addTo(layerCities);
"""

    # Infrastructure
    for item in infrastructure:
        color = '#eab308' if 'Azud' in item.get('name', '') or 'Blindaje' in item.get('name', '') else ('#0284c7' if 'Puerto' in item.get('name', '') else '#38bdf8')
        html += f"""
    L.circleMarker([{item['lat']}, {item['lon']}], {{
      radius: 8,
      fillColor: '{color}',
      color: '#ffffff',
      weight: 2,
      fillOpacity: 0.95
    }}).bindPopup("<h4>🏗️ {item['name']}</h4><p>{item.get('desc', '')}</p>").addTo(layerInfra);
"""

    html += """
    L.control.layers({
      "🏔️ OpenTopoMap (Curvas de Nivel SRTM)": openTopo,
      "🛰️ Google Satélite Híbrido (Vías y Nombres)": googleHybrid,
      "⛰️ Google Relieve / Terrain (Topografía)": googleTerrain,
      "🛰️ Google Satélite Puro": googleSat,
      "🗺️ Google Carreteras / Roadmap": googleRoad,
      "🛰️ Esri Satélite HD": esriSat,
      "🗺️ Esri Topográfico": esriTopo,
      "🏙️ OpenStreetMap Estándar": osm,
      "🌑 CartoDB Dark Matter (Modo Noche)": cartoDark
    }, overlays, { position: 'topright' }).addTo(map);

    // Botón de alternancia de la barra lateral
    const toggleBtn = document.getElementById('toggle-sidebar');
    const sidebar = document.getElementById('sidebar');
    toggleBtn.addEventListener('click', () => {
      sidebar.classList.toggle('collapsed');
      toggleBtn.classList.toggle('collapsed');
      toggleBtn.textContent = sidebar.classList.contains('collapsed') ? '▶ Mostrar Panel' : '◀ Ocultar Panel';
      setTimeout(() => { map.invalidateSize(); }, 350);
    });
  </script>
</body>
</html>
"""
    os.makedirs(os.path.dirname(os.path.abspath(output_html)), exist_ok=True)
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[GeoEngine] Mapa interactivo HTML generado con éxito en: {output_html}")


def generate_kml_map(config, main_river, stations, lateral_reservoirs, tunnels, infrastructure, roads, submerged_zones, resettlement_cities, output_kml):
    norm_main = normalize_points(main_river)

    kml = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>""" + config.get('title', 'Proyecto Territorial Kronos') + """</name>
    <description><![CDATA[""" + config.get('description', '') + """]]></description>

    <Style id="damStyle">
      <IconStyle>
        <scale>1.3</scale>
        <Icon><href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle_highlight.png</href></Icon>
        <color>ff0000ff</color>
      </IconStyle>
    </Style>
    <Style id="stationStyle">
      <IconStyle>
        <scale>0.8</scale>
        <Icon><href>http://maps.google.com/mapfiles/kml/shapes/donut.png</href></Icon>
        <color>ff00aaff</color>
      </IconStyle>
    </Style>
    <Style id="cityStyle">
      <IconStyle>
        <scale>1.2</scale>
        <Icon><href>http://maps.google.com/mapfiles/kml/shapes/homegardenbusiness.png</href></Icon>
        <color>ff55ff55</color>
      </IconStyle>
    </Style>
    <Style id="submergedStyle">
      <IconStyle>
        <scale>1.1</scale>
        <Icon><href>http://maps.google.com/mapfiles/kml/shapes/caution.png</href></Icon>
        <color>ff0000ff</color>
      </IconStyle>
    </Style>
    <Style id="riverMain">
      <LineStyle><color>ffffaa00</color><width>6</width></LineStyle>
    </Style>
    <Style id="tunnelStyle">
      <LineStyle><color>ff00ffff</color><width>4</width></LineStyle>
    </Style>
    <Style id="roadStyle">
      <LineStyle><color>ff00ff00</color><width>4</width></LineStyle>
    </Style>
    <Style id="submergedRoadStyle">
      <LineStyle><color>ff0000ff</color><width>3</width></LineStyle>
    </Style>
    <Style id="waterPolyStyle">
      <PolyStyle><color>99ef9010</color><outline>1</outline></PolyStyle>
      <LineStyle><color>ff00e5ff</color><width>2</width></LineStyle>
    </Style>

    <Folder>
      <name>1. Obras Principales e Infraestructura</name>
"""
    for item in infrastructure:
        cota = item.get('cota', 832)
        kml += f"""      <Placemark>
        <name>{item['name']}</name>
        <description><![CDATA[{item.get('desc', '')}]]></description>
        <styleUrl>#damStyle</styleUrl>
        <Point><coordinates>{item['lon']},{item['lat']},{cota}</coordinates></Point>
      </Placemark>
"""
    kml += """    </Folder>

    <Folder>
      <name>2. Traza Fluvial Principal</name>
"""
    if norm_main:
        kml += """      <Placemark>
        <name>Eje del Río Principal</name>
        <styleUrl>#riverMain</styleUrl>
        <LineString>
          <tessellate>1</tessellate>
          <coordinates>
"""
        for p in norm_main:
            kml += f"            {p['lon']:.6f},{p['lat']:.6f},0\n"
        kml += """          </coordinates>
        </LineString>
      </Placemark>
"""
    kml += """    </Folder>

    <Folder>
      <name>3. Quebradas y Reservorios Laterales</name>
"""
    for res in lateral_reservoirs:
        norm_poly = normalize_polygon(res.get('polygon', []))
        if not norm_poly:
            continue
        vol_str = f"Volumen Útil: {res.get('vol_hm3', 0)} hm3 | " if res.get('vol_hm3') else ""
        
        # Determine if polygon has holes (list of rings)
        if isinstance(norm_poly[0], list) and len(norm_poly[0]) > 0 and isinstance(norm_poly[0][0], list):
            outer = norm_poly[0]
            inners = norm_poly[1:]
        else:
            outer = norm_poly
            inners = []

        outer_coords_str = "".join([f"                {p[1]:.6f},{p[0]:.6f},828\n" for p in outer])
        
        inners_kml = ""
        for hole in inners:
            hole_coords_str = "".join([f"                {p[1]:.6f},{p[0]:.6f},828\n" for p in hole])
            inners_kml += f"""          <innerBoundaryIs>
            <LinearRing>
              <coordinates>
{hole_coords_str}              </coordinates>
            </LinearRing>
          </innerBoundaryIs>
"""

        kml += f"""      <Placemark>
        <name>{res.get('name', 'Vaso Lateral')}</name>
        <description><![CDATA[{vol_str}{res.get('desc', '')}]]></description>
        <styleUrl>#waterPolyStyle</styleUrl>
        <Polygon>
          <extrude>1</extrude>
          <altitudeMode>relativeToGround</altitudeMode>
          <outerBoundaryIs>
            <LinearRing>
              <coordinates>
{outer_coords_str}              </coordinates>
            </LinearRing>
          </outerBoundaryIs>
{inners_kml}        </Polygon>
      </Placemark>
"""
    kml += """    </Folder>

    <Folder>
      <name>4. Conducciones y Túneles</name>
"""
    for t in tunnels:
        norm_t = normalize_polygon(t.get('coords', []))
        kml += f"""      <Placemark>
        <name>{t.get('name', 'Túnel')}</name>
        <description><![CDATA[{t.get('desc', '')}]]></description>
        <styleUrl>#tunnelStyle</styleUrl>
        <LineString>
          <tessellate>1</tessellate>
          <coordinates>
"""
        for c in norm_t:
            kml += f"            {c[1]:.6f},{c[0]:.6f},0\n"
        kml += """          </coordinates>
        </LineString>
      </Placemark>
"""
    kml += """    </Folder>

    <Folder>
      <name>5. Estaciones Batimétricas Cada 500m</name>
"""
    for st in stations:
        kml += f"""      <Placemark>
        <name>{st['pk']}</name>
        <description><![CDATA[Distancia acumulada: {st['dist_m']} m<br>Cota Lecho: {st['lecho_cota']} msnm<br>Cota NAMO: {st['namo_cota']} msnm<br>Calado: {st['calado_m']} m]]></description>
        <styleUrl>#stationStyle</styleUrl>
        <Point><coordinates>{st['lon']:.6f},{st['lat']:.6f},{st['namo_cota']}</coordinates></Point>
      </Placemark>
"""
    kml += """    </Folder>

    <Folder>
      <name>6. Red Vial y Alternativas de Conectividad</name>
"""
    for r in roads:
        norm_r = normalize_polygon(r.get('coords', []))
        s_style = '#submergedRoadStyle' if 'Sumerg' in r.get('name', '') else '#roadStyle'
        kml += f"""      <Placemark>
        <name>{r.get('name', 'Vía')}</name>
        <description><![CDATA[{r.get('desc', '')}]]></description>
        <styleUrl>{s_style}</styleUrl>
        <LineString>
          <tessellate>1</tessellate>
          <coordinates>
"""
        for c in norm_r:
            kml += f"            {c[1]:.6f},{c[0]:.6f},830\n"
        kml += """          </coordinates>
        </LineString>
      </Placemark>
"""
    kml += """    </Folder>

    <Folder>
      <name>7. Zonas y Poblados Sumergidos</name>
"""
    for sz in submerged_zones:
        kml += f"""      <Placemark>
        <name>{sz.get('name', 'Poblado')}</name>
        <description><![CDATA[{sz.get('desc', '')}<br><b>Cota:</b> {sz.get('alt', 'N/D')} msnm<br><b>Tirante:</b> {sz.get('depth', 'N/D')} m]]></description>
        <styleUrl>#submergedStyle</styleUrl>
        <Point><coordinates>{sz['lon']},{sz['lat']},{sz.get('alt', 800)}</coordinates></Point>
      </Placemark>
"""
    kml += """    </Folder>

    <Folder>
      <name>8. Nuevas Ciudades de Reasentamiento</name>
"""
    for rc in resettlement_cities:
        kml += f"""      <Placemark>
        <name>{rc.get('name', 'Ciudad')}</name>
        <description><![CDATA[{rc.get('desc', '')}<br><b>Altitud:</b> {rc.get('alt', 'N/D')} msnm]]></description>
        <styleUrl>#cityStyle</styleUrl>
        <Point><coordinates>{rc['lon']},{rc['lat']},{rc.get('alt', 900)}</coordinates></Point>
      </Placemark>
"""
    kml += """    </Folder>
  </Document>
</kml>
"""
    os.makedirs(os.path.dirname(os.path.abspath(output_kml)), exist_ok=True)
    with open(output_kml, "w", encoding="utf-8") as f:
        f.write(kml)
    print(f"[GeoEngine] Archivo KML 3D generado con éxito en: {output_kml}")


def main():
    parser = argparse.ArgumentParser(description="Compilador Cartográfico Kronos GeoEngine")
    parser.add_argument("--config", required=True, help="Archivo JSON de configuración de proyecto")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    # Load dependencies
    main_river = cfg.get('main_river_geom', [])
    stations = cfg.get('stations', [])
    lateral_reservoirs = cfg.get('lateral_reservoirs', [])
    tunnels = cfg.get('tunnels', [])
    infrastructure = cfg.get('infrastructure', [])
    roads = cfg.get('roads', [])
    submerged_zones = cfg.get('submerged_zones', [])
    resettlement_cities = cfg.get('resettlement_cities', [])

    out_html = cfg.get('output_html', 'mapa_interactivo.html')
    out_kml = cfg.get('output_kml', 'mapa_georreferenciado.kml')

    generate_html_map(cfg, main_river, stations, lateral_reservoirs, tunnels, infrastructure, roads, submerged_zones, resettlement_cities, out_html)
    generate_kml_map(cfg, main_river, stations, lateral_reservoirs, tunnels, infrastructure, roads, submerged_zones, resettlement_cities, out_kml)

if __name__ == "__main__":
    main()
