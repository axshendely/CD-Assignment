echo "Somthing Changed!"
cd /home/CD-Assignment
echo "Printing working directory"
pwd
echo "pull"
git pull origin main
echo "restart application"
systemctl restart CD-Assignment
systemctl status CD-Assignment    
echo "You're up to date and application is restarted"
