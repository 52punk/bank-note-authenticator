mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"pankaj18-335@aec.ac.in\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml