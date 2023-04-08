# (Improved) Battlesnake Python Starter Project

This project is a fork of the [Battlesnake Python Starter Project](https://github.com/BattlesnakeOfficial/starter-snake-python), with improved networking performance, easy-to-use pre-made classes for basic game objects, and most importantly, **additional automation features** through GitHub actions and AWS LightSail Container Services, allowing you to automatically deploy each branch of your snake to a unique URL and test on the Battlesnake website.

## Table of Contents

## What Improvements?

## Important Setup

## Usage

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
