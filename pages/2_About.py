from PIL import Image
import streamlit as st

st.set_page_config(page_title = "About - Goldlion Services", page_icon = "gdllogo.png", layout = "wide")

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
    
st.title("About Us")
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
        Goldlion Services was established in 2010, staring with just on person, we ran successfully, excecuting and deploying projects for a while before getting
        registered with the Corporate Affairs Commission of the Federal Republic of Nigeria with company number RC: PL20420. After acquiring two more staff, we
        continued to expand until we now have a team of five.
        """
    )

    st.write("---")

    st.write(
        """
        For a guaranteed quality Study Abroad programmes, we are also recognized by ARCCOMS Association Loyal Agencies, an international association of Educational
        Agencies, headquartered in the United Kingdom, that is responsible for managing the international association of agencies in a large database of Educational
        Agent Counsellors'.
        """
    )

    st.write("---")

    st.write(
        """
        In technology, we are there executing quality projects ranging from Wired LANs, Wireless LANs with high internet network speeds using fibre optic cables
        technology, CCTV installations with high resolution static and rotational camera holding both HD and 4k features, Web Applications, Mobile Apps, as well as
        many others, we stand to give you top-of-the-line service.
        """
    )

    st.write("---")

    st.write(
        """
        We do quality delivery of general contracts too, ranging from Logistics, Procurements, Speed-of-light International Payments (freights, tuition fees,
        medical treatment e.t.c.) contracts, as well as other kinds of contracts, you are confident of the right contact point.
        """
    )

    st.write(
        """
        Social media presence is not left out with a 5-star rated Facbook Page and burgeoning followers as well as likes, a Branded-Content Certified Instagram
        Account and Sproutting X Account.
        """
    )
    
    st.write("[Learn more from our Facebook page](https://www.facebook.com/GoldlionServices/)")



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

