from PIL import Image
import streamlit as st

st.set_page_config(page_title = "Completed Projects - Goldlion Services", page_icon = "gdllogo", layout = "wide")

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
    st.title("Completed Projects")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Student Visas")
        st.write(
            """
            **NORTH CYPRUS VISA:**
            Completiton of Student Visa for the 2024 alumni of Emmmanuel International College Rayfield Jos, to study for BS/BEng. degree programs in North
            Cyprus. Featured programs include;
            - BEng. in Civil Engineering
            - BEng. in Mechanical Engineering
            - BS in Computer Engineering
            - BS in Software Engineering
            """
        )
        st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)") 
         

    with right_column:
        st.write("##")
        st.image("kosisochukwuobioraturkishvisapub.jpg")
        
                  
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("abrahamdanielturkishvisapub.jpg")
        
        with right_column:
            st.write(
                """
                **NORTH CYPRUS VISA:**
                Completiton of Student Visa for the 2023 alumni of ECWA Wuse II Academy, Garam, Abuja, to study for BS degree programs in North Cyprus. Featured
                programs include;    
                - Nursing
                - Public Heatlh Nursing
                - Veterinary Nursing
                """
            )
        
            st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)")



with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **MALAYSIA VISA:**
            Completiton of Student Visa for the staffer of Isa Mustapha Agwai 2 Polytechnic, Lafia, Nasarawa State, to study for PhD degree programs in Malaysia.
            Featured programs include;
            - Political Science
            - International Relations
            - Political Science and International Relations
            - Business Administration
            """
        )
        
        st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)") 
 
         

    with right_column:
        st.image("usmanahmedmalaysianvisapub.jpg")

    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("turlishvisapubsamuelayun.png")
            
        
        with right_column:
            st.write(
                """
                **NORTH CYPRUS VISA:**
                Completiton of Student Visa for the 2019 alumni of Kwara Football Academy, Illorin, Kwara State, to study for BS/BEng. degree programs in North
                Cyprus. Featured programs include;
                - BS in Software Engineering
                - BEng. in Civil Engineering
                - BEng. in Mechanical Engineering
                - BS in Computer Engineering
                """
            )
        
            st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)")


with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **UKRANIAN VISA:**
            Completiton of Student Visa for the 2020 alumni of Mahanaim Secondary School, Anatigha, Calabar, Cross River State, to study for MBBS/BS degree
            programs in Ukraine. Featured programs include;
            - MBBS in Medicine and Surgery
            - Dental Medicine (D.D.M.)
            - Pedodontics
            - Restorative Dentistry
            - Histology and Embriology
            - Medical Biochemnistry
            - Medical Microbiology and Clinical Microbiology
            - Molecular Medicine
            """
        )
            
        st.write("[Check out our instagram page for more pictures](https://www.instagram.com/goldlionservices/)")

 
         

    with right_column:
        st.image("ukrainianvisapubhovunehuvara.jpg")

    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("CCTV Installations")
            st.image("cctv3.jpg")
            
        
        with right_column:
            st.write("##")
            st.write(
                """
                **CCTV INSTALLATION:**
                CCTV Camera was installed at Solid Rock International College located at Lafia Nassarawa State;
                - About 800 meters square area competedly covered with CCTV camera surveiliance
                - Termly maintenance services
                """
            )
        
            st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)")


with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Wired LAN Installations")
        st.write(
            """
            **WIRED LAN INSTALLTION 1:**
            Wired Local Area Network was installed at the the China Habour Engineering Construction Company camp located at Alizaga in Nassarawa Eggon local
            government area of Nassarawa State, Nigeria using Fibre Optic tcehnology;
            - About 400 meters square area competedly covered with internet network
            - Monthly maintenance services
            """
        )

        st.write("[Check out our instagram page for Wired LAN installation posts](https://www.instagram.com/goldlionservices/)")

         

    with right_column:
        st.write("##")
        st.image("wiredlan1.png")

    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("wiredlan2.png")
            
        
        with right_column:
            st.write(
                """
                **WIRED LAN INSTALLATION 2:**
                Wired Local Area Network was installed at Isa Mustapha Agwai 2 Polytechnic Lafia, Nassarawa State, Nigeria using Fibre Optic tcehnology;
                - About 200 meters square area competedly covered with internet network
                - Monthly maintenance services.
                """
            )
        
            st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)")



with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Construction Jobs")
        st.write(
            """
            **INSTALLATION OF CAPES/CAPE SEALS ON THE ROAD:**
            Capes were installed at the lohol close layout road in rayfield for reinforcement against wearing destructive effect of rainfall. Featured activities
            include;
            - Measuring
            - Setting
            - Bedding
            - Laying
            - Binding
            """
        )

        st.write("[Check out our instagram page for construction jobs posts](https://www.instagram.com/goldlionservices/)")


    with right_column:
        st.write("##")
        st.image("capes.png")

	
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


