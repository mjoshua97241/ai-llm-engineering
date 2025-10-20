# Technical Context: Energy Anomaly Detection (EAD)

## Technology Stack

### Core Technologies

| Layer                   | Technology   | Version | Purpose                        |
| ----------------------- | ------------ | ------- | ------------------------------ |
| **Runtime**             | Python       | 3.10+   | Core application language      |
| **Interface**           | Marimo       | Latest  | Interactive notebook interface |
| **Data Processing**     | Pandas       | Latest  | Data manipulation and analysis |
| **Numerical Computing** | NumPy        | Latest  | Mathematical operations        |
| **3D Visualization**    | PyVista      | Latest  | Primary 3D rendering           |
| **3D Fallback**         | Trimesh      | Latest  | Alternative 3D processing      |
| **File Processing**     | ifcopenshell | Latest  | IFC model processing           |
| **AI Integration**      | OpenAI API   | Latest  | LLM explanations               |
| **AI Alternative**      | Claude API   | Latest  | Alternative LLM provider       |

### Development Tools

| Tool                | Purpose      | Configuration                  |
| ------------------- | ------------ | ------------------------------ |
| **Package Manager** | uv           | Fast Python package management |
| **Version Control** | Git          | Source code management         |
| **Environment**     | Python 3.10+ | Runtime environment            |
| **Testing**         | pytest       | Unit and integration testing   |
| **Linting**         | ruff         | Code quality and formatting    |

## Development Setup

### Prerequisites

- Python 3.10 or higher
- uv package manager
- Git for version control
- OpenAI or Claude API key

### Installation Process

```bash
# Clone repository
git clone <repository-url>
cd ai-llm-engineering-2/day_2

# Install dependencies
uv sync

# Set up environment variables
export OPENAI_API_KEY="your-api-key-here"
# OR
export CLAUDE_API_KEY="your-api-key-here"
```

### Project Structure

```
day_2/
├── memory_bank/           # Project documentation
│   ├── projectbrief.md
│   ├── productContext.md
│   ├── systemPatterns.md
│   ├── techContext.md
│   ├── activeContext.md
│   └── progress.md
├── hauska_ead/            # Main application code
│   ├── io/
│   │   └── etl.py         # Data loading and cleaning
│   ├── anomaly/
│   │   └── core.py         # Anomaly detection algorithms
│   ├── viz/
│   │   └── pyvista_view.py # 3D visualization
│   ├── llm/
│   │   └── explain.py     # AI explanation generation
│   ├── runs/
│   │   └── history.py     # Run logging and persistence
│   └── app.marimo.py      # Main Marimo application
├── data/                  # Sample data and models
│   ├── energy_data.csv    # Sample energy data
│   └── models/            # 3D model files (OBJ)
├── outputs/               # Generated results
│   └── runs/              # Run-specific outputs
├── tests/                 # Test files
├── pyproject.toml         # Project configuration
├── uv.lock               # Dependency lock file
└── README.md             # Project documentation
```

## Technical Constraints

### Performance Requirements

- **End-to-end runtime**: ≤ 30 seconds for ≤ 10k records
- **3D model loading**: ≤ 8 seconds
- **Memory usage**: Efficient handling of large datasets
- **API response time**: ≤ 5 seconds for LLM explanations

### Compatibility Requirements

- **Python**: 3.10+ (required for modern features)
- **Operating System**: Cross-platform (Windows, macOS, Linux)
- **Browser**: Modern browsers for Marimo interface
- **Hardware**: Standard laptop specifications

### Data Constraints

- **Input formats**: CSV, TimescaleDB, OBJ files
- **Data quality**: Handle ≤ 10% missing data
- **File sizes**: Support models up to 100MB
- **Time series**: Minimum 30 days of data

## Dependencies

### Core Dependencies

```toml
[dependencies]
pandas = "^2.0.0"
numpy = "^1.24.0"
pyvista = "^0.42.0"
trimesh = "^4.0.0"
ifcopenshell = "^0.7.0"
openai = "^1.0.0"
anthropic = "^0.7.0"
marimo = "^0.8.0"
```

### Development Dependencies

```toml
[dev-dependencies]
pytest = "^7.0.0"
pytest-cov = "^4.0.0"
ruff = "^0.1.0"
black = "^23.0.0"
mypy = "^1.0.0"
```

### Optional Dependencies

```toml
[dependencies.optional]
timescaledb = "^0.1.0"  # For TimescaleDB integration
plotly = "^5.0.0"       # For additional visualizations
jupyter = "^1.0.0"      # For Jupyter notebook support
```

## API Integrations

### OpenAI Integration

- **Model**: GPT-4 or GPT-3.5-turbo
- **Endpoint**: https://api.openai.com/v1/chat/completions
- **Authentication**: API key via environment variable
- **Rate limits**: Respect API rate limits
- **Cost management**: Monitor token usage

### Claude Integration

- **Model**: Claude-3-sonnet or Claude-3-haiku
- **Endpoint**: Anthropic API
- **Authentication**: API key via environment variable
- **Rate limits**: Respect API rate limits
- **Cost management**: Monitor token usage

### Configuration

```python
# API configuration
OPENAI_CONFIG = {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 1000,
    "timeout": 30
}

CLAUDE_CONFIG = {
    "model": "claude-3-sonnet-20240229",
    "temperature": 0.7,
    "max_tokens": 1000,
    "timeout": 30
}
```

## Data Processing Pipeline

### ETL Pipeline

1. **Data Loading**: CSV/TimescaleDB → Pandas DataFrame
2. **Data Cleaning**: Handle missing values, validate units
3. **Feature Engineering**: Calculate rolling means, residuals
4. **Anomaly Detection**: Z-score computation and classification
5. **Output**: Structured results for visualization

### Data Validation

```python
def validate_energy_data(df):
    """Validate energy data quality and completeness"""
    required_columns = ['timestamp', 'value', 'ifc_guid']
    missing_columns = set(required_columns) - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Check data quality
    missing_percentage = df['value'].isna().sum() / len(df) * 100
    if missing_percentage > 10:
        raise ValueError(f"Too much missing data: {missing_percentage:.1f}%")

    return True
```

## 3D Visualization Stack

### PyVista Configuration

```python
import pyvista as pv

# Configure PyVista
pv.set_plot_theme("document")
pv.global_theme.background = "white"
pv.global_theme.font.size = 12
```

### Model Loading

```python
def load_3d_model(model_path):
    """Load 3D model with error handling"""
    try:
        mesh = pv.read(model_path)
        return mesh
    except Exception as e:
        # Fallback to Trimesh
        import trimesh
        mesh = trimesh.load(model_path)
        return pv.wrap(mesh)
```

## Testing Strategy

### Unit Testing

- **Coverage target**: ≥ 80% code coverage
- **Test framework**: pytest
- **Mocking**: External API calls and file I/O
- **Fixtures**: Sample data and test models

### Integration Testing

- **End-to-end tests**: Complete workflow testing
- **Performance tests**: Runtime and memory benchmarks
- **API tests**: LLM integration testing

### Test Structure

```
tests/
├── unit/
│   ├── test_etl.py
│   ├── test_anomaly_detection.py
│   └── test_visualization.py
├── integration/
│   ├── test_full_pipeline.py
│   └── test_api_integration.py
└── fixtures/
    ├── sample_data.csv
    └── test_model.obj
```

## Deployment Considerations

### Local Development

- **Environment**: Python virtual environment
- **Dependencies**: Managed via uv
- **Configuration**: Environment variables
- **Data**: Local file system

### Production Deployment

- **Containerization**: Docker support
- **Scaling**: Horizontal scaling considerations
- **Monitoring**: Performance and error tracking
- **Security**: API key management

### Export Formats

- **CSV**: Structured anomaly data
- **JSON**: Metadata and configuration
- **HTML**: Interactive reports
- **PNG**: Static visualizations

## Performance Optimization

### Data Processing

- **Vectorization**: NumPy operations over loops
- **Chunking**: Process large datasets in chunks
- **Caching**: Cache intermediate results

### 3D Rendering

- **Level of detail**: Simplify models for performance
- **Culling**: Hide non-visible elements
- **Lazy loading**: Load models on demand

### Memory Management

- **Garbage collection**: Explicit cleanup of large objects
- **Memory profiling**: Monitor memory usage
- **Optimization**: Reduce memory footprint

## Security Considerations

### API Security

- **Key management**: Secure storage of API keys
- **Rate limiting**: Respect API rate limits
- **Error handling**: Don't expose sensitive information

### Data Privacy

- **Local processing**: Keep sensitive data local
- **Anonymization**: Optional data anonymization
- **Access control**: Secure file access

### Input Validation

- **File type validation**: Ensure valid input files
- **Data sanitization**: Clean user inputs
- **Error messages**: Don't expose system information
