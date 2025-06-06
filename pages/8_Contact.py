from PIL import Image
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(page_title = "Contact - Goldlion Services", page_icon = "gdllogo", layout = "wide")


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


#===Setting Website Header Section==========

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
with st.container():
    st.write("---")
    st.title("Contact")
    st.write(
        """
        To make a voice enquiry, call +234 70 8747 7700 or use the form below for text enquiries. To reach us on WhatsApp, chat +234 70 8747 7700 or use the form
        below for text enquiries. To reach us on Instagram, DM us @goldlionservices; otherwise, use the form below for further text enquiries.
        """)

with st.form(key = "contact_form"):
    background_color = "beige"
    user_name = st.text_input("Write your name", max_chars = 50)
    user_email = st.text_input("Write your email address", max_chars = 50)
    user_message = st.text_area("Your message", height = 150)
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_name and user_email and user_message:
            try:
                # Email Configuration
                sender_email = "peter.williams@goldlionservces.onrender.com"  # Replace with your custom domain email
                receiver_email = "goldlionservces@gmail.com"  # Replace with the real email address where emails will be forwarded
                password = "lacuna"  # Use an app-specific password if necessary

                # Email Content
                message = MIMEMultipart("alternative")
                message["Subject"] = f"New Contact Form Submission from {user_name}"
                message["From"] = sender_email
                message["To"] = receiver_email

                text = f"""
                You have a new message from {user_name} ({user_email}):
                
                {user_message}
                """
                part = MIMEText(text, "plain")
                message.attach(part)

                # Send Email
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message.as_string())

                st.success("Your message has been sent successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please fill out all fields in the form.")

css = """
<style>
    [data-testid = "stForm"] {
        background: white;  
    }
</style>
"""
st.write(css, unsafe_allow_html = True)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




#with st.container():
#    st.write("To make a voice enquiry, call +234 70 8747 7700 or use the form below for text enquiries.")
 #   st.write("To reach us on WhatsApp, chat +234 70 8747 7700 or use the form below for text enquiries.")
  #  st.write("To send an Instagram DM, DM us @goldlionservices or use the form below for text enquiries.")
    

        

   # with st.container():
    #    st.write("---")
     #   st.subheader("Reach Us")
      #  st.write("##")
   # contact_form = """
    #<form action = "https://formsubmit.co/servicesgoldlion@gmail.com", method = "POST">
     #   <input type = "hidden" name = "_captcha" value = "false">
      #  <input type = "text" name = "name" placeholder = "Your name" required>
       # <input type = "text" email = "email" placeholder = "Your email" required>
        #<textarea name = "message" placeholder = "Type your message here" required></textarea name>
       # <button type = "submit">Send </button>
   # </form>
    #"""
    #Code to stop the contact from from filling the entire screen width
   # left_column, right_column = st.columns((2))
   # with left_column:
    #    st.markdown(contact_form, unsafe_allow_html = True)
    #with right_column:
     #   st.empty()


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
