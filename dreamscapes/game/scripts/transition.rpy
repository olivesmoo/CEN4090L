label transition:
    "Do you want to keep playing"
    call navigationer
    return


screen navigationer():

    vbox:
            #xpos gui.navigation_xpos
        xalign 0.5
        yalign 0.9
        imagebutton auto "bg_test_%s.png" action MainMenu()