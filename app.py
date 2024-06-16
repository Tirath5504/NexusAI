import streamlit as st
import games.music_genre_game as music_genre_game
# import games.object_detection_game as object_detection_game
# import games.fashion_recognition_game as fashion_recognition_game
# import games.deepfake_detective_game as deepfake_detective_game
# import games.scene_analysis_game as scene_analysis_game

def main():
    st.set_page_config(page_title="NexusAI", page_icon="🎮", layout="wide")
    st.title("NexusAI")
    st.markdown(
        """
        Welcome to the NexusAI! Explore various interactive games powered by machine learning and deep learning.
        Choose a game category from the sidebar on the left to get started.
        """
    )

    st.sidebar.title("Game Categories")
    game_selection = st.sidebar.radio(
        "Select a Game:",
        ("Music Genre Classification", "None") # "Object Detection Challenge", "Fashion Style Recognition", "Deepfake Detective", "Scene Analysis and Prediction"
    )

    if game_selection == "Music Genre Classification":
        st.subheader("Music Genre Prediction time!")

        genres = {'0': 'blues',
        '1': 'classical',
        '2': 'country',
        '3': 'disco',
        '4': 'hiphop',
        '5': 'jazz',
        '6': 'metal',
        '7': 'pop',
        '8': 'reggae',
        '9': 'rock'}

        prediction = st.selectbox("Predict Genre of audio: ", tuple(genres.values()))

        audio_file_path = music_genre_game.get_audio()

        if audio_file_path is not None:
            st.audio(audio_file_path)

            if st.button("Classify Genre"):
                result = music_genre_game.classify_audio(audio_file_path)
                if "error" in result:
                    st.error(result["error"])
                else:
                    if prediction == result["label"]:
                        st.success(f"You know your music!")
                    else:
                        correct = result["label"]
                        st.error(f"Still a music noob! Correct Genre: {correct}")
                audio_file_path = music_genre_game.get_audio()

    # elif game_selection == "Object Detection Challenge":
    #     object_detection_game.play_game()
    # elif game_selection == "Fashion Style Recognition":
    #     fashion_recognition_game.play_game()
    # elif game_selection == "Deepfake Detective":
    #     deepfake_detective_game.play_game()
    # elif game_selection == "Scene Analysis and Prediction":
    #     scene_analysis_game.play_game()

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        "Created by Tirath Bhathawala with ❤️"
    )

if __name__ == "__main__":
    main()