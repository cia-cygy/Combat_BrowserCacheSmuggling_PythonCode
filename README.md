# Combat_BrowserCacheSmuggling_PythonCode

As the name suggests, this code is intended to delete .dll files from browser cache folders as the only scenario where a .dll file is stored in a browser cache folder is when the PC is under Browser Cache Smuggling attack.

I came to know about this attack from the following article:
https://cybersecuritynews.com/teams-malware-via-browsers-cache-smuggling/amp/

Attack Procedure:

Browser Cache Smuggling:

-> Attacker hosts a malicious DLL file on a webpage, disguised as an image.
-> The page embeds a hidden <img src="payload.dll">.
-> Browser caches the DLL, treating it as a legitimate resource due to manipulated Content-Type headers.

Delivery & Execution:

-> Attacker socially engineers the victim to run a PowerShell command.
-> PowerShell script searches browser cache (e.g., Firefox’s cache2/entries).
-> Script copies the cached DLL to Teams’ or OneDrive’s local directory.

DLL Proxying for Execution & Evasion:

-> Teams loads the DLL following Windows DLL search order.
-> Fake DLL proxies legitimate function calls while executing malware.
-> Payload (e.g., Cobalt Strike beacon) is executed.
-> Legitimate app continues running, reducing suspicion.


My idea is to keep updating this code to make it an automatic and seamless process of deleting .dll files as soon as they are cached by the browser.