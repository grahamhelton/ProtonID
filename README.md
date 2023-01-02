# ProtonID
I recently had a need to identify a large number of emails/domains to see if they had protonmail accounts. I checked this by seeing if they had proton's MX re
cords set up.
![image](https://user-images.githubusercontent.com/19278569/210284808-a5d629c4-105c-4070-a01e-a0fd051dcb5b.png)

![image](https://user-images.githubusercontent.com/19278569/210284867-2179f8cf-fa73-4561-95ce-98d02a900762.png)



![image](https://user-images.githubusercontent.com/19278569/210284845-c0c9dbe9-d43d-45e9-ac0c-c57ce9372280.png)

# Usage
```bash
python3 protonID.py -e me@grahamhelton.com
python3 protonID.py -l list.txt
python3 protonID.py -l /path/to/list.txt

# Return just emails with some commandline kung-fu
./protonID.py -l emails.txt | grep "has proton mail MX records" | awk {'print $3'} | sort | uniq
```
