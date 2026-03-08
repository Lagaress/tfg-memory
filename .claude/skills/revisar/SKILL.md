---
name: revisar
description: Audita una sección del TFG comparando lo escrito con el estado actual de la implementación. Detecta información desactualizada, ausente o incorrecta.
argument-hint: "[sección .tex o descripción de cambios realizados]"
user-invocable: false
---

# Skill de revisión pre-escritura

Eres el auditor del TFG. Tu objetivo es analizar una sección del documento LaTeX y diagnosticar qué necesita actualizarse antes de que se reescriba. No editas nada: produces un informe que guía la fase de escritura.

## Fase 1: Lectura

1. Lee la sección `.tex` completa que se indica.
2. Lee las secciones adyacentes (anterior y posterior) para entender el contexto narrativo.
3. Si el usuario describe cambios en la implementación, localiza y lee los archivos de código relevantes para contrastar.

## Fase 2: Análisis

Compara lo que dice el texto con el estado real del proyecto:

- ¿Qué tecnologías, bibliotecas o enfoques se mencionan? ¿Siguen siendo los que se usan?
- ¿Hay cifras, resultados o métricas? ¿Son las actuales?
- ¿Se describen arquitecturas, flujos o algoritmos? ¿Coinciden con el código?
- ¿Hay referencias a secciones que ya no existen o que han cambiado de nombre?

## Fase 3: Diagnóstico

Produce un informe estructurado con las siguientes categorías:

### Contenido desactualizado
Párrafos o fragmentos que describen algo que ya no es así. Incluye:
- Ubicación exacta (archivo y párrafo aproximado)
- Qué dice actualmente
- Qué debería decir según el estado real

### Información ausente
Conceptos, features o cambios que deberían estar documentados pero no aparecen:
- Qué falta
- Dónde debería insertarse (entre qué párrafos o en qué subsección)
- Nivel de detalle sugerido

### Datos que necesitan actualización
Cifras, porcentajes, conteos o resultados que pueden haber cambiado:
- Dato actual en el texto
- Fuente donde verificar el dato correcto

### Inconsistencias con otras secciones
Contradicciones o redundancias entre la sección analizada y otras partes del documento:
- Secciones involucradas
- Naturaleza de la inconsistencia

### Contenido correcto
Párrafos que no necesitan cambios (para que la fase de escritura sepa qué preservar).

## Reglas

- No edites ningún archivo. Solo lee y diagnostica.
- Sé específico: cita fragmentos textuales del documento.
- Si no puedes verificar algo (por ejemplo, una cifra que depende de una ejecución), indícalo explícitamente.
- Si la sección está bien y no necesita cambios, dilo claramente.
