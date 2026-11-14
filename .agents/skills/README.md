# 🛠️ Skills del Proyecto — Reformas Ecuador

Este directorio almacena los **skills personalizados del proyecto** que los agentes IA y subagentes pueden invocar y ejecutar.

---

## 📂 Estructura de un Skill

Cada skill reside en su propia subcarpeta con un archivo maestro `SKILL.md`:

```text
.agents/skills/
└── <nombre_del_skill>/
    ├── SKILL.md                 # Definición obligatoria con YAML frontmatter (name y description)
    ├── scripts/                 # (Opcional) Scripts auxiliares en Python, Bash o Node
    └── templates/               # (Opcional) Plantillas de documentos o esquemas
```

---

## 📝 Formato Requerido en `SKILL.md`

Todo skill debe iniciar con frontmatter YAML estándar:

```markdown
---
name: nombre-del-skill
description: Descripción concisa de una o dos oraciones explicando qué hace el skill y cuándo invocarlo.
---

# Título del Skill

Instrucciones detalladas, directrices y pasos para el agente...
```

---

## 📥 Cómo Copiar un Skill desde Otro Proyecto

1. **Copia Manual de Carpeta:**
   Copia la carpeta de tu skill desde el otro proyecto (ej. `OtroProyecto/.agents/skills/<nombre_del_skill>`) directamente a este directorio:
   `.agents/skills/<nombre_del_skill>/`

2. **A través de la conversación con Antigravity:**
   Puedes pegar el contenido del `SKILL.md` o indicar el repositorio origen, y el agente registrará el skill automáticamente en este directorio.
