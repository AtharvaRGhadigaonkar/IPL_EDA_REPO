# import streamlit as st

# # Set page configuration
# st.set_page_config(
#     page_title="IPL Data Dashboard",
#     page_icon="🏏",
#     layout="wide"
# )

# # Set the dark theme
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #1e1e1e;
#         color: #ffffff;
#     }
#     h1 {
#         color: #00bcd4;
#     }
#     h2 {
#         color: #ff4081;
#     }
#     h3 {
#         color: #ffeb3b;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Title and header
# st.title("🏏 IPL Data Dashboard")
# st.markdown(
#     """
#     Welcome to the IPL Data Dashboard! Here you can explore various statistics, player performances, and match results from the Indian Premier League.
    
#     ### What You Can Do Here:
#     - View player statistics
#     - Analyze match results
#     - Compare team performances
    
#     Feel free to navigate through the sections below and discover more about your favorite teams and players!
#     """
# )

# # Main content sections
# st.header("Home")
# st.write("This is the home section. You can find general information about IPL here.")

# st.header("Player Statistics")
# st.write("In this section, you'll find detailed statistics about players.")

# st.header("Match Results")
# st.write("Here you can explore the results of various IPL matches.")

# st.header("Team Analysis")
# st.write("Analyze the performance of different teams throughout the IPL seasons.")

# # Footer
# st.markdown(
#     """
#     --- 
#     Made with ❤️ by [Your Name]
#     """
# )

import streamlit as st
from PIL import Image

# Set page title and favicon
st.set_page_config(page_title="IPL Data Analysis", page_icon="🏏", layout="wide")

# Add a background image or header image (optional)
header_image = Image.open('pages/images/CSK_logo2.png')  # Use a cricket-related image
st.image(header_image, use_column_width=True)

# Main title and subtitle
st.markdown("<h1 style='text-align: center; color: #F39C12;'>IPL Data Analysis</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #27AE60;'>Explore the thrilling world of IPL with data-driven insights!</h3>", unsafe_allow_html=True)

# Brief introduction
st.markdown("""
<p style='text-align: center; font-size: 18px;'>
Welcome to the **IPL Data Analysis** app! Dive into the history of one of the biggest cricket leagues in the world - 
the **Indian Premier League (IPL)**. Whether you're a cricket enthusiast, a data nerd, or a curious mind, 
this app will help you uncover hidden patterns, trends, and insights from IPL data!
</p>
""", unsafe_allow_html=True)

# Call to action button
st.markdown("<p style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Get Started 🚀"):
    st.write("Redirecting to the main analysis page...")  # Add logic for redirection
st.markdown("</p>", unsafe_allow_html=True)

# Features section
st.markdown("---")
st.markdown("""
<h2 style='text-align: center; color: #2980B9;'>Features of the App</h2>
<div style='text-align: center;'>
    <ul style='list-style-type: none; font-size: 18px;'>
        <li>🏏 <b>Comprehensive Player Statistics</b>: Explore individual player performance across seasons.</li>
        <li>📊 <b>Match Insights</b>: Analyze match outcomes, strategies, and key moments.</li>
        <li>📅 <b>Season Trends</b>: Track the performance of teams and players across different IPL seasons.</li>
        <li>🤖 <b>Machine Learning Predictions</b>: Predict match results and player scores using advanced algorithms.</li>
        <li>📉 <b>Visualize Trends</b>: Aesthetic and interactive data visualizations for deeper insights.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Footer section
st.markdown("---")
st.markdown("""
<div style='text-align: center; font-size: 14px;'>
    <p>Developed with ❤️ using <b>Streamlit</b> and <b>Python</b> | Powered by IPL Data</p>
    <p style='color: #7f8c8d;'>© 2024 IPL Data Analysis | All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)