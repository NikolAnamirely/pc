mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"u19207287@utp.edu.pe\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
