def get_layers():
    return {
        "streets": {
            "width": {
                "motorway": 5,
                "trunk": 5,
                "primary": 4,
                "secondary": 3,
                "tertiary": 2,
                "residential": 2,
                "unclassified": 2,
                "service": 1.3,
                "path": 1,
                "footway": 1,
                "cycleway": 1
            }
        },
        "building": {
            "tags": {
                "building": True
            }
        },
        "green_areas": {
            "tags": {
                "leisure": [
                    "park", "garden", "nature_reserve", "pitch", "playground", 
                    "golf_course", "recreation_ground", "sports_centre"
                ],
                "landuse": [
                    "forest", "grass", "recreation_ground", "allotments", 
                    "meadow", "orchard", "village_green", "vineyard"
                ],
                "natural": [
                    "wood", "scrub", "grassland", "heath", "wetland", "meadow"
                ]
            }
        },
        "landuse": {
           "tags": {
                "landuse": True
            #     "landuse": [
            #         "industrial", "commercial", "residential", "retail", 
            #         "military", "railway", "brownfield", "cemetery", "construction",
            #         "farmland", "farmyard", "quarry"
            #     ],
            #     "leisure": [
            #         "marina", "stadium", "track", "sports_pitch", "fitness_station"
            #     ],
            #     "natural": [
            #         "bare_rock", "sand", "scree", "shingle", "fell", "beach"
            #     ]
            }
        },
        "water": {
            "tags": {
                "water": [
                    "river", "lake", "reservoir", "pond", "stream", "canal", 
                    "bay", "basin", "harbour"
                ],
                "natural": [
                    "water", "wetland", "bay", "spring"
                ],
                "waterway": [
                    "river", "stream", "canal", "drain", "ditch"
                ]
            }
        },
        "railways": {
            "tags": {
                "railway": [
                    "rail", "light_rail", "subway", "tram", "monorail", 
                    "narrow_gauge", "funicular"
                ]
            }
        },
        "perimeter": {}
    }

def get_styles():
    return {   
        "streets": {
            "fc": "#adadad",  # Light grey streets fill
            "ec": "#adadad",  # Medium-light grey for streets edge
            "alpha": 0.65,
            "lw": 0.3,        # Line width for streets
            "zorder": 3       # Layer order
        },
        "building": {
            # "fill": None,       # No fill for buildings
            "fc": "#ffffff",
            "ec": "#7a7a7a",  # Light grey for buildings edges
            "lw": 0.7,        # Line width for buildings
            "zorder": 4       # Layer order
        },
        "green_areas": {
            "fill": None,       # No fill for green areas
            "ec": "#a8d3c0",  # Light pastel green-grey for green areas edges
            "lw": 0.4,        # Line width for green areas
            "hatch": '//////',# Hatch pattern for green areas
            "zorder": 2       # Layer order
        },
        "landuse": {
            "alpha": 0.1,
            # "fill": None,       # No fill for landuse areas
            "fc": "#b3b3b3",
            "ec": "#b3b3b3",  # Lighter grey for landuse areas
            "lw": 0.7,        # Line width for landuse areas
            "zorder": 0       # Layer order
        },
        "water": {
            "alpha": 0.3,       # Transparency for water
            "ec": "#cfd8dc",  # Very light blue-grey for water edges
            "lw": 0.2,        # Line width for water bodies
            "hatch": '......', # Hatch pattern for water bodies
            "zorder": 1       # Layer order
        },
        "railways": {
            "fill": None,       # No fill for railways
            "ec": "#616161",  # Slightly darker grey for railways edges
            "lw": 0.8,        # Line width for railways
            "zorder": 2       # Layer order
        },
        "perimeter": {
            "fill": None,    # No fill for the perimeter
            "lw": 0,          # No line width
            "ec": '#e0e0e0',  # Very light grey for perimeter
            "zorder": 0       # Lowest layer order
        }
    }
