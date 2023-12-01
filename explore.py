import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def explore():
    data=pd.read_csv(r'Data.csv')
    tab1, tab2, tab3, tab4, tab5, tab6=st.tabs(["Importer/Exporter Overview","Geographical Analysis", "Product Analysis", "Financial Analysis", "Time-Series Analysis", "Key Insights and Trends"])
    with tab1:
        data.sort_values(by='IMPORT VALUE CIF', ascending=False, inplace=True)
        df = data.head(100)
        tab1_1, tab1_2=st.tabs(["Importer Insights", "Exporter Insights"])
        with tab1_1:
            image=px.bar(data_frame=df,x='IMPORTER NAME', y='IMPORT VALUE CIF',color="IMPORT VALUE CIF", barmode="stack")
            st.header(":green[Top Importers:]")
            st.plotly_chart(image, use_container_width=True)


        with tab1_2:
            df = data.head(10)
            image = px.bar(data_frame=df, x='EXPORTER NAME', y='IMPORT VALUE CIF', color="IMPORT VALUE CIF", barmode="stack")
            st.header(":green[Top Exporters:]")
            st.plotly_chart(image, use_container_width=True)

    with tab2:
        location = px.choropleth(data_frame=data,
                                 locations='IMPORTER COUNTRY',
                                 color='IMPORTER COUNTRY',
                                 hover_data={'HS CODE DESCRIPTION': True, 'IMPORTER NAME':True, 'EXPORTER NAME':True, 'IMPORTER COUNTRY': True, "IMPORT VALUE CIF":True, "IMPORT VALUE FOB":True, },
                                 locationmode='country names')
        st.header(":orange[Geo Visualization Rice Exports Data:]")
        location.update_layout(autosize=False, margin=dict(l=10, r=0, b=20, t=20, pad=9, autoexpand=True),
                               width=1000, )

        st.plotly_chart(location, use_container_width=True)

        col1, col2= st.columns([1,1])
        with col1:
            location = px.choropleth(data_frame=data,
                                     locations='IMPORTER COUNTRY',
                                     color='PORT OF ARRIVAL',
                                     hover_data={'PORT OF ARRIVAL': True, 'PORT OF DEPARTURE': True, "PRODUCT DETAILS":True },
                                     locationmode='country names')
            st.header(":green[Geo Visualization Port of Arrival:]")
            location.update_layout(autosize=False, margin=dict(l=10, r=0, b=20, t=20, pad=9, autoexpand=True),
                                   width=1000, )
            st.plotly_chart(location, use_container_width=True)
        with col2:
            location = px.choropleth(data_frame=data,
                                     locations='COUNTRY OF ORIGIN',
                                     color='COUNTRY OF ORIGIN',
                                     hover_data={'PORT OF ARRIVAL': True, 'PORT OF DEPARTURE': True,
                                                 "PRODUCT DETAILS": True},
                                     locationmode='country names')
            st.header(":violet[Geo Visualization Country of Orgin:]")
            location.update_layout(autosize=False, margin=dict(l=10, r=0, b=20, t=20, pad=9, autoexpand=True),
                                   width=1000, )
            st.plotly_chart(location, use_container_width=True)
    with tab3:
        image=px.bar(data,x="HS CODE DESCRIPTION", y="QUANTITY", barmode='stack', color='QUANTITY')
        st.header(":green[Variety vs Quantity:]")
        st.plotly_chart(image, use_container_width=True)

        image = px.bar(data, x="HS CODE DESCRIPTION", y="IMPORT VALUE CIF", barmode='stack', color='IMPORT VALUE CIF')
        st.header(":green[Variety vs IMPORT VALUE CIF:]")
        st.plotly_chart(image, use_container_width=True)
    with tab4:
        image = px.bar(data, x="IMPORT VALUE CIF", y="CURRENCY", barmode='stack', color='CURRENCY')
        st.header(":green[IMPORT VALUE CIF vs CURRENCY:]")
        st.plotly_chart(image, use_container_width=True)

        image = px.histogram(data, x="IMPORT VALUE CIF", y="PRODUCT DETAILS", color='CURRENCY')
        st.header(":green[IMPORT VALUE CIF vs Product Details:]")
        st.plotly_chart(image)
    with tab5:
        image = px.scatter(data, y="HS CODE DESCRIPTION", x="ARRIVAL DATE", color='ARRIVAL DATE')
        st.header(":green[HS CODE DESCRIPTION vs ARRIVAL DATE:]")
        st.plotly_chart(image, use_container_width=True)
    with tab6:
        st.header("Conclusion:")
        st.write("""Importer/Exporter Overview:\n
        We are able to find the \n
         1.Top Importer is STE DE DISTRUBUTION TOUTE M\n
         2.TOp Exporter is OLAM INTERNATIONAL LIMITED
        """)
        st.write("""Geographical Analysis:\n
                We are able to Visualize the\n 
                 1. Regions where product is exported\n 
                 2. The port of Arrival\n
                 3. The Country of Origin
                """)
        st.write("""Product Analysis:\n
                        We are able to Visualize the\n 
                         1. Various variety of Product and Quantity\n 
                         2. Various variety of Product and IMPORT VALUE OF CIF
                        """)
        st.write("""Financial Analysis:\n
                                We are able to Visualize the\n 
                                 1. CURRENCY across various products exported 
                                """)
        st.write("""Time-Series Analysis:\n
                                        We are able to Visualize the\n 
                                         1. Products over Time 
                                        """)