# Cliente 2 — CineMetrics

### Situación

La empresa cinematográfica **CineMetrics** quiere evaluar el desempeño de **A Minecraft Movie** (2025) para decidir si continuar invirtiendo en producciones similares — adaptaciones de videojuegos con presupuestos altos.

El equipo necesita entender no solo si la película fue rentable, sino también cómo fue recibida por el público, la crítica especializada y la conversación generada alrededor del estreno. Este caso es especialmente interesante porque la crítica y el público no coincidieron: la prensa especializada la calificó bastante mal, mientras que la audiencia la disfrutó y generó un fenómeno viral en redes sociales. Esa brecha entre crítica y público es justamente el tipo de matiz que CineMetrics necesita entender antes de decidir si vale la pena repetir la fórmula.


## Datos

Cada integrante del equipo investiga una dimensión distinta del problema. Coordinen la extracción entre ustedes: si dos personas necesitan el mismo tipo de dato (por ejemplo, presupuesto y recaudación), que lo saque una sola vez y lo comparta, en vez de duplicar llamadas a la misma API.

### 1. Desempeño comercial

- **Fuentes concretas:** la API de TMDB (The Movie Database) y la de OMDb son gratuitas, públicas, y devuelven presupuesto, recaudación, fecha de estreno y popularidad sin necesidad de scraping. Ambas piden solo registrarse para obtener una API key.
- **Datos a obtener:** presupuesto estimado, recaudación total, fecha de estreno, popularidad, y comparación con otras adaptaciones de videojuegos o películas familiares del mismo año.

### 2. Impacto y tendencias

- **Fuentes concretas:** Google Trends para evolución del interés de búsqueda antes/después del estreno (la librería `pytrends` es la forma más común de automatizar esto en Python, pero **no es una API oficial de Google** — puede fallar o dar rate-limit sin aviso, así que conviene tener también una captura manual de los datos como respaldo). Noticias y cobertura de medios especializados en cine para contexto cualitativo.
- **Datos a obtener:** evolución del interés antes y después del estreno, picos de búsqueda relacionados con momentos virales, temas asociados a la película.

### 3. Opinión del público

- **Fuentes concretas:** la API de Reddit (vía la librería `praw`) permite extraer comentarios de los subreddits relevantes, pero exige registrar una app de desarrollador antes de poder hacer la primera consulta — no lo dejen para el día de la clase, háganlo como tarea del cierre de la clase 1. Rotten Tomatoes y Metacritic tienen reseñas públicas, pero revisen sus términos de uso antes de scrapear directamente: si están restringidos, usen los scores agregados que sí exponen las APIs de TMDB/OMDb en vez de extraer las reseñas completas.
- **Datos a obtener:** calificaciones de crítica vs. audiencia, comentarios, sentimiento de las opiniones (positivo/negativo), y principales temas mencionados — presten especial atención a dónde diverge la crítica de la audiencia, porque ahí está el hallazgo más interesante de este caso.

## Objetivo

Determinar si "A Minecraft Movie" fue una inversión exitosa para CineMetrics y si el patrón (crítica dividida, audiencia entusiasta, fenómeno viral) es replicable o fue un caso puntual.

## Cómo se arma la síntesis final

Usen el bloque de "narrativa e insights" de la clase 2 para que cada integrante presente su hallazgo más fuerte (2-3 minutos, sin slides) y luego el equipo completo decida en conjunto cuáles de esos hallazgos se convierten en los 3 insights ejecutivos, revisando entre todos si hay una explicación alternativa antes de darlos por buenos. En este caso en particular, tengan cuidado con una explicación alternativa obvia: que la audiencia haya sido mayoritariamente familiar/infantil (por el rating y el marketing) no necesariamente predice el mismo resultado en una producción con otro público objetivo.

## Bonus

- ¿Qué otras adaptaciones de videojuegos o franquicias familiares tuvieron un patrón similar (crítica floja, público entusiasta) y cuáles no?
- ¿El fenómeno viral en redes (el meme del "Chicken Jockey") tuvo un efecto medible en la recaudación de las semanas siguientes al pico de conversación?