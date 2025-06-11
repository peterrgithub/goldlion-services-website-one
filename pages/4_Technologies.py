from PIL import Image
import streamlit as st

st.set_page_config(page_title = "Technologies - Goldlion Services", page_icon = "gdllogo.png", layout = "wide")

left_column, right_column = st.columns(2)
with left_column:
    st.image("gdllogo.png", width = 200)



banner_container = st.container()

# Add HTML content and styling for the banner
with banner_container:
    st.markdown(
        """
        <style>
        .banner {
            position: sticky;
            top: 0;
            width: 100%;
            background-color: #f0f0f0; /* Light grey background */
            height: 20px;        /* Adjust height as needed */
            display: flex;
            justify-content: center;  /* Center content horizontally */
            align-items: center;       /* Center content vertically */
            padding: 10px;        /* Add some padding around the text */
        }

        .banner-text {
            font-size: 20px;       /* Adjust text size as needed */
            font-weight: bold;
            color: navyblue;         /* Dark grey text */
        }
        </style>

        <div class="banner">
            <div class="banner-text">
                ... bent on improvements!
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )



st.sidebar.success("Surf our pages above")

def local_css(file_name):
    with open (file_name) as f:
        st.markdown (f"<style>{f.read()}</style>", unsafe_allow_html = True)
local_css("style/style.css")
    
#=====Loading Assets======


    #Our Services
with st.container():
    st.write("---")
    st.title("Technologies")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **FIBRE OPTIC POWERED NETWORKS:**
            With the extreme internet network technology quality that fibre optic cables bring to the table, we are leveraging this and providing organizations,
            schools, busnesses and even religious institutions with high-speed-of-light internet network installation services. These are in other words called
            conventionally as Wirled Local Area Networks. You could go ahead, give us a call and try that out for yourself. Highlight features include;
            - Long distance coverage as far as a 250 meters
            - Strong cables that withstand the forces of cutting and rupturing
            - Swift response to complains on installations
            - Effective deliery of maintenance routines e.t.c.
            """
        )
        st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)") 
         

    with right_column:
        st.image("fibreoptic2.jpg")
        st.image("fibreoptic2.jpg")
        
                  
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("websitewithpython1.jpeg")
        
        with right_column:
            st.write(
                """
                **PYTHON-BASED WEBSITE DESIGN:**
                With a strong desire to be unique and make a difference, one of our goals and ambition is to revolutionize and promote the use of python in
                Software Engineering as a whole, starting with website design, we are striving hard to continue to improve the usage of python in a novel way (with
                streamlit instead of flask) to desgin websites that are not only responsive too but just as good as those designed with HTML, functional as
                JavaScript-used and PhP-used websites, stylish as CSS-used websites and database driven as SQL-used websites - making sure that the python
                revolution is alive. Highlight features include;
                - Streamlit
                - Pillow
                - CSS
                - MySQLite
                """
            )
        
            st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)")



with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **VIDEO DOORBELLS:**
            With security threats, sneak attacks skyrocktting in today's world, a step up in security measures is now everyone's imperative. That is why we come in
            with installation of security video door bells to guarantee visual representation of all breaches, leaving precise evidences for both plaintiffs and
            law enforcements agancies to act on. Highlight features include;
            - Long distance coverage as far as a 250 meters
            - Strong camera capturing lenses
            - Water resistance to withstand harsh rainy weathers
            - Wide or divergent scope of coverage e.t.c.
            """
        )
        
        st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)") 
 
         

    with right_column:
        st.image("vidoorbell.png")

    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("kivy1.png")
            
        
        with right_column:
            st.write(
                """
                **PYTHON-BASED MOBILE APP DEVELOPMENT AND OTHER LANGUAGES:**
                With a strong desire to be unique and make a difference, one of our goals and ambition is to revolutionize and promote the use of python in
                Software Engineering as a whole, featuring mobile App development, we are striving hard to continue to improve the usage of python in a novel way
                to develop mobile Apps that are not only responsive too but just as good as those designed with Kotlin, functional as Android-used and Swift-used
                mobile Apps, stylish as flutter-used mobile Apps and database driven as SQL-used mobile Apps - making sure that the python revolution is alive.
                Notwithstanding, we still do mobile App projects with other languages too. Highlight features include;
                - Kivy
                - Pillow
                - Tkinter
                - MySQLite
                - Kotlin
                - Swift
                - Flutter e.t.c.
                """
            )
        
            st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)")

        
    with st.container():
        st.write("---")
        text_column1, text_column2, text_column3 = st.columns((1, 2, 3))
        with text_column1:
            st.subheader("Pay")
            st.write(
                """
                Cards\n
                Payoneer\n
                Paypal\n
                RedotPay\n
                Transfer\n
                Western Union\n
                """
            )
            
            st.subheader("License")
            st.write(
                """
                RC: PL20420
                """
            )
            
        with text_column2:
            st.subheader("Refund Policy")
            st.write(
                """
                Any client seeking for a refund must make such request prior to my submission of the first phase of work; if the first phase commences before a
                refund request is made, such request will not be considered.
                """
            )
            
            st.subheader("Location")
            st.write(
                """
                16, Gut Central, Along Rayfield Resort Road, Off P.R.T.V. Roundabout, Rayfield, Jos, Plateau State, Nigeria
                """
            )
            
        with text_column3:
            st.subheader("Partners")
            st.write(
                """
                Sheltonville Schools, Jos  |  Emmanuel International College, Jos  |  Day-by-Day Academy, Abuja  |  Jorola Integrations
                """
            )
        
 
           
st.markdown ("---")
st.write("© 2025 Goldlion Services. All rights reserved.")
