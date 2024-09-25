import streamlit as st
import prettymaps
from io import BytesIO
from layers_and_styles import get_layers, get_styles

# Helper function to set the plot trigger
def trigger_plot():
    """Set the flag in session_state to trigger a plot."""
    st.session_state.plot_triggered = True

# Function to save the plot as a bytes object for download
def save_plot_to_bytes(fig, file_format="png", dpi=300):
    """Save the plot as a bytes object for download with 300 DPI."""
    buf = BytesIO()
    fig.savefig(buf, format=file_format, bbox_inches='tight', dpi=dpi)
    buf.seek(0)  # Rewind the buffer to the beginning
    return buf

# Cache the plot result to avoid redundant calculations if inputs haven't changed
@st.cache_data(show_spinner=False)
def create_map_plot(location, radius, width, height, layers, styles, dilate=300):
    """Generate the map plot and store it in session state."""
    # Generate the map plot using prettymaps
    plot_result = prettymaps.plot(
        location,
        layers=layers,
        style=styles,
        circle=True,
        radius=radius,
        dilate=dilate,
        preset=None
    )

    # Set the plot size
    plot_result.fig.set_size_inches(width, height)

    # Store the plot in session state
    st.session_state["plot_fig"] = plot_result.fig

def filter_layers_and_styles(layers_enabled):
    """Filter layers and styles based on user input."""
    layers = get_layers()
    styles = get_styles()

    # Filter layers and styles based on what is enabled
    filtered_layers = {k: v for k, v in layers.items() if layers_enabled.get(k, False)}
    filtered_styles = {k: v for k, v in styles.items() if layers_enabled.get(k, False)}

    return filtered_layers, filtered_styles
