# set proxy config via profie.d - should apply for all users

export http_proxy="http://localhost:1082/"
export https_proxy="http://localhost:1082/"
export ftp_proxy="http://localhost:1082/"
export no_proxy="127.0.0.1,localhost"

# For curl
export HTTP_PROXY="socks5h://localhost:1080/"
export HTTPS_PROXY="socks5h://localhost:1080/"
export FTP_PROXY="http://localhost:1082/"
export NO_PROXY="127.0.0.1,localhost"
