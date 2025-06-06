from PIL import Image
import streamlit as st

st.set_page_config(page_title = "Home - Goldlion Services", page_icon = "gdllogo.png", layout = "wide")


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


st.write("---")

st.title("Welcome to Goldlion Services!")
st.sidebar.success("Surf our pages above")

def local_css(file_name):
    with open (file_name) as f:
        st.markdown (f"<style>{f.read()}</style>", unsafe_allow_html = True)
local_css("style/style.css")
    
#=====Loading Assets======


#===Setting Website Header Section==========

with st.container():
    st.write(
        """
        A very fast growing company that is improving the quality of services world wide in various departments of Education, Information Technology, and
        General Contracts, delivering services with the speed of light and gold stanadard quality.
        """
    )

    print("\n")
    st.write(
        """
        Over 1,250 student visas without a single denial to various countries including North Cyprus, Malaysia, Ukraine, e.t.c.
        """
    )
    
    st.write(
        """
        5 in-house Apps for two local IT firms.
        """
    )
    st.write(
        """
        1 CCTV Camera installation contract dusted.
        """
    )
    st.write(
        """
        2 Wired-LAN installation contracts dusted.
        """
    )

    st.write("---")
    st.write(
        """
        For Study Abroad programmes and see previous student visas we have successfully facilitated, click Study Abroad menu on the left. For technology projects,
        click Technology menu on the left. For general contracts, click on General Contracts menu on the left. For a brochure of our completed projects, click
        Completed Projects menu on the left. Click the downward arrow to reveal other pages menu. 
        """
    )
    
    st.write("[Jump on our Facebook page already](https://www.facebook.com/GoldlionServices/)")
    

    #Highlight reals of services
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Highlight Reels")
        st.write("##") #inserting a blank empty line
        st.write(
            """
            Super highlight reels for your perusal.

            - From students boarding flight, to arrival at the first port of entry, to arrival at final destination airport, to arrival on campus, to registration,
            to taking lectures.
            - From construction of capes/cape seals, e.t.c
            - From first meeting, drafting of wireframes, scripting, testing the software, debugging it, to final deployment.
            """
        )
        
        st.write("[Check out our Youtube Channel](https://www.youtube.com/@goldlionservices7002)") 
         

    with right_column:
        video1 = open("airportarrival.mp4", "rb") 
        st.video(video1)

    with right_column:
        video2 = open("installationofcapes.mp4", "rb") 
        st.video(video2)
                  
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Ongoing Projects")
        st.write("##")
        image_column1, text_column1 = st.columns((1, 2))
        with image_column1:
            image1 = Image.open("turkishvisa.jpg")
            st.image(image1)

        image_column2, text_column2 = st.columns((1, 2))
        with image_column2:
            image2 = Image.open("webconverter.png")
            st.image(image2)
        
        with text_column1:
            st.subheader("Education Project | Student Visa")
            st.write(
                """
                Student visa process facilitating for the 2023/2024 headboy of Emmanuel International College Jos to study civil engineering in Turkish Republic of
                Northern Cyprus. Admission was gotten for him with a 50% scholarship on tuition fees. Visa Interview was concluded on Tuesday 22 January, and we're
                currently, awaiting visa collection.
                """
            )
            
            st.write("[Indulge our instagram page](https://www.instagram.com/goldlionservices/)")

        with text_column2:
            st.subheader("Technology Project | Web Converter for Researchers")
            st.write(
                """
                Currently working on a Web Converter for researcehrs for the purpose of ensuring accuracy of sources used.
                """
            )
            st.write("[Indulge our instagram page](https://www.instagram.com/goldlionservices/)")


    with st.container():
        st.write("---")
        text_column1, text_column2, text_column3 = st.columns((1, 2, 3))
        with text_column1:
            st.header("Pay")
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
            
            st.header("License")
            st.write(
                """
                RC: PL20420
                """
            )
            
        with text_column2:
            st.header("Refund Policy")
            st.write(
                """
                Any client seeking for a refund must make such request prior to my submission of the first phase of work; if the first phase commences before a
                refund request is made, such request will not be considered.
                """
            )
            
            st.header("Location")
            st.write(
                """
                16, Gut Central, Along Rayfield Resort Road, Off P.R.T.V. Roundabout, Rayfield, Jos, Plateau State, Nigeria
                """
            )
            
        with text_column3:
            st.header("Partners")
            st.write(
                """
                Sheltonville Schools, Jos  |  Emmanuel International College, Jos  |  Day-by-Day Academy, Abuja  |  Jorola Integrations
                """
            )
        
 
           
st.markdown ("---")
st.write("© 2025 Goldlion Services. All rights reserved.")
