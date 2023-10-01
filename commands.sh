echo "Somthing Changed!"
cd /home/CD-Assignment
echo "Printing working directory"
pwd
echo "restart application"
git pull origin main
systemctl restart CD-Assignment
systemctl status CD-Assignment    
echo "You're up to date and application is restarted"
