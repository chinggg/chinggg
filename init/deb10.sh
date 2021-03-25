apt update
apt install apt-transport-https ca-certificates dirmngr curl vim -y
apt -y upgrade

cp /etc/apt/sources.list /etc/apt/sources.list.old
sed -i 's/http:\/\/mirrors.163.com/https:\/\/mirrors.sjtug.sjtu.edu.cn/g' /etc/apt/sources.list
sed -i 's/stretch/buster/g' /etc/apt/sources.list

apt update
apt -y upgrade
apt -y dist-upgrade
apt -y autoremove --purge
apt install zsh fdisk git net-tools screenfetch
apt install proxychains docker.io
