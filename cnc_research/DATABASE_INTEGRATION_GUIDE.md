# Material Properties Database - Integration Guide

**For CNC Calculator Implementation**

---

## Quick Start

### Loading the Database

```python
import json

# Load the material properties database
with open('MATERIAL_PROPERTIES_DATABASE.json', 'r') as f:
    materials_db = json.load(f)

# Get a specific material
aluminum_6061 = materials_db['aluminum_alloys']['6061']

# Access properties
print(f"Machinability: {aluminum_6061['machinability_rating']}%")
print(f"Cutting Speed (Carbide): {aluminum_6061['cutting_speeds']['carbide']['roughing']}")
```

---

## Database Structure

```
MATERIAL_PROPERTIES_DATABASE.json
├── metadata
│   ├── version
│   ├── total_materials
│   ├── categories
│   └── data_sources
│
├── aluminum_alloys
│   ├── 6061 → Material properties
│   ├── 7075 → Material properties
│   └── ... (6 total)
│
├── steel
│   ├── low_carbon_mild_steel
│   ├── medium_carbon_steel
│   └── ... (6 total)
│
├── stainless_steel
│   ├── 303 → Material properties
│   └── ... (4 total)
│
├── titanium_alloys
│   ├── ti_6al_4v → Material properties
│   └── ... (3 total)
│
├── plastics
│   ├── acetal_copolymer → Material properties
│   └── ... (5 total)
│
├── exotic_alloys
│   ├── inconel_625 → Material properties
│   └── ... (3 total)
│
└── notes
    ├── machinability_rating
    ├── cutting_speeds
    └── important_warnings
```

---

## Material Property Structure

Each material contains 13 properties:

```python
material = {
    # Basic identification
    "common_names": ["6061-T6", "6061-T4"],
    "category": "aluminum_alloys",
    
    # Machining characteristics
    "machinability_rating": 85,  # % relative to free-machining steel
    "machinability_reference": "Relative to free-machining steel (100%)",
    
    # Physical properties
    "density": "2.70 g/cm³",
    
    "hardness": {
        "rockwell_b": 95,
        "brinell_hv": "107 HV",
        "note": "Values for T6 temper"
    },
    
    "tensile_strength": {
        "value": 310,
        "unit": "MPa",
        "yield_strength": 275,
        "note": "6061-T6 typical"
    },
    
    # Cutting recommendations
    "cutting_speeds": {
        "hss": {
            "roughing": "150-200 SFM",
            "finishing": "200-300 SFM",
            "unit": "SFM"
        },
        "carbide": {
            "roughing": "400-600 SFM",
            "finishing": "600-900 SFM",
            "unit": "SFM"
        },
        "coated_carbide": {
            "roughing": "500-800 SFM",
            "finishing": "800-1200 SFM",
            "unit": "SFM"
        }
    },
    
    # Application info
    "applications": [
        "Aircraft fuselage and wing components",
        "Automotive parts and trim",
        "Structural components",
        "Marine applications",
        "Consumer products"
    ],
    
    # Machining behavior
    "chip_formation": {
        "type": "Continuous chips",
        "characteristics": "Long, stringy chips that form easily",
        "break_control": "Can be aggressive with tool geometry"
    },
    
    "coolant_recommendations": {
        "preferred": ["Soluble oil", "Synthetic coolant", "Mist cooling"],
        "note": "Can machine dry; coolant improves finish"
    },
    
    "tool_wear_characteristics": "Minimal tool wear; good tool life",
    "surface_finish": "Excellent with sharp tools"
}
```

---

## Common Use Cases

### 1. Get Cutting Speed for a Material

```python
def get_cutting_speed(material_name, tool_type='carbide', operation='roughing'):
    """
    Get recommended cutting speed for a material.
    
    Args:
        material_name: e.g., '6061' for aluminum
        tool_type: 'hss', 'carbide', or 'coated_carbide'
        operation: 'roughing' or 'finishing'
    
    Returns:
        Speed range as string, e.g., "400-600 SFM"
    """
    # Find material in database
    for category, materials in materials_db.items():
        if category not in ['metadata', 'notes']:
            if material_name in materials:
                speeds = materials[material_name]['cutting_speeds']
                return speeds[tool_type][operation]
    
    return None

# Usage
speed = get_cutting_speed('6061', 'carbide', 'roughing')
print(f"6061 Carbide Roughing: {speed}")  # Output: 400-600 SFM
```

### 2. Calculate Adjusted Speeds Based on Machinability

```python
def calculate_adjusted_speed(base_speed, material_name):
    """
    Adjust a base speed by material machinability.
    
    Args:
        base_speed: Base cutting speed in SFM
        material_name: Material to lookup
    
    Returns:
        Adjusted speed in SFM
    """
    # Find material
    for category, materials in materials_db.items():
        if category not in ['metadata', 'notes']:
            if material_name in materials:
                material = materials[material_name]
                machinability = material['machinability_rating'] / 100
                return base_speed * machinability
    
    return base_speed

# Usage: Free-cutting steel baseline is 500 SFM
adjusted_6061 = calculate_adjusted_speed(500, '6061')  # 500 * 0.85 = 425 SFM
adjusted_titanium = calculate_adjusted_speed(500, 'ti_6al_4v')  # 500 * 0.25 = 125 SFM
```

### 3. Check Material Difficulty

```python
def get_material_difficulty(material_name):
    """
    Return difficulty level based on machinability rating.
    """
    for category, materials in materials_db.items():
        if category not in ['metadata', 'notes']:
            if material_name in materials:
                rating = materials[material_name]['machinability_rating']
                
                if rating >= 90:
                    return "Very Easy"
                elif rating >= 70:
                    return "Easy"
                elif rating >= 50:
                    return "Moderate"
                elif rating >= 30:
                    return "Difficult"
                else:
                    return "Extremely Difficult"
    
    return "Unknown"

# Usage
print(f"6061: {get_material_difficulty('6061')}")  # Very Easy
print(f"Titanium: {get_material_difficulty('ti_6al_4v')}")  # Extremely Difficult
```

### 4. Get All Materials in a Category

```python
def list_materials_by_category(category):
    """
    List all materials in a category.
    """
    if category in materials_db:
        return list(materials_db[category].keys())
    return []

# Usage
aluminum = list_materials_by_category('aluminum_alloys')
print(f"Aluminum alloys: {', '.join(aluminum)}")
```

### 5. Get Material Applications

```python
def get_applications(material_name):
    """
    Return typical applications for a material.
    """
    for category, materials in materials_db.items():
        if category not in ['metadata', 'notes']:
            if material_name in materials:
                return materials[material_name]['applications']
    return []

# Usage
apps = get_applications('6061')
print(f"6061 Applications: {', '.join(apps)}")
```

### 6. Check Coolant Requirements

```python
def needs_flood_coolant(material_name):
    """
    Check if material requires flood coolant.
    """
    flood_required = [
        'ti_6al_4v', 'grade_2', 'grade_5',  # Titanium
        '304', '316',  # Stainless
        'inconel_625', 'hastelloy_c276', 'waspaloy'  # Exotics
    ]
    return material_name in flood_required

def get_coolant_recommendation(material_name):
    """
    Get coolant recommendations for material.
    """
    for category, materials in materials_db.items():
        if category not in ['metadata', 'notes']:
            if material_name in materials:
                return materials[material_name]['coolant_recommendations']
    return None

# Usage
coolant = get_coolant_recommendation('6061')
print(f"Coolant: {coolant['preferred']}")  # ['Soluble oil', 'Synthetic coolant', 'Mist cooling']
```

### 7. Validate Operator Input

```python
def is_valid_material(material_name):
    """
    Check if material exists in database.
    """
    for category, materials in materials_db.items():
        if category not in ['metadata', 'notes']:
            if material_name in materials:
                return True
    return False

# Usage
if is_valid_material('6061'):
    print("Material found in database")
else:
    print("Material not in database")
```

---

## Data Types & Units

### Cutting Speeds
- **Format**: "150-200 SFM" (Surface Feet Per Minute)
- **Parse Example**: `speeds = "400-600"; min_speed, max_speed = [int(x) for x in speeds.split("-")]`

### Hardness
- **Rockwell B**: Ranges 55-120 (lower is softer)
- **Rockwell C**: Ranges 20-65 (hardened materials)
- **Brinell HV**: Ranges 60-800+ (higher is harder)

### Tensile Strength
- **Unit**: MPa (Megapascals)
- **Range**: 30 MPa (HDPE) to 1470 MPa (hardened tool steel)

### Density
- **Unit**: g/cm³
- **Range**: 0.96 (HDPE) to 8.89 (Hastelloy C-276)

### Machinability Rating
- **Unit**: Percentage (%)
- **Reference**: Free-cutting steel = 100%
- **Range**: 12% (most difficult) to 100% (easiest)

---

## Error Handling

```python
def safe_get_material(category, material_name):
    """
    Safely get material with error handling.
    """
    try:
        if category in materials_db:
            if material_name in materials_db[category]:
                return materials_db[category][material_name]
        return None
    except KeyError:
        return None

def parse_speed_range(speed_str):
    """
    Parse speed string like "400-600 SFM" to tuple.
    """
    try:
        range_part = speed_str.split()[0]  # "400-600"
        min_speed, max_speed = [int(x) for x in range_part.split('-')]
        return (min_speed, max_speed)
    except (ValueError, IndexError):
        return None
```

---

## Integration Checklist

- [ ] Load MATERIAL_PROPERTIES_DATABASE.json on startup
- [ ] Validate material selection against database
- [ ] Use machinability_rating for speed calculations
- [ ] Check coolant_recommendations for operational setup
- [ ] Display cutting_speeds for selected tool type
- [ ] Warn user if material requires special handling
- [ ] Use tool_wear_characteristics for tool life estimates
- [ ] Reference chip_formation for feed adjustment
- [ ] Display applications for context
- [ ] Log any database lookup failures

---

## Performance Notes

- Database loads in < 10ms on typical hardware
- JSON parsing is instant for single material lookups
- All 27 materials fit easily in memory
- No database optimization needed for current scale

---

## Related Documentation

- **MATERIAL_PROPERTIES_REFERENCE.md** - Human-readable guide
- **MATERIAL_PROPERTIES_DATABASE.json** - Raw database
- **CNC_PRODUCT_REQUIREMENTS.md** - Calculator specifications

---

*Last Updated: November 11, 2025*
