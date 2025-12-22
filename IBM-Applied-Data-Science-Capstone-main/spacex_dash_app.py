# ============================================================================
# SpaceX Launch Dashboard - Interactive Data Visualization Application
# ============================================================================
# This Dash application provides an interactive dashboard to explore SpaceX
# launch data, allowing users to filter by launch site and payload mass.
# ============================================================================

# Import required libraries
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# ---- DATA LOADING AND PROCESSING ----
# Read SpaceX launch dataset from CSV
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Calculate payload mass range for slider bounds
min_payload = spacex_df['Payload Mass (kg)'].min()
max_payload = spacex_df['Payload Mass (kg)'].max()

# ---- DROPDOWN OPTIONS ----
# Extract unique launch sites from data and create dynamic dropdown options
# This ensures dropdown always reflects actual sites in dataset
LAUNCH_SITES = spacex_df['Launch Site'].unique().tolist()
site_options = [{'label': 'All Sites', 'value': 'ALL'}] + \
               [{'label': site, 'value': site} for site in LAUNCH_SITES]

# ---- STYLING CONSTANTS ----
# Define reusable CSS-like styles for dashboard components
HEADER_STYLE = {'textAlign': 'center', 'color': '#503D36', 'fontSize': 40, 'marginBottom': 20}
CONTAINER_STYLE = {'padding': '20px'}

# ---- APP INITIALIZATION ----
# Create Dash application instance
app = Dash(__name__)

# ---- LAYOUT DEFINITION ----
# Build the dashboard layout with title, dropdown, graphs, and slider
app.layout = html.Div([
    # Dashboard title
    html.H1('SpaceX Launch Records Dashboard', style=HEADER_STYLE),
    
    # Dropdown for launch site selection
    # Users can select a specific site or view all sites
    dcc.Dropdown(
        id='site-dropdown',
        options=site_options,
        value='ALL',
        placeholder="Select a Launch Site",
        searchable=True,
        style={'marginBottom': 20}
    ),
    
    # Pie chart showing success rate by site
    dcc.Graph(id='success-pie-chart'),
    
    # Payload mass range slider label
    html.P("Payload range (Kg):", style={'marginTop': 20}),
    
    # Range slider for filtering by payload mass
    # Users can select min and max payload to filter data
    dcc.RangeSlider(
        id='payload-slider',
        min=0, max=10000, step=1000,
        marks={i: str(i) for i in range(0, 10001, 2000)},
        value=[min_payload, max_payload],
        tooltip={"placement": "bottom", "always_visible": True}
    ),
    
    # Scatter plot showing payload vs launch outcome
    dcc.Graph(id='success-payload-scatter-chart'),
], style=CONTAINER_STYLE)

# ---- CALLBACK FUNCTIONS ----
# Callbacks are triggered when user interacts with dashboard components

# Callback 1: Update pie chart based on selected launch site
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def get_pie_chart(site):
    """
    Generate pie chart showing success rate by launch site.
    
    Args:
        site (str): Selected launch site ('ALL' for all sites or specific site name)
    
    Returns:
        plotly.graph_objects.Figure: Pie chart figure
    """
    if site == 'ALL':
        # Show success distribution across all sites
        fig = px.pie(spacex_df, values='class', names='Launch Site',
                     title='Success Rate by Launch Site')
    else:
        # Show success distribution for specific site
        filtered = spacex_df[spacex_df['Launch Site'] == site]
        fig = px.pie(filtered, names='class',
                     title=f'Success Rate - {site}')
    return fig

# Callback 2: Update scatter chart based on site selection and payload range
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_chart(site, payload_range):
    """
    Generate scatter plot showing relationship between payload mass and launch outcome.
    
    Args:
        site (str): Selected launch site ('ALL' for all sites or specific site name)
        payload_range (tuple): Min and max payload mass to filter by
    
    Returns:
        plotly.graph_objects.Figure: Scatter plot figure
    """
    # Extract min and max from payload range slider
    low, high = payload_range
    
    # Filter data by payload mass range
    filtered = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & 
                         (spacex_df['Payload Mass (kg)'] <= high)]
    
    # Further filter by launch site if specific site selected
    if site != 'ALL':
        filtered = filtered[filtered['Launch Site'] == site]
    
    # Create scatter plot with booster version color-coding
    fig = px.scatter(filtered, x='Payload Mass (kg)', y='class',
                     color='Booster Version Category',
                     title=f'Payload vs. Outcome - {site}')
    return fig

# ---- APPLICATION EXECUTION ----
if __name__ == '__main__':
    app.run(debug=True, port=8050)
