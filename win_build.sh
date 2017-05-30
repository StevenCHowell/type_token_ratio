pyinstaller --noconfirm --clean --onefile \
            --distpath win_app \
            -n ttr \
            --icon=ttr_icon.png \
            -p /c/Users/schowell/Anaconda3/envs/ttr35/lib/python3.5/site-packages/appJar/ \
            ./gui_ttr.py

# zip up the result
cd win_app/
zip ttr.zip ttr
