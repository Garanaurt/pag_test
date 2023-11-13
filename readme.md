**TrafficBot**

TrafficBot is a simple Python script designed to simulate organic traffic to a specified website by performing searches on Google and visiting random pages, including the target website. The script utilizes the PyAutoGUI library for automating mouse and keyboard actions.

### Features:

- **Search and Visit:**
  The main functionality involves performing searches on Google using predefined keywords (`search_keywords`) and then visiting random pages from the search results. If the target website (`site_url`) appears in the search results, the bot will visit it.

- **Proportional Mouse Movement:**
  The script simulates proportional mouse movement across the screen, making it adaptable to different screen sizes.

- **Random Scrolling:**
  During website visits, the bot performs random scrolling actions to simulate user engagement on the visited pages.



### Installation:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

   This command will install all the necessary dependencies listed in the `requirements.txt` file.

3. **Setup:**
   - Open the script (`main.py`) and customize the following variables:
     - `keywords_list`: List of keywords for the Google search.
     - `site`: The target website URL.
     - `num_visits`: Number of search and visit iterations.

4. **Screenshot:**
   - Place a screenshot of the target website URL named `site_url_screen.png` in the same folder as the script. This screenshot is used to locate the website link on the search page.
     
        ![screenshot of link](site_url_screen.png)

5. **Execution:**
   - Run the script using the command `python main.py`.

### Notes:

- The script is currently configured for Linux and Firefox browser. If you are using a different operating system, adjust the browser opening mechanism in the `start_browser` method accordingly.
