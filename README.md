# facebook_ID_finder
*Many online tools for this, but a tiny script hasn't hurt anyone.*

## what is this?

It's just a short python code for extracting the Facebook ID of a target. 
Useful for OSINT investigations or other stuff. 

**Requirements:** 

    pip install requests

**Run:** 

    python fbid_finder.py https://www.facebook.com/ellendegeneres
   
**Output:**

    >>> fb_with_args.py https://www.facebook.com/{myusername}                                           	
    [*] The Facebook ID for this account is:  35678900

*Note: The length of digits vary as I have seen in my tests.*
