import streamlit as st
import sqlite3

DB_PATH = "data/users.db"

def create_user(username, password):
    """Insert new user into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        st.success(f"✅ Account for '{username}' created successfully!")
    except sqlite3.IntegrityError:
        st.error(f"⚠️ Username '{username}' already exists. Try another one.")
    finally:
        conn.close()


def verify_user(username, password):
    """Verify user credentials."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user


def login():
    # Initialize login state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # If already logged in, skip login page entirely
    if st.session_state.logged_in:
        return True

    # Page layout
    st.title("🔐 Login to Sales Dashboard")

    tab_login, tab_signup = st.tabs(["Login", "Create New Account"])

    # ------------------------
    # LOGIN TAB
    # ------------------------
    with tab_login:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.button("Login")

    if login_btn:
        user = verify_user(username, password)
        if user:
            st.session_state.logged_in = True
            st.success("✅ Login successful! Loading dashboard...")
            st.balloons()  # nice visual effect, optional
            # ⚠️ No st.experimental_rerun() — Streamlit auto refreshes
            return True
        else:
            st.error("❌ Invalid username or password")


    # ------------------------
    # SIGNUP TAB
    # ------------------------
    with tab_signup:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")
        signup_btn = st.button("Create Account")

        if signup_btn:
            if new_user and new_pass:
                create_user(new_user, new_pass)
            else:
                st.warning("Please enter both username and password.")

    return st.session_state.logged_in
