# Welcome to organization The Black Wolves first project
Start to crash the system

AIM:
          The primary aim of this project is to analysis of ransomware attack and provide recovery methods to the infected system to recover the data.


OBJECTIVES:
          This idea the project is about what ransomware attacks are all about by understanding how they work which influence their consequences and counteractions against them. The work will largely center on studying conduct patterns as well as means applied during such attacks together with finding weak points that can be used by these forms of assault; moreover, we will also look into ways to recover from these situations. The final objective is to come up with a solid system that would help in preventing ransomware occurrences, minimizing losses caused by them and restore systems and data that have been negatively affected.



METHODOLOGY

Planning:

Gather Requirements:

A laptop to run the Host operating System
Virtual box
Windows virtual machine (Target system)
Kali Linux virtual machine (Attacker System)
A laptop to run the server for storing keys
Ransomware for testing

Research Existing Tools:

NextronSystem - ransomware-simulator (GitHub)
Leeberg - CashCatRansomwareSimulator (GitHub)
Marmos91 - ransomware (GitHub)
kh4sh3i - Ransomware (GitHub)
lawndoc - RanSim (GitHub)

Implementation:

Set Up the Development Environment:

I. Setup the Host Laptop
    1. Install the Host Operating System
    2. Make sure host OS is properly installed and updated.
    3. Install VirtualBox
    4. Download and install VirtualBox.
    5. Install the VirtualBox Extension Pack for more functionality.
II. Windows Virtual Machine (Target System)
Create Windows VM
    1. Open VirtualBox and click on “New” to create a new virtual machine.
    2. Set the name (for example, “Windows Target System”).
    3. Allocate enough memory (at least 4 GB) and create a virtual hard disk (50 GB)
Installing Windows OS
    1. Insert a Windows installation ISO and start the VM.
    2. Follow the installation process to set up Windows.
    3. After installation, install VirtualBox Guest Additions for better performance and integration.



Set Up the Target System
      Configure the system for testing ensuring it has standard user permissions and configurations.

III. Kali Linux Virtual Machine (Attacker System)
Create Kali Linux VM
 1. In VirtualBox create a new VM called “Kali Linux Attacker System.”
 2. Set Type as Linux and Version as Debian (64-bit).
 3. Allocate memory accordingly (4 GB) then create a virtual hard disk (50 GB)


Kali Linux Installation Process

1. Firstly, download the latest Kali Linux ISO and launch the VM with it.
2. Secondly, follow all installation steps for Kali Linux.
3. Finally, install VirtualBox Guest Additions after installation is complete.

Attacker System Setup

1. Kali Linux packages must be updated and upgraded.
2. Furthermore, additional tools necessary for penetration testing and analysis must be installed.
IV. A way of storing keys
Server Laptop Setup

1. On top of that, install an appropriate server operating system.
2. Additionally, ensure the server has enough resources (4GB RAM, 50GB storage).

Key Storage Server Setup

1. Moreover, set up secure key storage mechanisms (database or secure file system) for this purpose.
2. Also, encryption should be done for stored keys.
3. In addition, firewalls, access controls as well as the regular updates should be used to secure this server appropriately.

 

Ransomware Testing
Acquire Ransomware Samples

1. In addition, reliable sources such as research institutions are a good place to obtain ransomware samples.
2. Make sure that these samples are handled such a way that they are only applied within the controlled environment where they were obtained.

Creating Controlled Environments

1. To isolate the testing environment from any production networks or sensitive data.
2. Accidental spreading can be prevented through network segmentation firewall and other security measures.
Encryption and Decryption:
                   Encrypt the user data using Symmetric key encryption key algorithm (AES-256). In this algorithm the same key is used for both encryption and decryption. Then Encrypt the key using Asymmetric key encryption algorithm (RSA). In this algorithm two different keys are used. One key used for encryption is called Public Key and another key used for decryption is called Private Key. Here we encrypt the user data using AES-256 then encrypt the secret key using RSA public key, the data only decrypt using RSA private key 

RECOVERY METHOD
Monitor:
          Look for unusual system behaviours like file encryption, new file extension, ransom notes
Isolation:
          Disconnect affected systems from the network to prevent the ransomware spreading or don’t connect any external media devices to the infected system.
Analyze: 
          Examine the ransomware’s actions, including the files it’s targets, encryption methods, any communication with command and control and behaviour of the ransomware.
System Data:
          Focus on recovering the most critical system data, based on their importance to business operations.
Backup:
         Before attack to the system, backup system data securely, and restore data when clean all the ransomware from the system. Ensure that the backups are not infected with the ransomware.
Cleanup:
          Ensure that all traces of the ransomware are removed from infected systems. This may include malicious files, registry entries and any scripts or tools used by the attackers.
Reinstall OS:  
          For severely compromised systems, a complete reinstallation of the operating system may be necessary. This ensures that no remaining ransomware present in system.

# A thorough and methodical approach to analyzing and recovering from a ransomware attack is crucial to minimize damage and restore normal operations. It involves not only technical remediation but also strategic planning, communication and continuous improvement of security measures.    


TOOLS:
Programming Languages:
Go
Python


GITHUB REPOSITORY LINKS:
Project - https://github.com/TheBlackWolves/SmileyRansom
https://github.com/danielbrain2003
https://github.com/Creator-55
https://github.com/Sanjithrg

