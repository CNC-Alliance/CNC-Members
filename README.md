# CNC-Members Registration Instructions

# Registration
In this repo stake pool operators can register to become a member of the CNC Alliance. After you have become an official member your pool will be visible on https://adapools.org/alli 

**Disclaimer** By submitting a pull request you agree that all the submited information will be made publicly available to everyone. Also, by submitting you agree that you fit the critera of the CNC Alliance set out below. 

# Requirements:
- Github Account
- Pool_id
- Pool must operate on a 100% renewable energy (note there are expections where this requirement can be substituted by following the current ISPO application route, find out more about this in our Discord and read the information below)

# SPO Membership Types: 

CNC has two tiers of SPO members - **Passive** members and **Active** members

**Passive CNC members**🌱 are required to run their nodes on 100% renewable energy. They do not have to actively participate in the group’s meetings and hence are not directly contributing to any projects of the group. Passive members are encouraged to join our Discord server and learn more about our ongoing projects and long term vision. We want to have as many pools as possible to act on climate change and promote making Cardano Carbon Neutral. On the other hand, if you do have time, we very much welcome pools to consider becoming an Active member. 👇

**Active CNC members**🌿 are required to run their servers on 100% renewables and donate to environmental causes pioneered by the CNC Alliance. 
Donations should be at least 85 ADA for the 1st block produced of an epoch and they should participate in the regular meetings on projects and contribute to the progress of the group and its initiatives, like the Cardano Forest project and the CNC Ala project.

**ISPO pools are considered temporary Active members of CNC**
Pools participating and donating in the CNC Ala ISPO will be considered as offsetting their node energy consumption with their donations to the project, so they will qualify for active membership during this time. We also hope that many will continue to stay beyond the ISPO to run more pools on renewables and to fund more environmental projects. 

--------------------------------------------------
# STEP 1 (Fork the CNC-Members registration repo):
Go to github.com and login with your account.

Navigate to the CNC-Members registration Repo and fork it.
https://github.com/CNC-Alliance/CNC-Members

![image](https://user-images.githubusercontent.com/94197082/197391240-f2943874-58cb-4d1f-9ffa-ae92683481d8.png)

# STEP 2 (Add your pool info):
After the repo has been forked in your namespace click on the **cnc-alliance-member-registration.json** file
![image](https://user-images.githubusercontent.com/94197082/197391662-9c81bcdd-544c-403f-a006-93caa613c2a9.png)


**Click edit:**

![image](https://user-images.githubusercontent.com/94197082/197391760-d4d052d3-89ea-49be-9cf7-52543b67225b.png)

Add your pool information into the json list (use Copy-paste) from one of the other entries to copy the Json format easily.

**Registration JSON Example:**
- Remember to update the **number** counter higlighted in red below.
- Double check your commas syntax!

![Instructions copy](https://user-images.githubusercontent.com/94197082/197393510-32e4e0ee-97c8-4ae1-b0e2-a7767ff5ae21.png)

- Please specify whether you are looking to join as an **Active** or **Passive** member in the "membershipType" field
![image](https://user-images.githubusercontent.com/116071877/199316145-0618aece-1c0d-44a7-8432-1bfbb8d8023e.png)

- For **Active Members** joining please add the stake address (BECH32 format) of the wallet from which you are using to donate to our current Charity Project.
This will make it possible for us to automatically track your donations from the (**donationWalletStakeAddress** parameter)

- After you added all your information to the list click Commit changes:

![image](https://user-images.githubusercontent.com/94197082/197392347-bd3947dd-502f-438e-845a-ea0dba7c6d5c.png)


# STEP 3 (Create your pull request):
1) Click on “Pull requests”:
2) “New Pull Request”:
![image](https://user-images.githubusercontent.com/94197082/197392490-92e4743e-6431-490b-abe5-933b1a23520f.png)

3) “Create Pull Request:”

![image](https://user-images.githubusercontent.com/94197082/197392944-0ea70d47-e75c-4454-b7c7-bc98d4e1037b.png)

Give a name and confirm. If everything is done correctly you should see that all Checks have passed, if it fails something probably is wrong with the format of your Json file. Just drop a message in discord and we will fix it together.

# What next?
If you want to play an active role in this alliance, or just take part in Climate related discussions or just hang out with other like minded SPOs & Eco-friends, please join our discord: https://discord.gg/5wZg7cQJeM
