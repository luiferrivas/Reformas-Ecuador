#!/usr/bin/env python3
"""
Simulador de Casos Tarifarios Reales - Reforma del Sector Eléctrico Ecuador
Consorcio Industrial Kronos - Cumplimiento Mandatorio AGENTS.md

Calcula con exactitud matemática el impacto Antes vs. Después en 8 casos reales:
1. Hogar Vulnerable / Clase Media (180 kWh/mes)
2. Hogar con Confort / Carga Vehicular Eléctrica (420 kWh/mes)
3. Panadería Artesanal de Barrio con Amasadora (750 kWh/mes)
4. Molino de Harina y Trigo Nacional (1.5 GWh/mes, 70% local / 30% exportación)
5. Agroexportadora Camaronera Intensiva (350 MWh/mes, 100% exportación)
6. Gran Minería Metálica a Cielo Abierto (45 GWh/mes, alta tensión 230 kV)
7. Adulto Mayor Vulnerable (48 kWh/mes, 1 solo medidor)
8. Mansión Suntuaria con Fraude de Tercera Edad (450 kWh/mes)
"""

def simular_casos():
    casos = [
        {
            "id": "Hogar Vulnerable / Clase Media",
            "kwh_mes": 180,
            "desc": "Consumo familiar básico (refrigerador, luces LED, TV, lavadora)",
            "factura_antes": 180 * 0.095,
            "factura_despues": 180 * 0.095,
            "con_pronto_pago": (180 * 0.095) * 0.98,
            "notas": "0% incremento. Tarifa base regulada garantizada. Ahorro de 2% por pago puntual."
        },
        {
            "id": "Hogar Alto Consumo / Auto Eléctrico",
            "kwh_mes": 420,
            "desc": "180 kWh base hogar + 240 kWh (4 recargas VE o split continuo)",
            "factura_antes": 420 * 0.105,
            "factura_despues": (250 * 0.095) + (170 * 0.185), # Sin TOU
            "factura_despues_tou": (250 * 0.095) + (170 * 0.065), # Carga en horas valle 23:00-06:00
            "notas": "+25.2% sin modulación. Si recarga en horas valle (madrugada), la factura cae a $34.80 (-21.1%)."
        },
        {
            "id": "Panadería Artesanal con Amasadora",
            "kwh_mes": 750,
            "desc": "Amasadora espiral 4 HP + batidora + frío continuo (Soberanía Alimentaria)",
            "factura_antes": 750 * 0.100,
            "factura_despues": 750 * 0.098,
            "con_pronto_pago": (750 * 0.098) * 0.98,
            "notas": "Cero incremento. Protegida bajo el umbral de 800 kWh para frenar alza del pan."
        },
        {
            "id": "Molino de Trigo y Harina (Nacional)",
            "kwh_mes": 1500000,
            "desc": "3.5 MW en MT. 70% mercado local canasta básica, 30% exportación DAE",
            "factura_antes": 1500000 * 0.078,
            "factura_despues": (1050000 * 0.075) + (450000 * 0.145),
            "notas": "+23.1% de incremento total, pero 100% absorbido por la exportación en divisas. Harina local a $0.075/kWh."
        },
        {
            "id": "Agroexportadora Camaronera (100% Export)",
            "kwh_mes": 350000,
            "desc": "120 hectáreas con bombeo trifásico. 100% ventas externas en USD",
            "factura_antes": 350000 * 0.082,
            "factura_despues": 350000 * 0.112,
            "costo_diesel_equivalente": 35000 * 1.80, # Si operara con diésel subvencionado
            "notas": "+36.6% en factura eléctrica, pero ahorra $23,800/mes frente a operar con motores diésel."
        },
        {
            "id": "Gran Minería Metálica (Mirador / Fruta)",
            "kwh_mes": 45000000,
            "desc": "62 MW continuos en 230 kV. Molinos SAG de cobre/oro",
            "factura_antes": 45000000 * 0.070,
            "factura_despues": 45000000 * 0.150,
            "notas": "+114.3% de incremento. Recauda +$43.2 M USD/año adicionales de una sola mina transnacional."
        },
        {
            "id": "Adulto Mayor Vulnerable (1 solo medidor)",
            "kwh_mes": 48,
            "desc": "Hogar único, consumo esencial bajo 50 kWh",
            "factura_antes": 48 * 0.0475,
            "factura_despues": 48 * 0.0475,
            "notas": "0% incremento. 50% de subsidio vital intacto hasta 50 kWh ($2.28 USD/mes)."
        },
        {
            "id": "Mansión con Fraude de Tercera Edad",
            "kwh_mes": 450,
            "desc": "Residencia de lujo con piscina y sauna registrada a nombre de anciano",
            "factura_antes": 450 * 0.0475, # 50% de descuento fraudulento irrestricto previo
            "factura_despues": (50 * 0.0475) + (200 * 0.095) + (200 * 0.185),
            "notas": "+173.1% de incremento (de $21.38 a $58.38 USD). Erradica la evasión de estratos pudientes."
        }
    ]

    print("=" * 110)
    print("SIMULACIÓN DE IMPACTO TARIFARIO ANTES VS. DESPUÉS - REFORMA DEL SECTOR ELÉCTRICO ECUADOR")
    print("=" * 110)
    header = f"{'CASO / USUARIO':<38} | {'CONSUMO':<11} | {'ANTES (USD)':<12} | {'DESPUÉS (USD)':<14} | {'VARIACIÓN %':<12} | {'ESTADO'}"
    print(header)
    print("-" * 110)

    for c in casos:
        antes = c["factura_antes"]
        despues = c["factura_despues"]
        var_pct = ((despues - antes) / antes) * 100
        kwh_str = f"{c['kwh_mes']:,} kWh"
        antes_str = f"${antes:,.2f}"
        despues_str = f"${despues:,.2f}"
        var_str = f"{var_pct:+.1f}%"
        estado = "PROTEGIDO" if var_pct <= 0 else "AJUSTE REAL"
        print(f"{c['id']:<38} | {kwh_str:<11} | {antes_str:<12} | {despues_str:<14} | {var_str:<12} | {estado}")

    print("=" * 110)

if __name__ == "__main__":
    simular_casos()
