"""
Kronos GeoEngine - Script 1: Extractor de Hidrografía Vectorial Real OSM (Versión Montañosa / Alta Resiliencia)
Descarga geometrías vectoriales reales de ríos y quebradas desde OpenStreetMap (Overpass API).
Concatena segmentos de ways y relaciones en polilíneas continuas ordenadas sin roturas topológicas.
Incluye soporte multi-servidor (fallback automático) y consulta por BBox o por Nombre Oficial de Río.
"""

import sys
import os
import json
import urllib.request
import urllib.parse
import argparse
import time

OVERPASS_ENDPOINTS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.private.coffee/api/interpreter"
]

def execute_overpass_query(query, timeout_sec=90):
    data = urllib.parse.urlencode({'data': query}).encode('utf-8')
    last_err = None
    for ep in OVERPASS_ENDPOINTS:
        try:
            print(f"[GeoEngine] Consultando Overpass endpoint: {ep}...")
            req = urllib.request.Request(ep, data=data, headers={'User-Agent': 'KronosGeoEngine/2.0'})
            with urllib.request.urlopen(req, timeout=timeout_sec) as response:
                res_json = json.loads(response.read().decode('utf-8'))
                print(f"[GeoEngine] Respuesta exitosa recibida de: {ep}")
                return res_json
        except Exception as e:
            print(f"[GeoEngine] Advertencia: Fallo en endpoint {ep}: {e}. Probando siguiente...")
            last_err = e
            time.sleep(1)
            
    raise RuntimeError(f"Todos los servidores Overpass fallaron. Último error: {last_err}")

def query_overpass_by_name(river_name, bbox=None):
    if bbox:
        lat_min, lon_min, lat_max, lon_max = bbox
        query = f"""
        [out:json][timeout:90];
        (
          relation["waterway"="river"]["name"~"{river_name}",i]({lat_min},{lon_min},{lat_max},{lon_max});
          way["waterway"~"river|stream"]["name"~"{river_name}",i]({lat_min},{lon_min},{lat_max},{lon_max});
        );
        out body;
        >;
        out skel qt;
        """
    else:
        query = f"""
        [out:json][timeout:90];
        (
          relation["waterway"="river"]["name"~"{river_name}",i];
          way["waterway"~"river|stream"]["name"~"{river_name}",i];
        );
        out body;
        >;
        out skel qt;
        """
    return execute_overpass_query(query)

def query_overpass_bbox(lat_min, lon_min, lat_max, lon_max):
    query = f"""
    [out:json][timeout:90];
    (
      way["waterway"~"river|stream|canal"]({lat_min},{lon_min},{lat_max},{lon_max});
    );
    out body;
    >;
    out skel qt;
    """
    return execute_overpass_query(query)

def parse_osm_elements(osm_data):
    nodes = {}
    ways = {}
    relations = []
    
    for el in osm_data.get('elements', []):
        if el['type'] == 'node':
            nodes[el['id']] = (el['lat'], el['lon'])
        elif el['type'] == 'way':
            ways[el['id']] = el
        elif el['type'] == 'relation':
            relations.append(el)
            
    print(f"[GeoEngine] Nodos recibidos: {len(nodes)}, Tramos (ways): {len(ways)}, Relaciones: {len(relations)}")
    
    # Parse ways
    parsed_ways = []
    for wid, w in ways.items():
        name = w.get('tags', {}).get('name', 'Sin Nombre')
        w_nodes = w.get('nodes', [])
        coords = [nodes[n] for n in w_nodes if n in nodes]
        if len(coords) >= 2:
            parsed_ways.append({
                'id': wid,
                'name': name,
                'tags': w.get('tags', {}),
                'pts': len(coords),
                'geom': [{'lat': c[0], 'lon': c[1]} for c in coords]
            })
            
    return nodes, ways, relations, parsed_ways

def stitch_connected_ways(parsed_rivers, main_keyword=None, relations=None, ways_dict=None, nodes_dict=None):
    """
    Concatena segmentos que comparten nodos extremos para formar polilíneas continuas.
    Si existe una relación OSM oficial, respeta el orden de miembros de la relación.
    """
    # 1. Si hay una relación oficial para el río principal, intentar reconstruir desde miembros
    if relations and ways_dict and nodes_dict and main_keyword:
        for rel in relations:
            rel_name = rel.get('tags', {}).get('name', '')
            if main_keyword.lower() in rel_name.lower():
                print(f"[GeoEngine] Ensamblando río desde Relación OSM '{rel_name}' (ID: {rel['id']})...")
                rel_members = rel.get('members', [])
                full_chain = []
                for m in rel_members:
                    if m['type'] == 'way' and m['ref'] in ways_dict:
                        w = ways_dict[m['ref']]
                        w_coords = [nodes_dict[n] for n in w.get('nodes', []) if n in nodes_dict]
                        if len(w_coords) >= 2:
                            if not full_chain:
                                full_chain.extend(w_coords)
                            else:
                                # Comprobar continuidad con el extremo actual
                                curr_end = full_chain[-1]
                                d_start = (curr_end[0] - w_coords[0][0])**2 + (curr_end[1] - w_coords[0][1])**2
                                d_end = (curr_end[0] - w_coords[-1][0])**2 + (curr_end[1] - w_coords[-1][1])**2
                                if d_start <= d_end:
                                    full_chain.extend(w_coords[1:])
                                else:
                                    full_chain.extend(list(reversed(w_coords))[1:])
                if len(full_chain) >= 2:
                    print(f"[GeoEngine] Relación ensamblada con éxito: {len(full_chain)} puntos GPS.")
                    other_segs = [r for r in parsed_rivers if r['name'].lower() != rel_name.lower()]
                    return [{'lat': c[0], 'lon': c[1]} for c in full_chain], other_segs

    # 2. Heurística de proximidad de extremos
    main_segments = []
    other_segments = []
    for r in parsed_rivers:
        if main_keyword and main_keyword.lower() in r['name'].lower():
            main_segments.append(r)
        else:
            other_segments.append(r)
            
    if main_segments:
        print(f"[GeoEngine] Segmentos nombrados del río principal: {len(main_segments)}")
        stitched = [main_segments[0]['geom']]
        remaining = main_segments[1:]
        
        while remaining:
            curr_start = stitched[0][0]
            curr_end = stitched[-1][-1]
            best_idx = None
            best_rev = False
            best_pos = None
            min_dist = 0.05 # ~5 km tolerancia
            
            for i, cand in enumerate(remaining):
                c_start = cand['geom'][0]
                c_end = cand['geom'][-1]
                
                # Check end to start
                d1 = (curr_end['lat'] - c_start['lat'])**2 + (curr_end['lon'] - c_start['lon'])**2
                if d1 < min_dist:
                    min_dist = d1
                    best_idx = i
                    best_rev = False
                    best_pos = 'end'
                # Check end to end (reverse)
                d2 = (curr_end['lat'] - c_end['lat'])**2 + (curr_end['lon'] - c_end['lon'])**2
                if d2 < min_dist:
                    min_dist = d2
                    best_idx = i
                    best_rev = True
                    best_pos = 'end'
                    
            if best_idx is not None:
                match = remaining.pop(best_idx)['geom']
                if best_rev:
                    match = list(reversed(match))
                if best_pos == 'end':
                    stitched.append(match)
            else:
                break
                
        flat_main = []
        for seg in stitched:
            flat_main.extend(seg)
        print(f"[GeoEngine] Río principal concatenado con éxito: {len(flat_main)} puntos.")
    else:
        flat_main = []
        
    return flat_main, other_segments

def main():
    parser = argparse.ArgumentParser(description="Extractor Hidrográfico OSM Kronos GeoEngine")
    parser.add_argument("--bbox", required=False, default=None, help="lat_min,lon_min,lat_max,lon_max")
    parser.add_argument("--main-river", required=False, default=None, help="Nombre o palabra clave del río principal (ej. 'Guayllabamba', 'Paute', 'Mira')")
    parser.add_argument("--output", required=True, help="Ruta del archivo JSON de salida")
    args = parser.parse_args()
    
    if not args.bbox and not args.main_river:
        print("Error: Debe proporcionar al menos --bbox o --main-river.")
        sys.exit(1)
        
    bbox_parts = None
    if args.bbox:
        bbox_parts = [float(x.strip()) for x in args.bbox.split(",")]
        if len(bbox_parts) != 4:
            print("Error: --bbox debe contener 4 números: lat_min,lon_min,lat_max,lon_max")
            sys.exit(1)
            
    if args.main_river:
        print(f"[GeoEngine] Modo Búsqueda por Nombre Oficial: '{args.main_river}'")
        raw_data = query_overpass_by_name(args.main_river, bbox_parts)
    else:
        print(f"[GeoEngine] Modo Búsqueda por BBox: {bbox_parts}")
        raw_data = query_overpass_bbox(*bbox_parts)
        
    nodes, ways_dict, relations, parsed_ways = parse_osm_elements(raw_data)
    main_geom, others = stitch_connected_ways(parsed_ways, args.main_river, relations, ways_dict, nodes)
    
    out_payload = {
        'bbox': bbox_parts,
        'main_river_name': args.main_river,
        'main_river_geom': main_geom,
        'tributaries': others,
        'all_rivers_count': len(parsed_ways)
    }
    
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(out_payload, f, ensure_ascii=False, indent=2)
        
    print(f"[GeoEngine] Archivo hidrográfico exportado con éxito a: {args.output}")

if __name__ == "__main__":
    main()
