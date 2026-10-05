# 🚀 AI Dev Tools Zoomcamp 2026 — Homework Repository

Este repositorio consolida todas las tareas y proyectos prácticos realizados durante el curso **AI Dev Tools Zoomcamp 2026** de [DataTalks.Club](https://datatalks.club/), impartido por Alexey Grigorev.

**Autor:** Diego Gonzalez ([@NativelogXD](https://github.com/NativelogXD))  
**Cohorte:** 2026

---

## 📂 Estructura General del Monorepo

```text
homeworks/
├── homework-1/   # HW1: Household Chores Manager (Family Edition) - Django + Spec-driven workflow
├── homework-2/   # HW2: Mini Kanban Board - FastAPI + SQLite + React Vite
├── homework-3/   # HW3: Agent Relay - Containerization, PostgreSQL, K8s (kind) & CI/CD
└── homework-4/   # HW4: Order Tracker - Observability (OTel, Prometheus, Loki, Tempo, Grafana) & Incident Responder
```

---

## 📑 Resumen de Tareas y Tecnologías

| Módulo / Tarea | Nombre del Proyecto | Stack Tecnológico Central | Repositorio Individual / Enlace |
| :--- | :--- | :--- | :--- |
| **Homework 1** | **Household Chores Manager** | Python, Django, Spec-Driven Development, AI Loop Engineering | [hw1-zoomcamp](https://github.com/NativelogXD/hw1-zoomcamp) |
| **Homework 2** | **Mini Kanban Board** | FastAPI, SQLite, React, Vite, TailwindCSS, OpenAPI Contract | [mini-kanban](https://github.com/NativelogXD/mini-kanban) |
| **Homework 3** | **Agent Relay** | Python, FastAPI, Docker Multi-Stage, PostgreSQL, Kubernetes (`kind`), GitHub Actions CI/CD | [agent-relay](https://github.com/NativelogXD/agent-relay) |
| **Homework 4** | **Order Tracker & Observability** | FastAPI, SQLite, OpenTelemetry (OTel), Prometheus, Loki, Tempo, Grafana, Headless Incident Responder | [order-tracker](https://github.com/NativelogXD/order-tracker) |

---

## 🔍 Detalle de Homework 4: DevOps and Observability for AI-Built Apps

En esta tarea se implementó un ciclo cerrado de observabilidad y respuesta automatizada a incidentes para la aplicación **Order Tracker**:

1. **Tríada de Observabilidad con OpenTelemetry:**
   - Métricas: contador `http_requests_total` con dimensiones (`route`, `status_code`, `method`).
   - Trazas: Spans distribuidos correlacionados con cada solicitud HTTP.
   - Logs: Logs estructurados con inyección de `trace_id`.
2. **Pipeline de Telemetría (Docker Compose):**
   - **OpenTelemetry Collector:** Recibe OTLP en `4317` y distribuye hacia backends especializados.
   - **Prometheus (`:9090`):** Almacenamiento y consulta de series temporales.
   - **Loki (`:3100`):** Ingesta de logs de aplicación.
   - **Tempo (`:3200`):** Almacenamiento de trazas distribuidas.
   - **Grafana (`:3000`):** Dashboards integrados y reglas de alerta.
3. **Alertas Orientadas a Impacto Real:**
   - Regla de alerta en Grafana monitoreando tasas de error `5xx` con webhook hacia el responder.
4. **Agente de Guardia Automático (`incident-response` en `:8001`):**
   - Recibe alertas en `POST /alerts`, genera un paquete de evidencia acotado (*evidence packet*) y ejecuta un agente en modo *headless*.
5. **Corrección de Causa Raíz:**
   - Diagnóstico del error HTTP 500 en pedidos express (`express-1002`) por cálculo con `replace(day=day+2)` en fin de mes, remediado con `timedelta(days=2)`.

### 📝 Respuestas Oficiales — Homework 4

| N° | Pregunta | Respuesta Oficial |
| :---: | :--- | :--- |
| **Q1** | What does the health check return? | **`{"status":"ok"}`** |
| **Q2** | Which HTTP status code does the metric record for this lookup? (`standard-1001`) | **`200`** |
| **Q3** | Which HTTP status code does the metric show in Grafana? (`standard-1002`) | **`404`** |
| **Q4** | What state does Grafana show for the 5xx alert? | **`Normal`** |
| **Q5** | What did the agent respond? Include the last line from its answer. | `I investigated the alert 'ResponderTest'.`<br/>`The alert payload indicates test=true with summary: 'Test notification; no incident to fix'.`<br/>`This alert is a synthetic verification test / false positive.`<br/>`No incident detected, no reproduction steps needed, and no code changes were made.`<br/>`No code changes required.`<br/><br/>**Última línea:**<br/>`No code changes required.` |
| **Q6** | What was the problem? | **The express delivery date calculation tried to use a day that does not exist in that month.** |

---

## 🏃‍♂️ Cómo Ejecutar Cada Tarea

### Homework 1 (Chores Manager)
```bash
cd homework-1
uv run python manage.py migrate
uv run python manage.py runserver
```

### Homework 2 (Mini Kanban)
```bash
# Backend
cd homework-2/backend
uv run uvicorn main:app --reload --port 8000

# Frontend
cd ../frontend
npm install
npm run dev
```

### Homework 3 (Agent Relay)
```bash
cd homework-3
docker compose up --build -d
uv run pytest
```

### Homework 4 (Order Tracker & Telemetry Stack)
```bash
cd homework-4
docker compose up --build -d
# Verificar salud de la app:
curl http://localhost:8000/healthz
# Verificar responder:
curl http://localhost:8001/healthz
# Abrir Grafana:
# http://localhost:3000 (admin / admin)
```
