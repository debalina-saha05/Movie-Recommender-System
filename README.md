# AI-Powered Movie Recommender

A professional **Content-Based Movie Recommendation System** developed as a capstone project for my internship. This application demonstrates advanced skills in **Natural Language Processing (NLP)**, **Cloud Architecture**, and **Modern UI/UX Engineering**.

## Live Demo
[**Click here to view the Live Application**](https://movie-recommender-system-project2.streamlit.app/)

---

## Technical Highlights

### The Recommendation Engine
The system utilizes **NLP techniques** to analyze movie metadata, including genres, keywords, cast, and crew. 
* **Vectorization:** Text data is converted into high-dimensional vectors.
* **Cosine Similarity:** The app calculates the mathematical "distance" between vectors to identify films with the highest contextual similarity.

### Resilient Cloud Architecture
* **Hybrid Data Storage:** To maintain a lightweight GitHub repository, the 25MB **Similarity Matrix** is hosted on **Google Drive** and fetched dynamically at runtime using `gdown`.
* **API Resilience:** Designed with "Graceful Degradation." If external movie poster APIs are blocked, the app automatically generates **dynamic Google Search metadata links**, ensuring a 100% functional and informative UI.

### Premium UI/UX Design
* **Theater Dark Mode:** A custom "Cinema-themed" interface created using advanced CSS injection.
* **Base64 Image Encoding:** Background images are encoded directly into the CSS for faster loading and repository cleanliness.
* **Optimized Card Layout:** A custom **3+2 vertical column split** ensures that long movie titles remain perfectly aligned without breaking the layout.
* **Non-Tech Friendly:** UI elements are labeled intuitively (e.g., *"Click for Details"*) to ensure accessibility for all users.

---

## Tech Stack
* **Language:** Python 3.10+
* **Framework:** Streamlit
* **Libraries:** Pandas, Scikit-learn, Gdown, Pickle, OS
* **Deployment:** GitHub & Streamlit Cloud

---

## Project Structure
* `app.py` - Main application logic and Streamlit configurations.
* `style.css` - Custom CSS for the theater-themed UI and card alignment.
* `requirements.txt` - Configuration file for the cloud environment.
* `movie_dict.pkl` - Pre-processed movie metadata.
* `similarity.pkl` - (Cloud-fetched) The Similarity Matrix for recommendations.

---

## How to Run Locally
* **Clone the repository:**
  ```bash
  git clone https://github.com/debalina-saha05/movie-recommender-system-project2.git
