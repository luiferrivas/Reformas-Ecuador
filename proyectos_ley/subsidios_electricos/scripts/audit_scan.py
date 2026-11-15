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

print("=== 1. SCANNING FOR KATEX INSIDE MARKDOWN TABLES (RULE 5 VIOLATION) ===")
table_katex_violations = []
for file_path in files_to_check:
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            # Check if there is KaTeX inside markdown table cell: $...$ or $$...$$
            # Be careful: ignore plain text $ like $17.10 USD or \$
            # KaTeX typically has $ followed by letter or math symbol, e.g. $F_{\text{rec}}$ or $T_{\text{real}}$
            matches = re.findall(r"(?<!\\)\$([^$]+?)\$", line)
            for m in matches:
                # if m contains letters, backslashes, braces, or math operators, it's KaTeX inside table
                if re.search(r"[\\_{}^]|(?:\b[a-zA-Z]\b)", m):
                    table_katex_violations.append((file_path, idx, line.strip(), m))

if table_katex_violations:
    print(f"Found {len(table_katex_violations)} KaTeX in table violations:")
    for v in table_katex_violations:
        print(f"  {v[0]}:{v[1]} -> Match: ${v[3]}$ in: {v[2][:80]}")
else:
    print("Zero KaTeX in table violations found.")

print("\n=== 2. SCANNING FOR OUTDATED NUMBERS OR DISCREPANCIES ===")
discrepancies = []
for file_path in files_to_check:
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check "Costo + 5%" vs "Costo + 10%"
    matches_5 = re.findall(r"[Cc]osto\s*\+\s*5%", content)
    if matches_5:
        discrepancies.append((file_path, "Contains 'Costo + 5%' (should be Costo + 10%)", len(matches_5)))

    # Check "814.5" (old protected demand before adding water/irrigation/pharma)
    matches_814 = re.findall(r"814[\.,]5", content)
    if matches_814:
        discrepancies.append((file_path, "Contains old '814.5 GWh' (should be 879.5 GWh)", len(matches_814)))

    # Check "Net Metering 1:1" for industry (should be Net Billing 70/30)
    matches_nm = re.findall(r"[Nn]et\s+[Mm]etering\s+1:1\s+industrial", content, re.IGNORECASE)
    if matches_nm:
        discrepancies.append((file_path, "Contains 'Net Metering 1:1 industrial'", len(matches_nm)))

for d in discrepancies:
    print(f"  {d[0]}: {d[1]} (Count: {d[2]})")

print("\n=== 3. SCANNING FOR LEXICAL EVASION TRAPS ===")
traps = ["fácilmente", "óptimo", "se asume", "aprovechando la sinergia", "garantizado"]
trap_findings = []
for file_path in files_to_check:
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        for trap in traps:
            if re.search(r"\b" + re.escape(trap) + r"\b", line, re.IGNORECASE):
                trap_findings.append((file_path, idx, trap, line.strip()))

print(f"Found {len(trap_findings)} occurrences of lexical trap words across documents.")
for tf in trap_findings[:15]:
    print(f"  {tf[0]}:{tf[1]} [{tf[2]}]: {tf[3][:80]}")
