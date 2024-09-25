import streamlit as st
from slugify import slugify  # For converting location to a file-safe string
from utils import trigger_plot, save_plot_to_bytes, create_map_plot, filter_layers_and_styles  # Import helper functions
from layers_and_styles import get_layers, get_styles  # Import layer and style functions

# Configuration constants
A3_WIDTH = 16.5
A3_HEIGHT = 11.7

# Option to show or hide the toggle layers UI
show_layer_toggle = True  # Set this to False to hide the "Map Layers" accordion

# Main function to create and display the map
def create_prettymap_app():
    st.title("Prettymaps Plotter")

    # Initialize session state if not already set
    if "plot_triggered" not in st.session_state:
        st.session_state.plot_triggered = False

    # Initialize layers_enabled with default values (all True except for perimeter)
    if "layers_enabled" not in st.session_state:
        st.session_state["layers_enabled"] = {layer: True for layer in get_layers() if layer != "perimeter"}

    # User input: Location, Radius, and other parameters
    col1, col2 = st.columns([2, 1])

    with col1:
        location = st.text_input(
            "Location",
            "Elephant and Castle",
            help="Enter any location you can find on OpenStreetMap (https://www.openstreetmap.org)"
        )
    with col2:
        radius = st.slider("Radius", min_value=50, max_value=1500, value=300, step=50)

    # Slugify the location to create a file-safe name
    slugified_location = slugify(location)

    # Optional: Show layer toggles in an accordion, organized in rows and columns
    if show_layer_toggle:
        with st.expander("Map Layers", expanded=True):
            st.write("Enable or disable layers:")

            # Layout the switches in a grid for better compactness
            layer_list = list(get_layers().keys())
            cols = st.columns(3)  # Create 3 columns for the layer switches

            for i, layer in enumerate(layer_list):
                if layer != "perimeter":  # Exclude "perimeter" from the toggle options
                    with cols[i % 3]:  # Use modulo to distribute the layers into columns
                        st.session_state["layers_enabled"][layer] = st.checkbox(
                            f"{layer.capitalize()}",
                            value=st.session_state["layers_enabled"][layer],  # Retain previous state
                            key=layer
                        )

    # Plot button
    if st.button("Plot Map"):
        trigger_plot()
        # Only plot if the button was clicked
        try:
            # Filter layers and styles based on switches, ensure 'perimeter' is always on
            selected_layers, selected_styles = filter_layers_and_styles(st.session_state["layers_enabled"])
            selected_layers["perimeter"] = get_layers()["perimeter"]  # Always include perimeter
            selected_styles["perimeter"] = get_styles()["perimeter"]  # Always include perimeter style

            # Generate and display the map
            create_map_plot(location, radius, A3_WIDTH, A3_HEIGHT, selected_layers, selected_styles)
            st.session_state.plot_triggered = False  # Reset the trigger after plotting
        except Exception as e:
            st.error(f"Failed to generate the map: {str(e)}")

    # Display the generated plot if it exists
    if "plot_fig" in st.session_state:
        st.pyplot(st.session_state["plot_fig"])

        col1, col2 = st.columns(2)

        with col1:
            png_data = save_plot_to_bytes(st.session_state["plot_fig"], file_format="png")
            st.download_button(
                label="Download as PNG",
                data=png_data,
                file_name=f"{slugified_location}.png",
                mime="image/png"
            )

        with col2:
            svg_data = save_plot_to_bytes(st.session_state["plot_fig"], file_format="svg")
            st.download_button(
                label="Download as SVG",
                data=svg_data,
                file_name=f"{slugified_location}.svg",
                mime="image/svg+xml"
            )

# Run the app
if __name__ == "__main__":
    create_prettymap_app()
