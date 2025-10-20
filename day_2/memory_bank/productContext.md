# Product Context: Energy Anomaly Detection (EAD)

## Why This Project Exists

### The Problem

Current energy analysis tools suffer from a fundamental disconnect:

- **Energy analytics** (spreadsheets, BMS systems) operate in isolation
- **Spatial context** (BIM models) exists separately
- **Decision makers** lack integrated tools to understand energy anomalies in their spatial context

### The Vision

Create a lightweight, explainable system that bridges energy analytics and spatial context within a single Python interface, enabling users to **see, understand, and explain** energy anomalies in 3D space.

## Problems It Solves

### 1. Spatial-Energy Disconnect

- **Current State**: Energy data exists in spreadsheets, BIM models are static
- **Solution**: Real-time 3D visualization of energy anomalies mapped to building elements
- **Value**: Architects can see which spaces have energy issues

### 2. Lack of Explainability

- **Current State**: Anomaly detection outputs numbers without context
- **Solution**: LLM-generated explanations of anomalies with domain context
- **Value**: Non-technical stakeholders understand what's happening and why

### 3. Tool Fragmentation

- **Current State**: Multiple tools for data analysis, visualization, and reporting
- **Solution**: Single Python/Marimo interface for end-to-end workflow
- **Value**: Streamlined workflow from data to insights

## How It Should Work

### User Experience Flow

1. **Load Data**: Import energy CSV and 3D model (OBJ files)
2. **Configure Analysis**: Set time windows and anomaly thresholds
3. **Run Analysis**: Automated z-score computation and classification
4. **Visualize Results**: Interactive 3D model with color-coded anomalies
5. **Get Explanations**: AI-generated summary of top anomalies
6. **Export Results**: Structured outputs for further analysis

### Key User Interactions

- **3D Navigation**: Orbit, pan, zoom in 3D model
- **Element Inspection**: Click building elements to see energy metrics
- **Legend Interaction**: Toggle anomaly classes on/off
- **Export Options**: Download results as CSV/JSON

## User Experience Goals

### For AI Engineers/Students

- **Goal**: Showcase LLM + data fusion capabilities
- **Experience**: Demonstrate how AI can explain complex energy patterns
- **Success**: Clear demonstration of AI's value in energy analysis

### For Architects/BIM Managers

- **Goal**: Validate design vs measured energy use
- **Experience**: Visual identification of high-energy zones in 3D
- **Success**: Quick identification of design issues or operational problems

### For Sustainability Analysts

- **Goal**: Demonstrate traceable energy audit process
- **Experience**: Systematic analysis with documented assumptions
- **Success**: Reproducible results with clear audit trail

## Value Proposition

### Technical Value

- **Integration**: Combines data analysis, 3D visualization, and AI explanation
- **Reproducibility**: Consistent results with documented assumptions
- **Extensibility**: Modular design allows for future enhancements

### Business Value

- **Efficiency**: Single tool replaces multiple systems
- **Insight**: 3D context makes energy data actionable
- **Communication**: AI explanations bridge technical and business stakeholders

### Educational Value

- **Learning**: Demonstrates modern AI/ML engineering practices
- **Portfolio**: Showcases full-stack data science capabilities
- **Innovation**: Pushes boundaries of energy analysis tools

## Success Criteria

### Functional Success

- ✅ Load and process energy data
- ✅ Detect anomalies with statistical rigor
- ✅ Render 3D models with anomaly visualization
- ✅ Generate meaningful AI explanations
- ✅ Export structured results

### Performance Success

- ✅ Complete analysis in ≤ 30 seconds
- ✅ Load 3D models in ≤ 8 seconds
- ✅ Achieve ≥ 95% anomaly detection accuracy
- ✅ Generate ≥ 80% accurate AI explanations

### User Experience Success

- ✅ Intuitive 3D navigation
- ✅ Clear visual feedback
- ✅ Understandable AI explanations
- ✅ Smooth workflow from data to insights

## Future Vision

### Phase 2+ Enhancements

- **Contextual Regression**: Adjust for temperature and occupancy
- **ML Predictive Baselines**: XGBoost/Prophet forecasting
- **Web Integration**: Move to React + xeokit for web deployment
- **Continuous Learning**: Incremental model updates
- **Voice/Chat Assistant**: Natural language queries

### Long-term Impact

- **Industry Standard**: Establish new paradigm for energy analysis
- **Research Platform**: Enable new research in energy-AI integration
- **Educational Tool**: Train next generation of energy analysts
