This project aims to analyze GitHub users in Tokyo who have more than 200 followers. The analysis focuses on user characteristics, their repositories, and relationships between various metrics.

**Key points:**
* Data was collected using the GitHub API, which allows programmatic access to user profiles and their public repositories. The script iterated through paginated responses to gather information on users from Tokyo and their respective repositories.
* A surprising finding was that hireable users share their email addresses significantly more often than non-hireable users.
* Developers are recommended to focus on building a presence on GitHub by contributing to open-source projects, as active participation can enhance their experience, learning and attract more followers.


## Installation

1. Clone the repository:
   git clone https://github.com/[your_github_username]/[your_repository_name].git
   cd [your_repository_name]

2. Install the required libraries:
   pip install pandas requests statsmodels

3. Run the data collection and analysis scripts.