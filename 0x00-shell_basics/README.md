
# Shell Script Collection

## Overview

This repository contains a collection of shell scripts that cover various tasks related to system administration and automation. These scripts are designed to be educational and practical for anyone interested in shell scripting, system management, or automation tasks.

## Table of Contents

1. [Scripts Overview](#scripts-overview)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
4. [Contributing](#contributing)


## Scripts Overview

Here's a brief overview of the scripts available in this collection:

1. **Where am I?**: Print the absolute path name of the current working directory.
2. **What’s in there?**: Display the contents list of the current directory.
3. **There is no place like home**: Change the working directory to the user's home directory.
4. **The long format**: Display current directory contents in long format.
5. **Hidden files**: Display current directory contents, including hidden files, in the long format.
6. **I love numbers**: Display current directory contents in long format with user and group IDs displayed numerically, including hidden files.
7. **Welcome**: Create a directory named "my_first_directory" in the /tmp/ directory.
8. **Betty in my first directory**: Move the file "betty" from /tmp/ to /tmp/my_first_directory.
9. **Bye bye Betty**: Delete the file "betty" from /tmp/my_first_directory.
10. **Bye bye My first directory**: Delete the directory "my_first_directory" in the /tmp directory.
11. **Back to the future**: Change the working directory to the previous one.
12. **Lists**: List files in the current directory, parent directory, and /boot directory in long format.
13. **File type**: Print the type of the file named "iamafile."
14. **Copy HTML files**: Copy all HTML files from the current directory to the parent directory, checking for existing or newer versions.
15. **Let’s move**: Move files beginning with an uppercase letter to the directory /tmp/u.
16. **Clean Emacs**: Delete files in the current working directory ending with the character "~."
17. **Tree**: Create directories "welcome/", "welcome/to/", and "welcome/to/school" with minimal lines and spaces.
18. **Life is a series of commas, not periods**: List files and directories separated by commas, following specific sorting rules.
19. **File type: School**: Create a magic file "school.mgc" for detecting School data files.

## Getting Started

To use these scripts, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the directory containing the scripts:

   ```bash
   cd shell-script-collection
   ```

3. Make the scripts executable:

   ```bash
   chmod +x *.sh
   ```

Now, you're ready to use the scripts as described in the next section.

## Usage

Each script is documented with its purpose and usage in the comments at the beginning of the script file. To run a script, simply execute it from the command line using `./script-name.sh`. Make sure you have the appropriate permissions to execute the script.

For example, to run the "Where am I?" script:

```bash
./0-current_working_directory.sh
```

Follow the instructions provided in each script's comments to understand its behavior and usage fully.

## Contributing

Contributions to this collection of shell scripts are welcome! If you have improvements, bug fixes, or additional scripts to add, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes:

   ```bash
   git checkout -b feature/new-script
   ```

3. Make your changes and commit them with clear and concise commit messages.
4. Push your changes to your fork.
5. Create a pull request to the original repository.


