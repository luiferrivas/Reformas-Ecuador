import os
import re

files_to_check = [
    "proyectos_ley/subsidios_electricos/Proyecto_Ley_Subsidios_Electricos_Ecuador.md",
    "proyectos_ley/subsidios_electricos/Memoria_Tecnica_Economica.md",
    "proyectos_ley/subsidios_electricos/Auditoria_Politica_y_Optimizacion_Electrica.md",
    "proyectos_ley/subsidios_electricos/SUMMARY.md",
    "config/reformas/subsidios_electricos.yaml",
    "proyectos_ley/subsidios_electricos/scripts/simulacion_tarifaria_casos.py",
    "README.md"
]

print("=== 1. SCANNING FOR ACTUAL MARKDOWN TABLES WITH '$' (OUTSIDE CODE FENCES) ===")
table_violations = []
for file_path in files_to_check:
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    in_code = False
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if not in_code and stripped.startswith("|") and stripped.endswith("|"):
            if "$" in stripped:
                table_violations.append((file_path, idx, stripped))

print(f"Total markdown table lines containing '$': {len(table_violations)}")
for tv in table_violations:
    print(f"  {tv[0]}:{tv[1]} -> {tv[2][:100]}")
