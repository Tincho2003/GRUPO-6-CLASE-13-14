# Web scraping: cómo armar un bot para extraer datos (y por qué revisar robots.txt antes de correrlo)

Cuando necesitás datos para un análisis y no existe una API que te los entregue prolijamente en JSON, la alternativa es ir a buscarlos donde ya están: en el HTML de un sitio web. Eso es scraping — escribir un programa que visita una página, lee su estructura, y extrae la información que te interesa, en vez de que un humano copie y pegue precio por precio a mano.

Es una herramienta enorme para un consultor de datos. Portales inmobiliarios, catálogos de e-commerce, ofertas de empleo: gran parte del dato que necesitás para responder una pregunta de negocio vive publicado en una página, no en un dataset descargable. Pero justamente porque es tan directo — "visitá este sitio y traeme todo" — es fácil olvidarse de que del otro lado hay un servidor con reglas, costos, y a veces una postura explícita sobre si quiere que lo hagas.

## Cómo funciona un scraper por dentro

En su forma más simple, un scraper hace tres cosas: pide una página, la interpreta como estructura (no como texto plano), y extrae los pedazos que te interesan.

El primer paso es una request HTTP común, la misma que hace tu navegador cuando entrás a una URL:

```python
import requests

respuesta = requests.get("https://ejemplo.com/propiedades")
html = respuesta.text
```

Lo que llega en `html` es el mismo código fuente que verías con "ver código fuente" en el navegador: una maraña de etiquetas anidadas. Ahí es donde entra el segundo paso — parsear ese HTML para poder navegarlo como estructura, en vez de como un bloque de texto. La librería más usada en Python para esto es BeautifulSoup:

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
```

Con el HTML ya parseado, el tercer paso es encontrar los elementos que contienen el dato que buscás. Para eso necesitás mirar la página con las herramientas de desarrollador del navegador (clic derecho → "Inspeccionar") e identificar qué etiqueta y qué clase envuelve, por ejemplo, el precio de cada propiedad:

```python
propiedades = soup.find_all("div", class_="propiedad-card")

for propiedad in propiedades:
    precio = propiedad.find("span", class_="precio").text
    barrio = propiedad.find("span", class_="barrio").text
    print(precio, barrio)
```

Este patrón — request, parseo, extracción — es el esqueleto de prácticamente cualquier scraper simple. Lo que cambia de un sitio a otro son las etiquetas y clases específicas que tenés que identificar inspeccionando la página, y algunas complicaciones que aparecen seguido en la práctica: sitios que cargan el contenido con JavaScript después de la carga inicial (ahí `requests` no alcanza y necesitás algo como Selenium o Playwright, que sí ejecutan el JavaScript de la página), paginación (tenés que iterar sobre varias URLs, no solo una), y estructuras que cambian levemente entre elementos, lo que rompe tu scraper si no lo escribís con tolerancia a esos casos.

## Antes de correrlo: qué te está diciendo el sitio

Ahora que ya tenés la mecánica — un script que puede pedir cualquier página pública y extraer lo que quiera de ella — aparece la pregunta que realmente importa: ¿el sitio quiere que hagas esto?

Técnicamente, casi siempre podés. El servidor te va a responder igual sea un humano o un bot el que pida la página. Pero eso no es lo mismo que tener permiso, y esa distinción es la que te ahorra horas de trabajo tirado a la basura porque te bloquearon a mitad de semana, o te mete en un problema que no hacía falta tener.

Antes de escribir la primera línea de tu scraper — o al menos antes de dejarlo correr contra el sitio real — revisá dos cosas: el archivo `robots.txt` y los términos de uso del sitio.

### robots.txt

Es un archivo de texto plano que vive en la raíz de cualquier dominio, en una ruta predecible: `https://sitio.com/robots.txt`. No hace falta ninguna herramienta especial para verlo — es una URL como cualquier otra, así que podés abrirla directamente en el navegador.

El archivo le habla a los robots (crawlers, bots, scrapers) y les indica qué partes del sitio pueden visitar y cuáles no. Fue pensado originalmente para buscadores como Google, pero cualquier bot — incluido el tuyo — está invitado a leerlo y se espera que lo respete, aunque nada te obliga técnicamente a hacerlo.

Un archivo típico se ve así:

```text
User-agent: *
Disallow: /admin/
Disallow: /checkout/
Allow: /productos/

User-agent: Googlebot
Disallow: /busqueda/

Sitemap: https://sitio.com/sitemap.xml
```

Cada bloque empieza con `User-agent`, que indica a quién aplica la regla. El asterisco (`*`) significa "todos los bots". Después vienen las reglas: `Disallow` marca las rutas prohibidas, `Allow` las explícitamente permitidas (útil cuando hay una excepción dentro de una carpeta bloqueada). Si tu scraper se identifica con un user-agent propio, revisá si hay un bloque específico para él — a veces un sitio bloquea a todos menos a Googlebot, o bloquea explícitamente bots conocidos de scraping.

Buscá el bloque `User-agent: *`, que es el que te va a aplicar en la mayoría de los casos salvo que uses un user-agent identificable. Fijate qué rutas están en `Disallow`. Si la ruta que necesitás scrapear (por ejemplo `/propiedades/` o `/productos/`) está ahí, el sitio te está pidiendo explícitamente que no la visites con un bot. Si la URL de `robots.txt` no existe (te da 404), en general se interpreta como que no hay restricciones técnicas declaradas — pero eso no significa que el scraping esté necesariamente permitido, solo que no hay una regla bloqueándolo a ese nivel.

Si vas a automatizar esta verificación dentro de tu proyecto, en vez de revisarla a mano cada vez, Python trae una herramienta para esto en la librería estándar, así que no hace falta parsear el archivo vos mismo:

```python
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url("https://sitio.com/robots.txt")
rp.read()

puede_acceder = rp.can_fetch("*", "https://sitio.com/propiedades/")
print(puede_acceder)  # True o False
```

`can_fetch` te devuelve directamente si esa ruta específica está permitida para ese user-agent. Es la forma más simple de meter esta verificación como un paso automático antes de cada request, en vez de confiar en que te acordaste de revisarlo a mano.

### Términos de uso

`robots.txt` es una señal técnica, pero no es un documento legal. Los términos de uso (o "términos y condiciones") del sitio sí lo son, y muchos sitios prohíben el scraping ahí aunque el `robots.txt` no diga nada al respecto. Es común encontrar cláusulas del estilo "no está permitido el uso de bots, arañas, u otros medios automatizados para acceder al sitio", incluso en páginas que técnicamente no bloquean nada a nivel de robots.txt.

Buscá esa sección — normalmente está en el link de "Términos y Condiciones" o "Términos de Uso" en el pie de página del sitio. No hace falta leer el documento entero: buscá con Ctrl+F palabras como "scraping", "automatizado", "bot", "crawler" o "extracción de datos". Si el sitio lo prohíbe explícitamente, ahí ya no es una cuestión técnica: el sitio te está diciendo, en su propio texto legal, que no lo hagas.

## Qué hacer con lo que encontraste

Si el sitio permite el acceso a las rutas que necesitás y no hay una prohibición explícita en los términos de uso, podés avanzar con el scraper que armaste antes, pero igual con buenas prácticas: identificate con un user-agent real (no finjas ser un navegador), espaciá tus requests para no sobrecargar el servidor (un `time.sleep()` entre pedidos alcanza), y guardate solo lo que necesitás para tu análisis, no el sitio entero.

Si el sitio bloquea la ruta que te interesa o lo prohíbe en sus términos, no busques la forma de evadirlo — cambiando de IP, falsificando el user-agent, o cualquier técnica para saltarte la restricción. Además del problema ético y legal, es tiempo perdido: en el momento en que un sitio invierte en bloquear bots, generalmente también invierte en detectarlos cuando insisten. Es mejor buscar una fuente alternativa: una API pública del mismo dato, un dataset abierto equivalente, o un sitio que sí permita el acceso.

## La pregunta de fondo

Cada vez que evalúes una fuente para scrapear, hacete estas tres preguntas en orden: ¿el `robots.txt` permite esta ruta para mi user-agent? ¿Los términos de uso prohíben el scraping explícitamente? ¿Existe una alternativa más simple — una API, un dataset abierto — que me dé el mismo dato sin necesidad de scrapear? Si las primeras dos respuestas son favorables, adelante. Si no, la tercera pregunta casi siempre tiene una respuesta mejor que insistir.