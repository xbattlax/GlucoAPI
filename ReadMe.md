# GlucoAPI

# Metzger - Schwab - Mouhri

## singup

curl --request POST \
  --url http://127.0.0.1:8000/singup \
  --header 'Content-Type: application/json' \
  --data '{
	"username":"tes",
	"password": "test",
	"email": "test",
	"weight": 65
}'

return {
	"message": [
		"count",
		null
	]
} if success

## login

curl --request POST \
  --url http://127.0.0.1:8000/login \
  --header 'Content-Type: application/json' \
  --data '{
	"password": "test",
	"email": "test"
}'

return uuid code if success
{
	"message": "Success",
	"uuid": "da61fd19-c611-43f6-8c50-4b378b9e9d3e"
}

## add record gluco 

curl --request POST \
  --url http://127.0.0.1:8000/add_glucose_record \
  --header 'Content-Type: application/json' \
  --data '{
	"uuid": "da61fd19-c611-43f6-8c50-4b378b9e9d3e",
	"taux": "20",
	"created_at": "2022-05-04 09:00"
}'

return {
	"message": [
		"count",
		null
	]
} if success

## get gluco records

curl --request POST \
  --url http://127.0.0.1:8000/get_glucose_records \
  --header 'Content-Type: application/json' \
  --data '{
	"uuid": "da61fd19-c611-43f6-8c50-4b378b9e9d3e",
	"date1": "2022-05-04 09:00",
	"date2":"2022-05-04 09:30"
}'

return {
	"message": "Success",
	"data": [
		{
			"id": "9ea75f4c-24b9-4c34-9909-23d3e76dc742",
			"created_at": "2022-05-04T09:15:00+00:00",
			"user_id": "da61fd19-c611-43f6-8c50-4b378b9e9d3e",
			"taux": 20
		}
	]
} if success

## Install 
Python 3.8.9
> pip install -r requirements.txt

> uvicorn main:app --reload


## deploy on EC2
```bash
SSH into the ec2 instance and run following commands

sudo yum update -y
 
sudo yum install git -y
 
git version

# If you are running this for first time.
git clone https://github.com/xbattlax/GlucoAPI.git

cd GlucoAPI

# or 

git pull https://github.com/Valurank/initial-scoring-api.git


# if new EC2 instance
chmod 777 install-dependencies.sh
./dependencies.sh

# Use this script to deploy or redeploy.
chmod 777 deploy.sh
./deploy.sh

```




