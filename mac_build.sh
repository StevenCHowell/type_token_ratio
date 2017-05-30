pyinstaller --noconfirm --clean --onefile \
            --distpath mac_app \
            -n ttr \
            --icon=ttr_icon.png \
            -p /Users/schowell/data/myPrograms/anaconda3/envs/ttr35/lib/python3.5/site-packages/appJar/ \
            ./gui_ttr.py

# zip the result to keep it executable
cd mac_app
zip ttr.zip ttr
