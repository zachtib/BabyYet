# BabyYet
Because they're going to keep asking

## What is this?

This is a spiritual successor to a [small project](https://github.com/zachtib/HasAsiaHadTheBabyYet) I wrote ~3 years ago when my wife was pregnant with our first child, when people would often ask "Has she had the baby yet?" (Teddy wound up being 10 days late) as sort of a spoof on sites that contained a simple Yes/No answer to a question in the site name (such as Is it Tuesday?). While I could have dusted off the old project and redeployed it, it's small enough that I decided to do a rewrite, and not have to look at code I wrote three years ago. Plus I've added new features.

## How does it work?
It uses a pseudo-singleton pattern (it will create the database record if it doesn't exist) to store a boolean yes/no value, as well as things like a due date (and soon, a few more things). When a record is created, it also generates a "secret url" that can be used to easily update that record from a mobile device.

Unlike the previous iteration of this project, this version should be pretty easy to steal if you want to use it yourself. There's now an enviornment variable for "Mother's name", so if you deploy this on Heroku and set that environment variable, you should be good to go. If you then run `python manage.py createsuperuser`, you'll be able to log in and access the Django Admin.

## Django and Postgres seems like major overkill
Yep. They're just tools that I'm familiar with and let me knock this out in a couple hours with a full CI/CD pipeline deploying to Heroku. If I felt like learning something new, I probably would have written this in KTor. (Plus, this let me compare more directly to how I wrote it three years ago).

## What's left to do?
A decent amount, although I have some time. New in this version is displaying the due date, and I want to update the "Yep." side of things to allow the parent to add in some details (time, weight, etc) about the new baby. I also need to actually build out the form for updating the record assuming I don't want to have to use the Django Admin.
