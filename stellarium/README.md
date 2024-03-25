## Stellarium
Links to Stellarium and their documentation can be found in the main directory's README
___
### Configuration
**Set your save path in the screenshot script**
- Open `screenshots.ssc` in a text editor
- Find the line before the final loop that contains `// (true) ? "/my/save/path" :`
- Uncomment the line (remove the leading //)
- Replace /my/save/path with the path to the directory to save screenshots (don't remove the quotation marks)

**Other variables at the top of screenshots.ssc**
- hours: the number of hours to collect
- tickrate: seconds to elapse between screenshots
- date: a starting date+time

**Download additional data**
- Open the "Configuration window" [F2]
- Select the "Extras" tab
- Download all available "Star catalog updates"
- Select the "Plugins" tab
- Choose "Satellites" from the list on the left
- Select "configure" on the right
- Select the "Sources" tab
- Choose all "celestrak.org" entries
- Select the "Settings" tab
- Select "Update now"
- Once downloads have finished, close and reopen Stellarium

**The Stellarium user configuration file is stored at `~/.stellarium/config.ini`**

Options which may be desired to or need to be changed
- flag_allow_screenshots_dir = true
- flag_script_allow_write_absolute_path = true
- fullscreen = true
- screen_h = 1080
- screen_w = 1920
___
### Running the screenshots.ssc script
Using either method to run the script, Stellarium will display a fullscreen window as the script runs.

Ensure the save path has been set, as indicated in the [configuration](#configuration) section above.

To run Stellarium with the script from the command-line, stellarium must be provided with the full path, e.g.,:
```bash
$ stellarium --startup-script $(pwd)/screenshots.ssc
```
To run the script from the Stellarium GUI
- Open Stellarium
- Press F12 to open the "Script console" window
- Choose "Load file" to load a script file
- Navigate to the script, and open it
- Press the "Play" button to begin the script
  - The "Script console" window ***will*** be included in any screenshots
  - There is a small pause before screenshots begin, to provide time to close the console window
- Stellarium will remain open when the screenshot script has completed
- Press Alt+F4 to close the GUI window
___
