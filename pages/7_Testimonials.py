from PIL import Image
import streamlit as st

st.set_page_config(page_title = "Testimonials - Goldlion Services", page_icon = "gdllogo", layout = "wide")

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
    st.title("Testimonials")
    left_column, right_column = st.columns(2)
    with left_column:
        
        st.write(
            """
            "Tested and trusted" - Isaac Damilare Ojo, Lead Consultant and Tutor, Damty Consult and Educational Services, Illorin, Kwara State, Nigeria.\n
            [Check this testimony here](https://web.facebook.com/share/15gvpeTkb5/)
            
            "Congratulations to her. All thanks to the tested and trusted Goldlion Services" - Isaac Damilare Ojo, Lead Consultant and Tutor, Damty Consult and
            Educational Services, Illorin, Kwara State, Nigeria.\n
            [Check this testimony here](https://web.facebook.com/share/1Y4cS1cakw/)
            """
        )
         

    with right_column:
        st.image("isaacojo1.jpg")
        
                  
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
        image_column1, text_column1 = st.columns((1, 2))
        with image_column1:
            image1 = Image.open("peishkolade.jpg")
            st.image(image1)

        image_column2, text_column2 = st.columns((1, 2))
        with image_column2:
            image2 = Image.open("steveuvara.jpg")
            st.image(image2)
        
        with text_column1:
            st.subheader("Plateau State University, Bokkos")
            st.write(
                """
                "Mr P... You didn't attach date...hence the question. She's settled (in North Cyprus) and doing well. I chat with her often.... E no easy to leave
                home....Weldon!" - Dr. Patience Mamie Kolade, Senior Lecturer, Plateau State University, Bokkos, Plateau State, Nigeria.\n
                [Check this testimony here](https://web.facebook.com/share/1Y4cS1cakw/)
                """
            )
            
            
        with text_column2:
            st.subheader("Federal University Lafia")
            st.write(
                """
                "Um Hmm, yes oh! I trust Goldlion Services, so I am not surprised that my son's (Ukrainian) visa is finally out now". - Dr. Steve Uvara, Director
                of Finance, Federal University Lafia, Nasarawa State, Nigeria.
                """
            )
            


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


