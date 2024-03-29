## Stellarium
Links to Stellarium and their documentation can be found in the main repository `README`
___
### Configuration
***Required*** **: set the save path in the screenshot script if not using `driver.py`**
- Open `screenshots.ssc` in a text editor
- Find the line in the *User-defined variables* section that contains `// (true) ? "/my/save/path" :`
- Uncomment the line (remove the leading //)
- Replace /my/save/path with the path to the directory to save screenshots (don't remove the quotation marks)

***Optional*** **: configure user-defined variables near the top of `screenshots.ssc`** [^1]
- hours: the number of hours to collect
- minutes: the number of minutes to collect
- seconds: the number of seconds to collect
- tickspersec: the number of ticks (frames) per second
- secpertick: the number of seconds per tick (frame)
- date: the starting date+time, *e.g., 2024-02-29T12:00:00*

[^1]: Total time (hours+minutes+seconds), fps, and spf should be positive

**Download additional data: stars and satellites**
- Open the "Configuration window" **[F2]**
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

**Options which may be desired to or need to be changed**
- flag_allow_screenshots_dir = true
- flag_script_allow_write_absolute_path = true
- fullscreen = true
- screen_h = 1080
- screen_w = 1920
___
### Running the screenshots.ssc script
Using any method to run the script, Stellarium will display a fullscreen window as the script runs.
- The Stellarium GUI window will close after the script has completed
- Press **[Alt+F4]** to close the GUI window early

*If not using `driver.py`, ensure the save path has been set, as indicated in the [configuration](#configuration) section above.*

**Method 1**: use the `driver.py` script to "automate" running Stellarium
```bash
$ python3 driver.py --stellarium
```

**Method 2**: Run Stellarium from the command-line, Stellarium *must* be provided with the full script path
```bash
$ stellarium --startup-script $(pwd)/screenshots.ssc
```

**Method 3**: Run the script from Stellarium's GUI
- Open Stellarium
- Press **[F12]** to open the "Script console" window
- Choose "Load file" to load a script file
- Navigate to the script and open it
- Press the "Play" button to begin the script
  - The "Script console" window ***will*** be included in any screenshots
  - There is a small pause before screenshots begin to provide time to ***close*** the console window
___
