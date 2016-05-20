sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/test
sudo ln -s /home/box/web/ask/gunicorn.conf  /etc/gunicorn.d/test2
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start