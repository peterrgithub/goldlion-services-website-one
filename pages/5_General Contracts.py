from PIL import Image
import streamlit as st

st.set_page_config(page_title = "General Contracts - Goldlion Services", page_icon = "gdllogo.png", layout = "wide")

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


    #My Services
with st.container():
    st.write("---")
    st.title("General Contracts")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("CCTV Installations")
        st.write(
            """
            Installation of CCTV Camera at Schools, offices and other organizations as requested;
            - From 800 meters square area to bigger areas as desired, we can competely cover your area with CCTV camera surveiliance
            Just say the place and type of camera desired, we will show up and deliver.
            """
        )
        
        st.write("[Check our YouTube Channel](https://www.youtube.com/@goldlionservices7002)") 
         

    with right_column:
        st.image("cctv3.jpg")
        
                  
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
        image_column1, text_column1 = st.columns((1, 2))
        with image_column1:
            image1 = Image.open("wiredlan1.png")
            st.image(image1)
        
        with text_column1:
            st.subheader("Wired LAN Installations")
            st.write(
                """
                Installation of wired Local Area Network using Fibre Optic tcehnology with high internet browsing speeds on both PC and mobile platforms to enhance
                productivity and effective work delivery across offices, schools, churches and other organizations.
                """
                )
            st.write("[Check out our instagram page](https://www.instagram.com/goldlionservices/)")

        st.write("##")

with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Construction Jobs")
        st.write(
            """
            Construction projects ranging from building of schools, learning desks for classrooms, capes/cape seals along road paths and many more. Just say the
            place,and desired construction scope, we will give estimates and implement the job with good quality.
            """
        )
        
        st.write("[Check our YouTube Channel](https://www.youtube.com/@goldlionservices7002)") 
         

    with right_column:
        st.image("matthew10.png")

    
    with st.container():
        st.write("---")
        image_column2, text_column2 = st.columns((1, 2))
        with image_column2:
            image2 = Image.open("vidoorbell.png")
            st.image(image2)
        
        with text_column2:
            st.subheader("Video Doorbells")
            st.write(
                """
                Security is of very uttermost importannce to some persons especially those of certain social status as well as others who have particular concerns
                and needs. Such people, example politicians would always be interested in receiving only visitors who expected or on appointment to their hoomes. So
                having a doorbell rightly serves that purpose. Just give us a call and we will install a fuully functional and effective doorbell system right at
                your doorstep.
                """
                )
            st.write("[Check out our instagram page](https://www.instagram.com/goldlionservices/)")



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
