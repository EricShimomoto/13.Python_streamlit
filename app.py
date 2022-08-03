from hamcrest import none
import streamlit as st
import requests
from streamlit_lottie import st_lottie

#font of emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
#Setup some initial configuration
st.set_page_config(page_title="Eric 1st Streamlit page", page_icon=":panda_face:", layout="wide")

#functions to access the lottie file
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#HEADER
#The header can be in a different container as it is now
with st.container():
    st.subheader("Hi, My name is Eric")
    st.title("A Software engineer")
    st.write("Using programing languages to change the world one line of code at a time")
    st.write("[GitHub](https://github.com/EricShimomoto)")
#lOAD ASSETS
lottie=load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_tfb3estd.json')
#What I do
with st.container():
    #add a div
    st.write("---")
    #Add 2 columns
    left_column, right_column = st.columns(2)
    with left_column: 
        st.header("What I do")
        ##insert a space
        st.write("##")
        st.write(
            """
                Born and raised with computers and videogames, trained on the arts of mechanical and mechatronics technologies, coming back home to computer science
            """
        )
    #To insert anumation into the seccond column, use LottieFiles
    #insert animation in the left column
    with right_column:
        st_lottie(lottie,height=400, key="coding")
        
#https://www.youtube.com/watch?v=VqgUkExPvLY   
    
