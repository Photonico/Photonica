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

wine:     #a03264 #b94169 #cd4678 #dc5582 #eb6996 #f587a5 #faaabe #fac3d2 #ffdce1 #a54169 #af556e #d77891 #ff9bb9  
coral:    #b42846 #cd3c50 #dc465f #f05a6e #f58291 #fa9ba5 #ffb4be #facdd2 #ffdcdc #b93c50 #be5a64 #dc7d87 #faa0aa  
crimson:  #c81423 #e1322d #f03c3c #ff645a #ff968c #ffaaa5 #ffc3be #ffd2cd #ffdcd7 #b42328 #d23c41 #fa644b #ffa08c  
orange:   #eb731e #f5820a #fa8c14 #faa03c #ffb464 #ffc382 #ffcda0 #ffdcb4 #ffe6c8 #dc6914 #e1915a #eba064 #f0b478  
yellow:   #e1b400 #ebb914 #f0be1e #fac81e #ffd21e #ffe15f #ffeb78 #fff096 #fff5b4 #d29b14 #dcb964 #e6c86e #f0d278  
lime:     #82a019 #87aa1e #8cb423 #96be2d #aad241 #b4dc4b #c8e67d #d7eb9b #e6f0b9 #7d962d #8ca555 #96b455 #a0c85a  
green:    #196e28 #198228 #28963c #3cb446 #5ac850 #87dc82 #aae6a5 #b9ebb4 #cdf5c8 #286e28 #468246 #509b5f #5ab478  
cyan:     #1e6464 #1e7d7d #1e9696 #28a0a0 #32afaf #3cc8c8 #78e1e1 #9bebeb #bef0f0 #286e6e #468282 #509696 #50afaf  
azure:    #0050a0 #0064d2 #1478e1 #0f8cf0 #14a0ff #32b9ff #6ec8ff #96dcff #beebff #145aaa #3c73be #4b8cd2 #5aa5e6  
violet:   #554ba0 #645ac8 #8269f0 #a078ff #aa96ff #beafff #d2beff #dccdff #ebdcff #463c96 #6e69b9 #8782d2 #a596e6  
purple:   #6e2d8c #823ca5 #aa50c3 #d264e1 #f078ff #eb96f5 #f5aff5 #fac3fa #ffd7fa #783c78 #87559b #aa6ebe #d287dc  
silver:   #3c5078 #4b6491 #5073a5 #6487b4 #789bc3 #8caacd #a0b9d7 #b4cde1 #d2e1f0 #465a82 #5f7396 #7387aa #8ca0be  
titanium: #325096 #4664b9 #5078cd #698cd7 #7da0e1 #91afeb #a5c3f5 #bed2fa #d7e6ff #3c5aa0 #556eaf #6982be #7d9bcd  

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
