# PowerCo Emission Intensity Case Study

**Author:** Ricardo Modrego  
**Date:** May 2025  

---

## 📄 Overview  
Evaluation of PowerCo’s physical emission intensity (kg CO₂e/MWh) vs. German benchmarks, plus recommended data sources.

## 🗂️ Repository Structure
- `data/` – input Excel & CSV data  
- `notebooks/Ricardo_Data_Analysis.ipynb` – step-by-step code execution  
- `src/` – modular Python classes & utilities  
- `slides/Ricardo_Modrego_PowerCo_Case_Study.pptx` – two-slide summary  
- `LICENSE` – MIT License  
- `.gitignore` – ignores temp files, caches, etc.

## 🚀 Getting Started
1. **Clone** the repo
   ```bash
   git clone git@github.com:you/powerco-emission-intensity.git
   cd powerco-emission-intensity
2. Install dependencies
   ```bash
   pip install -r requirements.txt
3. Run Analysis
   Open `notebooks/Ricardo_Data_Analysis.ipynb` and follow the cells
4. View deliverables
   See `slides/Ricardo_Modrego_PowerCo_Case_Study.pptx`

## 🔧 Configuration
Edit `src/config.py` to adjust:
- File paths('POWERCO_XLSX', 'GLOBAL_PPP_CSV', 'EMBER_CSV')
- Geographic thresholds ('DISTANCE_THRESHOLD_DEG', 'NORTH_SEA_LAT_RANGE', 'NORTH_SEA_LON_RANGE')
- Emission & capacity factors ('PEAK_CAPACITY_FACTOR', 'WIND_PARK_EMISSION_INTENSITY', 'SOLAR_PARK_EMISSION_INTENSITY')

## 🧰 Running code
- DataLoader: loads and renames CSV/Excel files.
- CoordinateConverter: (optional) converts DMS to decimal degrees.
- SpatialMatcher: locates nearest Ember emissions to global plants.
- PowerPlantAnalyzer: filters by country or region, selects client plants, computes load proportions.
- CapacityFactorAnalyzer: computes and averages capacity factors.
- EmissionAnalyzer: computes emissions per MW and average intensity.
- EnergyCalculator & EmissionCalculator: calculate generation and final kg CO₂e/MWh metrics.

   ## 📝 Deliverables
- **Jupyter Notebook**: `notebooks/analysis.ipynb`  
- **Slides**: `slides/PowerCo_Emission_Intensity.pptx`
