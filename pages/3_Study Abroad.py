from PIL import Image
import streamlit as st

st.set_page_config(page_title = "Study Abroad - Goldlion Services", page_icon = "gdllogo.png", layout = "wide")

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
    st.title("Study Abroad")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **STUDY IN LITHUANIA:**
            Lithuania is one of Europe's biggest economies. A European Union country with average standard of living and affordable university tuition fees from
            €3,000 to €6,500 per year. Studying in Lithuania gives plenty of work opportuities especially with the pink card. In addition, being a schengen country,
            there is opportunity for you to visit 27 other countries with in the region without applying for visa during the off/holiday period. Featured programs
            include;
            - BA in Branding and Advertising Management
            - BEngr. in Light Engineering
            - BSc in in Information Systems and Cyber Security
            - BSc in Quantitative Economics e.t.c.
            - BSc in Digital Economy
            - LLM in LegalTech
            - MSc in DeepTech Entrepreneurship
            - MSc in Financial Technology
            - MSc in Photonics and Nanotechnology
            """
        )
        st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)") 
         

    with right_column:
        st.image("lithuania1.png")
        
                  
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("australia9.jpg")
        
        with right_column:
            st.write(
                """
                **STUDY IN AUSTRALIA:**
                One of the benefits of studying in Australia is its cultural diversity. As a home to the different cultures of Oceania, some great benefits of
                studying in Australia for Nigerian students, other nationals range from world-class education to vibrant multicultural experiences and post-study
                opportunities. Australia does not fail to offer a unique blend of high-quality education with ample emphasis on research, productivity and
                professionalism, valuable work experiences, and an enriching lifestyle for international students. As with quality anywhere, there are real costs
                attached with tuition fees from AU$28,000 per year to as much as is obtainable. plus you get a 2 years Postgraduate Work Permit. Popular courses
                among international students include;    
                - Accountancy
                - Nursing
                - Agricultural Science
                - Engineering
                - Architecture
                - Actuarial Science
                - Hospitality
                - Psychology
                - Earth Sciences
                """
            )
        
            st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)")



with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **STUDY IN UKRAINE:**
            We know that Russia has been fighting Ukraine for the past 3 years now, but the Ukrainians with their undying spirit are still delivering quality level
            university edcuation through distance learning mode. You get to study from the portal, then complete internship in a company in your location after an
            agreement between your university and the company of choice in your home country is signed. Upon graduation, you get a full-fledged university degree
            certificate. Featured programs include;
            - MBBS in Medicine and Surgery
            - Computer Sciences
            - Civil Engineering
            - Business Administration
            - Law
            - Design Studies
            - Hospitality and Tourism
            - Economics
            - Mathematics and Statistics
            """
        )
        
        st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)") 
 
         

    with right_column:
        st.image("ukraine1.jpg")

    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("studcanada.jpg")
            
        
        with right_column:
            st.write(
                """
                **STUDY IN CANADA:**
                Almost everyone in the world  now knows that Canadan has the best living standadrd in the whole world; no country beats Canada in that regard.
                Studying in Canada requires tuition fees starting from as low as CAD15,000 dollars per year. However, we can guaranty and get you tuition fees
                scholarships of a mouth-watering CAD10,000 dollars, leaving you to pay as low CAD5,000 dollars per year and finish your Bachelor's program in 2.5
                years; plus you get a 2 years Postgraduate Work Permit. Featured programs include;
                - BA in Business Administration and Management
                - BA in Film Studies
                - BA in Computing and Mobile Game Development
                - BA in Project Management
                - BS in Computer Engineering
                - BA in Journalism
                - Nursing
                - MSc in Financial Technologies
                - Information Technologies
                """
            )
        
            st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)")


with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **STUDY IN INDIA:**
            Granting that there are other programs in the field of Health Sciences, Social Sciences, Economic and Admisnistrative Sciences, we have
            decided to highlight the technological and Engineering programs because just like China, India is also well known for quality in technology and
            engineering. To burst your bubble, India founded most of the mathematical formulae in use today. Featured courses for programs in India include;
            - BTech. in Computer Science & Engineering > Specialization in Cyber Security and Forensics;
            - BTech. in Computer Science & Engineering > Specialization in Artificial Intelligence and Machine Learning;
            - BTech. in Computer Science & Engineering > Specialization in Cloud Computing and Virtualization Technology in Association with IBM Company;
            - BTech. in Computer Science & Engineering > Specialization in Cloud Technology and Information Security I-Nurture;
            - BTech. in Computer Science & Engineering > Specialization in Embeded Systems;
            - BSc/BEngr. in Electronics > Specialization in Robotics and Application (tuition fees for all above is US$4,000/year, finish in 4 year).
            NOTE: There is an opportunity to get up to 20% tuition fee scholarship until graduation.
            Also, there are Internship and Placement opportunities for students with top of the line Tech. companies like Microsoft, Amazon e.t.c.
            """
        )
            
        st.write("[Check out our instagram page for more pictures](https://www.instagram.com/goldlionservices/)")

 
         

    with right_column:
        st.image("studindia1.png")

    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("germany1.jpg")
            
        
        with right_column:
            st.write(
                """
                **STUDY IN GERMANY:**
                Germany has a strong emphasis on research, and with some of the oldest institutions of learning in the world, it is well equipped to support such.
                To study in Germany can be very rewarding even from the start with tuition fees starting from €13,000 per year because it is notorious for its
                strong job market and opportunities for international students to work while studying. Studying in Germany guarantess you a mouth-watering 2 years
                Postgraduate Work Permit, leaving you to stay back and work in Germany. Featured programs include;
                - BA in Business Administration and Management
                - Humanities and Art
                - Historical Studies
                - Language Studies
                - BS in Computer Engineering
                - Social Sciences
                - Legal Studies
                - Environmental Sciences
                - Automotive and Mechanical Engineering e.t.c.
                """
            )
        
            st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)")


with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **STUDY IN NORTH CYPRUS:**
            North Cyprus is a country between Europe and the Middle East with very high quality educational establishments. Low costs of living and yet affordable
            university tuition fees from as very low as €0 per year (if you get a 100% tuition fees scholarship) to €2,800 per year (if you get a 50% tuition fees
            scholarship). Studying in North Cyprus gives plenty of additional scholarships especially when you finish an academic session with high CGPA (called
            "High Honours Scholarship") or sportsman/student athlete scholarship given to students who are winning with the various clubs of their universities.
            It will shock you to discover that just like in the UK, there are world-class DOUBLE HONOURS/DOBULE MAJORS DEGREE PROGRAMS combinations in North Cyprus
            which is a testament to its very high quality eduction standards. Featured remarkable and popular courses include;
            - Biomedical Engineering
            - Audio Engineering
            - BS in in Information Systems and Cyber Security
            - Computer Education and Instructional Technology
            - Actuarial Science - Finance and Banking (Double Major) VICE VERSA
            - Actuarial Science - Mathematics and Computer Science (Double Major) VICE VERSA
            - Actuarial Science - Statistics and Computer Science (Double Major) VICE VERSA
            - Biomedical Engineering - Electrical and Electroic Engineering (Double Major) VICE VERSA
            - Chemistry - Molecular Biology and Genetics (Double Major)
            - Chemistry - Physics (Double Major)
            - Computer Engineering - Informatioon Systems Engineering (Double Major)
            - Computer Engineering - Software Engineering (Double Major)
            - Dental Medicine (D.D.M./Bachelors)
            - Digital Game Design
            - European Union Relations
            - Electrical and Electronic Engineering - Information Systems Engineering (Double Major) VICE VERSA
            - English Language Teaching
            - Pre-school teaching
            - Psychological Counselling and Guidance
            - Landscape Architecture
            - Electronics and Comminucation Engineering
            - Electrical and Electronic Engineering - Biomedical Engineering (Double Major)
            - Energy Systems Engineering
            - Public Administration
            - Audiology
            - Nutrition and Dietetics
            - Physiotherapy and Rehabilitation
            - Physical Education and SPorts Teaching
            - Social Work
            - Coaching Education
            - Sports Management
            - Recreation
            - Gastronomy and Culinary Arts
            - Industrial Engineering - Business Administration (Double Major)
            - Industrial Engineering - Mechanical Engineering (Double Major)
            - Industrial Engineering
            - English Language and Literature
            - Translation and Interpretation
            - Film Making and Broadcasting
            - Public Relations and Advertizing
            - Bio Engineering
            - Cyber Security Engineering
            - Data Analysis Engineering
            - Material Sciences and Nanotechnology Engineering
            - Petroleaum and Natural Gas Engineering
            - Construction Management and Strategies
            - Food Engineering
            - Interior Architecture
            - Physics Engineering
            - Environmental Sciences and Engineering
            - Pedodontics
            - Restorative Dentistry
            - Allergy and Immunology
            - Biostatistics
            - Histology and Embriology
            - Medical Biochemnistry
            - Medical Microbiology and Clinical Microbiology
            - Molecular Medicine
            - Public Health Nursing
            - Innovation and Knowledge Management
            - Analytical Chemistry
            - Clinical Pharmacy
            - Enterpreneureship and Leadership in Education Program
            - Pharmaceutical Botany
            - Pharmacognosy
            - Pharmaceutical Chemistry
            - Special Education
            - Midwifery
            - Urban Design
            """
        )

        st.write("[Check out our instagram page for North Cyprus posts](https://www.instagram.com/goldlionservices/)")

         

    with right_column:
        st.image("studnorthcyp1.png")

    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("ireland12.png")
            
        
        with right_column:
            st.write(
                """
                **STUDY IN IRELAND:**
                With qualifications equivalent to those in the UK and other countries, Ireland degrees from Ireland boast of high value in the international job
                market. In addition to enjoying your saty in one of the firendliest citieis in Europe, studying in Ireland guaantees skill development, research,
                and innovation from top class universities with tuition fees starting from as low as €9,000 per year to about €45,000 per year based on
                institutional differences. A guaranteed 2 years Postgraduate Work Permit is available to allow for a stay-back and opportunity to build a life with
                an additional residence permit within just 2 years, which is shorter than the 5 years period to get a residence permit in some countries. Featured
                programs include;
                - Business Intelligence
                - Film Production
                - Computer Science and Engineering
                - Materials Engineering
                - Cyber Security and Cloud Computing
                - Nursing and Healthcare
                - Classics and Development Studies
                - Finance and Accounting
                - Agriculture and Food Security e.t.c.
                """
            )
        
            st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)")



with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **STUDY IN MALAYSIA:**
            Malaysia is a small Island country in Asia with very high quality educational establishments but yet very low costs of living and very very low ranges
            of university tuition fees from as very low as US$1,000 per year tion fees. Studying in Malaysia gives plenty of comfort while studying because you are
            completely safe from the headcahes of financial difficulties. Not forgetting to mention that the universities are very good in carrying out academic
            research. Featured popular programs among international studnets include;
            - Computer Science
            - Engineering
            - Information Systems and Cyber Security
            - Architecture
            - Digital Media Production
            - Culinary Arts
            - Business Management
            - Financial Accounting
            - Nanotechnology e.t.c.
            """
        )

        st.write("[Check out our instagram page for Malaysia posts](https://www.instagram.com/goldlionservices/)")


 
    with right_column:
        st.image("malaysia1.jpg")

    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("uk3.jpg")
            
        
        with right_column:
            st.write(
                """
                **STUDY IN UK:**
                With very strong job prospects, high-quality education, global recognition of deggrees, almost everyone in the world  wants an opportunity to study
                in the UK. Despite the fact that it requires tuition fees as high as from £15,000 per year, the returns drives the courage to ignore the initial
                costs of getting there with a 90 percent guarantee of a greater rewarding future. In addition, most institutions give a 3 year duration to finish a
                Bachelor's program plus you get a 2 years Postgraduate Work Permit. For UK, it is a clear case of, "the end justifies the means" for most people.
                Featured programs include;
                - Computer Science and IT
                - Data Science
                - Artificial Intelligence
                - Mechanical Engineering
                - Electrical Engineering
                - Civil Engineering
                - Medicine
                - Pharmacology
                - Biotechnology e.t.c.
                """
            )
        
            st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)")


with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **STUDY IN POLAND:**
            Poland is a country in Eastern Europe with very high quality educational establishments but considerably low costs of living in general and affordable
            university tuition fees from as very low as €2,000 per year to €6,000 per year; Poland holds the record for one of the most affordable European countries
            for studies, and studying in Poland has rewarded many with a calm and peaceful settlement after graduation because the Polish women are naturally warm
            and welcoming to immigrants. Cited geographically at the center, of Europe, it is also a focal base for exploring other Europen countries. Featured
            popular programs include;
            - Medicine
            - Business and Management
            - Computer Science
            - Engineering (Mechanical, Civil, Electrical, ...)
            - Economics
            - Arts and History
            - Humanities like Political Science, International Relations, Law, Psychology, ...
            - Sociology
            - Anthropology e.t.c.
            """
        )

        st.write("[Check out our instagram page for Malaysia posts](https://www.instagram.com/goldlionservices/)")
 
         

    with right_column:
        st.image("poland1.jpg")

    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("usa4.jpg")
            
        
        with right_column:
            st.write(
                """
                **STUDY IN USA:**
                Almost everyone in the world knows that the USA boasts the best standadrds of education in the whole world; no country beats the USA in that regard.
                Simply put, "studying in USA requires even the best of brains". The tuition fees starting from as high as US$15,000 per year. However, we can
                guaranty you that no one who studies in the USA loses. Only gains are attainable, from diverse academic programs, renowned high-quality education,
                numerous opportunities for career advancements, huge high performance scholarships, sposts scholarships, university-wide scholarships, high-paying
                university-wide jobs on campus while studying, academic researcher benefits, university-wide industry-based projects incentives, mouth-watering jobs
                upon graduation, highest degree prestige and countless others, leaving you with "ONLY GAINS" when you finish your program and graduate; plus you get
                a 2 years Postgraduate Work Permit to stay-back and work too. Featured programs include;
                - Computer Science and Mathematics
                - Artificial Intelligence
                - Data Science
                - BA in Project Management
                - Engineering (Software, Biomedical, Electrical, Civil, ...)
                - Business and Management (Financce, Marketing, MBA, ...)
                - Health Sciences (Medicine, Nursing, Health Mamagement, ...)
                - Natural Sciences (Biology, Chemistry, Geology, Oil & Gas, Physics, ...)
                - Design Studies (Architecture, Graphics, Textiles, ...) e.t.c.
                """
            )
        
            st.write("[Check our Facebook page for more related posts](https://www.facebook.com/GoldlionServices/)")


with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            **STUDY IN MALTA:**
            Malta is a country between Europe, a member of the Schengen area with very good and reputable educational establishments. Average standard of living
            and fair university tuition fees from as very low as €9,000 per year. Though it is not so popular among international students, this makes studying in
            Malta a good venture because of its low population, making the jobs to go and round and be sufficient for everyone to earn a living, especially when
            you finish studyies and are interested in staying back. Plus being in the Schegen area, you get to travel to the other 27 Schengen countries without
            the need to get any visa again. Featured popular programs include;
            - BA in Business Admisnstration and Management
            - BA in Business Management
            - BA in Management
            - Masters in Management
            - Masters in Business Administration
            - MD in Medicine
            - BS in Computer Engineering
            - BS in Civil Engneering
            - BS in Electrical Engineering e.t.c.
            """
        )

        st.write("[Check out our instagram page for Malta posts](https://www.instagram.com/goldlionservices/)")

 
         

    with right_column:
        st.image("malta3.png")

    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("turkey1.jpg")
            
        
        with right_column:
            st.write(
                """
                **STUDY IN TURKEY:**
                With emphasis on research and innovation, Turksy holds one of the best educational systems in the world. Turkey is a member of the European Higher
                Education Area and applies the Bologna Process, which ensures that degrees are recognized across Europe. Two types of pre-arrival scholarships of
                20% and 50% are given to students before arrival on campus, which brings tuition fees to a relatively affordable amount ranging from US$5,500 per
                year. One shocking thing about Turkey is that while it doesn't give a Postgraduate Work Permit, it gives an option to apply for a CITIZENSHIP after
                5 years, which can be exploered by students. Popular programs include;
                - Tourism Management
                - Gatstronomy and Culinary Arts
                - Architecture
                - Communication and Design
                - Computer Engineering
                - Cartoons and Animation
                - Social Media and Digital Communication
                - Physotherapy
                - Business Administration and Management e.t.c.
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

