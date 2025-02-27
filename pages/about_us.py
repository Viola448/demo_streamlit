import streamlit as st

st.write("About us")
page_one = st. Page(
page= "pages/about_us.py",
title="About us"
)
page_two= st. Page(
page= "pages/username.py",
title="Username"
)
page_three = st. Page(
page= "pages/streamlit_app.py",
title="Statistics"
)
pages = st. navigation( [page_one, page_two, page_three])
pages. run()