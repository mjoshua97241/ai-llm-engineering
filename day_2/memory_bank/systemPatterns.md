# System Patterns: Energy Anomaly Detection (EAD)

## System Architecture

### High-Level Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Sources  │    │   Processing    │    │   Visualization │
│                 │    │                 │    │                 │
│ • CSV Files     │───▶│ • ETL Pipeline  │───▶│ • 3D Renderer   │
│ • TimescaleDB   │    │ • Anomaly Det.  │    │ • Interactive   │
│ • IFC Models    │    │ • Classification│    │ • Legend        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   AI Layer      │
                       │                 │
                       │ • LLM Summary   │
                       │ • Explanations  │
                       │ • Context       │
                       └─────────────────┘
```

### Component Relationships

#### Data Flow Pattern

1. **Input Layer**: CSV/TimescaleDB → Pandas DataFrame
2. **Processing Layer**: Rolling baseline + z-score computation
3. **Classification Layer**: Anomaly categorization (Normal/Near/Anomaly)
4. **Visualization Layer**: 3D model rendering with color mapping
5. **AI Layer**: LLM explanation generation
6. **Output Layer**: Structured exports (CSV/JSON)

## Key Technical Decisions

### 1. Modular Architecture

**Decision**: Separate concerns into distinct modules
**Rationale**: Enables testing, maintenance, and future extensions
**Implementation**:

```
hauska_ead/
├─ io/etl.py          # Data loading and cleaning
├─ anomaly/core.py     # Anomaly detection algorithms
├─ viz/pyvista_view.py # 3D visualization
├─ llm/explain.py      # AI explanation generation
├─ runs/history.py     # Run logging and persistence
└─ app.marimo.py       # User interface orchestration
```

### 2. Statistical Approach

**Decision**: Rolling baseline + z-score for anomaly detection
**Rationale**: Simple, interpretable, and computationally efficient
**Implementation**:

- Rolling mean calculation with configurable window
- Z-score computation: `z = (value - mean) / std`
- Classification thresholds: |z| ≥ 3 (Anomaly), 2 ≤ |z| < 3 (Near)

### 3. 3D Visualization Strategy

**Decision**: PyVista as primary renderer with Trimesh fallback
**Rationale**: PyVista provides better performance and interactivity
**Implementation**:

- Load OBJ meshes by IFC_GUID
- Color mapping: Gray (Normal), Amber (Near), Red (Anomaly)
- Interactive selection and tooltips

### 4. AI Integration Pattern

**Decision**: LLM explanation as separate module
**Rationale**: Decouples AI from core analysis, enables different models
**Implementation**:

- Structured prompt templates
- Context-aware explanations
- Configurable temperature and model selection

## Design Patterns in Use

### 1. Pipeline Pattern

**Application**: Data processing workflow
**Benefits**: Clear separation of concerns, testable components
**Implementation**:

```python
def process_energy_data(data):
    cleaned = clean_data(data)
    features = engineer_features(cleaned)
    anomalies = detect_anomalies(features)
    return anomalies
```

### 2. Strategy Pattern

**Application**: Anomaly detection algorithms
**Benefits**: Easy to swap different detection methods
**Implementation**:

```python
class AnomalyDetector:
    def __init__(self, strategy):
        self.strategy = strategy

    def detect(self, data):
        return self.strategy.compute(data)
```

### 3. Observer Pattern

**Application**: 3D visualization updates
**Benefits**: Decoupled UI updates from data changes
**Implementation**:

```python
class VisualizationObserver:
    def update(self, anomalies):
        self.update_colors(anomalies)
        self.update_legend(anomalies)
```

### 4. Factory Pattern

**Application**: 3D model loading
**Benefits**: Support multiple file formats (OBJ, IFC)
**Implementation**:

```python
class ModelLoaderFactory:
    @staticmethod
    def create_loader(file_type):
        if file_type == 'obj':
            return OBJLoader()
        elif file_type == 'ifc':
            return IFCLoader()
```

## Component Relationships

### Data Dependencies

```
ETL Module ──┐
             ├──▶ Anomaly Detection ──▶ Visualization
IFC Parser ──┘                         │
                                      ▼
                                 AI Explanation
```

### Interface Contracts

- **ETL Module**: Outputs standardized DataFrame with required columns
- **Anomaly Detection**: Inputs DataFrame, outputs classified anomalies
- **Visualization**: Inputs anomalies + 3D model, outputs interactive viewer
- **AI Module**: Inputs anomaly summary, outputs natural language explanation

## Performance Patterns

### 1. Lazy Loading

**Application**: 3D model loading
**Implementation**: Load meshes on-demand, cache loaded models
**Benefits**: Faster initial load, memory efficiency

### 2. Batch Processing

**Application**: Anomaly detection
**Implementation**: Process data in chunks for large datasets
**Benefits**: Memory efficiency, progress tracking

### 3. Caching Strategy

**Application**: LLM responses
**Implementation**: Cache explanations for similar anomaly patterns
**Benefits**: Reduced API calls, faster responses

## Error Handling Patterns

### 1. Graceful Degradation

**Application**: 3D rendering fallback
**Implementation**: PyVista → Trimesh → Static image
**Benefits**: System remains functional with reduced features

### 2. Validation Pipeline

**Application**: Data quality checks
**Implementation**: Multi-stage validation with clear error messages
**Benefits**: Early problem detection, user guidance

### 3. Retry Logic

**Application**: LLM API calls
**Implementation**: Exponential backoff with circuit breaker
**Benefits**: Resilience to temporary failures

## Testing Patterns

### 1. Unit Testing

**Application**: Individual modules
**Strategy**: Mock external dependencies, test core logic
**Coverage**: ETL, anomaly detection, data validation

### 2. Integration Testing

**Application**: End-to-end workflows
**Strategy**: Test complete pipeline with sample data
**Coverage**: Data flow, visualization, export functionality

### 3. Performance Testing

**Application**: Runtime and memory usage
**Strategy**: Benchmark with various dataset sizes
**Coverage**: Load times, memory consumption, API response times

## Security Patterns

### 1. Input Validation

**Application**: Data sanitization
**Implementation**: Validate file types, data ranges, required fields
**Benefits**: Prevent malicious input, ensure data quality

### 2. API Key Management

**Application**: LLM service integration
**Implementation**: Environment variables, secure storage
**Benefits**: Protect API credentials, enable different environments

### 3. Data Privacy

**Application**: Sensitive energy data
**Implementation**: Local processing, optional data anonymization
**Benefits**: Keep sensitive data on-premises

## Extensibility Patterns

### 1. Plugin Architecture

**Application**: Additional anomaly detection methods
**Implementation**: Interface-based plugin system
**Benefits**: Easy addition of new algorithms

### 2. Configuration Management

**Application**: User preferences and system settings
**Implementation**: YAML/JSON configuration files
**Benefits**: Flexible system behavior without code changes

### 3. Export Format Support

**Application**: Multiple output formats
**Implementation**: Strategy pattern for different exporters
**Benefits**: Easy addition of new export formats
