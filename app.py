import streamlit as st
import requests
import os
import pandas as pd
import json
from termcolor import colored

url = 'http://0.0.0.0:8000'
#url = 'https://api-summary-780137948407.europe-west1.run.app'

# st.set_page_config(layout="wide")
# st.image("application/Sci-paper-UI.jpg", use_container_width =True)

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Scientific paper summarizer")
st.subheader("Upload an Excel file: ")
file_buffer = st.file_uploader('')
df = pd.read_excel('raw_data/papers_test.xlsx')

st.text("\n")
st.subheader("Choose an Article: ")
# Banner that rolls down with document options
with st.expander("📂 Click to View and Select Documents"):
    # List of available documents

    documents = [f"{title}" for title in df['title']]

    # Multi-select allows the user to choose one document
    selected_doc = st.selectbox("Choose a document to summarize:", documents)
    #df.loc[selected_doc.split(':')[1]]
    doc = str(selected_doc.strip())
    selection = df[df['title'] == doc]

    if st.button("Article Content"):
        st.subheader(df['title'][df['title'] == doc].values[0])
        st.text("\n\n" + str(df['full-text'][df['title'] == doc].values[0]))


    selection.to_pickle("article.pkl")


# text = '\n\nIntroduction\n\nThe novel coronavirus disease 2019 (covid-19) pandemic has led to more than 24 million confirmed cases and over 820,000 deaths worldwide as of late august 2020. Early observational studies reported high rates of venous thromboembolism (vte) in critically ill patients with covid-2019. 1 a recent meta-analysis reported an incidence of 26% for vte among 3487 patients from 30 studies based on very low-quality evidence due to heterogeneity and risk of bias. 2 furthermore, studies have reported that elevated d-dimer values in covid-19 are associated with a higher risk of vte, mechanical ventilation, and mortality.\n\nMethods\n\nWe conducted a retrospective observational cohort study at new york-presbyterian hospital/weill cornell medical center and affiliated nonteaching hospital. We included all consecutive adult (age ≥18 years) cases of covid-19 confirmed by a positive reverse transcriptase-polymerase chain reaction test admitted to our two hospitals between 3 march 2020, the date of the first positive case, and 15 may 2020. Univariate analysis and multivariable logistic regression analysis were performed to evaluate the association between the initial d-dimer value during hospitalization, clinical characteristics, and the odds of vte.\n\nResults\n\nA total of 1739 hospitalized patients with covid-19 were included in the study. The median age was 66.5 years (iqr 53.7-77.3), 59% were men, and common comorbidities included hypertension (56%), diabetes mellitus (31%) and obesity (30%). Figure 1) . Multilevel likelihood ratios significantly changed at the following d-dimer levels: <1000 ng/ml: 0.14 (95% ci, 0.07-0.30); 1000-7500 ng/ ml: 1.19 (0.97-1.47); and >7500 n/l: 4.10 (2.94-5.\n\nDiscussion\n\nIn our study of a large cohort of hospitalized covid-19 patients in new york city the prevalence of objectively confirmed vte was 7%. 6 elevated d-dimer levels were associated with higher probability of vte, consistent with reports by others. 1 other significant predictors of v te in our cohort included black race, need for supplemental oxygen on presentation, higher platelet counts, and prolonged prothrombin time. 7 a possible explanation for this is that black patients have a greater prevalence of comorbidities such as obesity, hypertension and diabetes, and may have sickle cell trait.\n\nData collection\n\nObjective: this study aimed to investigate the relationship between demographic, clinical characteristics and radiology characteristics of patients in a tertiary-care hospital and the quality of care provided by the radiology department. Methods: data were extracted manually from electronic medical records using a quality-controlled protocol in a redcap database. Data were analyzed using an algorithm-based automated process to extract vital signs and laboratory values from electronic records. Results: a total of 4,769 patients were enrolled in this study. Of whom, 1,832 (62.7%) were admitted to the hospital with a history of cancer. The majority (82.8%) had been admitted to a hospital in the tertiary care unit.\n\nClinical characteristics\n\nWe evaluated age, gender, race, ethnicity, comorbidities including obesity (defined as body mass index >30 kg/m 2 ), hypertension, coronary artery disease, heart failure, diabetes mellitus, and active cancer.\n\n'



# st.markdown(
#             f"<span style='color:#d16919de'>{text}</span>",
#             unsafe_allow_html=True
#         )


if selection is not None:
    if st.button("Summarize"):
        #res = requests.post(url + "/predict", files={'myfile': selection}).json()
        #res = requests.post(url + "/predict", json={'myfile': str(selection)}).json()
        with open('article.pkl', 'rb') as f:
            response = requests.post(
                url + "/predict",
                files={'myfile': f}
            ).json()

        output = response.get('Summary')

        st.markdown(
            f"<span style='color:#d16919de'>{output}</span>",
            unsafe_allow_html=True
        )












# # Use the correct API URL (local or cloud deployment)
# API_URL = os.getenv("https://api-summary-780137948407.europe-west1.run.app/")

# st.title("Scientific Paper Summarizer")

# # Input text area for the user
# text = st.text_area("Enter the scientific paper content:")

# if st.button("Summarize"):
#     if text:
#         # Send input to your FastAPI model
#         response = requests.post(API_URL, json={"text": text})
#         if response.status_code == 200:
#             summary = response.json().get("summary", "No summary available")
#             st.subheader("Summary:")
#             st.write(summary)
#         else:
#             st.error("Error: Failed to fetch summary from API.")
#     else:
#         st.warning("Please enter text to summarize.")
