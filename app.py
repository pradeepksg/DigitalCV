from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Pradeep_Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Pradeep K"
PAGE_ICON = ":wave:"
NAME = "PRADEEP K"
DESCRIPTION = """
Senior Software Engineer, Entrepreneurial minded, passionate for tech, driven by intellectual curiosity, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "pradeep.ksg@gmail.com.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
}
PROJECTS = {
    "🏆 Developed 50+ new script/code for Rating Engine for Insurance company website.",
    "🏆 Data Conversion: Auto and Home insurance data stored in AL3 (Automation Level 3) format was converted into ACORD standards using JavaScript, XML and RegEx.",
    "🏆 PDF Document Generation: ACORD XML data was used to generate the PDF, thereby saving the valuable time of the Insurance Companies and the Vendors.",
    "🏆 Live telecasting – Zeboba, GeoTrazer (GPS Systems), etc.",
	"🏆 Web scraping: Proficiently scraped the data of Appraisal Info and Tax Collector Info, from 250+ counties in 25+ states using Python, PHP and Selenium.",
	"🏆 Automation: Used Selenium, BeatuifulSoup Python library to extract desired data from the URL an automated way.",
	"🏆 Data Extraction: Successfully extracted the required data from 20+ counties US County Clerk website. PDF/TIFF files were first downloaded and were converted to text file using OCR- Tesseract and the data was extracted using RegEx.",
	"🏆 Data Extraction in AI/ML: Dataset was prepared and was trained to extract the data using the AI/ML algorithms in Python." 
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Over 15+ years of experience as Software Developer and Business Analyst in the domain of Insurance, Mortgage, Healthcare.
- ✔️ Experienced in Python and PHP based environment, along with data analytics, data wrangling and Excel Data extracts.
- ✔️ Expert in writing PHP and Python scripts to scrape web data for data usage/collection using Selenium, BeautifulSoup, and Scrapy.
- ✔️ Hands on experience in working with various version control systems including CVS, SVN.
- ✔️ Excellent analytical, problem-solving and critical thinking skills with ability to learn quickly to the emerging new technologies and paradigms. 
- ✔️ Experienced in Analysing, compiling, documenting, and communicating test results to the broader team. 
- ✔️ Good understanding of statistical principles and their respective applications.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- Programming: Python, PHP, Javascript, SQL
- Databases: MongoDB, MySQL
- Framework:  Selenium, Scrapy
- Library: Pandas, Matplotlib, Numpy, NLP, BeautifulSoup, Matplotlib, TesseractOCR
- Tools: SVN, CVS
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Software Engineer | Stellar Innovations Pvt Ltd, Bangalore**")
st.write("Nov 2016 – Sept 2022")
st.write(
    """
- ► Web scraping: Proficiently scraped the data of Appraisal Info and Tax Collector Info, from 250+ counties in 25+ states using Python, PHP and Selenium.
- ► Automation: Used Selenium, BeatuifulSoup Python library to extract desired data from the URL an automated way.
- ► Data Extraction: Successfully extracted the required data from 20+ counties US County Clerk website. PDF/TIFF files were first downloaded and were converted to text file using OCR- Tesseract and the data was extracted using RegEx.
- ► Data Extraction in AI/ML: Dataset was prepared and was trained to extract the data using the AI/ML algorithms in Python.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Business Consultant  | Pentamine Technologies Pvt. Ltd., Bangalore**")
st.write("Aug 2012 – Oct 2016")
st.write(
    """
- ► Performed market research to understand the market requirements for new product development. 
- ► Involved in identifying the needs of the company and integrating market research to determine the needs and goals of new products.
- ► 20+ products were researched and documented. 10+ products were not implemented due to market constraints. 4+ products were in market which was later discarded due to tough competition.
- ► 5+ products are successfully implemented, which is generating the revenue.
- ► Implemented Projects: Live telecasting – Zeboba, GeoTrazer (GPS Systems), etc.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Sr. Script Engineer  | Webcetera Software Solutions Ltd. (Applied Systems India Pvt. Ltd.), Bangalore**")
st.write("Oct 2009 – Apr 2012")
st.write(
    """
- ► Data Conversion: Auto and Home insurance data stored in AL3 (Automation Level 3) format was converted into ACORD standards using JavaScript, XML and RegEx.
- ► PDF Document Generation: ACORD XML data was used to generate the PDF, thereby saving the valuable time of the Insurance Companies and the Vendors.

"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Script Engineer  | Webcetera Software Solutions Ltd. (Applied Systems India Pvt. Ltd.), Bangalore**")
st.write("Aug 2006 – Mar 2008")
st.write(
    """
- ► Enhanced the code for 20+ Insurance company website for online quoting of newly added states. 
- ► Demonstrated expertise in developing 50+ new script/code by studying the Insurance company website.
- ► Tested the Script/Code manually, with all the possible scenarios along with Regression.
- ► Provided Online & Offline Support for 100+ scripts/code of various Insurance Company’s for 40+ states in US.
- ► Proficiently troubleshot simple and complex technological issues for different Insurance Company’s project.
- ► Enhanced the Script’s features by effectively fixing the bugs in the real time and optimized the overall performance, reliability and performance.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project in PROJECTS:
    st.write(f"{project}")