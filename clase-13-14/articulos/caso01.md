# Cliente 1 — TalentHub

## Situación

La empresa tecnológica **TalentHub** planea lanzar un nuevo bootcamp de formación profesional orientado al mercado laboral actual. Antes de definir el programa académico, necesita entender qué conocimientos, tecnologías y habilidades están siendo más demandadas por las empresas para asegurar que sus estudiantes desarrollen competencias alineadas con las oportunidades reales de empleo.

El equipo necesita analizar el mercado laboral tecnológico para identificar tendencias, perfiles buscados y herramientas con mayor demanda.

## Datos

Cada integrante del equipo se enfoca en una dimensión distinta del problema, pero **la extracción de datos es una sola y compartida**: una persona del equipo lidera la obtención (API, scraping o dataset abierto) y deja el dataset crudo disponible en `data/raw/` para que el resto trabaje sobre esa misma base. Esto evita que cuatro integrantes scrapeen el mismo portal en paralelo — algo que además de ineficiente puede terminar bloqueando al equipo si el sitio detecta el exceso de requests — y asegura que los cuatro análisis se puedan cruzar entre sí al final, porque parten de la misma estructura de datos.

### 1. Tecnologías y habilidades más demandadas

- **Fuentes posibles:** APIs de empleo, portales laborales, datasets de ofertas de trabajo, scraping de sitios que permitan extracción de datos (recordá revisar `robots.txt` y términos de uso antes de scrapear).
- **Datos a obtener:** Títulos de puestos, tecnologías mencionadas, lenguajes de programación, frameworks, herramientas y habilidades técnicas requeridas.

### 2. Perfil del profesional buscado

- **Fuente:** el mismo dataset extraído en el punto 1.
- **Datos a obtener:** Años de experiencia solicitados, nivel de seniority, formación académica, certificaciones, idiomas y habilidades blandas requeridas.

### 3. Tendencias del mercado tecnológico

- **Fuente:** el mismo dataset extraído en el punto 1, complementado si hace falta con reportes públicos o datasets abiertos de series históricas.
- **Datos a obtener:** Evolución de la demanda de tecnologías, crecimiento de nuevos perfiles profesionales, herramientas emergentes y cambios en las necesidades del mercado.

### 4. Comparación de perfiles profesionales

Este punto no es una fuente de datos nueva: es una síntesis que se arma con los datos ya extraídos en 1 y 2, segmentados por rol. Arranca una vez que esos dos análisis tienen resultados, no en paralelo.

- **Datos a obtener:** comparación entre roles tecnológicos —

  - Data Analyst
  - Data Scientist
  - Full Stack Developer
  - QA Engineer
  - Cloud Engineer

  Analizar diferencias en tecnologías solicitadas, experiencia requerida, herramientas utilizadas, modalidad de trabajo (remoto/híbrido/presencial) y demanda relativa del mercado.

  Salario **no** es un dato confiable de partida: la mayoría de los portales de empleo en LatAm no lo publica en la oferta. Si el equipo quiere incluirlo, va como bonus, cruzando con una fuente separada que sí lo tenga (por ejemplo, encuestas salariales públicas del sector, como la de Sysarmy en Argentina).

## Objetivo

Identificar las habilidades más demandadas por el mercado.

## Cómo se arma la síntesis final

Los 3 insights ejecutivos que pide la Consulting Week no son cuatro reportes individuales pegados uno al lado del otro — son el resultado de que el equipo cruce sus cuatro análisis y decida juntos qué contar. Para eso, usen el bloque de "narrativa e insights" de la clase 2 así:

Los primeros 15-20 minutos, cada integrante presenta al resto su hallazgo más fuerte de su dimensión — 2 o 3 minutos, sin slides, solo "esto encontré y por qué le importa a TalentHub". Los 30 minutos restantes el equipo completo decide en conjunto cuáles de esos cuatro candidatos se convierten en los 3 insights finales, y ahí mismo — entre todos, no cada uno revisando el suyo — hacen el ejercicio de buscar una explicación alternativa para cada hallazgo antes de darlo por bueno. Cruzar miradas en este paso es más efectivo que hacerlo en solitario: lo que a quien encontró el patrón le puede parecer obvio, a otro integrante del equipo se le puede ocurrir cuestionarlo.

## Bonus

Detectar oportunidades y tendencias:

- ¿Qué tecnologías tienen mayor crecimiento?
- ¿Qué habilidades aparecen juntas con mayor frecuencia?
- ¿Qué perfiles tienen mayor demanda?