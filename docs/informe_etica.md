# ⚖️ Informe de Ética y Responsabilidad Profesional

**Proyecto:** TelcoGuard AI – Predicción de Fuga de Clientes (Churn)  
**Organización simulada:** NovaTel Telecomunicaciones  
**Responsable:** Sofía Rovenzzo (Product Owner) — Equipo TelcoGuard AI  

---

## 1. Privacidad y Protección de Datos
Dado que el proyecto trabaja con información de clientes de telecomunicaciones, la privacidad se integró desde el diseño (*Privacy by Design*). Durante la ingesta de datos (**US-04**), se aplicó un proceso estricto de **anonimización**, eliminando todo dato de identificación personal (PII) como nombre, apellido, DNI, correo electrónico, teléfono y domicilio exacto. El análisis y modelado se realizan exclusivamente mediante un identificador alfanumérico encriptado (`customer_id`).

## 2. Mitigación de Sesgos Algorítmicos
Un riesgo crítico en modelos de retención comercial es la discriminación indirecta (por ejemplo, ofrecer mejores beneficios a determinados barrios, géneros o edades). Para garantizar la equidad algorítmica:
* Se excluyeron variables sensibles y *proxies* demográficos del entrenamiento del modelo.
* El algoritmo utiliza únicamente variables objetivas de comportamiento del servicio: antigüedad, tipo de contrato, historial de reclamos técnicos y nivel de uso.

## 3. Transparencia y Explicabilidad
En lugar de implementar algoritmos de "caja negra" difíciles de auditar, se priorizó un modelo interpretable (**Random Forest** con análisis de importancia de variables). Esto permite explicar con claridad al área comercial los motivos por los cuales un cliente es clasificado en riesgo, asegurando que la decisión final siempre cuente con supervisión humana (*Human-in-the-loop*).

## 4. Impacto Social y Uso Responsable
El sistema predictivo fue diseñado exclusivamente para mejorar la experiencia del usuario mediante soporte técnico proactivo y ofertas de retención transparentes. Queda estrictamente descartado su uso para penalizar clientes, restringir servicios o aplicar tarifas abusivas.
