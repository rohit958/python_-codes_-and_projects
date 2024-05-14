import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import xlrd
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Superstore!!!",page_icon="bar_chart:",layout="wide")

st.title(" :bar_chart: Sample SuperStore EDA")

st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file:",type=(["csv","txt","xlsx","xls"]))

if fl is not None:
    file_name= fl.name
    st.write(file_name)
    df=pd.read_excel(file_name)
else:
    os.chdir(r"C:\git\rohit958\python_-codes_-and_projects\Dashboards")
    df=pd.read_excel("Superstore.xls")
#--server.enableXsrfProtection false

#date columns

col1,col2=st.columns(2)
df["Orderdate"]= pd.to_datetime(df["Order Date"])


startdate= pd.to_datetime(df["Orderdate"]).min()
enddate= pd.to_datetime(df["Orderdate"]).max()

with col1:
    date1=pd.to_datetime(st.date_input("Start date",startdate))

with col2:
    date2=pd.to_datetime(st.date_input("End date",enddate))

df= df[(df["Orderdate"]>=date1)&(df["Orderdate"]<=date2)].copy()

#side bar filters
st.sidebar.header("Choose your Filter:")
region=st.sidebar.multiselect("Pick your Region",df["Region"].unique())

if not region:
    df2=df.copy()
else:
    df2=df[df["Region"].isin(region)]


state = st.sidebar.multiselect("Pick the State",df2["State"].unique())

if not state:
    df3=df2.copy()
else:
    df3=df2[df2["State"].isin(state)]

city = st.sidebar.multiselect("Pick the City",df2["City"].unique())

#filterin city state and region

if not region and not state and city:
    filtereddf= df
elif not state and not city:
    filtereddf= df[df["Region"].isin(region)]
elif not region and not city:
    filtereddf= df[df["State"].isin(state)]
elif state and city:
    filtereddf= df3[df["State"].isin(state)& df3["City"].isin(city)]
elif state and region:
    filtereddf= df3[df["State"].isin(state)& df3["Region"].isin(region)]
elif region and city:
    filtereddf= df3[df["Region"].isin(region)& df3["City"].isin(city)]
elif city:
    filtereddf=df3[df3["City"].isin(city)]

else:
    filtereddf=df3[df3["State"].isin(state)] & df3[df3["City"].isin(city)] & df3[df3["Region"].isin(region)]

# category charts

categorydf= filtereddf.groupby(by=["Category"],as_index=False)["Sales"].sum()

with col1:
    st.subheader("Category with Sales")
    fig=px.bar(categorydf,x="Category", y="Sales", text= ['${:,.2f}'.format(x) for x in categorydf["Sales"]],
        template="seaborn")
    st.plotly_chart(fig,use_container_width=True,height=200)
with col2:
    st.subheader("Region with sales")
    fig=px.pie(filtereddf,values="Sales",names="Region",hole=0.5)
    fig.update_traces(text=filtereddf["Region"],textposition="outside")
    st.plotly_chart(fig,use_container_width=200)

