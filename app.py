import streamlit as st
import tifffile
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO




'''
# BioMassters App
'''

st.markdown(f'''
See an image being predicted by our model in real time!!
''')

st.image('https://images.unsplash.com/photo-1604009506606-fd4989d50e6d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80')
#         caption='Photo by <a href="https://unsplash.com/@chelseabock?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Chelsea Bock</a> on <a href="https://unsplash.com/s/photos/forest?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>')

st.markdown('''
            See the BioMassters challenge in this link: [https://www.drivendata.org/competitions/99/biomass-estimation/page/534/](https://www.drivendata.org/competitions/99/biomass-estimation/page/534/)
            ''')


col1, col2 = st.columns(2)

uploaded_file1 = None
uploaded_file2 = None

with col1:
    uploaded_file1 = st.file_uploader("Choose S1 file:")

with col2:
    uploaded_file2 = st.file_uploader("Choose S2 file:")

if (uploaded_file1 is not None):
    with st.expander("S1 SATELLITE IMAGES"):
        col1, col2 = st.columns(2)
        XS1 = tifffile.imread(uploaded_file1)
        with col1:
            fig1 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS1[:,:,0])
            st.pyplot(fig1)
            fig2 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS1[:,:,2])
            st.pyplot(fig2)
        with col2:
            fig3 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS1[:,:,1])
            st.pyplot(fig3)
            fig4 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS1[:,:,3])
            st.pyplot(fig4)

if (uploaded_file2 is not None):
    with st.expander("S2 SATELLITE IMAGES"):
        col1, col2, col3 = st.columns(3)
        XS2 = tifffile.imread(uploaded_file2)
        with col1:
            fig5 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS2[:,:,0])
            st.pyplot(fig5)
            fig6 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS2[:,:,3])
            st.pyplot(fig6)
            fig7 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS2[:,:,6])
            st.pyplot(fig7)
            fig8 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS2[:,:,9])
            st.pyplot(fig8)

        with col2:
            fig9 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS2[:,:,1])
            st.pyplot(fig9)
            fig10 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS2[:,:,4])
            st.pyplot(fig10)
            fig11 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS2[:,:,7])
            st.pyplot(fig11)
            fig12 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS2[:,:,10])
            st.pyplot(fig12)

        with col3:
            fig13 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS2[:,:,2])
            st.pyplot(fig13)
            fig14 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS2[:,:,5])
            st.pyplot(fig14)
            fig15 = plt.figure()
            plt.xticks([])
            plt.yticks([])
            plt.imshow(XS2[:,:,8])
            st.pyplot(fig15)

'''
# Predicted Image
'''

if (uploaded_file1 is not None) and (uploaded_file2 is not None):
    url = 'https://biomassters-wsbi2k6wha-ew.a.run.app/predict/'
    #files = [('files', tifffile.imread(uploaded_file1)), ('files', tifffile.imread(uploaded_file2))]
    files = [('files', XS1), ('files', XS2)]

    response = requests.post(url=url, files=files).json()

    array =np.array(response["file"]).reshape(256,256,1)/256

    fig = plt.figure()
    plt.xticks([])
    plt.yticks([])
    plt.imshow(array)
    st.pyplot(fig)


uploaded_filey = st.file_uploader("Choose a target file:")

if (uploaded_filey is not None):
    st.subheader('''
             Target LiDAR Image
             ''')
    y = tifffile.imread(uploaded_filey)
    figy = plt.figure()
    plt.xticks([])
    plt.yticks([])
    plt.imshow(y)
    st.pyplot(figy)
