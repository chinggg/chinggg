apt update
apt install apt-transport-https ca-certificates dirmngr curl vim -y
apt -y upgrade

apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6
mv /etc/apt/sources.list /etc/apt/sources.list.debian
cat <<EOF > /etc/apt/sources.list
deb https://mirrors.sjtug.sjtu.edu.cn/kali kali-rolling main non-free contrib
# deb-src https://mirrors.sjtug.sjtu.edu.cn/kali kali-rolling main non-free contrib
EOF

apt update
apt -y upgrade
apt -y dist-upgrade
apt -y autoremove --purge
apt install zsh fdisk wget git net-tools screenfetch
apt install kali-linux-core proxychains docker.io
