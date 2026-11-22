<div align="center">
  <h1>📡 TelcoGuard AI: Predicción de Fuga de Clientes (Churn)</h1>
  <p><strong>Simulación Profesional en Ciencia de Datos e Inteligencia Artificial</strong></p>
  <p>
    <img src="https://img.shields.io/badge/Metodolog%C3%ADa-Scrum-blue?style=for-the-badge" alt="Scrum"/>
    <img src="https://img.shields.io/badge/Sprint-2%20(En%20Cierre)-orange?style=for-the-badge" alt="Sprint 2"/>
    <img src="https://img.shields.io/badge/Python-3.10-yellow?style=for-the-badge&logo=python" alt="Python"/>
    <img src="https://img.shields.io/badge/Trello-Tablero_Activo-0079BF?style=for-the-badge&logo=trello" alt="Trello"/>
  </p>
</div>

---

## 📌 1. Definición del Problema
**NovaTel Telecomunicaciones** registró en el último semestre un aumento en su tasa de cancelación mensual (*churn*) del **15% al 22%**. Dado que adquirir un cliente nuevo cuesta hasta 5 veces más que retener uno actual, el negocio necesita anticiparse a las bajas.

**Objetivo:** Diseñar y planificar un sistema predictivo basado en Machine Learning para identificar con 30 días de anticipación a los clientes con alta probabilidad de fuga, permitiendo al equipo comercial ejecutar campañas de retención focalizadas.

---

## 👥 2. Equipo de Trabajo (Simulación Scrum)

<table>
  <thead>
    <tr>
      <th>Integrante</th>
      <th>Rol</th>
      <th>Responsabilidad Principal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Sofía Rovenzzo</strong></td>
      <td>Product Owner (PO)</td>
      <td>Definición de negocio, KPIs, priorización del backlog y marco ético.</td>
    </tr>
    <tr>
      <td><strong>Lourdes Splendido</strong></td>
      <td>Scrum Master (SM)</td>
      <td>Gestión del tablero Trello, ceremonias ágiles y presentación final.</td>
    </tr>
    <tr>
      <td><strong>Camila Torres</strong></td>
      <td>Data / ML Engineer</td>
      <td>Gestión de GitHub, ingesta y anonimización de datos (PII) y documentación.</td>
    </tr>
    <tr>
      <td><strong>Valentina Ruiz</strong></td>
      <td>Data Analyst</td>
      <td>Limpieza de datos, Análisis Exploratorio (EDA) y visualizaciones de negocio.</td>
    </tr>
    <tr>
      <td><strong>Lucas Gavazzi</strong></td>
      <td>Data Scientist</td>
      <td>Feature engineering, entrenamiento y optimización del modelo predictivo.</td>
    </tr>
  </tbody>
</table>

---

## 🔄 3. Planificación Ágil (Product Backlog & Sprints)

<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Historia de Usuario / Tarea</th>
      <th>Responsable</th>
      <th>Sprint</th>
      <th>Estado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>US-01</strong></td>
      <td>Definir problema de negocio, alcance y KPIs de retención</td>
      <td>Sofía Rovenzzo</td>
      <td>Sprint 1</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><strong>US-02</strong></td>
      <td>Configurar tablero de Trello y flujo de trabajo</td>
      <td>Lourdes Splendido</td>
      <td>Sprint 1</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><strong>US-03</strong></td>
      <td>Crear repositorio en GitHub, <code>.gitignore</code> y ramas</td>
      <td>Camila Torres</td>
      <td>Sprint 1</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><strong>US-04</strong></td>
      <td>Ingestar dataset y anonimizar datos sensibles (PII)</td>
      <td>Camila Torres</td>
      <td>Sprint 1</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><strong>US-05</strong></td>
      <td>Limpieza de datos y Análisis Exploratorio (EDA)</td>
      <td>Valentina Ruiz</td>
      <td>Sprint 1</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><strong>US-06</strong></td>
      <td>Visualizaciones de negocio con motivos de fuga</td>
      <td>Valentina Ruiz</td>
      <td>Sprint 1</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><strong>US-07</strong></td>
      <td>Preprocesamiento y entrenamiento de modelo base</td>
      <td>Lucas Gavazzi</td>
      <td>Sprint 2</td>
      <td>✅ Done</td>
    </tr>
    <tr>
      <td><strong>US-08</strong></td>
      <td>Evaluación y ajuste priorizando Recall y Precision</td>
      <td>Lucas Gavazzi</td>
      <td>Sprint 2</td>
      <td>🔍 In Review</td>
    </tr>
    <tr>
      <td><strong>US-09</strong></td>
      <td>Redacción del Informe de Ética y mitigación de sesgos</td>
      <td>Sofía Rovenzzo</td>
      <td>Sprint 2</td>
      <td>🔍 In Review</td>
    </tr>
    <tr>
      <td><strong>US-10</strong></td>
      <td>Consolidación de GitHub y documentación técnica</td>
      <td>Camila Torres</td>
      <td>Sprint 2</td>
      <td>🚧 In Progress</td>
    </tr>
    <tr>
      <td><strong>US-11</strong></td>
      <td>Sprint Review y preparación de presentación final</td>
      <td>Lourdes Splendido</td>
      <td>Sprint 2</td>
      <td>📋 To Do</td>
    </tr>
  </tbody>
</table>

---

## 📊 4. Resultados Clave (Simulación)
* **Hallazgo del EDA:** Los clientes con contrato *mes a mes* y más de 2 reclamos técnicos en el último trimestre concentran el **68% de las cancelaciones**.
* **Desempeño del modelo (Random Forest):**
  * **Recall:** `84%` *(métrica prioritaria para detectar la mayor cantidad posible de clientes en riesgo)*.
  * **Precision:** `76%`
  * **F1-Score:** `80%`

---

## 🛠️ 5. Herramientas y Enlaces
* **Tablero de Gestión (Trello):** 👉 *https://trello.com/b/OzU9PoOo/telcoguard-ai-prediccion-de-churn*
* **Control de Versiones:** Git & GitHub (flujo `dev` → `main` mediante Pull Request)
* **Stack Técnico:** Python, Pandas, Scikit-Learn

---

## ⚖️ 6. Ética y Responsabilidad Social
El análisis completo sobre privacidad, anonimización y mitigación de sesgos se encuentra documentado en:  
👉 [Informe de Ética y Privacidad](docs/informe_etica.md)

---

<div align="center">
  <p>Proyecto Integrador Final — <strong>[Tu Nombre y Apellido]</strong><br/>
  Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial | Instituto Nuevos Aires</p>
</div>
