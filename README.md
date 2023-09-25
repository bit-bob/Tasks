# Tasks

## Initial Setup

## Python Env Setup

```
make venv
source .venv/bin/activate
```

> **_NOTE:_** `source .venv/bin/activate` can't go in the makefile because source is a shell built-in command, not an executable that you can start from anywhere but a shell
> see https://superuser.com/questions/1758394/makefile-with-source-command-not-working

## Installing Requirements

### First Time Installation
```
brew install openapi-generator
```

### Regular Installation
```
make install
```

## Running Storybook to see the components

```
make storybook
```

## Running the app

```
make run
```

## Using the app

[Local App](http://localhost:3000/)

## Using the API

[Local API Access](http://localhost:3000/docs)

## Running the tests

```
make test
```

## Cleaning and Generating the code

```
make clean
```
