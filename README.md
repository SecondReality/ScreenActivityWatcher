# Screen Activity Watcher

This script watches your screen and sends a Pushbullet notification if motion stops beyond a specified threshold.

Requires Numpy, Pillow and Pushbullet packages.

# How it works

Every minute it makes a capture of your desktop waits 30 seconds and then it takes another and compares them to see if the difference is over a given threshold. It will send a maximum of one notification every 10 minutes.
