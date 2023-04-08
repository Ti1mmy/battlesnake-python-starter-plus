# (Improved) Battlesnake Python Starter Project

This project is a fork of the [Battlesnake Python Starter Project](https://github.com/BattlesnakeOfficial/starter-snake-python), with improved networking performance, easy-to-use pre-made classes for basic game objects, and most importantly, **additional automation features** through GitHub actions and AWS LightSail Container Services, allowing you to automatically deploy each branch of your snake to a unique URL and test on the Battlesnake website.
## What Improvements?
* Automatically deploys each branch of your snake to a unique URL, allowing you to test each branch's changes on the Battlesnake website.
* Pre-made classes for basic game objects (Board, and Snake), with methods for getting information about the game state.
* Uses WSGI instead of Flask's built-in server, which is much faster, and handles multiple requests at once without timeouts.
* Uses Python 3.11, improving performance.

## Important Setup

### 1. Create a new repository from this template
Create a new repository from this template by clicking [here](https://github.com/BattlesnakeOfficial/starter-snake-python/generate). Or you can click the "Use this template" button at the top of this page, either works.

### 2. Set up your AWS account
[Set up an AWS account](https://docs.aws.amazon.com/polly/latest/dg/setting-up.html). You may need to set up a billing method, but you may only need to pay a small (or no) amount if you use the free tier (micro instance), which is what this project uses, up to a certain amount.

### 3. Add your AWS credentials to your GitHub repository secrets
[Set up an Access Key](https://lightsail.aws.amazon.com/ls/webapp/account/advanced) for your AWS account. Then, add the following secrets to your GitHub repository:

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`

Navigate to your repository's Settings, then `Secrets and variables`, then `Actions` and add a new secret for each of the above.

### 5. Edit your GitHub Actions
* `deploy.yml`, `create-instance.yml` and `delete-instance.yml` files in the `.github/workflows` directory.
* In each of these files, replace `AWS_LIGHTSAIL_SERVICE_NAME` and `AWS_REGION` to your desired values.

### 6. Create a container service for your main branch
You will need to start this project off by manually creating a main branch container service. This is because the GitHub action that creates the container services for each branch will not run on the main branch. I'll see if I can fix this in the future.

For now though:
* Go to the [AWS Lightsail console](https://lightsail.aws.amazon.com/ls/webapp/home/instances)
* Click `Create container service`
* Select `Micro` for the instance size (this is free tier eligible)
* Change the name of your service to `<your-service-name>-main`. `<your-service-name>` is the same as `AWS_LIGHTSAIL_SERVICE_NAME` in the last step.


## Usage
* After you have made a commit, the GitHub action will automatically deploy your branch's latest code to a unique URL. You can find the URL by clicking on the status checkmark next to your commit, then expanding the `Push and Deploy` section. 

You will see:
```sh
Deploy URL is: https://snekky-snek-main.k8qp50l4q8292.us-west-2.cs.amazonlightsail.com/
```

Note: Once GitHub reports that the action has completed, it may take a few minutes for AWS to actually deploy your container service.

## Play a Game Locally

Install the [Battlesnake CLI](https://github.com/BattlesnakeOfficial/rules/tree/main/cli)
* You can [download compiled binaries here](https://github.com/BattlesnakeOfficial/rules/releases)
* or [install as a go package](https://github.com/BattlesnakeOfficial/rules/tree/main/cli#installation) (requires Go 1.18 or higher)

Command to run a local game

```sh
battlesnake play -W 11 -H 11 --name 'Python Starter Project' --url http://localhost:8000 -g solo --browser
```

## Next Steps

Continue with the [Battlesnake Quickstart Guide](https://docs.battlesnake.com/quickstart) to customize and improve your Battlesnake's behavior.

**Note:** To play games on [play.battlesnake.com](https://play.battlesnake.com) you'll need to deploy your Battlesnake to a live web server OR use a port forwarding tool like [ngrok](https://ngrok.com/) to access your server locally.
