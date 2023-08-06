# Laetitude Bots

### One time script for saving config files to DynamoDB

`python laetitudebots/live/migrate.py --config --stage --api_key --api_secret`

- config - the .cfg file to save e.g. `./lambda/<strategy>/<strategy>.cfg`
- stage - dev or prod, the stage environment to save.
- api_key - api key to use.
- api_secret - api_secret to use.
