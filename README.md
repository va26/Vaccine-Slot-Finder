Vaccine-Slot-Finder
===================================

This python script can be used to get a notification for vaccine slot availability on your mobile device. Implemented this as there is acute shortage of vaccine and it is difficult to find slots for 18+ population in India. The script takes `state`, `district` and `channel-name` as inputs and runs indefinitely until it finds a slot. The notification of the slot found is sent to your slack channel which can be also viewed on your smart phone.

# Getting Started

1. Create a slack account and your own **personal workspace**. Refer the following [link][1].
2. Create a slack app on using this [link][2]. Click on `Create your Slack app` as shown.

![first_image](https://github.com/va26/Vaccine-Slot-Finder/blob/main/Images/Create_app.PNG)

3. Click on the `Create New App` as shown.

![second_image](https://github.com/va26/Vaccine-Slot-Finder/blob/main/Images/app_1.PNG)

4. Choose `From scratch` in the dialog box shown.

![third_image](https://github.com/va26/Vaccine-Slot-Finder/blob/main/Images/from_scratch.PNG)

5. Select an app name and the workspace you created in step 1. For example, I have chosen the app name as `vaccine_alert` and workspace as `Example`.

![fourth_image](https://github.com/va26/Vaccine-Slot-Finder/blob/main/Images/workspace.PNG)

6. Once the app is created add a `bot` to it by choosing the following option.

![fifth_image](https://github.com/va26/Vaccine-Slot-Finder/blob/main/Images/add_bot.PNG)

7. Add relevant scopes to the bot, to enable it to send (write) message to a channel of the worspace it belongs to.

![sixth_image](https://github.com/va26/Vaccine-Slot-Finder/blob/main/Images/add_scopes.PNG)
![seventh_image](https://github.com/va26/Vaccine-Slot-Finder/blob/main/Images/bot_scopes.PNG)

You can expirement with other scopes as well to enable the bot to send messages/notifications to private chat :relaxed:.

8. Once the app is created and bot with relevant scopes is added, intall it to your workspace as shown below.

![eighth_image](https://github.com/va26/Vaccine-Slot-Finder/blob/main/Images/install_workspace.PNG)

9. Once the app installation to your personal workspace is complete it will generate a bot, which is used to authenticate the bot to send message. Click on copy to copy the token and add it to your environment variable as `SLACK_BOT_TOKEN`. Refer the [link][4] for more info on how to store token safely.

![ninth_image](https://github.com/va26/Vaccine-Slot-Finder/blob/main/Images/bot_token.PNG)

After the following the above steps you're all set to receive notifications :smile:. Just add the bot to a channel and pass that channel name as a parameter in `slack_message` function in the [script][5]. See the **Usage** section for more info on how to run it.

# Usage

This repository is only compatible with Python3.
1. Clone the github repo using:
```sh
git clone https://github.com/va26/Vaccine-Slot-Finder.git
```
2. Install slack for python
```sh
pip install slackclient
```
3. Run the following command from the project root directory specifying the `state`, `district` and `channel-name` as arguments.
```sh
# For example:
python Vaccine_notification.py --state "Karnataka" --district "BBMP" --channel-name "#alert_me"
```
The program will keep running indefinitely until it finds a slot, while occasionally sleeping between 1 to 10 secs to avoid overloading the **Cowin portal with too many** API calls.

# Author

Vatsal Aggarwal 


[1]: https://slack.com/intl/en-in/get-started#/createnew
[2]: https://api.slack.com/bot-users#getting-started
[3]: https://www.ffmpeg.org/download.html
[4]: https://slack.dev/python-slackclient/auth.html
[5]: https://github.com/va26/Vaccine-Slot-Finder/blob/main/Vaccine_notification.py
