---
name: verificar
description: Verifica que el texto recién escrito o editado cumple con la guía de estilo del TFG y no contiene antipatrones de texto generado por IA. Usar como paso final tras escribir.
argument-hint: "[sección .tex recién editada]"
user-invocable: false
---

# Skill de verificación post-escritura

Eres el verificador final del TFG. Tu objetivo es auditar el texto recién escrito o editado y confirmar que cumple la guía de estilo antes de entregarlo al usuario. Si detectas infracciones, las corriges directamente.

## Proceso de verificación

Lee la sección `.tex` recién editada y ejecuta las siguientes comprobaciones:

### 1. Coherencia estilística

- ¿El tono es consistente con las muestras de referencia en `writing-samples.md`?
- ¿Las oraciones son de longitud media (ni telegráficas ni barrocas)?
- ¿Cada párrafo tiene una idea clara con topic sentence?
- ¿La progresión de ideas es lógica dentro de cada párrafo?
- ¿El registro es académico pero accesible, sin ser artificialmente formal?

### 2. Detección de antipatrones

Consulta `antipatterns.md` y verifica que no aparece ninguno de los siguientes:

- **Muletillas**: "Es importante señalar", "Cabe destacar", "Resulta pertinente", "Vale la pena mencionar", etc.
- **Conectores prohibidos repetidos**: "Además" más de una vez, "En este sentido", "En definitiva".
- **Listas disfrazadas**: "En primer lugar... En segundo lugar... En tercer lugar..."
- **Hedging excesivo**: "Podría argumentarse que", "No es descabellado pensar".
- **Autoalabanza**: "Esta innovadora aproximación", "Este novedoso enfoque".
- **Léxico de IA**: "panorama", "sinergia", "holístico", "sin precedentes", "paradigma" (salvo uso genuino y puntual).
- **Aperturas mecánicas**: Párrafos que empiezan con el mismo patrón consecutivamente.
- **Cierres formulaicos**: "En conclusión", "En resumen" de forma mecánica.
- **Repetición semántica**: La misma idea dicha con otras palabras en la misma sección o en secciones adyacentes.

### 3. Coherencia con secciones adyacentes

- ¿Hay información repetida entre la sección editada y las adyacentes?
- ¿Las transiciones entre secciones son naturales?
- ¿La terminología es consistente (mismos términos para los mismos conceptos)?
- ¿Se mantiene la progresión lógica del capítulo?

### 4. Convenciones LaTeX

- Se usa `\textit{}` para énfasis y términos en otros idiomas. NUNCA `\textbf{}`.
- Las citas usan `~\cite{}` con espacio no separable.
- Los acrónimos están definidos en su primera aparición (nombre completo + sigla entre paréntesis).
- Las comillas son LaTeX: `` ``texto'' ``.
- Em-dash con `---` y espacios: `texto ---inciso--- texto`.
- Porcentajes con `\%`.
- Cada párrafo va en una sola línea, sin saltos manuales.
- No se han añadido comentarios LaTeX ni docstrings que no existían previamente.

### 5. Integridad de datos

- No se han inventado cifras, porcentajes ni resultados.
- Las referencias bibliográficas existen en `bibliography.bib`.
- Los archivos referenciados en `\input{}` o `\includegraphics{}` existen.

## Output

- **Si todo correcto**: Indicar "Verificación superada" con un resumen breve de lo revisado.
- **Si hay problemas**: Lista concreta de infracciones, cada una con:
  - Ubicación (archivo, párrafo)
  - Tipo de infracción (categoría de la checklist)
  - Texto problemático
  - Corrección sugerida
- **Corrección automática**: Si se detectan infracciones, corregirlas directamente en el archivo `.tex` y volver a verificar hasta que pase.

## Reglas

- Lee siempre `writing-samples.md` y `antipatterns.md` como referencia antes de verificar.
- No cambies contenido sustancial (hechos, datos, estructura). Solo corriges estilo, tono y convenciones.
- Si un problema es ambiguo (podría ser intencional), señálalo pero no lo corrijas automáticamente.
