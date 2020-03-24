cd /opt/Flask-API
git init
git add -A
git config --global user.email 'ajay' 
git config --global user.name 'ajay' 
git commit -m 'lets'
git remote add origin https://github.com/prodevans/sentiment_analysis.git
read -p 'Enter the branch name: ' branchname
git branch $branchname
git checkout $branchname
git push -u origin $branchname
oc login -u dhanusha -p dhanusha https://console.prod.pdcloudex.com:8443 --insecure-skip-tls-verify
oc new-app https://github.com/prodevans/sentiment_analysis.git#$branchname -n mlpaas
oc create route edge --service=finaldep -n mlpaas
echo -en "\n\nhttps://`oc get route finaldep -o template --template {{.spec.host}} -n mlpaas`\n\n"