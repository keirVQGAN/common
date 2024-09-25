import streamlit as st
from layers_and_styles import get_layers, get_styles
import prettymaps
import matplotlib.pyplot as plt
from io import BytesIO
from slugify import slugify  # For converting location to a file-safe string

# Function to create and display the map
def create_prettymap_app():
    st.title("Prettymaps Plotter")

    # Initialize session state to track whether the plot button was clicked
    if "plot_triggered" not in st.session_state:
        st.session_state.plot_triggered = False

    # User input: Location, Radius, and Dilate (on the same row)
    col1, col2 = st.columns([2, 1])

    with col1:
        location = st.text_input("Location", "Elephant and Castle", on_change=trigger_plot)
    with col2:
        radius = st.slider("Radius", min_value=50, max_value=2000, value=200, step=50)
    # with col3:
        # dilate = st.slider("Dilate", min_value=0, max_value=500, value=200, step=50)

    # Slugify the location to create a file-safe name
    slugified_location = slugify(location)

    # Plot button
    if st.button("Plot Map"):
        trigger_plot()

    # Only plot if the button was clicked or Enter was pressed in the location input
    if st.session_state.plot_triggered:
        # Generate the map plot using prettymaps
        layers = get_layers()
        styles = get_styles()

        # prettymaps.plot automatically returns a matplotlib figure and axis
        plot_result = prettymaps.plot(
            location, 
            layers=layers, 
            style=styles, 
            circle=True, 
            radius=radius, 
            dilate=300,
            preset=None
        )

        # Set up to be A3 landscape for saving
        plot_result.fig.set_size_inches(16.5, 11.7)  # A3 landscape size in inches

        # Store the plot in session state
        st.session_state["plot_fig"] = plot_result.fig

        # Reset the plot trigger to false after plotting
        st.session_state.plot_triggered = False

    # Check if a plot has been generated (stored in session state)
    if "plot_fig" in st.session_state:
        # Display the map again
        st.pyplot(st.session_state["plot_fig"])

        st.subheader("Download Plot")
        col1, col2 = st.columns(2)

        with col1:
            png_data = save_plot_to_bytes(st.session_state["plot_fig"], file_format="png")
            st.download_button(
                label="Download as PNG",
                data=png_data,
                file_name=f"{slugified_location}.png",  # Filename based on location
                mime="image/png"
            )

        with col2:
            svg_data = save_plot_to_bytes(st.session_state["plot_fig"], file_format="svg")
            st.download_button(
                label="Download as SVG",
                data=svg_data,
                file_name=f"{slugified_location}.svg",  # Filename based on location
                mime="image/svg+xml"
            )

# Helper function to set the plot trigger
def trigger_plot():
    """Set the flag in session_state to trigger a plot."""
    st.session_state.plot_triggered = True

# Function to save the plot as a bytes object for download
def save_plot_to_bytes(fig, file_format="png"):
    """Save the plot as a bytes object for download."""
    buf = BytesIO()
    fig.savefig(buf, format=file_format, bbox_inches='tight')
    buf.seek(0)  # Rewind the buffer to the beginning
    return buf

# Run the app
if __name__ == "__main__":
    create_prettymap_app()
