[![Circle CI](https://circleci.com/gh/JasonBoyles/bumper.svg?style=svg)](https://circleci.com/gh/JasonBoyles/bumper)

# bumper
bumper updates tags for hot template releases

## Installation
    pip install git+https://github.com/JasonBoyles/bumper

## Usage
    bumper bump github_organization github_repo_name

### return values
0 indicates success, all values >0 failure.

### positional arguments
  * `github_organization`: the Github username or organization under which the repo lives
  * `github_repo_name`: the name of the repo

### environment variables
  bumper requires a `GITHUB_TOKEN` environment variable containing a token
  with the ability to delete and create tags in the target repo.
