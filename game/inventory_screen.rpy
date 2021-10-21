init python:
    import re

screen inventory_screen():
    vbox:            
        yalign 1.0
        xfill True
        $ tooltip = GetTooltip()
        if tooltip:
            text "[tooltip]" color "FFFFFF"
        else:
            text " "    
        hbox:        
            spacing 10
            #label "Inventory"
            $ sorted_items = inventory.toList()
            for i in sorted_items:
                if (items[i["name"]]):
                    $ splitted = re.split('(\!|\?|\.) ',items[i["name"]])
                    $ desc = splitted[0] + splitted[1]
                    imagebutton:
                        sensitive in_room
                        idle "images/" + i["name"]+".png"
                        tooltip desc
                        action NullAction()
                        at icon_size