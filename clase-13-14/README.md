# Consulting challenge - Data Analytics Lab

Durante esta semana actuarán como una consultora de datos contratada por un cliente. Su misión **no es generar gráficos**. Su misión es **resolver un problema de negocio utilizando datos**.

Cada equipo recibirá un brief de cliente y deberá:

* Obtener datos.
* Limpiar datos.
* Analizarlos.
* Generar visualizaciones.
* Elaborar recomendaciones.
* Presentar hallazgos ejecutivos.

## Cronograma y Checkpoints

Esta no es una semana de días libres. El formato real son dos clases presenciales de 3 horas con trabajo autónomo del equipo en el medio. Eso significa que el tiempo en el aula es el recurso más escaso de todo el ejercicio, no alcanza para improvisar, así que cada bloque tiene un entregable mínimo que el instructor valida antes de cerrar la clase. Si un equipo no llega a un checkpoint, no seguimos como si nada, se ajusta el alcance ahí mismo (menos registros, menos variables, un análisis más acotado) para llegar a un cierre completo, aunque más chico.

### Clase 13 (3 horas)

Foco: pasar de "tenemos un cliente" a "tenemos un dataset limpio". Toda la clase gira en conseguir y validar los datos, porque sin eso no hay nada que analizar en la segunda clase.

| Bloque | Actividad | Checkpoint de salida |
| --- | --- | --- |
| 1 | Presentación del brief de cliente, formación de roles dentro del equipo | Cada integrante sabe qué parte del pipeline lidera |
| 2 | Obtención de datos (API, scraping o dataset abierto) | Dataset crudo guardado en `data/raw/`, con fuente documentada y volumen mínimo definido por el instructor |
| 3 | Limpieza y validación | Dataset limpio en `data/processed/`, con nulos/duplicados resueltos y tipos de datos correctos |
| 4 | Cierre: qué queda para la casa | Equipo sale con al menos 2 preguntas de negocio para explorar en el EDA |

**Trabajo autónomo:** avanzar el EDA inicial con las preguntas definidas en el cierre de la clase 13. No hace falta llegar con el análisis terminado, sí con las primeras distribuciones y relaciones entre variables exploradas, para no arrancar la clase 14 de cero.

### Clase 14 (3 horas)

Foco: convertir el análisis en una historia que un cliente pueda usar para decidir algo.

| Bloque | Actividad | Checkpoint de salida |
| --- | --- | --- |
| 1 | Cierre del EDA: estadística descriptiva, distribuciones, outliers | Notebook con al menos 2 hipótesis de negocio contrastadas contra los datos |
| 2 | Narrativa e insights | 3 hallazgos redactados en formato "insight de negocio" (no estadístico), cada uno con al menos una explicación alternativa descartada |
| 3 | Armado del deck ejecutivo | Presentación de máximo 10 slides completa |
| 4 | Ensayo y presentación | Cada equipo presenta ante la clase (o el instructor en rol de cliente) |

Si un equipo llega al bloque 3 sin hallazgos sólidos, prioricen cerrar uno o dos insights bien argumentados antes que forzar los tres. Un hallazgo bien sustentado vale más que tres apurados.

# Entregables

Al finalizar la semana, cada equipo deberá entregar:

## 1. Repositorio GitHub

El repositorio deberá contener una estructura similar a la siguiente:

```text
consulting-challenge/
│
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── images/ <--- en caso de que haya
├── presentation/
└── README.md
```

### README.md

El README debe incluir:

* Descripción del proyecto.
* Objetivo del cliente.
* Fuente de datos.
* Metodología utilizada.
* Principales hallazgos.
* Recomendaciones.
* Instrucciones para reproducir el análisis.

## 2. Notebook de Análisis

El notebook debe documentar claramente todo el proceso.

### Obtención de Datos

* API pública.
* Web Scraping.
* Dataset público.

**Nota sobre scraping:** antes de scrapear cualquier sitio, revisen su `robots.txt` y sus términos de uso ([ver articulo de web scrapping y revision del archivo `robots.txt`](./articulos/web-scrapping-y-robots.md)). Si el sitio bloquea el acceso automatizado, no insistan tratando de evadirlo — es momento perdido que no suma al objetivo del ejercicio. No hay un dataset de respaldo preparado para estos casos: conseguir el dato, y resolver cuando una fuente falla, es parte del desafío. Si una fuente los bloquea, busquen otra (una API distinta, un dataset abierto equivalente) en vez de insistir contra el bloqueo.

### Limpieza

* Tratamiento de valores nulos.
* Eliminación de duplicados.
* Conversión de tipos de datos.
* Validación de calidad de datos.

### Exploratory Data Analysis (EDA)

* Estadística descriptiva.
* Distribuciones.
* Relaciones entre variables.
* Detección de outliers.

### Hallazgos

El notebook debe explicar claramente qué se descubrió y por qué es importante. Para cada hallazgo, el notebook debe registrar al menos una explicación alternativa que se consideró y por qué se descartó (ver "Qué esperamos ver").

## 3. Presentación Ejecutiva

Máximo 10 diapositivas. No se evalúa la cantidad de gráficos, se evalúa la capacidad de comunicar hallazgos y recomendaciones.

## Qué esperamos ver

No esperamos algo como: `"La media es 53.2"`

Esperamos algo como: `"Los inmuebles de Palermo presentan un valor por m² 18% inferior a zonas comparables, representando una posible oportunidad de inversión."` La diferencia entre un analista y un consultor es la capacidad de convertir datos en decisiones.

**Pero cuidado:** un consultor tampoco convierte cualquier diferencia en una recomendación. Antes de escribir un insight como el de arriba, pregúntense: ¿esa diferencia de precio podría explicarse por antigüedad del inmueble, tamaño promedio, o composición de la muestra, en vez de por una oportunidad real? Si no pueden descartar al menos una explicación alternativa con los propios datos, el hallazgo todavía es una hipótesis, no una recomendación.

# Estructura Recomendada de la Presentación

El ejemplo de abajo usa un cliente ficticio (Urban Capital) que no es ninguno de los casos asignados — es solo para mostrar el formato y el tipo de insight esperado, no para copiar. Reemplacen el contenido por el de su propio cliente.

### Slide 1 — Portada

```text
Proyecto:
Análisis del Mercado Inmobiliario

Consultora:
Data Insights Group
```

### Slide 2 — Problema del Cliente

```text
Cliente:
Urban Capital

Objetivo:
Identificar zonas con potencial de inversión inmobiliaria.
```

### Slide 3 — Datos Utilizados

```text
Fuente:
Portal inmobiliario

Registros:
4.532 propiedades

Variables:
Precio
Metros cuadrados
Barrio
Ambientes
```

### Slide 4 — Metodología

```text
1. Extracción
2. Limpieza
3. EDA
4. Visualización
5. Recomendaciones
```

### Slide 5 — Hallazgo #1

```text
Incluir gráfico.

Insight: Palermo muestra precios 15% inferiores al promedio esperado para propiedades equivalentes.
```

### Slide 6 — Hallazgo #2

```text
Incluir gráfico.

Insight: Belgrano presenta mayor estabilidad de precios.
```

### Slide 7 — Hallazgo #3

```text
Incluir gráfico.

Insight: Las propiedades de 2 ambientes tienen mayor rotación.
```

### Slide 8 — Recomendaciones

```text
1. Priorizar Palermo.
2. Focalizar inmuebles de 2 ambientes.
3. Monitorear evolución trimestral.
```

### Slide 9 — Riesgos y Limitaciones

```text
- Muestra limitada.
- Datos públicos.
- No se incluyeron costos notariales.
```

### Slide 10 — Resumen Ejecutivo

```text
✓ Qué descubrimos
✓ Qué significa para el negocio
✓ Qué recomendamos hacer
```

# Casos Disponibles

Cada equipo recibirá un cliente distinto. No hay dataset de respaldo: conseguir el dato es parte del desafío, incluyendo resolver cuando una fuente falla o bloquea el acceso.

- [Cliente 1 — TalentHub](./articulos/caso01.md)
- [Cliente 2 — CineMetrics](./articulos/caso02.md)
- [Cliente 3 — EcoFood](./articulos/caso03.md)

## ¿Qué hace un equipo excelente?

Un equipo excelente no es el que produce más gráficos. Un equipo excelente es el que logra responder:

> ¿Qué debería hacer el cliente mañana basándose en estos datos?

Si su análisis permite tomar una decisión concreta, han cumplido el objetivo de esta Consulting challenge.

## Filosofía de la Consulting challenge

En la vida real los clientes no entregan datasets perfectos. Los clientes entregan problemas. Su trabajo como analistas consiste en:

1. Conseguir los datos necesarios.
2. Validar su calidad.
3. Analizarlos.
4. Extraer conclusiones.
5. Transformar esas conclusiones en recomendaciones accionables.

Ese es exactamente el trabajo que realizarán durante esta experiencia.