# 🧩 Product Requirements Document (PRD)

## Product: **Energy Anomaly Detection (EAD)**

**Version:** v1.1 (Demo Edition) **Date:** Oct 2025
**Owner:** MJ (Data Science) **Mentor:** PSI AI Academy
**Status:** Demo Prototype for AI/LLM Engineering Capstone

---

## 1. Objective

Deliver a **self-contained Python/Marimo app** that detects and visualizes energy-use anomalies in BIM-derived models.
The demo showcases **data → analytics → 3D visualization → LLM explanation** without Revit dependencies.

**Core Goal:**
Show how IoT/energy data can be analyzed and interpreted by an AI assistant in a 3D, Revit-like environment.

**Success Metrics**

| Metric                  | Target                   | Rationale              |
| ----------------------- | ------------------------ | ---------------------- |
| End-to-end runtime      | ≤ 30 s on laptop         | Demo responsiveness    |
| Valid anomaly flag rate | ≥ 95 %                   | Analytical credibility |
| Viewer load time        | ≤ 8 s                    | Smooth 3D UX           |
| LLM summary accuracy    | ≥ 80 % factual alignment | Explainability         |
| Reproducibility         | ≥ 95 % identical reruns  | Traceability           |

---

## 2. Scope (MVP Demo)

**In-Scope**

- Load **CSV/TimescaleDB** energy + temperature data
- Compute **rolling-baseline + z-score** anomalies
- Render **3D IFC/OBJ** model with colored elements (PyVista / Trimesh)
- Provide **interactive legend + click-to-inspect** behavior
- Generate **LLM summary** of top anomalies
- Export **CSV/JSON** results (`run_id`, `ifc_guid`, `class`)

**Out of Scope (for now)**

- Real-time data streaming
- ML predictive baselines (XGBoost/LSTM)
- Multi-user web hosting
- Native Revit integration

---

## 3. Target Users & Use Cases

| Persona                     | Goal                               | Example Scenario                    |
| --------------------------- | ---------------------------------- | ----------------------------------- |
| **AI Engineer / Student**   | Showcase LLM + data fusion         | Explain anomalies using GPT summary |
| **Architect / BIM Manager** | Validate design vs measured use    | Visualize high-load zones in 3D     |
| **Sustainability Analyst**  | Demonstrate traceable energy audit | Export run logs for report          |

---

## 4. Problem Statement

Current tools separate **energy analytics** (spreadsheets, BMS) from **spatial context** (BIM).
The goal is to create a lightweight, explainable system that brings both together — within a single Python interface — to help users **see, understand, and explain** energy anomalies.

---

## 5. Solution Overview

### Architecture

```
Energy CSV / TimescaleDB
     ↓
Pandas ETL → Rolling Mean + Z-Score
     ↓
Results {ifc_guid, metrics, class}
     ↓
3D Viewer (PyVista/Trimesh OBJ Meshes)
     ↓
LLM Summary (GPT/Claude API)
     ↓
Exports (CSV / JSON + run_id + assumption_pack)
```

### Data Contract

`anomalies.csv` →
`run_id, ifc_guid, ts, value, expected, residual, zscore, class, assumption_pack_version`

---

## 6. Functional Requirements

| Category           | Requirement                                                            | Priority |
| ------------------ | ---------------------------------------------------------------------- | -------- |
| **Data Input**     | Read CSV or TimescaleDB query; enforce ≥ 30 days & ≤ 10 % missing      | High     |
| **Computation**    | Apply rolling baseline + z-score; user-configurable window & threshold | High     |
| **3D Viewer**      | Load IFC-derived OBJ meshes; color by anomaly class                    | High     |
|                    | Implement legend & click-to-inspect tooltips                           | Med      |
| **Explainability** | Generate LLM summary (top zones, causes, recommendations)              | High     |
| **Traceability**   | Persist `run_id`, `assumption_pack_version`, timestamps in logs        | High     |
| **Export**         | CSV/JSON output for each run                                           | High     |

---

## 7. Non-Functional Requirements

| Area             | Specification                               |
| ---------------- | ------------------------------------------- |
| **Performance**  | Full run ≤ 30 s for ≤ 10 k records          |
| **Usability**    | Interactive 3D model (orbit/pan/legend)     |
| **Reliability**  | Reproducible outputs ≥ 95 %                 |
| **Transparency** | Visible assumption pack & LLM prompt logged |
| **Portability**  | Runs locally in Marimo (> Python 3.10)      |

---

## 8. Data & Visualization Pipeline

1. **Data Cleaning (ETL):**

   - Validate units (kWh / kW).
   - Resample to hourly means if needed.
   - Impute ≤ 10 % gaps (linear interp).

2. **Feature Engineering:**

   - ΔT = θ_in – θ_out; rolling mean, residual, z-score.

3. **Anomaly Classification:**

   - |z| ≥ 3 → “Anomaly”, 2 ≤ |z| < 3 → “Near”, else “Normal”.

4. **Visualization:**

   - Load OBJ meshes named by `IFC_GUID`.
   - Apply palette {gray, amber, red}.
   - Interactive selection → show metrics.

5. **Explainability:**

   - LLM prompt: _Summarize top anomalies and possible causes using domain context._

---

## 9. Technology Stack

| Layer                   | Tools / Libraries                                  |
| ----------------------- | -------------------------------------------------- |
| **Data ETL & Analysis** | Pandas, NumPy                                      |
| **3D Visualization**    | PyVista (primary) / Trimesh fallback               |
| **File Prep**           | ifcopenshell → per-element OBJ export              |
| **Explainability**      | OpenAI / Claude API cell                           |
| **Interface**           | Marimo interactive cells (Python + HTML)           |
| **Storage**             | Local CSV/JSON per run (extendable to TimescaleDB) |

---

## 10. Workflow for Demo Execution

1. **Load data & model**

   - Import energy CSV and OBJ folder (exported via `ifcopenshell`).

2. **Configure run**

   - Select time window & threshold.

3. **Run analysis**

   - Compute z-scores and flag anomalies.

4. **Visualize 3D**

   - Display colored model + legend + click info.

5. **Explain results**

   - Generate LLM summary cell.

6. **Export results**

   - Write `run_id` folder with CSV/JSON and logs.

---

## 11. Acceptance Criteria

| Criterion           | Definition of Done                                          |
| ------------------- | ----------------------------------------------------------- |
| **Computation**     | Correct z-score classification for ≥ 95 % records           |
| **3D Viewer**       | Loads OBJ model < 8 s; legend colors match classes          |
| **Interactivity**   | User can click elements to see values / GUID                |
| **Explainability**  | LLM summary matches top anomalies (no hallucinated metrics) |
| **Traceability**    | Run metadata (JSON) saved with outputs                      |
| **Reproducibility** | Same inputs → identical outputs (± 1 %)                     |

---

## 12. Future Enhancements (Phase 2+)

| Feature                    | Description                                            |
| -------------------------- | ------------------------------------------------------ |
| **Contextual regression**  | Adjust for temperature and occupancy variables         |
| **ML predictive baseline** | XGBoost / Prophet forecast vs actual                   |
| **Web viewer integration** | Move PyVista render → Hauska Co-Pilot (React + xeokit) |
| **Continuous learning**    | Incremental model updates from new runs                |
| **Voice / Chat assistant** | Natural-language queries over results                  |

---

## 13. Open Items / Dependencies

- Prepare sample IFC model → per-element OBJ export (maintain GUIDs).
- Obtain sample energy dataset (≥ 30 days).
- Add OpenAI or Claude API key to Marimo environment.
- Verify Marimo 3D render compatibility (PyVista WebGL widget).
- Define LLM prompt template and temperature settings.

### Implementation Note (for repo scaffolding)

Project modules will be structured for portability:
hauska_ead/
├─ io/etl.py # load & clean energy data
├─ anomaly/core.py # rolling baseline + z-score
├─ viz/pyvista_view.py # 3D visualization & legend
├─ llm/explain.py # GPT/Claude summary functions
├─ runs/history.py # run logging & exports
└─ app.marimo.py # UI cells calling the modules
