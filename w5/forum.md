1:
JMeter
JMeter facilita automatizar pruebas de rendimiento (en vez de hacerlo a mano) usando test plans con hilos, peticiones y listeners; es la base para luego hacer escenarios más avanzados y usar plugins.
https://www.youtube.com/watch?v=mXGcBvWYl-U

Locust
Locust es una herramienta de pruebas de carga escrita en Python que permite definir el comportamiento de usuarios virtuales mediante código y simular cientos o miles de usuarios concurrentes para medir el rendimiento de una aplicación web o API.
https://www.youtube.com/watch?v=3fOKyLz16Tw

Gatling
Gatling es una herramienta de pruebas de carga y rendimiento para aplicaciones web y APIs, que permite definir escenarios de usuarios mediante código (Scala/Java), ejecutar miles de usuarios virtuales y obtener métricas detalladas de tiempos de respuesta, throughput y errores, con buena integración en pipelines de DevOps.

https://www.youtube.com/watch?v=AqnKbaz32HQ

2:

Grafana
Grafana es una herramienta open source de visualización y monitoreo que permite crear dashboards interactivos a partir de datos de distintas fuentes (bases de datos, Prometheus, InfluxDB, logs, APIs, etc.), muy usada para observar métricas de rendimiento, infraestructura y aplicaciones en tiempo real.

https://www.youtube.com/watch?v=riFxqD_6XYI

AppDynamics
AppDynamics es una herramienta de Application Performance Monitoring (APM) de Cisco que permite monitorear en tiempo real el rendimiento de aplicaciones (backend, frontend, bases de datos, servicios), detectar cuellos de botella y errores, y seguir el “viaje” de una transacción desde el usuario hasta los servicios internos.

https://www.youtube.com/watch?v=7t1w_oNHOdM

Prometheus
Prometheus es una herramienta open source de monitoreo y métricas orientada a series de tiempo, diseñada para recolectar datos (por ejemplo de servicios, contenedores y sistemas) mediante “scraping” de endpoints HTTP y almacenarlos con timestamps para luego consultarlos con su propio lenguaje de consultas (PromQL).

https://www.youtube.com/watch?v=NqrNg5sfGQM

dstat
dstat es una herramienta de línea de comandos para Linux que muestra en tiempo real estadísticas del sistema (CPU, memoria, disco, red, I/O, etc.) de forma unificada, reemplazando y combinando comandos como vmstat, iostat, netstat y ifstat.

https://www.youtube.com/watch?v=wn_Utksv9sc

3. Se realiza la configuración correspondiente para la simulación de una api que integre fibonacci.
   Existen 2 apis:
   1: /fib fibonaccy con secuencia 10
   1: /fib-cached fibonaccy memoizada con secuencia 15

Se configura:

- 10 usuarios
- 2 usuarios creados por segundo

Las metricas nos señalan que la api con la versión cacheada (/fib-cached) es ligeramente más eficiente en promedio, pero en estos tamaños de n la mejora es mínima; ambas son perfectamente utilizables bajo esta carga y no ha existido perdidas, ni excepciones.
