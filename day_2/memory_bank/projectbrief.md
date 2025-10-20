# Project Brief: Energy Anomaly Detection (EAD)

## Project Overview

**Energy Anomaly Detection (EAD)** is a self-contained Python/Marimo application that detects and visualizes energy-use anomalies in BIM-derived models. This is a demo prototype for AI/LLM Engineering Capstone showcasing data → analytics → 3D visualization → LLM explanation workflow.

## Core Mission

Show how IoT/energy data can be analyzed and interpreted by an AI assistant in a 3D, Revit-like environment without Revit dependencies.

## Key Requirements

- **Self-contained**: Python/Marimo app with no external dependencies
- **Performance**: ≤ 30s end-to-end runtime on laptop
- **Accuracy**: ≥ 95% valid anomaly flag rate
- **Visualization**: ≤ 8s viewer load time
- **Explainability**: ≥ 80% LLM summary accuracy
- **Reproducibility**: ≥ 95% identical reruns

## Success Metrics

| Metric                  | Target                  | Rationale              |
| ----------------------- | ----------------------- | ---------------------- |
| End-to-end runtime      | ≤ 30s on laptop         | Demo responsiveness    |
| Valid anomaly flag rate | ≥ 95%                   | Analytical credibility |
| Viewer load time        | ≤ 8s                    | Smooth 3D UX           |
| LLM summary accuracy    | ≥ 80% factual alignment | Explainability         |
| Reproducibility         | ≥ 95% identical reruns  | Traceability           |

## Project Scope (MVP Demo)

**In-Scope:**

- Load CSV/TimescaleDB energy + temperature data
- Compute rolling-baseline + z-score anomalies
- Render 3D IFC/OBJ model with colored elements (PyVista/Trimesh)
- Interactive legend + click-to-inspect behavior
- Generate LLM summary of top anomalies
- Export CSV/JSON results with run_id, ifc_guid, class

**Out of Scope (for now):**

- Real-time data streaming
- ML predictive baselines (XGBoost/LSTM)
- Multi-user web hosting
- Native Revit integration

## Target Users

1. **AI Engineer/Student**: Showcase LLM + data fusion
2. **Architect/BIM Manager**: Validate design vs measured use
3. **Sustainability Analyst**: Demonstrate traceable energy audit

## Problem Statement

Current tools separate energy analytics (spreadsheets, BMS) from spatial context (BIM). The goal is to create a lightweight, explainable system that brings both together within a single Python interface to help users see, understand, and explain energy anomalies.

## Solution Architecture

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

## Data Contract

`anomalies.csv` → `run_id, ifc_guid, ts, value, expected, residual, zscore, class, assumption_pack_version`

## Technology Stack

- **Data ETL & Analysis**: Pandas, NumPy
- **3D Visualization**: PyVista (primary) / Trimesh fallback
- **File Prep**: ifcopenshell → per-element OBJ export
- **Explainability**: OpenAI / Claude API cell
- **Interface**: Marimo interactive cells (Python + HTML)
- **Storage**: Local CSV/JSON per run (extendable to TimescaleDB)

## Project Structure

```
hauska_ead/
├─ io/etl.py # load & clean energy data
├─ anomaly/core.py # rolling baseline + z-score
├─ viz/pyvista_view.py # 3D visualization & legend
├─ llm/explain.py # GPT/Claude summary functions
├─ runs/history.py # run logging & exports
└─ app.marimo.py # UI cells calling the modules
```

## Current Status

- **Phase**: Initial setup and memory bank initialization
- **Next Steps**: Begin implementation of core modules
- **Dependencies**: Sample IFC model, energy dataset, API keys
