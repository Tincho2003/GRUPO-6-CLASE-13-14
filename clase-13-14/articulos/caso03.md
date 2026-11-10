# Cliente 3 — EcoFood

### Situación

La empresa **EcoFood** quiere lanzar una nueva línea de productos alimenticios sostenibles en Buenos Aires. Antes de realizar la inversión, necesita comprender cómo está evolucionando el mercado, qué productos tienen mayor potencial, qué características valoran los consumidores y qué oportunidades existen para diferenciarse frente a la competencia.

El equipo deberá analizar diferentes fuentes de información para identificar tendencias de consumo saludable, sostenible y responsable.

## Datos

Cada integrante del equipo investiga una dimensión distinta del problema, pero la extracción de la base de establecimientos es una sola y compartida: la hace la persona a cargo del punto 1 y el resto trabaja sobre esa misma base para no duplicar el trabajo ni terminar con estructuras que no se puedan cruzar.

### 1. Oferta gastronómica y mercado actual

- **Fuente concreta:** el dataset abierto "Oferta y Establecimientos Gastronómicos" del Gobierno de la Ciudad de Buenos Aires (`data.buenosaires.gob.ar/dataset/oferta-establecimientos-gastronomicos`) se descarga directo en CSV, sin necesidad de scraping, e incluye rubro, dirección, barrio y comuna de cada local.
- **Datos a obtener:** cantidad y distribución de establecimientos, tipos de oferta disponibles, categorías de negocios, ubicación geográfica y concentración por zonas.

Ejemplos de análisis:

- ¿Qué barrios tienen mayor presencia de propuestas saludables o alternativas?
- ¿Existen zonas con potencial de crecimiento?
- ¿Qué categorías gastronómicas tienen mayor presencia?

### 2. Tendencias de consumo saludable y sostenible

- **Fuente concreta:** Google Trends filtrado a Argentina, vía la librería `pytrends`. Tengan en cuenta que no es una API oficial y puede fallar sin aviso — conviene guardar una captura de los datos apenas los consigan, en vez de volver a pedirlos si el instructor los necesita revisar después.
- **Datos a obtener:** evolución del interés por conceptos como alimentación saludable, productos orgánicos, veganismo, productos sin TACC, café de especialidad y alimentos naturales.

Ejemplos de análisis:

- ¿Qué tendencias están creciendo?
- ¿Qué conceptos generan mayor interés?
- ¿Cómo evolucionaron las preferencias de los consumidores?

### 3. Opinión y percepción de consumidores

- **Fuentes posibles:** reseñas gastronómicas públicas. Antes de scrapear cualquier plataforma (Google Maps, TripAdvisor, etc.) revisen `robots.txt` y términos de uso — la mayoría restringe el acceso automatizado. Si el sitio elegido lo permite, adelante.
- **Datos a obtener:** opiniones de consumidores, valoración de productos, sentimiento de comentarios y principales temas mencionados.

Ejemplos de análisis:

- ¿Qué valoran más los consumidores?
- ¿Qué problemas aparecen con frecuencia?
- ¿El precio es una barrera para adoptar productos sostenibles?

### 4. Análisis de competencia y oportunidades

Este punto no sale a buscar una fuente nueva: es un corte distinto sobre el mismo dataset del punto 1, filtrado por rubro y categoría, para ver qué está sobrerrepresentado en el mercado y qué falta.

- **Datos a obtener:** distribución de categorías dentro de la oferta "saludable/sostenible" (identificada a partir del rubro del establecimiento), concentración geográfica de esas categorías, y — si el tiempo alcanza — precios de referencia de un puñado de marcas o locales conocidos del rubro, relevados manualmente en vez de scrapeados, dado el volumen chico que hace falta.

Ejemplos de análisis:

- ¿Qué productos están poco representados en el mercado?
- ¿Qué oportunidades existen para diferenciar una nueva marca?
- ¿Qué segmentos parecen tener mayor potencial?

## Objetivo

Identificar zonas y categorías de Buenos Aires con mayor potencial para el lanzamiento de una línea de productos alimenticios sostenibles.

## Cómo se arma la síntesis final

Usen el bloque de "narrativa e insights" de la clase 2 para que cada integrante presente su hallazgo más fuerte (2-3 minutos, sin slides) y luego decidan en conjunto cuáles de esos hallazgos se convierten en los 3 insights ejecutivos, revisando entre todos si hay una explicación alternativa antes de darlos por buenos. Por ejemplo: si un barrio muestra "poca oferta saludable", chequeen si no es simplemente un barrio con poca oferta gastronómica en general antes de llamarlo oportunidad.

## Bonus

- ¿Dónde hay alta búsqueda (punto 2) pero baja oferta instalada (punto 1)? Ese cruce suele señalar la oportunidad de negocio más concreta de todo el análisis.
- ¿Qué zonas de Buenos Aires presentan mayor oportunidad comercial combinando ambos factores?