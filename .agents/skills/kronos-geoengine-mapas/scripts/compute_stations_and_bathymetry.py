"""
Kronos GeoEngine - Script 2: Computador de Estaciones Equidistantes, Perfil Batimétrico y Snapping Fluvial Obligatorio
Calcula hitos batimétricos cada N metros (default 500m) a lo largo de la traza real meándrica del río.
Incluye Snapping Matemático Obligatorio: Bloquea obras civiles (presas, tomas, casas de máquinas) al eje fluvial
con tolerancia 0.00m, detecta puntos desfasados en laderas montañosas y valida la monotonicidad hidráulica descendente.
"""

import sys
import os
import json
import math
import argparse

def haversine_m(lat1, lon1, lat2, lon2):
    R = 6371000.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2.0)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2.0)**2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return R * c

def snap_point_to_river(lat, lon, river_pts):
    """
    Encuentra el nodo exacto del río más cercano al punto dado.
    Retorna: (snapped_lat, snapped_lon, node_idx, distancia_m)
    """
    min_dist = float('inf')
    best_idx = -1
    best_pt = None
    
    for idx, p in enumerate(river_pts):
        p_lat = p['lat'] if isinstance(p, dict) else p[0]
        p_lon = p['lon'] if isinstance(p, dict) else p[1]
        d = haversine_m(lat, lon, p_lat, p_lon)
        if d < min_dist:
            min_dist = d
            best_idx = idx
            best_pt = (p_lat, p_lon)
            
    return best_pt[0], best_pt[1], best_idx, min_dist

def validate_hydraulic_monotonicity(projects):
    """
    Verifica que la secuencia hidráulica cumpla con el gradiente descendente estricto:
    tail_idx < dam_idx < ch_idx y cota_namo > cota_lecho > cota_descarga.
    """
    errors = []
    for p in projects:
        t_idx = p.get('tail_idx')
        d_idx = p.get('dam_idx')
        ch_idx = p.get('ch_idx')
        name = p.get('name', p.get('id', 'Proyecto'))
        
        if t_idx is not None and d_idx is not None:
            if t_idx >= d_idx:
                errors.append(f"[{name}] ERROR TOPOLÓGICO: Cola del embalse (nodo {t_idx}) no está aguas arriba de la presa (nodo {d_idx}).")
        if d_idx is not None and ch_idx is not None:
            if d_idx >= ch_idx:
                errors.append(f"[{name}] ERROR HIDRÁULICO: Presa (nodo {d_idx}) está después de la casa de máquinas (nodo {ch_idx}). Flujo invertido.")
                
        c_namo = p.get('cota_namo')
        c_lecho = p.get('cota_lecho')
        c_descarga = p.get('cota_descarga')
        if c_namo and c_lecho and c_namo <= c_lecho:
            errors.append(f"[{name}] ERROR ALTIMÉTRICO: Cota NAMO ({c_namo} m) <= Cota Lecho ({c_lecho} m).")
        if c_lecho and c_descarga and c_lecho < c_descarga:
            errors.append(f"[{name}] ERROR ALTIMÉTRICO: Cota Lecho Presa ({c_lecho} m) < Cota Descarga ({c_descarga} m). Salto negativo.")
            
    return errors

def compute_stations(river_pts, interval_m=500.0, cota_start=970.0, cota_dam=825.0, cota_namo=960.0):
    if len(river_pts) < 2:
        return [], 0.0
    
    # Normalize points to dict format
    norm_pts = []
    for p in river_pts:
        if isinstance(p, dict):
            norm_pts.append({'lat': float(p['lat']), 'lon': float(p['lon'])})
        elif isinstance(p, (list, tuple)):
            norm_pts.append({'lat': float(p[0]), 'lon': float(p[1])})
    river_pts = norm_pts

    cum_dists = [0.0]
    total_dist = 0.0
    for i in range(1, len(river_pts)):
        d = haversine_m(river_pts[i-1]['lat'], river_pts[i-1]['lon'], river_pts[i]['lat'], river_pts[i]['lon'])
        total_dist += d
        cum_dists.append(total_dist)
        
    stations = []
    curr_target = 0.0
    seg_idx = 0
    
    while curr_target <= total_dist:
        while seg_idx < len(cum_dists) - 1 and cum_dists[seg_idx+1] < curr_target:
            seg_idx += 1
            
        p1 = river_pts[seg_idx]
        p2 = river_pts[seg_idx+1]
        d1 = cum_dists[seg_idx]
        d2 = cum_dists[seg_idx+1]
        
        fraction = (curr_target - d1) / (d2 - d1) if (d2 - d1) > 0 else 0.0
        lat_interp = p1['lat'] + fraction * (p2['lat'] - p1['lat'])
        lon_interp = p1['lon'] + fraction * (p2['lon'] - p1['lon'])
        
        prog_frac = curr_target / total_dist if total_dist > 0 else 0.0
        lecho = cota_start - prog_frac * (cota_start - cota_dam)
        calado = max(0.0, cota_namo - lecho)
        
        stations.append({
            'pk': f"PK {curr_target/1000.0:.1f} km",
            'dist_m': round(curr_target, 1),
            'lat': round(lat_interp, 6),
            'lon': round(lon_interp, 6),
            'lecho_cota': round(lecho, 1),
            'namo_cota': round(cota_namo, 1),
            'calado_m': round(calado, 1)
        })
        
        curr_target += interval_m
        
    # Último punto en la presa si falta
    if stations[-1]['dist_m'] < total_dist:
        p_last = river_pts[-1]
        lecho_last = cota_dam
        calado_last = max(0.0, cota_namo - lecho_last)
        stations.append({
            'pk': f"PK {total_dist/1000.0:.1f} km",
            'dist_m': round(total_dist, 1),
            'lat': round(p_last['lat'], 6),
            'lon': round(p_last['lon'], 6),
            'lecho_cota': round(lecho_last, 1),
            'namo_cota': round(cota_namo, 1),
            'calado_m': round(calado_last, 1)
        })
        
    return stations, total_dist

def main():
    parser = argparse.ArgumentParser(description="Computador de Batimetría y Snapping Fluvial Kronos GeoEngine")
    parser.add_argument("--input", required=True, help="Archivo JSON generado por extract_osm_hydrography.py")
    parser.add_argument("--interval", type=float, default=500.0, help="Intervalo entre estaciones en metros (default 500)")
    parser.add_argument("--cota-start", type=float, required=False, default=1000.0, help="Cota lecho al inicio del tramo (msnm)")
    parser.add_argument("--cota-dam", type=float, required=False, default=500.0, help="Cota lecho al pie de la presa (msnm)")
    parser.add_argument("--cota-namo", type=float, required=False, default=950.0, help="Cota NAMO espejo de agua (msnm)")
    parser.add_argument("--snap-points", required=False, default=None, help="Archivo JSON con puntos de infraestructura para snapping obligatorio al río")
    parser.add_argument("--output", required=True, help="Archivo JSON de salida con las estaciones")
    args = parser.parse_args()
    
    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    pts = data.get('main_river_geom', [])
    if not pts:
        print("Error: No se encontró main_river_geom en el archivo de entrada.")
        sys.exit(1)
        
    stations, total_len = compute_stations(pts, args.interval, args.cota_start, args.cota_dam, args.cota_namo)
    print(f"[GeoEngine] Longitud meándrica total: {total_len/1000.0:.2f} km | Estaciones generadas: {len(stations)}")
    
    # Snapping si fue solicitado
    if args.snap_points:
        with open(args.snap_points, "r", encoding="utf-8") as f:
            infra_data = json.load(f)
        print(f"\n--- AUDITORÍA FORENSE DE SNAPPING FLUVIAL (MANDATO MONTAÑOSO) ---")
        snapped_infra = []
        for item in infra_data:
            orig_lat = item.get('lat', item.get('dam_lat'))
            orig_lon = item.get('lon', item.get('dam_lon'))
            name = item.get('name', 'Punto Infraestructura')
            if orig_lat is not None and orig_lon is not None:
                s_lat, s_lon, s_idx, s_dist = snap_point_to_river(orig_lat, orig_lon, pts)
                item['snapped_lat'] = s_lat
                item['snapped_lon'] = s_lon
                item['river_node_idx'] = s_idx
                item['offset_to_river_m'] = round(s_dist, 2)
                snapped_infra.append(item)
                if s_dist > 50.0:
                    print(f"⚠️ [RED TEAM ALERTA] '{name}' estaba a {s_dist:.1f} m en ladera montañosa! Bloqueado a nodo OSM {s_idx} ({s_lat:.6f}, {s_lon:.6f}).")
                else:
                    print(f"✅ '{name}': Coincidencia fluvial confirmada (desviación: {s_dist:.2f} m).")
                    
        # Guardar archivo con puntos bloqueados
        snap_out = args.snap_points.replace(".json", "_snapped.json")
        with open(snap_out, "w", encoding="utf-8") as f:
            json.dump(snapped_infra, f, ensure_ascii=False, indent=2)
        print(f"[GeoEngine] Archivo de infraestructura bloqueada guardado en: {snap_out}\n")
    
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(stations, f, ensure_ascii=False, indent=2)
        
    print(f"[GeoEngine] Estaciones batimétricas guardadas en: {args.output}")

if __name__ == "__main__":
    main()
