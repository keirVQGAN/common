# A Common Key - Streamlit App

This Streamlit application is a simple wrapper around the [Prettymaps](https://github.com/marceloprates/prettymaps) project, which allows users to generate custom map plots using data from [OpenStreetMap](https://www.openstreetmap.org/). The app provides an easy-to-use web interface to toggle map layers, customize plots, and download them in A3-sized PNG and SVG formats.

## Features

- **Location-based map plots**: Enter any location to generate a map using OpenStreetMap data.
- **Layer control**: Toggle individual map layers (streets, buildings, green areas, etc.) for customization.
- **Downloadable maps**: Download generated maps as high-quality PNG or SVG files in A3 landscape format.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
    ```

2. Install the required dependencies (requires Python 3.10):
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app (requires Python 3.10):
    ```bash
    streamlit run app.py
    ```

## Dependencies

This project uses the following libraries:

- [Streamlit](https://streamlit.io/) for the web interface.
- [Prettymaps](https://github.com/marceloprates/prettymaps) for generating map plots.
- [Slugify](https://github.com/un33k/python-slugify) for converting location names into file-safe strings.
- [Matplotlib](https://matplotlib.org/) for displaying and saving plots.
- [OpenStreetMap](https://www.openstreetmap.org/) for map data.

## How It Works

This app provides an intuitive web interface, allowing users to generate maps based on any location found via OpenStreetMap. It serves as a wrapper for the [Prettymaps](https://github.com/marceloprates/prettymaps) project, which handles the underlying map plotting using OSM data. 

Users can toggle layers such as streets, buildings, water, and more to customize the appearance of the maps. Once the map is generated, users can download it as a PNG or SVG file with A3 dimensions.

## Credits

This app is built using the amazing [Prettymaps](https://github.com/marceloprates/prettymaps) library created by [Marcelo Prates](https://github.com/marceloprates).

All map data is sourced from [OpenStreetMap](https://www.openstreetmap.org/).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
