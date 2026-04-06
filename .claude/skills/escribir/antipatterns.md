# Antipatrones de texto IA en español académico

Catálogo exhaustivo de señales que delatan texto generado por inteligencia artificial. Úsalo como checklist negativa: si tu texto contiene alguno de estos patrones, reescríbelo.

Fuentes principales: Wikipedia (Signs of AI writing), GPTZero (3.3M textos analizados), Pangram Labs, Colin Gorrie (análisis retórico), Blake Stockton (serie de 101 antipatrones), PNAS (Reinhart et al.), Science Advances (Liang et al.).

---

## 1. Muletillas recurrentes

Frases vacías que añaden palabras sin añadir información. Si puedes eliminar la frase introductoria y la oración sigue teniendo sentido, elimínala.

| Antipatrón | Ejemplo malo | Reescritura |
|---|---|---|
| "Es importante señalar que" | "Es importante señalar que los pictogramas carecen de flexión verbal." | "Los pictogramas carecen de flexión verbal." |
| "Cabe destacar que" | "Cabe destacar que el sistema alcanzó un 85\% de precisión." | "El sistema alcanzó un 85\% de precisión." |
| "Resulta pertinente mencionar" | "Resulta pertinente mencionar que existen alternativas." | "Existen alternativas." |
| "Vale la pena mencionar que" | "Vale la pena mencionar que esta técnica fue propuesta en 2018." | "Esta técnica fue propuesta en 2018~\cite{ref}." |
| "Es menester considerar" | "Es menester considerar las limitaciones del enfoque." | "El enfoque tiene limitaciones." |
| "No se puede pasar por alto" | "No se puede pasar por alto la importancia de la evaluación." | "La evaluación es un paso necesario." |
| "Es fundamental tener en cuenta" | "Es fundamental tener en cuenta que los resultados varían." | "Los resultados varían según el corpus." |
| "En el contexto de" | "En el contexto de la CAA, los pictogramas son esenciales." | "En CAA, los pictogramas son esenciales." |
| "En este sentido" | "En este sentido, la gramática formal ofrece garantías." | "La gramática formal ofrece garantías." |
| "En definitiva" | "En definitiva, el sistema cumple sus objetivos." | "El sistema cumple sus objetivos." |
| "Desde una perspectiva más amplia" | "Desde una perspectiva más amplia, la NLG aborda este problema." | "La NLG aborda este problema." |
| "A la luz de lo anterior" | "A la luz de lo anterior, se optó por FastText." | "Se optó por FastText." |
| "Con el objetivo de" | "Con el objetivo de mejorar la cobertura..." | "Para mejorar la cobertura..." |
| "En lo que respecta a" | "En lo que respecta a la evaluación..." | "La evaluación..." |
| "En relación con" (como apertura) | "En relación con los embeddings..." | "Los embeddings..." |
| "Es necesario enfatizar que" | "Es necesario enfatizar que este paso es crítico." | "Este paso es crítico." |
| "No se puede subestimar" | "No se puede subestimar la importancia de X." | "X es necesario para Y." |
| "A fin de" | "A fin de evaluar la calidad..." | "Para evaluar la calidad..." |

---

## 2. Patrones estructurales

### Listas disfrazadas de prosa

**Mal**:
"En primer lugar, el sistema analiza la secuencia de entrada. En segundo lugar, aplica las reglas gramaticales correspondientes. En tercer lugar, genera la oración final. En cuarto lugar, verifica la corrección del resultado."

**Bien**:
"El sistema analiza la secuencia de entrada y aplica las reglas gramaticales que correspondan. A partir de estas reglas genera la oración, que pasa por una verificación final de corrección."

### Párrafos espejo

Cuando dos párrafos consecutivos siguen la misma estructura: presentar concepto, decir ventaja, decir desventaja, cerrar con transición.

**Regla**: Varía la estructura entre párrafos. No todos necesitan el mismo arco.

### Paralelismo excesivo

"X ofrece A. Y ofrece B. Z ofrece C." Tres oraciones seguidas con la misma estructura sintáctica.

**Regla**: Rompe el paralelismo. Reformula al menos una de las oraciones con estructura diferente.

### Tricolon abusivo (regla del tres)

Los LLMs agrupan conceptos de tres en tres compulsivamente: "un enfoque flexible, escalable y robusto", "la precisión, la coherencia y la naturalidad". La regla del tres es un recurso retórico legítimo, pero la IA lo convierte en fórmula al usarlo en cada párrafo.

**Mal**: "El sistema es preciso, eficiente y escalable. La interfaz es intuitiva, accesible y moderna. Los resultados son prometedores, consistentes y reproducibles."

**Bien**: "El sistema es preciso y eficiente. La interfaz facilita el acceso a usuarios sin experiencia técnica. Los resultados se mantienen consistentes entre ejecuciones."

**Regla**: Si tienes más de un tricolon por página, elimina alguno.

### Apilamiento de oraciones (sentence stacking)

Oraciones autónomas del mismo peso, sin subordinación ni variación de longitud. Cada oración es una unidad independiente sin jerarquía.

**Mal**: "El sistema recibe pictogramas. El módulo gramatical los procesa. Se generan las concordancias. Se produce la oración final."

**Bien**: "Cuando el sistema recibe los pictogramas, el módulo gramatical los procesa para establecer concordancias y producir la oración final."

### Uniformidad de longitud

Todos los párrafos tienen aproximadamente la misma longitud (4-6 líneas). Los humanos varían naturalmente: un párrafo de una línea tras uno de ocho es normal y crea ritmo. La IA produce bloques uniformes.

Lo mismo ocurre con las oraciones: la IA mantiene una longitud media constante (baja "burstiness"), mientras que los humanos alternan oraciones cortas y largas.

**Regla**: Varía la longitud de tus párrafos y oraciones. Un párrafo corto tras uno largo crea énfasis.

### Múltiples conclusiones

La IA tiende a cerrar cada subsección con una mini-conclusión, además de la conclusión general. Esto produce redundancia y una sensación de cierre repetitivo.

**Regla**: No todas las subsecciones necesitan un cierre explícito. Muchas veces la última idea del último párrafo basta.

---

## 3. Problemas de tono

### Hedging (cobertura excesiva)

| Antipatrón | Reescritura |
|---|---|
| "Podría argumentarse que este enfoque es eficaz." | "Este enfoque es eficaz." |
| "No sería descabellado pensar que..." | Eliminar y afirmar directamente. |
| "Parece razonable suponer que..." | Afirmar o citar evidencia. |
| "Es posible que los resultados sugieran..." | "Los resultados muestran..." |

**Regla**: Si tienes evidencia, afirma. Si no la tienes, busca la referencia. No te cubras con lenguaje vago.

### Autoalabanza

| Antipatrón | Reescritura |
|---|---|
| "Esta innovadora aproximación" | "Esta aproximación" |
| "Este novedoso enfoque" | "Este enfoque" |
| "Nuestra sofisticada implementación" | "La implementación" |
| "El elegante diseño del sistema" | "El diseño del sistema" |

**Regla**: Deja que los resultados y la descripción técnica hablen por sí mismos.

### Grandilocuencia

| Antipatrón | Reescritura |
|---|---|
| "Ha revolucionado el panorama de la NLG" | "Ha cambiado las prácticas habituales en NLG" |
| "Un avance sin precedentes" | Describir qué mejoró concretamente. |
| "Abre un abanico de posibilidades infinitas" | "Permite nuevas aplicaciones como X e Y" |
| "Supone un antes y un después" | Describir el cambio concreto. |

### Afirmaciones emocionales vacías

La IA hace afirmaciones que suenan huecas porque carecen de contenido concreto.

| Antipatrón | Reescritura |
|---|---|
| "Esto resulta fascinante" | Eliminar o explicar por qué es relevante técnicamente. |
| "Los resultados son realmente prometedores" | "Los resultados mejoran la baseline en X puntos." |
| "Este apasionante campo" | Eliminar el adjetivo. |

### Énfasis excesivo en la importancia

La IA no puede resistirse a explicar por qué todo importa: "un momento pivotal", "un avance crucial", "desempeña un papel fundamental".

| Antipatrón | Reescritura |
|---|---|
| "X desempeña un papel crucial en Y" | "X permite Y" o "X es necesario para Y" |
| "Es de vital importancia para" | Describir la función concreta. |
| "Esto subraya la relevancia de" | Eliminar; la relevancia debe ser evidente por el contexto. |
| "Es un componente indispensable" | "El sistema requiere X" |

---

## 4. Señales léxicas

Palabras y expresiones sobreusadas por modelos de lenguaje. No están prohibidas, pero si aparecen más de una vez en el documento, probablemente sobran. Datos de GPTZero (3.3M textos): "crucial" aparece 182x más en texto IA que en texto humano; "showcasing" 20x más; "aligns" 16x más.

### Sustantivos y expresiones nominales

| Palabra | Problema | Alternativa contextual |
|---|---|---|
| "panorama" | Sobreusada como metáfora | "estado actual", "situación", "campo" |
| "ámbito" | Vaga si no se concreta | "área de X", "en el campo de X" |
| "paradigma" | Rara vez es un paradigma real | "enfoque", "modelo", "marco" |
| "sinergia" | Casi nunca necesaria | "complementariedad", "combinación" |
| "ecosistema" (para software) | Metáfora sobreusada | "conjunto de herramientas", "entorno" |
| "catalizador" | Metáfora gastada | "factor", "elemento que contribuye a" |
| "piedra angular" | Sobreusada | "base", "fundamento" |
| "hoja de ruta" | Sobreusada | "plan", "guía" |
| "brecha" (gap) | Sobreusada cuando es genérica | "diferencia", "carencia", "limitación" |
| "abanico" (de posibilidades) | Metáfora gastada | "conjunto", "variedad" |
| "tapiz" (tapestry) | Metáfora IA pura | Eliminar la metáfora directamente. |

### Adjetivos y adverbios

| Palabra | Frecuencia IA vs humano | Alternativa |
|---|---|---|
| "holístico" | Muy alta | "integral", "completo", "global" |
| "sin precedentes" | Muy alta | "nuevo", "no explorado previamente" |
| "robusto" (genérico) | Alta | "tolerante a X", "estable ante Y" |
| "significativo" (sin test) | Alta, implica significancia estadística | "notable", "considerable", "de X puntos" |
| "intrincado" (intricate) | 100x más en IA | "complejo" |
| "pivotal" | 182x más en IA | "clave", "central" |
| "crucial" | 182x más en IA | "importante", "clave" |
| "exhaustivo" | Alta | "completo", "detallado" |
| "meticuloso" | Alta | "cuidadoso", "preciso" |
| "inequívoco" | Alta | "claro" |
| "fundamental" (para todo) | Muy alta | Reservar para lo que genuinamente lo sea. |
| "de vanguardia" | Alta | "reciente", "avanzado" |
| "sin fisuras" (seamless) | Alta | "fluido", "integrado" |
| "innovador" | Alta | Describir la innovación concreta. |
| "multifacético" | Muy alta | "variado", "diverso" |
| "matizado" (nuanced) | Muy alta | "con matices" solo si es necesario. |
| "palpable" | 100x más en IA | Eliminar o describir concretamente. |

### Verbos

| Verbo | Frecuencia IA vs humano | Alternativa |
|---|---|---|
| "profundizar" (delve) | 269x más en IA | "examinar", "analizar" |
| "aprovechar" (leverage) | Muy alta | "usar", "utilizar" |
| "potenciar" (empower) | Alta | "mejorar", "facilitar" |
| "impulsar" (foster/drive) | Alta | "promover", "contribuir a" |
| "optimizar" | Alta | "mejorar" (salvo contexto técnico preciso) |
| "desbloquear" (unlock) | Alta | "permitir", "hacer posible" |
| "alinearse con" | 16x más en IA | "corresponder a", "coincidir con" |
| "evidenciar" (por "mostrar") | Alta | "mostrar" directamente |
| "fomentar" | Alta | "promover" |
| "navegar" (como metáfora) | Muy alta | "gestionar", "afrontar" |
| "implementar" (para ideas) | Alta | "aplicar", "poner en práctica", "adoptar" |

---

## 5. Aperturas y cierres mecánicos

### Aperturas que delatan IA

| Antipatrón | Por qué es malo |
|---|---|
| "En el vasto mundo de la X..." | Apertura genérica y grandilocuente. |
| "Desde tiempos inmemoriales..." | Innecesario y casi siempre falso. |
| "En la era digital actual..." | Cliché. |
| "A lo largo de la historia..." | Vago y rara vez relevante. |
| "En los últimos años, X ha experimentado un crecimiento exponencial..." | "Exponencial" rara vez es literal. |
| "En el mundo actual de X..." | Variante de "en la era digital". |
| "En el ámbito de X, Y ha cobrado una relevancia sin precedentes" | Combina muletilla + léxico IA + grandilocuencia. |
| "Cuando hablamos de X, nos referimos a..." | Innecesariamente didáctico. |
| "Si hay algo que ha transformado X, es Y" | Estructura "if there's one thing" típica de IA. |
| "X no es solo Y, sino también Z" | Estructura "not only... but also" sistemática. |
| "Imagina un mundo donde..." | Apertura de promesa vacía. |
| "Un ejemplo ilustra..." / "Un ejemplo representativo es..." / "Este caso ilustra..." | Introducciones artificiales a ejemplos. Ir directamente al ejemplo: "Para la entrada X, el sistema produce Y". |

**Regla**: Empieza con el tema concreto, no con una panorámica histórica o filosófica.

### Cierres formulaicos

| Antipatrón | Alternativa |
|---|---|
| "En conclusión, podemos afirmar que..." | Cerrar con la implicación concreta del trabajo. |
| "En resumen, se ha demostrado que..." | Si hace falta recapitular, hacerlo sin anunciar que se recapitula. |
| "Todo lo anterior demuestra que..." | Dejar que el lector llegue a esa conclusión. |
| "Como se ha visto a lo largo de esta sección..." | Redundante. El lector acaba de leerla. |

---

## 6. Transiciones artificiales

| Antipatrón | Alternativa |
|---|---|
| "Dicho esto," | Eliminar o reformular la conexión. |
| "Teniendo en cuenta lo anterior," | Hacer la conexión implícita. |
| "En este orden de ideas," | No es español natural. Eliminar. |
| "Habiendo analizado X, ahora procederemos a examinar Y." | Empezar directamente con Y. |
| "En la siguiente sección se abordará..." | Empezar la siguiente sección directamente. |
| "Como se mencionó anteriormente," | Integrarlo en la nueva oración sin anunciarlo. |
| "Además" (en cada párrafo) | En IA es la transición por defecto. Limitar a 1-2 usos por capítulo. |
| "Por otro lado" (sin contraposición real) | Eliminar si no hay contraste genuino. |
| "Así pues" (vacío) | Hacer la conexión causal explícita o eliminar. |
| "Es por ello que" | Transición causal forzada. Reformular. |
| "En esta línea" | Variante de "en este sentido". Eliminar. |
| "En efecto" (Indeed) | Confirmación innecesaria. Eliminar. |
| "De hecho" (abusado) | Reservar para datos que genuinamente sorprendan. |

**Regla**: La mejor transición es una conexión lógica implícita entre el último párrafo de una sección y el primero de la siguiente.

---

## 7. Repetición semántica

Decir lo mismo con otras palabras, ya sea dentro de un párrafo, entre párrafos, o entre secciones.

**Mal** (mismo párrafo):
"El sistema genera oraciones correctas gramaticalmente. Las frases producidas por el sistema respetan las reglas de la gramática española."

**Mal** (entre secciones):
- Sección 3.1: "El corpus contiene 232 pictogramas organizados en 9 categorías."
- Sección 4.2: "Se utilizan 232 pictogramas, clasificados en 9 categorías diferentes."

**Regla**: Cada dato y cada idea se explican una sola vez en el lugar más apropiado. Las demás secciones pueden referirse a ello brevemente o con una referencia cruzada, pero sin repetir la explicación.

---

## 8. Patrones de puntuación

### Abuso de la raya (em dash) — SEÑAL DE IA MÁS DOCUMENTADA

GPT-4o usa rayas **10 veces más** que GPT-3.5. Un escritor humano usa una raya cada ~500 palabras; los LLMs las insertan cada ~50-80 palabras. Un estudio de Carnegie Mellon (2025) confirmó que los patrones de puntuación, especialmente las rayas, permiten identificar texto generado por IA con alta fiabilidad. OpenAI reconoció el problema en noviembre de 2025 permitiendo a los usuarios pedir explícitamente que ChatGPT no use rayas. El término "GPT-ismo" se acuñó en 2025 para referirse a este abuso.

**Mal**: "El sistema ---que fue diseñado para maximizar la cobertura--- genera oraciones ---en muchos casos correctas--- que los evaluadores ---tanto expertos como no expertos--- consideraron naturales."

**Bien**: "El sistema, diseñado para maximizar la cobertura, genera oraciones que los evaluadores (tanto expertos como no expertos) consideraron naturales en la mayoría de los casos."

**Jerarquía de la RAE para incisos** (de menor a mayor aislamiento):

| Signo | Nivel de aislamiento | Usar para |
|---|---|---|
| Comas (,) | Bajo | Aclaraciones breves, ligadas al hilo principal |
| Rayas (---) | Medio | Incisos que merecen énfasis pero siguen siendo parte del argumento |
| Paréntesis ( ) | Alto | Datos suplementarios, referencias, fechas, siglas |

**Dos puntos (:)** son a menudo la mejor alternativa cuando se introduce una explicación, lista o consecuencia: justo donde la IA pondría una raya, los dos puntos son más naturales en español académico.

**Reglas**:
- Máximo **una raya (un par de rayas) por párrafo**. Si hay más de una, sustituir por comas o paréntesis.
- Máximo **3 rayas en una sección de 500 palabras**. Por encima de eso, el texto suena a IA.
- Antes de escribir una raya, preguntarse: ¿funcionaría mejor una coma, un paréntesis o dos puntos?
- Las rayas son legítimas para incisos de longitud media que requieren más separación visual que una coma. No están prohibidas; están sobreusadas.

### Abuso de los dos puntos en títulos

La IA usa compulsivamente la estructura "Título: Subtítulo" y dentro del texto "Concepto: explicación".

**Mal**: "Fase 1: Análisis de entrada: Procesamiento de pictogramas"

**Bien**: "Análisis de la entrada" o "Procesamiento de pictogramas en la primera fase"

### Formas largas innecesarias

La IA usa sistemáticamente formas largas donde el español natural prefiere formas cortas.

| Forma IA | Forma natural |
|---|---|
| "con el fin de" | "para" |
| "llevar a cabo" | "hacer", "realizar" |
| "con anterioridad" | "antes" |
| "con posterioridad" | "después" |
| "en la actualidad" | "hoy", "actualmente" |
| "a lo largo de" | "durante" |
| "dar comienzo a" | "empezar", "iniciar" |
| "hacer uso de" | "usar" |
| "tener la capacidad de" | "poder" |

---

## 9. Antítesis y negación sistemática

La IA usa compulsivamente la estructura "No es X, es Y" o "No solo X, sino Y" para aparentar profundidad. En retórica clásica esto es "antítesis" y es un recurso potente, pero la IA lo convierte en muletilla.

| Antipatrón | Ejemplo |
|---|---|
| "No se trata solo de X, sino de Y" | "No se trata solo de generar texto, sino de generar texto natural" |
| "No es simplemente X, es Y" | "No es simplemente una gramática, es un sistema completo" |
| "Más allá de X, Y" | "Más allá de la precisión, la naturalidad es clave" |
| "X no es solo Y: es Z" | "Dixi no es solo una aplicación: es una herramienta de inclusión" |

**Regla**: Si usas esta estructura más de una vez en todo el documento, probablemente sobra.

---

## 10. Abuso del gerundio (específico del español)

Los modelos, entrenados predominantemente en inglés (donde el gerundio es mucho más versátil), producen gerundios incorrectos o forzados en español.

| Uso incorrecto | Corrección |
|---|---|
| "El sistema generando oraciones correctas" (gerundio como adjetivo del sujeto) | "El sistema genera oraciones correctas" o "El sistema, que genera oraciones correctas, ..." |
| "Se propone una técnica mejorando la precisión" (gerundio de posterioridad) | "Se propone una técnica que mejora la precisión" |
| "Obteniendo resultados satisfactorios" (inicio de oración) | "Se obtuvieron resultados satisfactorios" |
| "Los pictogramas siendo procesados por el módulo" (being + participle) | "Los pictogramas que procesa el módulo" |

**Regla**: El gerundio en español expresa simultaneidad o modo. Si no lo hace, usar una oración de relativo o una forma conjugada.

---

## 11. Adjetivos descriptivos por defecto

La IA recurre a adjetivos positivos genéricos donde un humano sería más específico. En un TFG, esto produce afirmaciones vacías que suenan a marketing.

| Antipatrón | Alternativa |
|---|---|
| "Una solución elegante" | Describir por qué funciona. |
| "Un resultado satisfactorio" | Dar el dato numérico. |
| "Una interfaz intuitiva" | Describir qué la hace fácil de usar. |
| "Un algoritmo eficiente" | Dar la complejidad o el tiempo. |
| "Un enfoque prometedor" | Explicar qué resultados iniciales lo sugieren. |
| "Una implementación robusta" | Describir ante qué es tolerante. |

**Regla**: Si un adjetivo no aporta información concreta y verificable, eliminarlo o sustituirlo por un dato.

---

## 12. Voz pasiva excesiva

Los LLMs usan construcciones pasivas 3-5 veces más que escritores humanos. En español, esto se combina con el abuso de la pasiva refleja ("se observa", "se determina", "se evidencia") y de las impersonales.

**Mal**: "Fue determinado que los resultados obtenidos fueron considerados como satisfactorios por los evaluadores."

**Bien**: "Los evaluadores consideraron satisfactorios los resultados."

En escritura académica española, la pasiva refleja es natural y apropiada ("se observa que", "se propone un método"). El problema es cuando cada oración de un párrafo empieza con "se + verbo".

**Regla**: Varía las construcciones. Alterna pasiva refleja, sujeto activo y formas impersonales. Si tres oraciones seguidas empiezan con "se", reescribe al menos una.

---

## 13. Densidad nominal excesiva

Investigación publicada en PNAS demuestra que los LLMs instruction-tuned tienen un estilo "noun-heavy": denso en sustantivos, con menos verbos, menos adjetivos y menos adverbios que los humanos. Esto produce cadenas nominales poco legibles.

**Mal**: "La implementación de la funcionalidad de generación de texto a partir de secuencias de pictogramas mediante técnicas de procesamiento de lenguaje natural..."

**Bien**: "El módulo genera texto a partir de secuencias de pictogramas usando técnicas de PLN."

**Regla**: Si una frase tiene más de tres preposiciones encadenadas ("de... de... de... de..."), reestructurarla con verbos activos.

---

## 14. Baja perplejidad y predicibilidad

La IA tiende a elegir siempre la palabra más probable estadísticamente, produciendo texto que "suena correcto pero obvio". Un humano introduce elecciones léxicas inesperadas, opiniones, matices o metáforas originales que un modelo no seleccionaría.

Esto no es un antipatrón que se pueda detectar palabra por palabra, sino una propiedad global del texto. Se manifiesta como:

- Vocabulario previsible: siempre la misma palabra para el mismo concepto.
- Ausencia de voz propia: el texto podría ser de cualquier autor.
- Falta de opinión: todo es descriptivo, nada es argumentativo.

**Regla**: Introduce tu perspectiva. Usa la palabra que tú usarías, no la más "segura". Si describes un enfoque que no funcionó, di por qué crees que no funcionó, no solo que "presenta limitaciones".

---

## 15. Frases de apertura de párrafo estadísticamente anómalas

GPTZero encontró que ciertas frases aparecen con frecuencia estadísticamente anómala al inicio de párrafos en texto IA:

| Frase | Frecuencia IA/humano |
|---|---|
| "Pese a los desafíos" / "A pesar de enfrentar" | Muy alta |
| "En la era digital actual" | Muy alta |
| "Con el objetivo de comprender" | Alta |
| "Esto pone de manifiesto" | 20x |
| "El objetivo de este estudio" | 50x+ |
| "Es importante destacar que" | Muy alta |

**Regla**: Varía las aperturas de párrafo. Si dos párrafos consecutivos empiezan con el mismo patrón sintáctico, reescribe uno.

---

## Cómo usar este catálogo

1. **Antes de escribir**: Lee el catálogo para activar tu "radar" de antipatrones.
2. **Después de escribir**: Recorre cada categoría y busca coincidencias en tu texto.
3. **Si encuentras uno**: Reescribe el fragmento siguiendo la alternativa sugerida.
4. **Duda razonable**: Si un patrón listado aquí es genuinamente la mejor forma de expresar algo en un contexto concreto, úsalo. Esto es una guía, no una lista de palabras prohibidas.
