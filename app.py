import streamlit as st
import pickle
import pandas as pd
import os
import gdown

# File ID
file_id = '1gjj5dOnzGTxzUjq2nGptVTdQxJWUovnB'
url = f'https://drive.google.com/uc?id={file_id}'
output = 'similarity.pkl'

# This checks if the file exists on the Streamlit server; if not, it downloads it
if not os.path.exists(output):
    gdown.download(url, output, quiet=False)

# 1. Page Config
st.set_page_config(
    page_title="Movie Recommender System",
    layout="wide"
)

# 2. Load CSS
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# 3. Large File Handling (Similarity Matrix)
SIMILARITY_PKL_FILE_ID = "1gjj5dOnzGTxzUjq2nGptVTdQxJWUovnB"
SIMILARITY_PKL_PATH = 'similarity.pkl'

if not os.path.exists(SIMILARITY_PKL_PATH):
    with st.spinner("Initializing System... Please wait."):
        try:
            gdown.download(id=SIMILARITY_PKL_FILE_ID, output=SIMILARITY_PKL_PATH, quiet=True, fuzzy=True)
        except Exception as e:
            st.error(f"Error loading system files: {e}")
            st.stop()

# 4. Data Loading Logic
@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open(SIMILARITY_PKL_PATH, 'rb'))
    
    # Optimized IMDb URL to ensure it finds Feature Films
    BASE_SEARCH_URL = 'https://www.imdb.com/find?s=tt&ttype=ft&q='
    movies['movie_link'] = BASE_SEARCH_URL + movies['title'].str.replace(' ', '+')
    return movies, similarity

movies, similarity = load_data()

# 5. Recommendation Logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_data = []
    for i in movies_list:
        movie_data = movies.iloc[i[0]]
        recommended_data.append({
            'title': movie_data['title'],
            'link_url': movie_data['movie_link']
        })
    return recommended_data

# --- SIDEBAR (Project Info) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2503/2503508.png", width=100) # Simple Movie Icon
    st.title("Project Details")
    st.info("""
    **Model:** Content-Based Filtering  
    **Framework:** Streamlit / Python  
    **Internship:** Movie Recommender System
    """)
    st.write("This system uses cosine similarity to find the most mathematically similar movies based on genres and tags.")

# --- MAIN UI (Center Selection) ---
st.title('🎬 Movie Recommender System')
st.write("Select a movie you've watched, and I'll suggest 5 similar ones you might enjoy!")

# The MAIN Selection Box (Front and Center)
selected_movie_name = st.selectbox(
    'Which movie did you like?',
    movies['title'].values,
    help="Type or select a movie from the list"
)

# Center the button a bit using columns
_, btn_col, _ = st.columns([2, 1, 2])
with btn_col:
    do_recommend = st.button('Get Recommendations', use_container_width=True)

st.markdown("---")

# 6. Display Results
if do_recommend:
    recommendations = recommend(selected_movie_name)
    st.subheader(f"Recommendations for: {selected_movie_name}")
    
    # Create the 2 main columns
    left_col, right_col = st.columns(2, gap="large")

    with left_col:
        for i in range(3):
            # We use recommendations[i] because there is no 'rec' variable in this loop
            st.markdown(f"#### {recommendations[i]['title']}")
            st.link_button("Click for Details", recommendations[i]['link_url'], use_container_width=False)
            st.write("") 

    with right_col:
        for i in range(3, 5):
            st.markdown(f"#### {recommendations[i]['title']}")
            st.link_button("Click for Details", recommendations[i]['link_url'], use_container_width=False)
            st.write("")
# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 | Internship Project | Data sourced via IMDb")