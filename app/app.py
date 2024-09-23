import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="IPL Data Dashboard",
    page_icon="🏏",
    layout="wide"
)

# Set the dark theme
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    h1 {
        color: #00bcd4;
    }
    h2 {
        color: #ff4081;
    }
    h3 {
        color: #ffeb3b;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and header
st.title("🏏 IPL Data Dashboard")
st.markdown(
    """
    Welcome to the IPL Data Dashboard! Here you can explore various statistics, player performances, and match results from the Indian Premier League.
    
    ### What You Can Do Here:
    - View player statistics
    - Analyze match results
    - Compare team performances
    
    Feel free to navigate through the sections below and discover more about your favorite teams and players!
    """
)

# Main content sections
st.header("Home")
st.write("This is the home section. You can find general information about IPL here.")

st.header("Player Statistics")
st.write("In this section, you'll find detailed statistics about players.")

st.header("Match Results")
st.write("Here you can explore the results of various IPL matches.")

st.header("Team Analysis")
st.write("Analyze the performance of different teams throughout the IPL seasons.")

# Footer
st.markdown(
    """
    --- 
    Made with ❤️ by [Your Name]
    """
)

