# Proyecto: Diseño de Pruebas, Cobertura y Análisis Estático (Java)

Este proyecto corresponde al laboratorio de **Diseño de Pruebas, Control de Calidad y Mantenimiento**.  
Integra tres ejes principales:

- Un escenario de **Diseño de Experimentos (DOE)** y pruebas combinatorias para un módulo de compra de entradas de cine.
- Un **algoritmo de búsqueda binaria** en Java con:
  - Pruebas unitarias (JUnit).
  - Análisis de **cobertura de código** con JaCoCo.
  - **Análisis estático** con PMD y un conjunto de reglas personalizado.
- Integración de estas herramientas en un flujo de **build y verificación automática** (Maven, y CI en GitHub Actions en la rama principal del repositorio original).

---

## Estructura del proyecto

```text
.
├── CineTicketingDOE.xml                # Modelo ACTS para el DOE (casos combinatorios)
├── acts_basic_1.0 3.jar                # JAR de ACTS (herramienta de testing combinatorio)
├── img                                 # Imágenes usadas en el informe (ACTS, JaCoCo, PMD, etc.)
├── pom.xml                             # Configuración Maven (JaCoCo, PMD, JUnit, etc.)
├── src
│   ├── main
│   │   ├── java
│   │   │   └── com/uide/binarySearch
│   │   │       └── BinarySearch.java   # Implementación de búsqueda binaria (healthy + con anomalías)
│   │   └── resources
│   │       └── config/pmd
│   │           └── custom-rules.xml    # Ruleset personalizado de PMD (CyclomaticComplexity, etc.)
│   └── test
│       └── java/com/uide/binarySearch
│           ├── AppTest.java
│           └── BinarySearchTest.java   # Pruebas unitarias de binarySearch / binarySearchHealthy
└── target                              # Artefactos generados por Maven (build, reports)
    ├── binarySearch-1.0-SNAPSHOT.jar   # JAR del proyecto
    ├── site/jacoco                     # Reporte HTML de JaCoCo
    ├── reports/pmd.html                # Reporte HTML de PMD
    └── ...                             # Otros reportes (Surefire, SpotBugs, etc.)
```

## Comandos principales (Maven)

### 1. Compilar y ejecutar pruebas

```bash
mvn clean test
```

- Ejecuta las pruebas unitarias (`BinarySearchTest` y `AppTest`).
- Genera el fichero de ejecución de cobertura `target/jacoco.exec`.

### 2. Build completo + cobertura + análisis estático

```bash
mvn clean verify
```

Este comando:

- Compila el proyecto.
- Ejecuta los tests.
- Genera el reporte de JaCoCo.
- Ejecuta PMD con el ruleset personalizado.
- Genera los reportes HTML en `target/site` y `target/reports`.
