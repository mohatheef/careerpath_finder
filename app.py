import streamlit as st
import json

# ----------------------------------------------------------
# Load Data
# ----------------------------------------------------------
@st.cache_data
def load_data():
    with open("data/courses.json", "r", encoding="utf-8") as f:
        return json.load(f)

courses_data = load_data()

# ----------------------------------------------------------
# Page Config
# ----------------------------------------------------------
st.set_page_config(page_title="CareerPath Finder", layout="wide")

st.title("🎓 CareerPath Finder – Explore Every Career Path")
st.subheader("Helping students from every background find affordable and meaningful education opportunities")

st.markdown("""
Discover diplomas, degrees, and vocational programs across Science, Commerce, Arts, Paramedical, and Engineering streams.
Learn about scholarships, low-cost colleges, and study paths in India and abroad.
""")

# ----------------------------------------------------------
# Tabs
# ----------------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "✨ Explore by Interest",
    "📘 Explore by Stream",
    "💰 Scholarships & Low-Cost Options"
])

# ----------------------------------------------------------
# Tab 1: Explore by Interest
# ----------------------------------------------------------
with tab1:
    interests = st.multiselect(
        "Select your interests:",
        ["Science", "Technology", "Medicine", "Arts", "Commerce", "Social Work",
         "Vocational/ITI", "Design", "Sports", "Environment", "Law", "Education"]
    )

    if interests:
        matched_courses = [
            c for c in courses_data if any(i in c["tags"] for i in interests)
        ]
        if matched_courses:
            st.markdown(f"### 🌟 Showing {len(matched_courses)} matching courses")
            for c in matched_courses:
                with st.expander(f"🎯 {c['course_name']}  —  {c['stream']}"):
                    st.markdown(f"**Level:** {c['level']}  |  **Duration:** {c['duration']}")
                    st.markdown(f"**Eligibility:** {c['eligibility']}")
                    st.markdown(f"**Description:** {c['description']}")
                    st.markdown(f"**Typical Fees:** {c['typical_fees']}")
                    st.markdown(f"**Career Opportunities (India):** {c['career_opportunities_india']}")
                    st.markdown(f"**Career Opportunities (Abroad):** {c['career_opportunities_abroad']}")
                    st.markdown(f"**Top Colleges:** {', '.join(c['top_colleges'])}")
                    st.markdown(f"**Scholarships:** {', '.join(c['scholarships'])}")
                    st.markdown(f"**Low-Cost Options:** {', '.join(c['low_cost_options'])}")
                    st.markdown(f"**Online Alternatives:** {', '.join(c['online_alternatives'])}")
        else:
            st.warning("No matches found. Try selecting more or different interests.")
    else:
        st.info("Please select at least one interest to begin.")

# ----------------------------------------------------------
# Tab 2: Explore by Stream
# ----------------------------------------------------------
with tab2:
    stream = st.selectbox(
        "Select your stream:",
        sorted(list(set(c["stream"] for c in courses_data)))
    )

    filtered = [c for c in courses_data if c["stream"] == stream]
    st.markdown(f"### 📚 {len(filtered)} Courses in {stream}")

    for c in filtered:
        with st.expander(f"🎓 {c['course_name']}"):
            st.markdown(f"**Level:** {c['level']}  |  **Duration:** {c['duration']}")
            st.markdown(f"**Eligibility:** {c['eligibility']}")
            st.markdown(f"**Description:** {c['description']}")
            st.markdown(f"**Fees:** {c['typical_fees']}")
            st.markdown(f"**Career in India:** {c['career_opportunities_india']}")
            st.markdown(f"**Career Abroad:** {c['career_opportunities_abroad']}")
            st.markdown(f"**Top Colleges:** {', '.join(c['top_colleges'])}")
            st.markdown(f"**Scholarships:** {', '.join(c['scholarships'])}")
            st.markdown(f"**Low-Cost Options:** {', '.join(c['low_cost_options'])}")
            st.markdown(f"**Online Alternatives:** {', '.join(c['online_alternatives'])}")

# ----------------------------------------------------------
# Tab 3: Scholarships & Low-Cost Options
# ----------------------------------------------------------
with tab3:
    st.markdown("### 💰 Key Government & NGO Scholarships")
    st.markdown("""
    - **AICTE Pragati / Saksham Scholarships** – for girls and differently-abled students  
    - **INSPIRE Scholarship** – for meritorious science students  
    - **National Means-cum-Merit Scholarship (NMMS)** – for students from economically weaker sections  
    - **Post-Matric SC/ST/OBC Scholarships** – state-wise aid  
    - **Kishore Vaigyanik Protsahan Yojana (KVPY)** – for science research aspirants  
    - **PMKVY Skill India** – free vocational & ITI training
    """)

    st.markdown("### 🏫 Low-Cost Institutions")
    st.markdown("""
    - Government Colleges & State Universities  
    - IGNOU and State Open Universities  
    - Government ITIs and Polytechnics  
    - SWAYAM / NPTEL / Coursera online certification programs  
    """)

st.markdown("---")
st.markdown(
    "Created with ❤️ by **Mohammed Atheef G A** | "
    "[LinkedIn](https://www.linkedin.com/in/mohammedatheefga/) | "
    "M.Tech in Medical Informatics, Manipal Institute of Technology, Manipal"
)

st.warning(
    "⚠️ **Disclaimer:** This app is currently in the development phase. "
    "Some course details, fees, or career information may be inaccurate or incomplete. "
    "Users are advised to verify information from official sources before making educational or career decisions."
)

