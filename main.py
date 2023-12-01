import sys
import streamlit as st
from PIL import Image

from DataPreprocess import data
from explore import explore

sys.path.insert(1,r"C:\Users\Vinoth\PycharmProjects\RiceExportsDataAnalysis\venv\Lib\site-packages")
import streamlit_option_menu
icon=Image.open(r"C:\Users\Vinoth\PycharmProjects\RiceExportsDataAnalysis\images\page icon.jpg")
st.set_page_config(layout="wide", page_title="Rice exports data analysis",page_icon=icon)

selected=streamlit_option_menu.option_menu("Menu",["About", "Data", "Data Explore", "Contact"],
                                           icons=["exclamation-circle","search","bar-chart","globe",'telephone-forward' ],
                                           menu_icon="cast",
                                           default_index=0,
                                           orientation="horizontal",
                                           styles={"nav-link": {"font-size": "15px", "text-align": "centre",
                                                                "--hover-color": "#d1798e"},
                                                   "nav-link-selected": {"background-color": "#b30e35"},"width":"100%"},)


if selected=="About":
    st.header("""Project Title: Rice Exports Data Analysis\n
Technologies: Data Cleansing, EDA, Visualization,PowerBI/Tableau/Streamlit\n
Domain: Fast Moving Consumer Goods
""")
    st.write("""About:\n
    The comprehensive dataset contains detailed information about rice exports from various exporters from all over the world.\n
    The dataset encompasses essential attributes such as importer/exporter names, addresses, quantities, values, and other pertinent details.\n
    Goal is to conduct an extensive data analysis to extract meaningful insights and address key questions regarding the rice export transactions. """)
if selected=="Data":
    data()

if selected=="Data Explore":
    explore()

if selected=='Contact':
    col1, col2=st.columns([0.5,1.5], gap='small')
    with col2:
        st.subheader("Name: :green[Vinoth Palanivel]")
        st.write("Degree: :green[Bachelor of Engineering in Electrical and Electronics Engineering]")
        st.write("E-mail: :green[vinothchennai97@gmail.com]")
        st.write("Mobile: :green[7904197698 or 9677112815]")
        st.write("Linkedin: :orange[https://www.linkedin.com/in/vinoth-palanivel-265293211/]")
        st.write("Github: :orange[https://github.com/Vinoth0208/]")