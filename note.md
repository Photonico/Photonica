# Developing Tips

* Activated theme location  
  * Linux: `~/.vscode/extensions`  
  * macOS: `~/.vscode/extensions`  
  * Windows:

* Activated Photonica location in Linux / macOS  
  * Dark: `~/.vscode/extensions/conantares.photonica-1.0.11/themes/photonica_dark.json`  
  * Light Wine: `~/.vscode/extensions/conantares.photonica-1.0.11/themes/photonica_light_wine.json`  
  * Light Coral: `~/.vscode/extensions/conantares.photonica-1.0.11/themes/photonica_light_coral.json`  
  * Light Warm: `~/.vscode/extensions/conantares.photonica-1.0.11/themes/photonica_light_warm.json` (id "Photonica Light Orange", renamed from Orange)  
  * Light Green: `~/.vscode/extensions/conantares.photonica-1.0.11/themes/photonica_light_green.json`  
  * Light Cyan: `~/.vscode/extensions/conantares.photonica-1.0.11/themes/photonica_light_cyan.json`  
  * Light Azure: `~/.vscode/extensions/conantares.photonica-1.0.11/themes/photonica_light_azure.json`  
  * Light Silver: `~/.vscode/extensions/conantares.photonica-1.0.11/themes/photonica_light_silver.json`  
  * Light Violet: `~/.vscode/extensions/conantares.photonica-1.0.11/themes/photonica_light_violet.json`  

* Color Straw  
  * Linux:      Color Picker
  * macOS:      Digital Color Meter

* Shortcut of inspecting editor tokens and scopes  
  * Linux:      Alt T  
  * macOS:      ⌥ T  

* Tools Installation  
  `npm install -g yo generator-code @vscode/vsce`

* Generate a template
  `yo code`

* Package the file
  `vsce package`

* Publish the project
  `vsce publish`

* VSCode theme generator  
  `npm install -g yo generator-code`

* VSCode UI architecture  
  `https://code.visualstudio.com/api/references/extension-guidelines`

* VSCode components reference
  `https://code.visualstudio.com/docs/editor/editingevolved`

* Colors references  
  `https://code.visualstudio.com/api/references/theme-color`

* Light theme colors

wine:     #963c4b #b4505f #c8646e #dc7882 #eb919b #f5aab4 #ffbec8 #ffcdd2 #ffdce1 #a04655 #aa6469 #be787d #d29196  
coral:    #a5413c #c85046 #e15f50 #f57364 #ff8c78 #ffa591 #ffbeaf #ffcdbe #ffdcd2 #af4b46 #be645a #d2786e #e69182  
crimson:  #a01423 #c81423 #e1322d #f03c3c #ff6464 #ff918c #ffafaa #ffc8c3 #ffdcd7 #aa2328 #b94b46 #cd5a55 #e16e69  
orange:   #eb7823 #f08223 #ff8c28 #ffa02d #ffb464 #ffc382 #ffcda0 #ffdcb4 #ffe6c8 #dc6914 #e1915a #eba064 #f0b478  
yellow:   #dcaa28 #e6b41e #f0be1e #fac828 #ffd732 #ffe15f #ffeb78 #fff096 #fff5b4 #d29b14 #dcb964 #e6c86e #f0d278  
lime:     #64871e #739b1e #82aa1e #96be2d #aacd46 #b9dc6e #c8e696 #d7ebaa #e1f0c3 #6e912d #829b50 #96af5f #aac36e  
green:    #19642d #288237 #379b4b #46b45a #6ec878 #87dc9b #afe6b9 #beebbe #c8f0c8 #286e32 #468250 #5a9b64 #6eb478  
cyan:     #196464 #147878 #0a8c8c #28a0a0 #46b4b4 #64c8c8 #96dcdc #a5e6e6 #bef0f0 #1e6e6e #3c7d7d #559191 #6eaaaa  
azure:    #0050a0 #0064d2 #0a78e1 #0f8cff #14a5ff #32b9ff #6ec8ff #96dcff #beebff #145aaf #3c73be #4b8cd2 #5aa5e6  
iris:     #37508c #4b64af #5578c8 #6e8cd7 #82a0e1 #96afe6 #aac3f0 #bed2f5 #d7e6ff #415a96 #5a6ea5 #6e82b4 #829bc8  
violet:   #5a3ca5 #7350cd #8c64f0 #a078ff #af96ff #beafff #d2beff #dccdff #ebdcff #6446af #7864be #8c7dd2 #a596e6  
purple:   #82288c #9b37aa #b946c3 #d25adc #e673f0 #eb96f5 #f5aff5 #fac3fa #ffd7fa #8c3796 #9655a0 #af69b9 #cd7dd2  
silver:   #3c5078 #4b6491 #5073a5 #6487b4 #789bc3 #8caacd #a0b9d7 #b4cde1 #d2e1f0 #465a82 #5f7396 #7387aa #8ca0be  

* Dark theme colors

gray:     #000000 #191919 #1e1e1e #232323 #282828 #2d2d2d #3c3c3c #464646 #505050 #646464 #787878 #8c8c8c #a0a0a0 #b4b4b4 #c8c8c8 #d7d7d7 #e6e6e6 #f0f0f0 #fafafa #ffffff  
red:      #a51919 #c86464 #ff283c #d27878 #ff5050 #ff5a91 #f0788c #ff7878 #C81423  
orange:   #ff7814 #ff9600  
yellow:   #f0c850 #ffc800 #ffd71e #ffdc64 #ffeb00  
green:    #7dbea0 #8cbe82 #8cc878 #a0c88c #5ae6aa #96e18c #afdc9b #64f050 #c8f064 #c8ff46  
cyan:     #28b4b4 #50c3a0 #8cb4be #96bebe #8cc8b4 #64dcdc #8ce1e1 #78ebd7 #c8faff  
azure:    #0a78E1 #008cf0 #788ca0 #6496c8 #1ea0ff #64a0dc #82a0c8 #3cbeff #8cb4ff #87c8e1 #64d2ff #a0c8ff #8cdcff #c8d7dc #b4dcf0 #c8ebff  
violet:   #8C64f0 #9b91ff #af8cf0 #b49bff  
magenta:  #D25ADC #a078c8 #d28cfa #dc96be #dcaad2 #e1a0ff #d2b4ff #f0dcff  

* references

"normal", "Orbital", "orbital", "Orbitals", "orbitals"):
        color_set.append("#145AAA") # color[0]: Base
        color_set.append("#1478E1") # color[1]: total
        color_set.append("#14A0FF") # color[2]: Integral

        color_set.append("#8C64F0") # color[3]: s-orbital
        color_set.append("#D25ADC") # color[4]: px-orbital
        color_set.append("#F03C64") # color[5]: py-orbital
        color_set.append("#FA8C00") # color[6]: pz-orbital
        color_set.append("#FAC828") # color[7]
        color_set.append("#96C800") # color[8]: d-orbital
        color_set.append("#14AFAF") # color[9]: f-orbital
        color_set.append("#1E8CA0") # color[10]
        return color_set

    if color_family in ("Grey", "grey", "Gray", "grey"):
        color_set.append("#3C3C3C")
        color_set.append("#787878")
        color_set.append("#B4B4B4")

        color_set.append("#E1322D")
        color_set.append("#FA8C00")
        color_set.append("#FAC828")
        color_set.append("#96BE2D")
        color_set.append("#28AF3C")
        color_set.append("#19A0A0")
        color_set.append("#1478E1")
        color_set.append("#8C64F0")
        return color_set

    if color_family in ("Silver", "silver"):
        color_set.append("#787D8C")
        color_set.append("#AAAFBE")
        color_set.append("#C8CDD7")

        color_set.append("#E1322D")
        color_set.append("#FA8C00")
        color_set.append("#FAC828")
        color_set.append("#96BE2D")
        color_set.append("#28AF3C")
        color_set.append("#19A0A0")
        color_set.append("#1478E1")
        color_set.append("#8C64F0")
        return color_set

    if color_family in ("Red", "red"):
        color_set.append("#C81423")
        color_set.append("#E1322D")
        color_set.append("#FF644B")

        color_set.append("#FA8C00")
        color_set.append("#FAC828")
        color_set.append("#96BE2D")
        color_set.append("#28AF3C")
        color_set.append("#19A0A0")
        color_set.append("#1478E1")
        color_set.append("#8C64F0")
        color_set.append("#D25ADC")
        return color_set

    if color_family in ("Orange", "orange"):
        color_set.append("#EB731E")
        color_set.append("#FA8C00")
        color_set.append("#FFA03C")

        color_set.append("#FAC828")
        color_set.append("#96BE2D")
        color_set.append("#28AF3C")
        color_set.append("#19A0A0")
        color_set.append("#1478E1")
        color_set.append("#8C64F0")
        color_set.append("#D25ADC")
        color_set.append("#F03C64")
        return color_set

    if color_family in ("Yellow", "yellow", "Gold", "gold"):
        color_set.append("#EBC31E")
        color_set.append("#FAC828")
        color_set.append("#FFD732")

        color_set.append("#96BE2D")
        color_set.append("#28AF3C")
        color_set.append("#19A0A0")
        color_set.append("#1478E1")
        color_set.append("#8C64F0")
        color_set.append("#D25ADC")
        color_set.append("#F03C64")
        color_set.append("#FA8C00")
        return color_set
    
    if color_family in ("Lime", "lime"):
        color_set.append("#8CB423")
        color_set.append("#96BE2D")
        color_set.append("#A0C837")

        color_set.append("#28AF3C")
        color_set.append("#19A0A0")
        color_set.append("#1478E1")
        color_set.append("#8C64F0")
        color_set.append("#D25ADC")
        color_set.append("#F03C64")
        color_set.append("#FA8C00")
        color_set.append("#FAC828")
        return color_set

    if color_family in ("Green", "green"):
        color_set.append("#238C4B")
        color_set.append("#28AF3C")
        color_set.append("#73C81E")

        color_set.append("#19A0A0")
        color_set.append("#1478E1")
        color_set.append("#8C64F0")
        color_set.append("#D25ADC")
        color_set.append("#F03C64")
        color_set.append("#FA8C00")
        color_set.append("#FAC828")
        color_set.append("#96BE2D")
        return color_set

    if color_family in ("Cyan","cyan"):
        color_set.append("#1E7878")
        color_set.append("#19A0A0")
        color_set.append("#14AFAF")

        color_set.append("#1478E1")
        color_set.append("#8C64F0")
        color_set.append("#D25ADC")
        color_set.append("#F03C64")
        color_set.append("#FA8C00")
        color_set.append("#FAC828")
        color_set.append("#96BE2D")
        color_set.append("#28AF3C")
        return color_set

    if color_family in ("Blue", "blue", "Azure", "azure"):
        color_set.append("#145AAA") # color[0]
        color_set.append("#1478E1") # color[1]
        color_set.append("#14A0FF") # color[2]

        color_set.append("#8C64F0") # color[3]
        color_set.append("#D25ADC") # color[4]
        color_set.append("#F03C64") # color[5]
        color_set.append("#FA8C00") # color[6]
        color_set.append("#FAC828") # color[7]
        color_set.append("#96BE2D") # color[8]
        color_set.append("#28AF3C") # color[9]
        color_set.append("#19A0A0") # color[10]
        return color_set

    if color_family in ("Violet", "violet"):
        color_set.append("#643CC3")
        color_set.append("#8C64E1")
        color_set.append("#AF96FF")

        color_set.append("#D25ADC")
        color_set.append("#F03C64")
        color_set.append("#FA8C00")
        color_set.append("#FAC828")
        color_set.append("#96BE2D")
        color_set.append("#28AF3C")
        color_set.append("#19A0A0")
        color_set.append("#1478E1")
        return color_set

    if color_family in ("Purple", "purple"):
        color_set.append("#AA3CB9")
        color_set.append("#D25ADC")
        color_set.append("#F078FF")

        color_set.append("#F03C64")
        color_set.append("#FA8C00")
        color_set.append("#FAC828")
        color_set.append("#96BE2D")
        color_set.append("#28AF3C")
        color_set.append("#19A0A0")
        color_set.append("#1478E1")
        color_set.append("#8C64F0")
        return color_set

    if color_family in ("Wine", "wine"):
        color_set.append("#AA1E64")
        color_set.append("#C82364")
        color_set.append("#F03C64")

        color_set.append("#FA8C00")
        color_set.append("#FAC828")
        color_set.append("#96BE2D")
        color_set.append("#28AF3C")
        color_set.append("#19A0A0")
        color_set.append("#1478E1")
        color_set.append("#8C64F0")
        color_set.append("#D25ADC")
        return color_set

    if color_family in ("Brown", "brown"):
        color_set.append("#966450")
        color_set.append("#B47D50")
        color_set.append("#D29650")

        color_set.append("#FA8C00")
        color_set.append("#FAC828")
        color_set.append("#96BE2D")
        color_set.append("#28AF3C")
        color_set.append("#19A0A0")
        color_set.append("#1478E1")
        color_set.append("#8C64F0")
        color_set.append("#D25ADC")
        return color_set