mkdir -p ~/.stremlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
"> ~/.stremlit/config.toml